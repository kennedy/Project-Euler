"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
highest = 600851475143
lpf = 3
while lpf < highest:
    if highest % lpf == 0:
        highest = highest / lpf
        lpf += 2
    else:
        lpf += 2
print lpf

