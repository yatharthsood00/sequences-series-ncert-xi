''' A person has 2 parents, 4 grandparents, 8 great grandparents, and so on.
Find the number of his ancestors during the ten generations preceding his own.'''

vals, no = [2,4], 10
r = vals[1]/vals[0]
[vals.append(vals[-1]*r) for i in range(2, no)]
print(int(sum(vals)))