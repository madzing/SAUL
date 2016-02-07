import math
class Bearing():
    def __init__(self,bearing):
            bearing = bearing % 360
            self.bearing = bearing

    def getDiffTo(self,bearing):
        if math.fabs(bearing.bearing - self.bearing) <=180:
            return bearing.bearing - self.bearing
        else:
            if bearing.bearing < 180:
                return self.getDiffTo360degree(self)+self.getDiffTo360degree(bearing)
            else:
                return -(self.getDiffTo360degree(self)+self.getDiffTo360degree(bearing))
#Always returns positive values
    def getDiffTo360degree(self,bearing):
        if bearing.bearing<=180:
            return bearing.bearing
        else:
            return 360 - bearing.bearing

    def add(self,bearing):
        if isinstance(bearing,Bearing):
            summe = self.bearing + bearing.bearing
        else:
            summe = self.bearing + bearing
        return Bearing(summe)

    def substract(self,bearing):
        if isinstance(bearing,Bearing):
            diff = self.bearing - bearing.bearing
        else:
            diff = self.bearing - bearing
        return Bearing(diff)


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
        if math.sqrt((x*x)+(y*y)) < 1:
            return None
        elif x > 0 and y >= 0:
            return Bearing(90 - math.degrees(math.atan(y/x)))
        elif x >= 0 and y < 0:
            return Bearing(180 - math.degrees(math.atan(x/math.fabs(y))))
        elif x < 0 and y <= 0:
            return Bearing(270 - math.degrees(math.atan(math.fabs(y)/math.fabs(x))))
        elif x <= 0 and y > 0:
            return Bearing(360 - math.degrees(math.atan(math.fabs(x)/y)))

