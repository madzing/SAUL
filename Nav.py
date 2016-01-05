import math
from VesselInfoList import VesselInfoList

class Nav(self):
    def __init__(self,sensorService):
        vesselInfoList = VesselInfoList(100) # die letzten 100 Messungen werden gespeichert
        sensorService = sensorService
    def calculateNewDesiredCompassBearing(self):
        vesselInfoList.writeNewInfo(sensorService.getPosition,sensorService.getDateTime,sensorService.getCompassBearing,sensorService.getWindDirection,sensorService.getBattery)





# Private Methods --->
    def __distanceCalc(self,pos1,pos2):
        start_lat = math.radians(pos1[0])
        start_long = math.radians(pos1[1])
        end_lat = math.radians(pos2[0])
        end_long = math.radians(pos2[1])
        d_lat = end_lat - start_lat
        d_long = end_long - start_long
        a = math.sin(d_lat/2)**2 + math.cos(start_lat) * math.cos(end_lat) * math.sin(d_long/2)**2
        c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
        return 6371 * c *1000

    def __getTimeDiff(self,time1,time2):
        if time1 >= time2:
            dt = time1 - time2
        else:
            dt = time2 - time1
        dtSec = dt.days*24*60*60 + dt.seconds + dt.microseconds/1000000
        return dtSec

    def calculate_initial_compass_bearing(self,pointA, pointB):
        """
        Calculates the bearing between two points.
        The formulae used is the following:
            θ = atan2(sin(Δlong).cos(lat2),
                      cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
        :Parameters:
          - `pointA: The tuple representing the latitude/longitude for the
            first point. Latitude and longitude must be in decimal degrees
          - `pointB: The tuple representing the latitude/longitude for the
            second point. Latitude and longitude must be in decimal degrees
        :Returns:
          The bearing in degrees
        :Returns Type:
          float
        """
        if (type(pointA) != tuple) or (type(pointB) != tuple):
            raise TypeError("Only tuples are supported as arguments")

        lat1 = math.radians(pointA[0])
        lat2 = math.radians(pointB[0])

        diffLong = math.radians(pointB[1] - pointA[1])

        x = math.sin(diffLong) * math.cos(lat2)
        y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                * math.cos(lat2) * math.cos(diffLong))

        initial_bearing = math.atan2(x, y)

        # Now we have the initial bearing but math.atan2 return values
        # from -180° to + 180° which is not what we want for a compass bearing
        # The solution is to normalize the initial bearing as shown below
        initial_bearing = math.degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360

        return compass_bearing
