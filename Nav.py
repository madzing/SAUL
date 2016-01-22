import math
from Sensors import *
from Bearing import Bearing
class Nav:
    """
    Waypoints ---> [ID,lat,lon,acceptableDeviation]
    """
    def __init__(self,sensorService,wegpunkte,wegpunkteLog):
        self.wegpunkte = wegpunkte
        self.wegpunkteLog = wegpunkteLog
        self.sensorService = sensorService
        self.lastWaypoint = [0,0,0,0]
        self.nextWaypoint = [0,0,0,0]
        self.checkWaypoints()
        self.pos =  self.sensorService.getPosition()
        self.lastCalculation = None
        self.desiredBearing = self.calculateNewDesiredBearing()

    def getDesiredBearing(self,calculateNewEveryXSeconds):
        self.pos = self.sensorService.getPosition()
        self.checkWaypoints()
        dateTime = self.sensorService.getDateTime()
        if  self.lastCalculation == None or getTimeDiff(lastCalculation, datetime) >= calculateNewEveryXSeconds:
            self.calculateNewDesiredBearing()
            self.lastCalculation = dateTime
        return self.desiredBearing

# Private Methods --->
    def calculateNewDesiredBearing(self):
        """
        variables to use:
        self.lastWaypoint
        self.nextWaypoint
        self.pos
        """
        self.desiredBearing = self.calculate_initial_compass_bearing((self.pos[0],self.pos[1]),(self.nextWaypoint[1],self.nextWaypoint[2]))
        distAndBearingDiffToTrack = self.getDistanceAndBearingDiffToTrackline()
        ausgleichswinkel = Bearing(math.degrees(math.atan(distAndBearingDiffToTrack[0] / self.nextWaypoint[3])))
        if math.fabs(distAndBearingDiffToTrack[1]) >= 90:
            self.desiredBearing = self.desiredBearing
        elif distAndBearingDiffToTrack[1] <0:
            self.desiredBearing = self.desiredBearing.add(-ausgleichswinkel.bearing)
        else:
            self.desiredBearing = self.desiredBearing.add(ausgleichswinkel.bearing)

    def getDistanceAndBearingDiffToTrackline(self):
        """

        """
        trackBearing = self.calculate_initial_compass_bearing((self.nextWaypoint[1],self.nextWaypoint[2]),(self.lastWaypoint[1],self.lastWaypoint[2]))
        bearingFromNextWaypoint = self.calculate_initial_compass_bearing((self.nextWaypoint[1],self.nextWaypoint[2]),(self.pos[0],self.pos[1]))
        alpha = trackBearing.getDiffTo(bearingFromNextWaypoint)
        valueAlpha = math.fabs(alpha)
        return (math.sin(math.radians(valueAlpha))*self.distanceCalc((self.nextWaypoint[1],self.nextWaypoint[2]),self.pos),alpha)

    def checkWaypoints(self):
        if self.lastWaypoint == [0,0,0,0] or self.nextWaypoint == [0,0,0,0]:
            self.getNewWaypoints()
        elif self.distanceCalc(self.pos,[self.nextWaypoint[1],self.nextWaypoint[2]])<=self.nextWaypoint[3]:
            fout = open(self.wegpunkteLog,"a")
            fout.write(self.nextWaypoint[0]+",")
            fout.flush()
            fout.close()
            self.getNewWaypoints()

    def getNewWaypoints(self):
        waypointLog = open(self.wegpunkteLog,"r")
        log_string = waypointLog.read()
        waypointLog.close()
        log_liste = log_string.split(",")
        if len(log_liste) == 0:
            ID_lastWaypoint = 0
        else:
            ID_lastWaypoint = int(log_liste[len(log_liste)-1])

        waypoints = open(self.wegpunkte,"r")
        waypoint_string = waypoints.read()
        waypoints.close()
        waypoint_liste = waypoint_string.split(";")
        if len(waypoint_liste) > ID_lastWaypoint:
            ID_nextWaypoint = ID_lastWaypoint + 1
        else:
            ID_nextWaypoint = ID_lastWaypoint
        self.nextWaypoint = waypoint_liste[ID_nextWaypoint-1].strip().split(" ")
        if ID_lastWaypoint > 0:
            self.lastWaypoint = waypoint_liste[ID_lastWaypoint-1].strip().split(" ")
        else:
            self.lastWaypoint = self.nextWaypoint
        for i in range(4):
            if i == 0 or i == 3:
                self.nextWaypoint[i] = int(self.nextWaypoint[i])
                self.lastWaypoint[i] = int(self.lastWaypoint[i])
            else:
                self.nextWaypoint[i] = float(self.nextWaypoint[i])
                self.lastWaypoint[i] = float(self.lastWaypoint[i])


    def distanceCalc(self,pos1,pos2):
        """
        returns distance in meters
        """
        start_lat = math.radians(pos1[0])
        start_long = math.radians(pos1[1])
        end_lat = math.radians(pos2[0])
        end_long = math.radians(pos2[1])
        d_lat = end_lat - start_lat
        d_long = end_long - start_long
        a = math.sin(d_lat/2)**2 + math.cos(start_lat) * math.cos(end_lat) * math.sin(d_long/2)**2
        c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
        return 6371 * c *1000

    def getTimeDiff(self,time1,time2):
        """
        returns time difference in seconds
        """
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

        return Bearing(compass_bearing)
