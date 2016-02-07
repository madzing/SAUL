from Sensors import Sensors
from ServoControl import ServoControl
from Bearing import Bearing
import math

class Sailor:
    def __init__(self,sensorService):
        self.lastRudderAdjustment = None
        self.sensorService = sensorService
        self.servoControl = ServoControl(6,6)
        self.hoeheAmWind = 30 # Min Höhe am Wind
        self.toleranz = 1 # grad pro sekunde

    def sail(self,desiredBearing,adjustRudderEveryXSeconds):
        dateTime = self.sensorService.getDateTime()
        if  self.lastRudderAdjustment == None or getTimeDiff(self.lastRudderAdjustmen, datetime) >= adjustRudderEveryXSeconds:
            self.lastRudderAdjustment = dateTime
            windDirection = self.sensorService.getWindDirection()
            actualCompassBearing = self.sensorService.getCompassBearing()
            courseMadeGood = self.sensorService.getCourseMadeGood()
            winkelgesch = self.sensorService.getWinkelgesch()
            meanCompassBearing = self.sensorService.getMeanCompassBearing()

            desiredCompassBearing = self.calculateDesiredCompassBearing(actualCompassBearing,meanCompassBearing,courseMadeGood,desiredBearing)
            # do stuff so that actual an desired-compassBearing become equal --->
            if math.fabs(windDirection.getDiffTo(desiredCompassBearing)) >= self.hoeheAmWind:
                self.adjustRudder(desiredCompassBearing,actualCompassBearing,winkelgesch)
            elif desiredBearing.getDiffTo(actualCompassBearing)>0:
                self.adjustRudder(windDirection.add(30),actualCompassBearing,winkelgesch)
            else:
                self.adjustRudder(windDirection.substract(30),actualCompassBearing,winkelgesch)
            # adjust Sails -->
            self.adjustSails(actualCompassBearing,windDirection)

    def calculateDesiredCompassBearing(self,actualCompassBearing,meanCompassBearing,courseMadeGood,desiredBearing):
        if not isinstance(meanCompassBearing,Bearing):
            return desiredBearing
        else:
            abdrift = meanCompassBearing.getDiffTo(courseMadeGood)
            if abdrift > 20:    #eine Abdrift größer 20 Grad hat wahrscheinlich andere Hintergründe
                abdrift = 0
            return desiredBearing.substract(abdrift)

    def adjustSails(self,compassBearing,windDirection):
        self.servoControl.changeSailPos(math.fabs(compassBearing.getDiffTo(windDirection)))

    def adjustRudder(self,desiredCompassBearing,actualCompassBearing,winkelgesch):
        bearingDiff = actualCompassBearing.getDiffTo(desiredCompassBearing)
        desiredWinkelgesch = (bearingDiff * bearingDiff) / 20
        if bearingDiff < 0:
            desiredWinkelgesch = desiredWinkelgesch * -1
        if winkelgesch < desiredWinkelgesch - self.toleranz or winkelgesch > desiredWinkelgesch + self.toleranz:
            print("mach was")
            self.servoControl.turn(desiredWinkelgesch,winkelgesch)
            print("desiredWinkelgesch:",desiredWinkelgesch)
        else:
            print("mach Nix")
            print("desiredWinkelgesch:",desiredWinkelgesch)

    def getTimeDiff(self,time1,time2):
        """
        returns time difference in seconds
        """
        if time1 >= time2:
            dt = time1 - time2
        else:
            dt = time2 - time1
        dtSec = dt.days*24*60*60 + dt.seconds + dt.microseconds/1000000
        return dtSec
