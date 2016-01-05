from ReadSerial import ReadSerial
from Sensors import Sensors
from Nav import Nav
from Sailor import Sailor
import time

sensorService = Sensors()
Nav = Nav(SensorService)


serialRead = ReadSerial("/dev/ttyAMA0",9600,"$GPRMC.log","w")
serialRead.setDaemon(True)
serialRead.start()

while true():
    runTime = time.time()
    ##################################################---> Hauptschleifeninhalt
    NewDesiredCompassBearing = Nav.calculateNewDesiredCompassBearing()

    ##################################################<--- Hauptschleifeninhalt
    endTime = time.time()
    wait = round((1/50)-(endTime-runTime),5)
    if wait > 0:
        time.sleep(wait)

serialRead.stop()
serialRead.join()
