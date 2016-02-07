from Sailor import Sailor
from Sensors import Sensors
from Bearing import Bearing

sens = Sensors()
sailor = Sailor(sens)

sailor.sail(Bearing(30))
