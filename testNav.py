from Sensors import Sensors
from Nav import Nav
import math

sens = Sensors()
nav = Nav(sens,"Wegpunkte.txt","WegpunkteLog.txt")

print("Letzter Wegpunkt  : " + str(nav.lastWaypoint[1]) +" "+ str(nav.lastWaypoint[2]))
print("Nächster Wegpunkt : " + str(nav.nextWaypoint[1]) +" "+ str(nav.nextWaypoint[2]))
print("Schiffsposition   : " + str(nav.pos[0]) +" "+ str(nav.pos[1]))
print("Kurs von Start zu Ziel : " + str(nav.calculate_initial_compass_bearing((nav.lastWaypoint[1],nav.lastWaypoint[2]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
print("Direkter Kurs zum Ziel : " + str(nav.calculate_initial_compass_bearing((nav.pos[0],nav.pos[1]),(nav.nextWaypoint[1],nav.nextWaypoint[2])).bearing))
print("Vorgeschlagener Kurs : "+str(nav.getDesiredBearing(1).bearing))
