'''The Fibonacci sequence is defined by.... Find A(n+1)/A(n) for n = 1 - 5'''

from fractions import Fraction

terms, n = [1, 1], 5

[terms.append(terms[i+1] + terms[i]) for i in range(n + 1)]
[print(Fraction(terms[i+1]/terms[i]).limit_denominator(100)) for i in range(n)]
