'''Find the sum of all natural numbers lying between 100 and 1000, which are
multiples of 5.'''

vals, d = [100, 1000], 5
n = int(((vals[1] - vals[0])/d))
[vals.insert(- 1, (vals[i] + d)) for i in range(n - 1)]
print(sum(vals[1:-1]))