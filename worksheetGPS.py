from math import sin, cos, sqrt, atan2, radians, asin

class Gps:
	count = 0
	def __init__(self, longitude, latitude):
		self.longitude = longitude
		self.latitude = latitude




def print_distance(longitude, latitude, dest_longit, dest_latit):
	r = 6373000
	# rad_logngitude = radians(longitude)
	# rad_latitude = radians(longitude)
	# rad_dest_longit = radians(dest_longit)
	# rad_dest_latit = radians(dest_latit)


	# dlon =  radians(rad_dest_longit-rad_logngitude)
	# dlat = radians(rad_dest_latit-rad_latitude)
	# a = sin(dlat/2)**2+cos(rad_latitude)*sin(dlon/2)**2
	# c = 2*asin(sqrt(a))


	dlon = longitude - dest_longit
	dlat = latitude - dest_latit
	a = (sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2))**2
	c = 2*atan2(sqrt(a))


	dist = c * r
	return dist

c1 = Gps(42.990967,-71.463767)
c2 = Gps(44.991967,-71.463767)


print print_distance(c1.longitude, c1.latitude, c2.longitude, c2.latitude)