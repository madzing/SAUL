from Sailor import Sailor
from SensorsForTesting import Sensors
from Bearing import Bearing

'''Test1
Erwartungshaltung: Schiff soll nichts ändern!
'''
sens = Sensors()
sailor = Sailor(sens)

print ("\nTest1: Erwartungshaltung: Schiff soll nichts ändern!")
desiredBearing = Bearing(90)
sens.setWindDirection(0)
sens.setCompassBearing(90)
sens.setWinkelgesch(0)
sens.setCourseMadeGood(90)
sens.setMeanCompassBearing(90)

sailor.sail(desiredBearing)


'''Test2
Erwartungshaltung: Schiff soll nichts ändern!
'''
sens = Sensors()
sailor = Sailor(sens)

print ("\nTest2: Erwartungshaltung: Schiff soll nichts ändern!")
desiredBearing = Bearing(90)
sens.setWindDirection(0)
sens.setCompassBearing(100)
sens.setWinkelgesch(0)
sens.setCourseMadeGood(90)
sens.setMeanCompassBearing(100)

sailor.sail(desiredBearing)

'''Test3
Erwartungshaltung: Schiff soll weiter nach links (Backbord) fahren!
'''
sens = Sensors()
sailor = Sailor(sens)

print ("\nTest3: Erwartungshaltung: Schiff soll weiter nach links (Backbord) fahren!")
desiredBearing = Bearing(90)
sens.setWindDirection(0)
sens.setCompassBearing(100)
sens.setWinkelgesch(0)
sens.setCourseMadeGood(90)
sens.setMeanCompassBearing(95)

sailor.sail(desiredBearing)

