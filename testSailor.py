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

'''Test4
Fahren hoch am Wind! Daher kann der Kurs nicht gefahren werden,
stattdessen wird 30 grad am Wind gefahren!
Erwartungshaltung: Schiff soll nichts ändern!
'''
sens = Sensors()
sailor = Sailor(sens)

print ("\nTest4: Erwartungshaltung: Schiff soll nichts ändern!")
desiredBearing = Bearing(0)
sens.setWindDirection(0)
sens.setCompassBearing(30)
sens.setWinkelgesch(0)
sens.setCourseMadeGood(30)
sens.setMeanCompassBearing(30)

sailor.sail(desiredBearing)

'''Test5
Wende machen! 
'''
sens = Sensors()
sailor = Sailor(sens)

print ("\nTest5: Erwartungshaltung: Schiff soll weiter nach links (Backbord) fahren!")
desiredBearing = Bearing(270)
sens.setWindDirection(0)
sens.setCompassBearing(30)
sens.setWinkelgesch(0)
sens.setCourseMadeGood(30)
sens.setMeanCompassBearing(30)

sailor.sail(desiredBearing)


