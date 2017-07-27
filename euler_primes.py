"""
AUTHOR: Kevin Xia and Ian Renfro

PURPOSE:
    Create a general-use library for number theory problems.

DEVELOPER NOTES:
    When using any of these functions, make sure to call setPrimeList to generate
    a memo of prime numbers for this script. Use the a limit higher than the highest
    prime number than you think you will need. Internal prime list is set to store
    all prime numbers below 100,000 by default.
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import fractions
from math import sqrt
primelist = []

# =============================================================================

def isPrime(n):
    """Checks if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieveOfErat(high):
    """Returns a list of all primes up to n."""
    primes = []
    numlist = [1] * high
    for i in range(2, high):
        if numlist[i] == 1:
            primes.append(i)
            for j in range(i, high, i):
                numlist[j] = 0
    return primes

def rangedSieveOfErat(i, j):
    """
    :param i: lower number of the range
    :param j: higher number of the range
    :return: returns the set of primes within the range of numbers
    """
    primes = sieveOfErat(int(sqrt(j)))
    return [n for n in range(i, j) if all(n % p for p in primes)]

def primeFactorize(n):
    """Returns a sorted list of all prime factors of n."""
    faclist = []
    num = n
    ind = 0
    while num > 1:
        if num % primelist[ind] == 0:
            faclist.append(primelist[ind])
            num = num / primelist[ind]
        else:
            ind += 1
    return faclist

def totient(n):
    """Returns the number of integers below n that are relatively prime to n."""
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def totientFromSieve(n):
    """Returns an entry from totientlist."""
    global totientlist
    return totientlist[n]

def totientSieve(n):
    """Returns a list of all totient values up to n."""
    phi = [0] * n
    phi[1] = 1
    for i in range(2, n):
        if phi[i] == 0:
            phi[i] = i - 1
            j = 2
            while i * j < n:
                if phi[j] == 0:
                    j += 1
                    continue
                q = j
                f = i - 1
                while q % i == 0:
                    f = f * i
                    q = q // i
                phi[i * j] = f * phi[q]
                j += 1
    return phi

def totientVals(n):
    """Returns a list of all integers below n that are relatively prime to n."""
    faclist = set(primeFactorize(n))
    vals = [1]
    plist = [_ for _ in primelist if _ not in faclist and _ < n]
    vals.extend(_totientVHelp(1, n, plist))
    return sorted(vals)

def _totientVHelp(base, cap, plist):
    """Helper function for totientVals."""
    curlist = []
    nlist = plist[:]
    for p in plist:
        baseup = p * base
        if baseup <= cap:
            curlist.append(baseup)
            newplist = nlist[:]
            curlist.extend(_totientVHelp(baseup, cap, newplist))
        nlist.remove(p)
    return curlist

def setPrimeList(n):
    """Sets the internal prime number list for other functions."""
    global primelist
    primelist = sieveOfErat(n)

def setTotientList(n):
    """Sets the internal totient list for other functions."""
    global totientlist
    totientlist = totientSieve(n)

primelist = sieveOfErat(100000)
totientlist = totientSieve(10000)
