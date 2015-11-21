class Sensors():
    def __init__(self):
        self.__setAllValues()

############################################ getter -->

    def getWindDirection(self):
        return self.__windDirection

    def getCompassCourse(self):
        return self.__compassCourse

    def getAkku(self):
        return self.__Akku

    def getPosition(self):
        return self.__Position

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
        pass
    def __setCompassCourse(self):
        pass
    def __setAkku(self):
        pass
    def __setPosition(self):
        pass
    def __setCourseMadeGood(self):
        pass
    def __setSpeedOverGround(self):
        pass
