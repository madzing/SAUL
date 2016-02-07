import datetime
from Bearing import Bearing
class Sensors():
    def __init__(self):
        self.setAllValues()

############################################ getter -->

    def getWindDirection(self):
        return self.__windDirection

    def getCompassBearing(self):
        return self.__compassBearing

    def getWinkelgesch(self):
        return self.__winkelgesch

    def getBattery(self):
        return self.__battery

    def getPosition(self):
        return self.__Position

    def getDateTime(self):
        return self.__DateTime

    def getCourseMadeGood(self):
        return self.__courseMadeGood

    def getMeanCompassBearing(self):
        return self.__meanCompassBearing

    def getSpeedOverGround(self):
        return self.__speedOverGround

############################################  set all values

    def setAllValues(self):
        self.setWindDirection(0)
        self.setCompassBearing(90)
        self.setWinkelgesch(0)
        self.setBattery(100)
        self.setPosition([53.570110,9.674878])
        self.setCourseMadeGood(90)
        self.setSpeedOverGround(2)
        self.setMeanCompassBearing(30)
        self.setDateTime()


############################################ setter (read Sensors) -->

    def setWindDirection(self,windDirection):
        self.__windDirection = Bearing(windDirection)
    def setCompassBearing(self,compassBearing):
        self.__compassBearing = Bearing(compassBearing)
    def setWinkelgesch(self,winkelgesch):
        self.__winkelgesch = winkelgesch
    def setBattery(self,battery):
        self.__battery = battery
    def setPosition(self,position):
        self.__Position = position
    def setDateTime(self):
        self.__DateTime = datetime.datetime.now()
    def setCourseMadeGood(self,courseMadeGood):
        self.__courseMadeGood = Bearing(courseMadeGood)
    def setMeanCompassBearing(self,meanCompassBearing):
        self.__meanCompassBearing = Bearing(meanCompassBearing)
    def setSpeedOverGround(self,speedOverGround):
        self.__speedOverGround = speedOverGround
