import fractions

primelist = []

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieveOfErat(n):
    primes = []
    numlist = [1] * n
    for i in range(2, n):
        if numlist[i] == 1:
            primes.append(i)
            for j in range(i, n, i):
                numlist[j] = 0
    return primes

def primeFactorize(n):
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
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def totientVals(n):
    faclist = set(primeFactorize(n))
    vals = [1]
    plist = [_ for _ in primelist if _ not in faclist and _ < n]
    vals.extend(_totientVHelp(1, n, plist))
    return sorted(vals)

def _totientVHelp(base, cap, plist):
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
    global primelist
    primelist = sieveOfErat(n)

primelist = sieveOfErat(100000)
