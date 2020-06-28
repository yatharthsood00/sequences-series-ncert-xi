'''Find the sum of odd integers from 1 to 2001'''

vals, d = [1, 2001], 2
n = int(((vals[1] - vals[0])/d))
[vals.insert(-1, (vals[i] + d)) for i in range(n - 1)]
print(sum(vals))