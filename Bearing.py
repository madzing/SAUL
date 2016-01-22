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

    def getDiffTo360degree(self,bearing):
        if bearing.bearing<=180:
            return bearing.bearing
        else:
            return 360 - bearing.bearing

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

    @staticmethod
    def calculateMeanBearing(bearingList):
        x = 0
        y = 0
        for element in bearingList:
            if element.bearing <= 90:
                x = x + math.cos(math.radians(90 - element.bearing))
                y = y + math.sin(math.radians(90 - element.bearing))
            elif element.bearing <= 180:
                x = x + math.sin(math.radians(180 - element.bearing))
                y = y - math.cos(math.radians(180 - element.bearing))
            elif element.bearing <= 270:
                x = x - math.cos(math.radians(270-element.bearing))
                y = y - math.sin(math.radians(270-element.bearing))
            else:
                x = x - math.sin(math.radians(360-element.bearing))
                y = y + math.cos(math.radians(360-element.bearing))
        if x > 0 and y >= 0:
            return 90 - math.degrees(math.atan(y/x))
        elif x >= 0 and y < 0:
            return 180 - math.degrees(math.atan(x/math.fabs(y)))
        elif x < 0 and y <= 0:
            return 270 - math.degrees(math.atan(math.fabs(y)/math.fabs(x)))
        elif x <= 0 and y > 0:
            return 360 - math.degrees(math.atan(math.fabs(x)/y))
        else:
            return None
