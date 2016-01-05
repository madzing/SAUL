import datetime

class Sensors():
    def __init__(self):
        self.__setAllValues()

############################################ getter -->

    def getWindDirection(self):
        return self.__windDirection

    def getCompassBearing(self):
        return self.__compassCourse

    def getBattery(self):
        return self.__Akku

    def getPosition(self):
        return self.__Position

    def getDateTime(self):
        return self.__Time

    def getCourseMadeGood(self):
        return self.__courseMadeGood

    def getSpeedOverGround(self):
        return self.__speedOverGround

############################################  set all values

    def setAllValues(self):
        self.__windDirection = self.__setWindDirection()
        self.__compassCourse = self.__setCompassCourse()
        self.__Akku = self.__setAkku()
        self.__Position = self.__setPosition()
        self.__courseMadeGood = self.__setCourseMadeGood()
        self.__speedOverGround = self.__setSpeedOverGround()

############################################ setter (read Sensors) -->

    def __setWindDirection(self):
        return 0
    def __setCompassBearing(self):
        return 40
    def __setBattery(self):
        return 100
    def __setPosition(self):
        return [53.570110,9.674878]
    def setDateTime(self):
        return datetime.datetime.now()
    def __setCourseMadeGood(self):
        return 45
    def __setSpeedOverGround(self):
        return 1.8
