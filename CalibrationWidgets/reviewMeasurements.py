'''

This step lets you review your measurements before moving on.

'''
from   kivy.uix.gridlayout                          import   GridLayout
from   kivy.properties                              import   ObjectProperty
from   kivy.app                                     import   App

class ReviewMeasurements(GridLayout):
    readyToMoveOn   = ObjectProperty(None)
    
    
    def on_Enter(self):
        '''
        
        This function runs when the step is entered
        
        '''
        
        self.data = App.get_running_app().data
        
        tempString = "[color=02cafc] LETS REVIEW THE MEASUREMENTS TO MAKE SURE EVERYTHING LOOKS GOOD. [/color]\n You can use the back button to repeat any step.\n\n "
        tempString = tempString + "\n   Distance between motors: [b][color=f89405]" + self.data.config.get('Maslow Settings', 'motorSpacingX') + "mm[/color][/b]"
        tempString = tempString + "\n   Vertical motor offset: [b][color=f89405]" + self.data.config.get('Maslow Settings', 'motorOffsetY') + "mm[/color][/b]"
        tempString = tempString + "\n   Kinematics type: [b][color=f89405]" + self.data.config.get('Advanced Settings', 'kinematicsType') + "[/color][/b]"
        tempString = tempString + "\n   Chain feed type: [b][color=f89405]" + self.data.config.get('Advanced Settings', 'chainOverSprocket') + "[/color][/b]"
        if self.data.config.get('Advanced Settings', 'kinematicsType') == 'Triangular':
            tempString = tempString + "\n   Rotation radius: [b][color=f89405]" + self.data.config.get('Advanced Settings', 'rotationRadius') + "mm[/color][/b]"
            tempString = tempString + "\n   Chain sag correction value: [b][color=f89405]" + self.data.config.get('Advanced Settings', 'chainSagCorrection') + "[/color][/b]"
        else:
            tempString = tempString + "\n   Sled mount spacing: [b][color=f89405]" + self.data.config.get('Maslow Settings', 'sledWidth') + "mm[/color][/b]"
        
        self.measurementsReadout.text = tempString
    
    def loadNextStep(self):
        self.readyToMoveOn()
    
    def on_Exit(self):
        '''
        
        This function run when the step is completed
        
        '''
        pass