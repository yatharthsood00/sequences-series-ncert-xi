'''The difference between any two consecutive interior angles of a polygon is 5°.
If the smallest angle is 120° , find the number of the sides of the polygon.'''

vals, d = [120], 5
while ((len(vals) - 2)*180 != sum(vals)) or len(vals) < 2:
	vals.append(vals[-1] + d)
print(f"Number of sides = {len(vals)}")