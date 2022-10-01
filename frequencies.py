"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        if isinstance(i, int):
            frequencies[str(i)] = items.count(i) + items.count(str(i))

        elif isinstance(i, str) and i not in frequencies:
            frequencies[i] = items.count(i)
    return frequencies