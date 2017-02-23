"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
answer: 232792560
"""
def smallest(data):
    for i in xrange(1,20,1):
        if data%i != 0:
            return False
    return True

i = 2520
while not smallest(i):
    i += 2520;
print("final")
print i