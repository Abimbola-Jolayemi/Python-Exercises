def cylinder(radius, length):
	area = 3.14159 * radius ** 2
	volume = area * length
	return area, volume

print(cylinder(2, 4))