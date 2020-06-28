''' Find the 10th term of the G.P. 5, 25,125,…'''

vals, no = [5,25,125], 10
r = int(vals[1]/vals[0])
[vals.append(vals[-1]*r) for i in range(len(vals), no)]
[print(vals[i]) for i in range(len(vals))]