# Importing sample Fusion Command
# Could import multiple Command definitions here
from .ShowHiddenCommand import ShowHiddenCommand

#### Define parameters for 1st command #####
commandName1 = 'Show All Bodies'
commandDescription1 = 'Show all bodies in active design'
commandResources1 = './resources/SAB'
cmdId1 = 'SAB_CmdId'

#### Define parameters for 1st command #####
commandName2 = 'Show Hidden Bodies'
commandDescription2 = 'Show hidden bodies in active design'
commandResources2 = './resources/SHB'
cmdId2 = 'SHB_CmdId'

#### Define parameters for 2nd command #####
commandName3 = 'Show All Components'
commandDescription3 = 'Show all components in active design'
commandResources3 = './resources/SAC'
cmdId3 = 'SAC_CmdId'

#### Define parameters for 2nd command #####
commandName4 = 'Show Hidden Components'
commandDescription4 = 'Show hidden components in active design'
commandResources4 = './resources/SHC'
cmdId4 = 'SHC_CmdId'

#### Define parameters for 1st command #####
commandName5 = 'Show All Planes'
commandDescription5 = 'Show all planes in active design'
commandResources5 = './resources/SAP'
cmdId5 = 'SHP_CmdId'

#### Define parameters for 2nd command #####
commandName6 = 'Show Hidden Planes'
commandDescription6 = 'Show hidden planes in active design'
commandResources6 = './resources/SHP'
cmdId6 = 'SAP_CmdId'

#### Define parameters for 2nd command #####
commandName7 = 'Hide All Planes'
commandDescription7 = 'Hide All in active design'
commandResources7 = './resources/HAP'
cmdId7 = 'HAP_CmdId'


#### Define parameters for Drop Down Command #####
DC_Resources = './resources/DC'
DC_CmdId = 'Show Hidden4'

# Set to True to display various useful messages when debugging your app
debug = False

# Creates the commands for use in the Fusion 360 UI
newCommand1 = ShowHiddenCommand(commandName1, commandDescription1, commandResources1, cmdId1, DC_CmdId, DC_Resources, debug, 'bodies', 'showAll')
newCommand2 = ShowHiddenCommand(commandName2, commandDescription2, commandResources2, cmdId2, DC_CmdId, DC_Resources, debug, 'bodies', 'showHidden')
newCommand3 = ShowHiddenCommand(commandName3, commandDescription3, commandResources3, cmdId3, DC_CmdId, DC_Resources, debug, 'components', 'showAll')
newCommand4 = ShowHiddenCommand(commandName4, commandDescription4, commandResources4, cmdId4, DC_CmdId, DC_Resources, debug, 'components', 'showHidden')
newCommand5 = ShowHiddenCommand(commandName5, commandDescription5, commandResources5, cmdId5, DC_CmdId, DC_Resources, debug, 'planes', 'showAll')
newCommand6 = ShowHiddenCommand(commandName6, commandDescription6, commandResources6, cmdId6, DC_CmdId, DC_Resources, debug, 'planes', 'showHidden')
newCommand7 = ShowHiddenCommand(commandName7, commandDescription7, commandResources7, cmdId7, DC_CmdId, DC_Resources, debug, 'planes', 'hideAll')
#newCommand5 = Fusion360Command(commandName5, commandDescription5, commandResources5, cmdId5, myWorkspace5, myToolbarPanelID5, debug)
#newCommand5 = Fusion360Command(commandName5, commandDescription6, commandResources6, cmdId6, myWorkspace6, myToolbarPanelID6, debug)

def run(context):
    newCommand1.onRun()
    newCommand2.onRun()
    newCommand3.onRun()
    newCommand4.onRun()
    newCommand5.onRun()
    newCommand6.onRun()
    newCommand7.onRun()
def stop(context):
    newCommand1.onStop()
    newCommand2.onStop()
    newCommand3.onStop()
    newCommand4.onStop()
    newCommand5.onStop()
    newCommand6.onStop()
    newCommand7.onStop()
    
#    
