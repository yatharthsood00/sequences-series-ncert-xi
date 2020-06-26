n = 2  		#same as the question
t = [1] 	#first term as given
i = 5 		#number of terms to find out
while (n <= i):
	t.append(t[n - 2] + 2)
	n = n + 1
for val in range(len(t)):
	print(t[val])	