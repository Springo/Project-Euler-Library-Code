"""
AUTHOR: Kevin Xia

PURPOSE:
    Create a general-use library for generic algorithms.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

# =============================================================================

def binarySearch(li, val):
    """
    Returns the index of the first occurrence of val within the sorted list, li.
    Returns -1 if element is not found.
    """
    bot = 0
    top = len(li)
    mid = (bot + top) // 2
    found = -1
    done = False
    while not done and bot < top:
        if li[mid] < val:
            bot = mid + 1
        elif li[mid] == val:
            found = mid
            if found == 0 or li[found - 1] != li[found]:
                done = True
            else:
                top = mid
        else:
            top = mid
        mid = (bot + top) // 2
    if bot >= top:
        return -1
    return found

def isSquare(n):
    """Returns True if n is a perfect square."""
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True
