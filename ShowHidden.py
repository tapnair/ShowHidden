#Author-Patrick Rainsberry
#Description-Quickly SHow all hidden or simply show all bodies or components


import adsk.core, adsk.fusion, traceback

# global event handlers referenced for the duration of the command
handlers = []

menu_panel = 'InspectPanel'
commandResources = './resources'

commandId = 'showHidden'
commandName = 'Show Hidden'
commandDescription = 'Shows Hidden Bodies or Components'

def showHidden(inputs):
    typeInput = None
    hideInput = None

    for inputI in inputs:
        global commandId
        if inputI.id == commandId + '_type':
            typeInput = inputI
        elif inputI.id == commandId + '_hide':
            hideInput = inputI

    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
   
    if typeInput.selectedItem.name != 'Bodies':
        # Get the root component of the active design.
        rootComp = adsk.fusion.Component.cast(design.rootComponent)
        # Get All occurences inside the root component
        allOccurences = rootComp.allOccurrences
        
        for occurence in allOccurences:
            if occurence.isLightBulbOn and hideInput.selectedItem.name == 'Show Hidden (Invert Display of)':
                occurence.isLightBulbOn = False
            else:
                occurence.isLightBulbOn = True     
    
    if typeInput.selectedItem.name != 'Components':
        allComponents = design.allComponents
        for component in allComponents:
            bodies = component.bRepBodies
            for body in bodies:
                if body.isVisible and hideInput.selectedItem.name == 'Show Hidden (Invert Display of)':
                    body.isVisible = False
                else: 
                    body.isVisible = True 

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        class displayInvertInputChangedHandler(adsk.core.InputChangedEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    cmd = args.firingEvent.sender
                    inputs = cmd.commandInputs
                    showHidden(inputs)
                    adsk.doEvents()
                except:
                    if ui:
                        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                
        class displayInvertExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:  
                    cmd = args.firingEvent.sender
                    inputs = cmd.commandInputs
                    showHidden(inputs)
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'
                        .format(traceback.format_exc()))
                
        class displayInvertCreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__() 
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = displayInvertExecuteHandler()
                    cmd.execute.add(onExecute)

                    onInputChanged = displayInvertInputChangedHandler()
                    cmd.inputChanged.add(onInputChanged)
                    # keep the handler referenced beyond this function
                    handlers.append(onExecute)
                    handlers.append(onInputChanged)
                    inputs = cmd.commandInputs               
                  
                    global commandId
                    hideInput = inputs.addDropDownCommandInput(commandId + '_hide', 'What to show?', adsk.core.DropDownStyles.TextListDropDownStyle)
                    hideInput.listItems.add('Show All', True)
                    hideInput.listItems.add('Show Hidden (Invert Display of)', False)
                    
                    typeInput = inputs.addDropDownCommandInput(commandId + '_type', 'What type?',adsk.core.DropDownStyles.TextListDropDownStyle)
                    typeInput.listItems.add('Bodies', False)
                    typeInput.listItems.add('Components', True)
                    typeInput.listItems.add('Both', False)               
                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'
                        .format(traceback.format_exc()))
                                       
        # Get the UserInterface object and the CommandDefinitions collection.
        cmdDefs = ui.commandDefinitions
         
        # Create a basic button command definition.
        buttonDef = cmdDefs.addButtonDefinition(commandId, 
                                                commandName, 
                                                commandDescription, 
                                                commandResources)                                               
        # Setup Event Handler
        onCommandCreated = displayInvertCreatedHandler()
        buttonDef.commandCreated.add(onCommandCreated)
        handlers.append(onCommandCreated)

        # Add the controls to the Inspect toolbar panel.
        menuPanel = ui.allToolbarPanels.itemById(menu_panel)
        buttonControl = menuPanel.controls.addCommand(buttonDef, '')
        buttonControl.isVisible = True

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        commandDef = ui.commandDefinitions.itemById(commandId)
        if commandDef:
            commandDef.deleteMe()
        
        # Delete the controls to the Inspect toolbar panel.
        menuPanel = ui.allToolbarPanels.itemById(menu_panel)
        buttonControl = menuPanel.controls.itemById(commandId)
        if buttonControl:
            buttonControl.deleteMe()
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
