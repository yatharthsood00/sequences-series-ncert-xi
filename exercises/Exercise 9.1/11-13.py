'''Write the first five terms of each of the sequences Q11-13.'''

from fractions import Fraction

def make_the_series(no, problem):
	t, t1 = [], 0
	if problem == 11:
		t1 = 3
		t.append(t1)
		[t.append(3*t[i] + 2) for i in range(no)]
	elif problem == 12:
		t1 = - 1
		t.append(t1) 
		[t.append(t[i - 1]/i) for i in range(1, no)]
	elif problem == 13:
		t1 = 2
		t.append(t1)
		t.append(t1)
		[t.append(t[i - 1] - 1) for i in range(2, no)]	
	else: 
		print("Enter a question number between 11 to 13")
		exit()
	return t

def print_the_series(terms, no):
	[print(Fraction(terms[no]).limit_denominator(10**10), "+ ", end = "")  for no in range(n)]
	print("...")


prob = int(input("Enter problem number 11 to 13: "))
n = 5
print(f"Question No. {prob}, series up to {n} terms: ")
terms = make_the_series(n, prob)
print_the_series(terms, n)