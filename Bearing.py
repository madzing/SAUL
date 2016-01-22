import math
class Bearing():
    def __init__(self,bearing):
            bearing = bearing % 360
            if bearing < 0:
                bearing = 360 - bearing
            self.bearing = bearing

    def getDiffTo(self,bearing):
        if math.fabs(bearing.bearing - self.bearing) <=180:
            return bearing.bearing - self.bearing
        else:
            if bearing.bearing < 180:
                return self.getDiffTo360degree(self)+self.getDiffTo360degree(bearing)
            else:
                return -(self.getDiffTo360degree(self.bearing)-self.getDiffTo360degree(bearing))

    def getDiffTo360degree(self,B):
        if B.bearing<=180:
            return B.bearing
        else:
            return 360 - B.bearing

    def add(self,bearing):
        if type(bearing) == "Bearing":
            summe = self.bearing + bearing.bearing
        else:
            summe = self.bearing + bearing
        if summe <=360 and summe >= 0:
            return  Bearing(summe)
        elif summe < 0:
            return Bearing(360 + summe)
        else:
            return Bearing(0 - summe)

    def substract(self,bearing):
        if type(bearing) == "Bearing":
            diff = self.bearing - bearing.bearing
        else:
            diff = self.bearing - bearing
        if diff <=360 and diff >=0:
            return Bearing(diff)
        elif diff < 0 :
            return Bearing(360 + diff)
        else:
            return Bearing(0-diff)
    def calculateMeanBearing(self,BearingList):
        pass
