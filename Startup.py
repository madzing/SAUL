import time
from ReadSerial import ReadSerial
from Sensors import Sensors
from Nav import Nav
from Sailor import Sailor

sensorService = Sensors()
nav = Nav(SensorService,"Wegpunkte.txt","WegpunkteLog.txt")
sailor = Sailor(SensorService)

serialRead = ReadSerial("/dev/ttyAMA0",9600,"$GPRMC.log","w")
serialRead.setDaemon(True)
serialRead.start()

while true():
    runTime = time.time()
    ##################################################---> Hauptschleifeninhalt
    sensorService.setAllValues()
    DesiredBearing = nav.getDesiredBearing(1)
    sailor.sail(DesiredBearing)
    ##################################################<--- Hauptschleifeninhalt
    endTime = time.time()
    wait = round((1/50)-(endTime-runTime),5)
    if wait > 0:
        time.sleep(wait)

serialRead.stop()
serialRead.join()
