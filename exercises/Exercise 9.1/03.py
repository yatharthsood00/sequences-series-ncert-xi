'''Q. Write the first five terms of each of the sequences in Exercises 1 to 6 whose nth
terms are: 2^n'''

n = 5
terms = []
for i in range(1, n + 1):
	t = (2**i)
	terms.append(t)
for no in range(len(terms)):
	print(terms[no])