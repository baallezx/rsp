import math
def _get_distance(vec_a, vec_b):
	return math.sqrt( ( vec_b[0] - vec_a[0] ) ** 2 + (vec_b[1] - vec_a[1]) ** 2 )

def get_points(vec_a, vec_b):
	"""
	return the points that intersect
	"""
	# a = (r02 - r12 + d2 ) / (2 d)
	distance = _get_distance( vec_a, vec_b )
	try:
		# a = (r02 - r12 + d2 ) / (2 d)
		a = (vec_a[2]**2 - vec_b[2]**2 + distance ** 2) / (2 * distance)
		# h**2 = r0**2 - a**2
		h = math.sqrt( vec_a[2] ** 2 - a ** 2 )
		# p2 = p0 + a ( p1 - p0 ) / d
		# where p0 = vec_a -and- p1 = vec_b 
		p2 = ( vec_a[0] + a*(vec_b[0] - vec_a[0]) / distance , vec_a[1] + a*(vec_b[1] - vec_a[1]) / distance )
	
		x0 = p2[0] + h * (vec_b[1] - vec_a[1]) / distance
		y0 = p2[1] - h * (vec_b[0] - vec_a[0]) / distance
	
		x1 = p2[0] - h * (vec_b[1] - vec_a[1]) / distance
		y1 = p2[1] + h * (vec_b[0] - vec_a[0]) / distance
		p3 = (x0, y0)
		p4 = (x1, y1)
		print p3[0], p3[1]
		if p4 != p3:
			print p4[0], p4[1]
	except:
		# circles do not have intersection points
		pass

if __name__ == "__main__":
	import sys
	l = sys.argv[1:]
	r = open(l[0],'r').read().split('\n')
	r.remove('')
	# print r
	vec_a = [float(i) for i in r[0].split(' ')]
	vec_b = [float(i) for i in r[1].split(' ')]
	# print vec_a, vec_b
	get_points(vec_a, vec_b)
