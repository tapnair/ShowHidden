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

SAB_CmdId = 'SAB_CmdId'
SAC_CmdId = 'SAC_CmdId'
SHB_CmdId = 'SHB_CmdId'
SHC_CmdId = 'SHC_CmdId'
Split_CmdId = 'Split_CmdId'

cmdIds = [SAB_CmdId, SAC_CmdId, SHB_CmdId, SHC_CmdId]

def commandDefinitionById(id):
    app = adsk.core.Application.get()
    ui = app.userInterface
    if not id:
        ui.messageBox('commandDefinition id is not specified')
        return None
    commandDefinitions_ = ui.commandDefinitions
    commandDefinition_ = commandDefinitions_.itemById(id)
    return commandDefinition_

def commandControlByIdForNav(id):
    app = adsk.core.Application.get()
    ui = app.userInterface
    if not id:
        ui.messageBox('commandControl id is not specified')
        return None
    toolbars_ = ui.toolbars
    toolbarNav_ = toolbars_.itemById('NavToolbar')
    toolbarControls_ = toolbarNav_.controls
    toolbarControl_ = toolbarControls_.itemById(id)
    return toolbarControl_

def destroyObject(uiObj, tobeDeleteObj):
    if uiObj and tobeDeleteObj:
        if tobeDeleteObj.isValid:
            tobeDeleteObj.deleteMe()
        else:
            uiObj.messageBox('tobeDeleteObj is not a valid object')
            
def displayUpdate(showHidden, showBodies):

    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
   
    if not showBodies:
        # Get the root component of the active design.
        rootComp = adsk.fusion.Component.cast(design.rootComponent)
        # Get All occurences inside the root component
        allOccurences = rootComp.allOccurrences
        
        for occurence in allOccurences:
            if occurence.isLightBulbOn and showHidden:
                occurence.isLightBulbOn = False
            else:
                occurence.isLightBulbOn = True     
    
    if showBodies:
        allComponents = design.allComponents
        for component in allComponents:
            bodies = component.bRepBodies
            for body in bodies:
                if body.isVisible and showHidden:
                    body.isVisible = False
                else: 
                    body.isVisible = True 

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        class SAB_CreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__() 
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = SAB_ExecuteHandler()
                    cmd.execute.add(onExecute)
                    # keep the handler referenced beyond this function
                    handlers.append(onExecute)               
                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'
                        .format(traceback.format_exc()))     

        class SAB_ExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:  
                    showHidden = False
                    showBodies = True
                    displayUpdate(showHidden, showBodies)
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'
                        .format(traceback.format_exc()))   
                        
        class SAC_CreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__() 
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = SAC_ExecuteHandler()
                    cmd.execute.add(onExecute)
                    # keep the handler referenced beyond this function
                    handlers.append(onExecute)               
                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'
                        .format(traceback.format_exc()))     

        class SAC_ExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    showHidden = False
                    showBodies = False
                    displayUpdate(showHidden, showBodies)
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'
                        .format(traceback.format_exc()))   
                        
        class SHB_CreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__() 
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = SHB_ExecuteHandler()
                    cmd.execute.add(onExecute)
                    # keep the handler referenced beyond this function
                    handlers.append(onExecute)               
                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'
                        .format(traceback.format_exc()))     

        class SHB_ExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    showHidden = True
                    showBodies = True
                    displayUpdate(showHidden, showBodies)
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'
                        .format(traceback.format_exc()))   
                        
        class SHC_CreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__() 
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = SHC_ExecuteHandler()
                    cmd.execute.add(onExecute)
                    # keep the handler referenced beyond this function
                    handlers.append(onExecute)               
                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'
                        .format(traceback.format_exc()))     

        class SHC_ExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    showHidden = True
                    showBodies = False
                    displayUpdate(showHidden, showBodies)
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'
                        .format(traceback.format_exc()))   
                          
        # Get the UserInterface object and the CommandDefinitions collection.
        cmdDefs = ui.commandDefinitions

        #global showAllBodiesCmdId
        #otherCmdDefs = [showAllCompsCmdId, showHiddenBodiesCmdId, showHiddenCompsCmdId]
        # add a command button on Quick Access Toolbar
        toolbars_ = ui.toolbars
        navBar = toolbars_.itemById('NavToolbar')
        toolbarControlsNAV = navBar.controls
        
        SAB_Control = toolbarControlsNAV.itemById(SAB_CmdId)
        if not SAB_Control:
            SAB_cmdDef = cmdDefs.itemById(SAB_CmdId)
            if not SAB_cmdDef:
                # commandDefinitionNAV = cmdDefs.addSplitButton(showAllBodiesCmdId, otherCmdDefs, True)
                SAB_cmdDef = cmdDefs.addButtonDefinition(SAB_CmdId, 'Show All Bodies', 'Show all bodies in active design',commandResources)
            onCommandCreated = SAB_CreatedHandler()
            SAB_cmdDef.commandCreated.add(onCommandCreated)
            # keep the handler referenced beyond this function
            handlers.append(onCommandCreated)
#            SAB_Control = toolbarControlsNAV.addCommand(SAB_cmdDef)
#            SAB_Control.isVisible = True
        
        SAC_Control = toolbarControlsNAV.itemById(SAC_CmdId)
        if not SAC_Control:
            SAC_cmdDef = cmdDefs.itemById(SAC_CmdId)
            if not SAC_cmdDef:
                # commandDefinitionNAV = cmdDefs.addSplitButton(showAllBodiesCmdId, otherCmdDefs, True)
                SAC_cmdDef = cmdDefs.addButtonDefinition(SAC_CmdId, 'Show All Components', 'Show all components in active design',commandResources)
            onCommandCreated = SAC_CreatedHandler()
            SAC_cmdDef.commandCreated.add(onCommandCreated)
            # keep the handler referenced beyond this function
            handlers.append(onCommandCreated)
#            SAC_Control = toolbarControlsNAV.addCommand(SAC_cmdDef)
#            SAC_Control.isVisible = True
            
        SHB_Control = toolbarControlsNAV.itemById(SHB_CmdId)
        if not SHB_Control:
            SHB_cmdDef = cmdDefs.itemById(SHB_CmdId)
            if not SHB_cmdDef:
                # commandDefinitionNAV = cmdDefs.addSplitButton(showAllBodiesCmdId, otherCmdDefs, True)
                SHB_cmdDef = cmdDefs.addButtonDefinition(SHB_CmdId, 'Show Hidden Bodies', 'Show hidden bodies in active design',commandResources)
            onCommandCreated = SHB_CreatedHandler()
            SHB_cmdDef.commandCreated.add(onCommandCreated)
            # keep the handler referenced beyond this function
            handlers.append(onCommandCreated)
#            SHB_Control = toolbarControlsNAV.addCommand(SHB_cmdDef)
#            SHB_Control.isVisible = True
            
        SHC_Control = toolbarControlsNAV.itemById(SHC_CmdId)
        if not SHC_Control:
            SHC_cmdDef = cmdDefs.itemById(SHC_CmdId)
            if not SHC_cmdDef:
                # commandDefinitionNAV = cmdDefs.addSplitButton(showAllBodiesCmdId, otherCmdDefs, True)
                SHC_cmdDef = cmdDefs.addButtonDefinition(SHC_CmdId, 'Show Hidden Components', 'Show hidden components in active design',commandResources)
            onCommandCreated = SHC_CreatedHandler()
            SHC_cmdDef.commandCreated.add(onCommandCreated)
            # keep the handler referenced beyond this function
            handlers.append(onCommandCreated)
#            SHC_Control = toolbarControlsNAV.addCommand(SHC_cmdDef)
#            SHC_Control.isVisible = True
            
#        Split_Control = toolbarControlsNAV.itemById(Split_CmdId)
#        if not Split_Control:
        objColl = adsk.core.ObjectCollection.create()
        objColl.add(SAC_cmdDef)
        objColl.add(SHB_cmdDef)
        objColl.add(SHC_cmdDef)
        others = [SAC_cmdDef, SHB_cmdDef, SHC_cmdDef]
        Split_Control = toolbarControlsNAV.addSplitButton(SAB_cmdDef, others, True,'','m',False)
        #Split_Control = toolbarControlsNAV.addSplitButton(SAB_cmdDef, objColl, True)
        Split_Control.isVisible = True
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        objArrayNav = []
        
        for cmdId in cmdIds:
            commandControlNav_ = commandControlByIdForNav(cmdId)
            if commandControlNav_:
                objArrayNav.append(commandControlNav_)
    
            commandDefinitionNav_ = commandDefinitionById(cmdId)
            if commandDefinitionNav_:
                objArrayNav.append(commandDefinitionNav_)
            
        for obj in objArrayNav:
            destroyObject(ui, obj)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
