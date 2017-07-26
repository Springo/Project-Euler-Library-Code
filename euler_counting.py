"""
AUTHOR: Kevin Xia

PURPOSE:
    Create a general-use library for counting problems.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

# =============================================================================

def factorial(n):
    """Computes and returns n!."""
    if n == 0:
        return 1
    res = 1
    for i in range(1,n + 1):
        res *= i
    return res

def permutation(n, r):
    """Computes and returns nPr."""
    res = n
    for i in range(n - r + 1, n):
        res *= i
    return res

def combination(n, r):
    """Computes and returns nCr."""
    if r > (n - r):
        return combination(n, n - r)
    res = 1
    for i in range(n - r + 1, n + 1):
        res *= i
    res = res // factorial(r)
    return res

def getCombinations(symbols):
    """Takes a list and returns all possible orderings of elements in the list."""
    return list(set(_getComboHelp([], sorted(symbols))))

def _getComboHelp(base, other):
    """Helper function for getCombinations."""
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
    """Check if two lists or strings are permutations of each other."""
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
    """Counts number of ways to partition an integer of base."""
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
    """integerPartition but with an inital memo"""
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
    """Computes and returns the rth element of the nth row of pascal's triangle."""
    return combination(n + r - 1, r)

def polygonal(n, s):
    """Computes and returns the nth s-gonal number."""
    return ((n ** 2) * (s - 2) - n * (s - 4)) // 2

def negSwap(k):
    """
    Returns an incremented list, where every element is paired with its negative
    counterpart.
    """
    return ((-1) ** (k - 1)) * ((k + 1) // 2)
