'''Example 7:  The income of a person is Rs. 3,00,000, in the first year and he receives an
increase of Rs.10,000 to his income per year for the next 19 years. Find the total
amount, he received in 20 years'''

inc = [300000]
time = 19
[inc.append(inc[i] + 10000) for i in range(time)]
print(sum(inc))