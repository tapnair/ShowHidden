import adsk.core, adsk.fusion, traceback

from .Fusion360CommandBase import Fusion360NavCommandBase

def displayUpdateBodies(action):
    pass
def displayUpdate(showHidden, showBodies, showPlanes):

    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
   
    if not showBodies:
        # Get the root component of the active design.
        rootComp = adsk.fusion.Component.cast(design.rootComponent)
        # Get All occurences inside the root component
        allOccurences = rootComp.allOccurrences
        
        for occurence in allOccurences:      
            if occurence.isLightBulbOn and showHidden:
                if occurence.childOccurrences.count == 0:
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

    if showPlanes:
        allComponents = design.allComponents
        for component in allComponents:
            planes = component.constructionPlanes
            for plane in planes:
                if plane.isLightBulbOn and showHidden:
                    plane.isLightBulbOn = False
                else: 
                    plane.isLightBulbOn = True 
                    
############# Create your Actions Here #################################################
class ShowHiddenCommand(Fusion360NavCommandBase):
    
    def __init__(self, commandName, commandDescription, commandResources, cmdId, DC_CmdId, DC_Resources, debug, showHidden, showBodies, showPlanes):
    
        super().__init__(commandName, commandDescription, commandResources, cmdId, DC_CmdId, DC_Resources, debug)
        # Initialize Override to get state.
        self.showHidden = showHidden
        self.showBodies = showBodies
        self.showPlanes = showPlanes
        
         
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
        displayUpdate(self.showHidden, self.showBodies, self.showPlanes)  
    
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        pass
    
    
    
    
    
    
    