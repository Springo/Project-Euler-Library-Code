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
    while li[mid] != val and bot < top:
        if li[mid] < val:
            bot = mid + 1
        else:
            top = mid
        mid = (bot + top) // 2
    if bot >= top:
        return -1
    while mid > 0 and li[mid - 1] == val:
        mid -= 1
    return mid
