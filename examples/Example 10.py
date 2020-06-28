'''Which term of the G.P., 2,8,32, ... up to n terms is 131072'''

fin, vals = 131072, [2,8,32]
r = int(vals[1]/vals[0])
while (vals[-1] != fin):
	vals.append(vals[-1]*r)
else:
	print((len(vals)))