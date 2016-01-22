import datetime
from Bearing import Bearing
class Sensors():
    def __init__(self):
        self.setAllValues()

############################################ getter -->

    def getWindDirection(self):
        return self.__windDirection

    def getCompassBearing(self):
        return self.__compassCourse

    def getWinkelgesch(self):
        return self.__winkelgesch

    def getBattery(self):
        return self.__Akku

    def getPosition(self):
        return self.__Position

    def getDateTime(self):
        return self.__DateTime

    def getCourseMadeGood(self):
        return self.__courseMadeGood

    def getSpeedOverGround(self):
        return self.__speedOverGround

############################################  set all values

    def setAllValues(self):
        self.__windDirection = self.__setWindDirection()
        self.__compassCourse = self.__setCompassBearing()
        self.__winkelgesch = self.__setWinkelgesch()
        self.__Akku = self.__setBattery()
        self.__Position = self.__setPosition()
        self.__courseMadeGood = self.__setCourseMadeGood()
        self.__speedOverGround = self.__setSpeedOverGround()
        self.__DateTime = self.__setDateTime()


############################################ setter (read Sensors) -->

    def __setWindDirection(self):
        return Bearing(0)
    def __setCompassBearing(self):
        return Bearing(40)
    def __setWinkelgesch(self):
        return 2
    def __setBattery(self):
        return 100
    def __setPosition(self):
        return [53.570110,9.674878]
    def __setDateTime(self):
        return datetime.datetime.now()
    def __setCourseMadeGood(self):
        return Bearing(45)
    def __setSpeedOverGround(self):
        return 1.8
