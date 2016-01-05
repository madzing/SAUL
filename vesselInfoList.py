import math
import datetime

class VesselInfoList(self):
    def __init__(self,maxListLen):
        self.__list = []
        self.__maxListLen = maxListLen

    def writeNewInfo(self,pos,time,CompassBearing,WindDirection,Battery):
        self.__list.append([pos,time,CompassBearing,WindDirection,Battery]) #append list
        if len(self.__list) > self.__maxListLen:
            self.__list.pop(0) #delete oldest measurement

    def getInfo(self):
        return self.__list
