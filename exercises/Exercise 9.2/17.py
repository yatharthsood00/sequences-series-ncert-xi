'''A man starts repaying a loan as first instalment of Rs. 100. If he increases the
instalment by Rs 5 every month, what amount he will pay in the 30th instalment?'''

vals, d, nos = [100], 5, 30
[vals.append((vals[0] + d*i)) for i in range(1, nos)]
print(f"Amount in {nos}th installment = Rs {vals[nos - 1]}")