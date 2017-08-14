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
from math import floor, sqrt
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


def isPandigital(n, digits='123456789'):
    """
    :param n: The number to check if it contains all of the numbers in :param digits once
    :param digits: a string containing the numbers to check for pandigital numbers
    :return: Boolean
    """
    t = digits
    x = str(n)
    for i in x:
        digits = digits.replace(i, '')
    return len(x) == len(t) and len(digits) == 0


def day(year, month, day):
    """
    Gauss' Algorithm to determine the day of the week
        https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

        w = (d + floor(2.6 * m - 0.2) + y + floor(y / 4) + floor(c / 4) - 2 * c) mod 7

        Y is the year minus 1 for January or February, and the year for any other month
        y is the last 2 digits of Y
        c is the first 2 digits of Y
        d is the day of the month (1 to 31)
        m is the shifted month (March=1,...,February=12)
    w is the day of week (0=Sunday,...,6=Saturday). If w is negative you have to add 7 to it.
    """
    if month < 3:
        year -= 1
    m = (month - 3) % 12 + 1
    y = year % 100
    c = (year - (year % 100)) / 100

    return int((day + floor(2.6 * m - .02) + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7)


def sumDiv(num):
    """
    :param num:
    :return: the sum of the divisors of the passed in number
    """
    x = 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            if i == num / i:
                x += i
            else:
                x += i + num / i
    return int(x + 1)
