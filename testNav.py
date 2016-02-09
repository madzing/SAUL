from Sensors import Sensors
from Nav import Nav
import math
import unittest
import time
print("Test: Schiff fährt von Ost nach West")
print("\nS = ship, N = next waypoint, L = last waypoint")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,N,0,0,0,0,0,0,0,0,0,0,0,L,0]")
print("[0,0,0,0,0,0,0,0,S,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
sens = Sensors()
nav = Nav(sens,"Wegpunkte.txt","WegpunkteLog.txt")
nav.lastWaypoint = [0,53.872773,8.970337,500]
nav.nextWaypoint = [1,53.871963,8.775330,500]
nav.pos = [53.864271,8.864594]
print("Letzter Wegpunkt       : " + str(nav.lastWaypoint[1]) +" "+ str(nav.lastWaypoint[2]))
print("Nächster Wegpunkt      : " + str(nav.nextWaypoint[1]) +" "+ str(nav.nextWaypoint[2]))
print("Schiffsposition        : " + str(nav.pos[0]) +" "+ str(nav.pos[1]))
print("Abstand zum Track      : " + str(nav.getDistanceAndBearingDiffToTrackline()[0]))
print("Radius nextWaypoint    : " + str(nav.nextWaypoint[3]))
print("Kurs von Start zu Ziel : " + str(nav.calculate_initial_compass_bearing((nav.lastWaypoint[1],nav.lastWaypoint[2]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
print("Direkter Kurs zum Ziel : " + str(nav.calculate_initial_compass_bearing((nav.pos[0],nav.pos[1]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
nav.calculateNewDesiredBearing()
print("Vorgeschlagener Kurs   : "+str(nav.desiredBearing.bearing))

print("Test: Schiff fährt von West nach Ost")
print("\nS = ship, N = next waypoint, L = last waypoint")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,L,0,0,0,0,0,0,0,0,0,0,0,N,0]")
print("[0,0,0,0,0,0,0,0,S,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
sens = Sensors()
nav = Nav(sens,"Wegpunkte.txt","WegpunkteLog.txt")
nav.nextWaypoint = [0,53.872773,8.970337,500]
nav.lastWaypoint = [1,53.871963,8.775330,500]
nav.pos = [53.864271,8.864594]
print("Letzter Wegpunkt       : " + str(nav.lastWaypoint[1]) +" "+ str(nav.lastWaypoint[2]))
print("Nächster Wegpunkt      : " + str(nav.nextWaypoint[1]) +" "+ str(nav.nextWaypoint[2]))
print("Schiffsposition        : " + str(nav.pos[0]) +" "+ str(nav.pos[1]))
print("Abstand zum Track      : " + str(nav.getDistanceAndBearingDiffToTrackline()[0]))
print("Radius nextWaypoint    : " + str(nav.nextWaypoint[3]))
print("Kurs von Start zu Ziel : " + str(nav.calculate_initial_compass_bearing((nav.lastWaypoint[1],nav.lastWaypoint[2]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
print("Direkter Kurs zum Ziel : " + str(nav.calculate_initial_compass_bearing((nav.pos[0],nav.pos[1]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
nav.calculateNewDesiredBearing()
print("Vorgeschlagener Kurs   : "+str(nav.desiredBearing.bearing))

print("Test: Schiff fährt von West nach Ost, der Radius von nextWaypoint ist um Faktor 10 größer")
print("\nS = ship, N = next waypoint, L = last waypoint")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,L,0,0,0,0,0,0,0,0,0,0,0,N,0]")
print("[0,0,0,0,0,0,0,0,S,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
print("[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]")
sens = Sensors()
nav = Nav(sens,"Wegpunkte.txt","WegpunkteLog.txt")
nav.nextWaypoint = [0,53.872773,8.970337,5000]
nav.lastWaypoint = [1,53.871963,8.775330,5000]
nav.pos = [53.864271,8.864594]
print("Letzter Wegpunkt       : " + str(nav.lastWaypoint[1]) +" "+ str(nav.lastWaypoint[2]))
print("Nächster Wegpunkt      : " + str(nav.nextWaypoint[1]) +" "+ str(nav.nextWaypoint[2]))
print("Schiffsposition        : " + str(nav.pos[0]) +" "+ str(nav.pos[1]))
print("Abstand zum Track      : " + str(nav.getDistanceAndBearingDiffToTrackline()[0]))
print("Radius nextWaypoint    : " + str(nav.nextWaypoint[3]))
print("Kurs von Start zu Ziel : " + str(nav.calculate_initial_compass_bearing((nav.lastWaypoint[1],nav.lastWaypoint[2]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
print("Direkter Kurs zum Ziel : " + str(nav.calculate_initial_compass_bearing((nav.pos[0],nav.pos[1]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
nav.calculateNewDesiredBearing()
print("Vorgeschlagener Kurs   : "+str(nav.desiredBearing.bearing))



time.sleep(50000)
