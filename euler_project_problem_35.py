""" Problem 35
"""

import math

# get all primes under 1000000

primes = []

def is_prime_iterative(number, primes):
    for i in primes:
        if number % i == 0:
            return False
    return True

for i in xrange(2, 1000000):
    if is_prime_iterative(i, primes):
        primes.append(i)

print 'I\'m done with primes calculation!'
        
def get_rotations(number):
    rotations = set()
    for i in xrange(len(str(number))):
        rotations.add(int((number % 10 ** i) * 10 ** (len(str(number)) - i) + math.floor(number / 10 ** i)))
    return rotations

prime_rotations = set()

for i in xrange(2, 1000000):
    is_prime = True
    for rotation in get_rotations(i):
        if rotation not in primes:
            is_prime = False
    if is_prime:
        prime_rotations = prime_rotations | get_rotations(i)
    if i % 100000 == 0:
        print 'I\'ve finished ', i, ' iterations!'

print len(prime_rotations)
