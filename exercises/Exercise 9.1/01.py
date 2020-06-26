'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: n*(n + 2) '''

n = 5	#required number of terms
terms = []
for i in range(1, n + 1): 
	terms.append((i*(i+2)))
for t in range(len(terms)):
	print(terms[t])
	