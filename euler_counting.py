def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1,n + 1):
        res *= i
    return res

def permutation(n, r):
    res = n
    for i in range(n - r + 1, n):
        res *= i
    return res

def combination(n, r):
    if r > (n - r):
        return combination(n, n - r)
    res = 1
    for i in range(n - r + 1, n + 1):
        res *= i
    res = res // factorial(r)
    return res

def getCombinations(symbols):
    return list(set(_getComboHelp([], sorted(symbols))))

def _getComboHelp(base, other):
    combos = []
    if len(other) == 1:
        return [''.join(base) + other[0]]
    for item in other:
        newb = base[:]
        newo = other[:]
        newb.append(item)
        newo.remove(item)
        combos.extend(_getComboHelp(newb, newo))
    return combos

def arePermutations(l1, l2):
    if len(l1) != len(l2):
        return False
    l1dict = dict()
    for n in l1:
        l1dict[n] = l1dict.get(n, 0) + 1
    for n in l2:
        if l1dict.get(n, 0) < 1:
            return False
        else:
            l1dict[n] -= 1
    return True

def integerPartition(base):
    optarr = [1]
    for i in range(1, base + 1):
        result = 0
        j = 1
        nextind = i - polygonal(negSwap(j), 5)
        while nextind >= 0:
            result += ((-1) ** (((j + 1) // 2) - 1)) * optarr[nextind]
            j += 1
            nextind = i - polygonal(negSwap(j), 5)
        optarr.append(result)
    return optarr[base]

def integerPartitionMemo(base, memo):
    # prepend a 1 to your memo
    for i in range(len(memo), base + 1):
        result = 0
        j = 1
        nextind = i - polygonal(negSwap(j), 5)
        while nextind >= 0:
            result += ((-1) ** (((j + 1) // 2) - 1)) * memo[nextind]
            j += 1
            nextind = i - polygonal(negSwap(j), 5)
        memo.append(result)
    return memo[base]

def simplex(n, r):
    return combination(n + r - 1, r)

def polygonal(n, s):
    return ((n ** 2) * (s - 2) - n * (s - 4)) // 2

def negSwap(k):
    return ((-1) ** (k - 1)) * ((k + 1) // 2)
