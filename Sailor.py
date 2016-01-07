from Sensors import Sensors
from ServoControl import ServoControl

class Sailor():
    def __init__(self,sensorService):
        self.sensorService = sensorService
        startRudderPos = 0
        startSailPos = 0
        self.servoControl = ServoControl(startRudderPos,startSailPos)

    def sail(self,desiredCompassBearing):
        windDirection = self.sensorService.getWindDirection()
        actualCompassBearing = self.sensorService.getCompassBearing()
        rudderPosition = self.servoControl.getCurrentRudderPos()
        sailPosition = self.servoControl.getCurrentSailPos()
        # do stuff so that actaul an desired-compassBearing become equal --->
        """ Pseudocode
        if desiredCompassBearing in wind Direction:
            kreuzen --> change desiredCompassBearing
        adjustRudder(desiredCompassBearing,actualCompassBearing,rudderPosition)

        """
        # adjust Sails -->
        self.adjustSails(actualCompassBearing,windDirection,sailPosition)

    def adjustSails(self,CompassBearing,windDirection,sailPosition):
        pass

    def adjustRudder(self,desiredCompassBearing,CompassBearing,rudderPosition):
        pass
