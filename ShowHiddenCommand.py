import adsk.core, adsk.fusion, traceback

from .Fusion360CommandBase import Fusion360NavCommandBase

def displayUpdateBodies(action):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    
    allComponents = design.allComponents
    for component in allComponents:
        bodies = component.bRepBodies
        for body in bodies:
            if body.isVisible and (action == 'showHidden'):
                body.isVisible = False
            else: 
                body.isVisible = True
                
def displayUpdateComponents(action):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    # Get the root component of the active design.
    rootComp = adsk.fusion.Component.cast(design.rootComponent)
    # Get All occurences inside the root component
    allOccurences = rootComp.allOccurrences
    
    for occurence in allOccurences:      
        if occurence.isLightBulbOn and (action == 'showHidden'):
            if occurence.childOccurrences.count == 0:
                occurence.isLightBulbOn = False
        else:
            occurence.isLightBulbOn = True 


def displayUpdatePlanes(action):
    
    app = adsk.core.Application.get()    
    design = adsk.fusion.Design.cast(app.activeProduct)
    allComponents = design.allComponents
    for component in allComponents:
        planes = component.constructionPlanes
        for plane in planes:
            if plane.isLightBulbOn and (action == 'showHidden'):
                plane.isLightBulbOn = False
            elif action == 'showAll': 
                plane.isLightBulbOn = True 
            else:
                plane.isLightBulbOn = False
                    
############# Create your Actions Here #################################################
class ShowHiddenCommand(Fusion360NavCommandBase):
    
    def __init__(self, commandName, commandDescription, commandResources, cmdId, DC_CmdId, DC_Resources, debug, target, action):
    
        super().__init__(commandName, commandDescription, commandResources, cmdId, DC_CmdId, DC_Resources, debug)
        # Initialize Override to get state.
        self.target = target
        self.action = action
        
         
    # Runs when Fusion command would generate a preview after all inputs are valid or changed
    def onPreview(self, command, inputs):
        pass
    
    # Runs when the command is destroyed.  Sometimes useful for cleanup after the fact
    def onDestroy(self, command, inputs, reason_):    
        pass
    
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
    
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        if self.target == 'bodies':
            displayUpdateBodies(self.action)
        elif self.target == 'components':
            displayUpdateComponents(self.action)
        elif self.target == 'planes':
            displayUpdatePlanes(self.action)

    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        pass
    
    
    
    
    
    
    