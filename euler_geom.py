"""
AUTHOR: Kevin Xia

PURPOSE:
    Create a general-use library for geometry problems.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

from fractions import gcd

# =============================================================================

def genPrimPythTriples(perimcap):
    """
    Uses Euclid's formula to generate all primitive pythagorean triples less than
    or equal to a perimeter bound.
    """
    cap = int(perimcap ** 0.5)
    triples = []

    for m in range(2, cap):
        for n in range(m % 2 + 1, m, 2):
            if gcd(m, n) == 1:
                a = (m ** 2) - (n ** 2)
                b = 2 * m * n
                c = (m ** 2) + (n ** 2)
                perim = a + b + c
                if perim <= perimcap:
                    triples.append(sorted([a, b, c]))
    return triples

def genPythTriples(perimcap):
    """
    Generates all pythagorean triples less than or equal to a perimeter bound.
    """
    prim_triples = genPrimPythTriples(perimcap)
    all_triples = prim_triples[:]
    for trip in prim_triples:
        mul = 2
        newperim = 0
        while newperim <= perimcap:
            newtrip = []
            newperim = 0
            for num in trip:
                newtrip.append(mul * num)
                newperim += mul * num
            if newperim <= perimcap:
                all_triples.append(newtrip)
            mul += 1
    return all_triples
