"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
copied algorithm from problem 7
"""
from math import sqrt, ceil
import numpy

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Inumpyut n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(int(n//3 + (n%6==2)), dtype=numpy.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=int(3*i+1|1)
            sieve[   int((k*k)/3)      ::2*k] = False
            sieve[int((k*k+4*k-2*k*(i&1))/3)::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0]+1)|1)]

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def main():
    # products = primesfrom2to(2e6)
    products = primesfrom2to(10)
    return(sum(products))

if __name__ == "__main__": main()
