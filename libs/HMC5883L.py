#!/usr/bin/python
import smbus
import time
import math

def get_sum(a, b):
	return a+b

class HMC5883L():
	def __init__(self, address, bus):
		self.address = address
		self.bus = bus
		self.HMC5883L = smbus.SMBus(self.bus)
		self.dig_res  = 0.92 #mG/lsb
	
	def get_X(self):
		reg03 = self.HMC5883L.read_byte_data(self.address, 0x03)
		reg04 = self.HMC5883L.read_byte_data(self.address, 0x04)
	
		return self.convert_2c(reg03*256+reg04)

	def get_Y(self):
		reg05 = self.HMC5883L.read_byte_data(self.address, 0x07)
		reg06 = self.HMC5883L.read_byte_data(self.address, 0x08)
	
		return self.convert_2c(reg05*256+reg06)

	def get_Z(self):
		reg07 = self.HMC5883L.read_byte_data(self.address, 0x05)
		reg08 = self.HMC5883L.read_byte_data(self.address, 0x06)
	
		return self.convert_2c(reg07*256+reg08)

	def get_stat(self):
		reg09 = self.HMC5883L.read_byte_data(self, 0x09)
		return reg09

	def get_RDY(self):
		reg09 = self.HMC5883L.read_byte_data(self, 0x09)
		RDY = (reg09%2)	
		return RDY

	def get_act_bir(self):
		#returns angle between magnetic field in x-y-plane and x axis
		x = self.get_X() 
		y = self.get_Y() 
		z = self.get_Z()
		
		phi = math.atan2(y, x)
		return math.degrees(phi)
	
	def convert_2c(self, val):
		if (val >= 32767+1):
			return -((65535 - val) + 1)
		else:
			return val

	def set_nos(self, nos):
		#sets number of samples/measurements which are taken and avaraged
		CRA = self.HMC5883L.read_byte_data(self, 0x00)

		if (nos == 1):
			MA0 = 0
			MA1 = 0
		elif (nos == 2):
			MA0 = 1
			MA1 = 0
		elif (nos == 4):
			MA0 = 0
			MA1 = 1
		elif (nos == 8):
			MA0 = 1
			MA1 = 1
		else:
			print "Error, set not allowed resoltution in set_nos!"
			return 0
	
		CRA = self.set_bit(CRA, 5, MA0)
		CRA = self.set_bit(CRA, 6, MA1)
		self.MC5883L.write_byte_data(self, 0x00, CRA)
		return 1

	def set_isc_speed(self, speed):
		#set I2C speed, high=3400 kHz, low=???? (default)
		CRM = self.HMC5883L.read_byte_data(self, 0x02)
		if (speed == high):
			CRM = self.set_bit(CRM, 7, 1)
		elif (speed == low):
			CRM = self.set_bit(CRM, 7, 0)
		else:
			print "Error, set not allowed i2c speed in set_i2c_speed!"
			return 0

		self.HMC5883L.write_byte_data(self, 0x02, CRM)
		return 1


	def set_mode(self, mode):
		#sets measureing mode of sensor, options: single, cont, idle
		CRM = self.HMC5883L.read_byte_data(self.address, 0x02)
		if (mode == "single"):
			MR1 = 0
			MR0 = 1
		elif (mode == "cont"):
			MR1 = 0
			MR0 = 0
		elif (mode == "idle"):
			MR0 = 1
			MR1 = 1
		else:
			print "Error, set not allowed mode in set_mode!"
			return 0

		CRM = self.set_bit(CRM, 0, MR0)
		CRM = self.set_bit(CRM, 1, MR1)
		self.HMC5883L.write_byte_data(self.address, 0x02, CRM)
		return 1

	def set_res(self, res):
		# setting resolution of sensor res=1: +/-1.3 Ga, dig_res= 0.92 mG/lsb 
		CRB = res*32
		self.HMC5883L.write_byte_data(self.address, 0x01, CRB)
		if (res == 0):
			self.dig_res = 0.73 #mG/lsb
		if (res == 1):
			self.dig_res = 0.92 #mG/lsb
		if (res == 2):
			self.dig_res = 1.22 #mG/lsb
		if (res == 3):
			self.dig_res = 1.52 #mG/lsb
		if (res == 4):
			self.dig_res = 2.27 #mG/lsb
		if (res == 5):
			self.dig_res = 2.56 #mG/lsb
		if (res == 6):
			self.dig_res = 3.03 #mG/lsb
		if (res == 7):
			self.dig_res = 4.35 #mG/lsb
		return self.dig_res

	def set_bit(self, byte, bit, val):
		# sets 'bit' in 'bytes' to val (0,1)    	
		if val:
			return byte | (1<<bit)
		if not val:
			return byte & ~(1<<bit)
