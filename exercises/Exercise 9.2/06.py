'''If the sum of a certain number of terms of the A.P. 25, 22, 19, … is 116. Find the
last term.'''

vals, ssum = [25, 22], 116
d = vals[1] - vals[0]
while sum(vals) != ssum:
	vals.append(vals[-1] + d)
else:
	print(f"The last term of the series for sum to be {ssum} = {vals[-1]}")