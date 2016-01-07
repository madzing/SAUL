import math
import datetime

class VesselInfoList():
    def __init__(self,maxListLen):
        self.list = []
        self.maxListLen = maxListLen

    def writeNewInfo(self,pos,time,CompassBearing,WindDirection,Battery):
        self.__list.append([pos,time,CompassBearing,WindDirection,Battery]) #append list
        if len(self.list) > self.maxListLen:
            self.list.pop(0) #delete oldest measurement

    def getInfo(self):
        return self.list
