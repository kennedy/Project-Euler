"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*** using algorithm in http://stackoverflow.com/a/3436152
"""
b = 0
for a in range(1, 500):
    if 1000*(500-a) % (1000-a) == 0:
        b = int(1000*(500-a) / (1000-a))
        print(a, b)
        break
c = 1000 - a - b
print(c)
print(c*b*a)
