#!/usr/bin/python
import smbus
import time
import math
import HMC5883L

compass = HMC5883L.HMC5883L(0x1e, 1)
print "Address of compass: ", hex(compass.address)
compass.set_mode('cont')
compass.set_res(8)
print "Angle between magnetic field in x-y-plane and x-axis:"

while True:
	time.sleep(0.5)
	print compass.get_act_bir()
