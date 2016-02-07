from Sensors import Sensors
from ServoControl import ServoControl
from Bearing import Bearing
import math

class Sailor:
    def __init__(self,sensorService):
        self.sensorService = sensorService
        self.servoControl = ServoControl(6,6)
        self.compassBearingList = []
        self.hoeheAmWind = 30 # Min Höhe am Wind
        self.toleranz = 1 # grad pro sekunde

    def sail(self,desiredBearing):
        windDirection = self.sensorService.getWindDirection()
        actualCompassBearing = self.sensorService.getCompassBearing()
        courseMadeGood = self.sensorService.getCourseMadeGood()
        winkelgesch = self.sensorService.getWinkelgesch()

        desiredCompassBearing = self.calculateDesiredCompassBearing(actualCompassBearing,courseMadeGood,desiredBearing)
        # do stuff so that actual an desired-compassBearing become equal --->
        if math.fabs(windDirection.getDiffTo(desiredCompassBearing)) >= self.hoeheAmWind:
            self.adjustRudder(desiredCompassBearing,actualCompassBearing,winkelgesch)
        elif desiredBearing.getDiffTo(actualCompassBearing)>0:
            self.adjustRudder(desiredBearing.add(30),actualCompassBearing,winkelgesch)
        else:
            self.adjustRudder(desiredBearing.substract(30),actualCompassBearing,winkelgesch)
        # adjust Sails -->
        self.adjustSails(actualCompassBearing,windDirection)

    def calculateDesiredCompassBearing(self,actualCompassBearing,courseMadeGood,desiredBearing):
        self.compassBearingList.append(actualCompassBearing)
        lenList = len(self.compassBearingList)
        if lenList > 10:
            self.compassBearingList[0].pop()
        if lenList >= 5:
            meanCompassBearing = Bearing.calculateMeanBearing(self.compassBearingList)
            abdrift = meanCompassBearing.getDiffTo(courseMadeGood)
            if abdrift > 20:    #eine Abdrift größer 20 Grad hat wahrscheinlich andere Hintergründe
                abdrift = 0
            return desiredBearing.add(abdrift)
        return desiredBearing

    def adjustSails(self,compassBearing,windDirection):
        self.servoControl.changeSailPos(math.fabs(compassBearing.getDiffTo(windDirection)))

    def adjustRudder(self,desiredCompassBearing,actualCompassBearing,winkelgesch):
        bearingDiff = actualCompassBearing.getDiffTo(desiredCompassBearing)
        desiredWinkelgesch = (bearingDiff * bearingDiff) / 20
        if bearingDiff < 0:
            desiredWinkelgesch = desiredWinkelgesch * -1
        if winkelgesch < desiredWinkelgesch - self.toleranz:
            self.servoControl.turnRight
        if winkelgesch > desiredWinkelgesch + self.toleranz:
            self.servoControl.turnLeft
