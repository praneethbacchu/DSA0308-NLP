# Finite State Automaton to recognize strings ending with 'ab'

def fsa_ends_with_ab(string):
    """Return True iff the input string ends with 'ab'.

    Simplified implementation to reduce cognitive complexity.
    """
    return string.endswith('ab')


# Test cases
test_strings = [
    "ab",
    "aab",
    "aaab",
    "bab",
    "abab",
    "aba",
    "abb",
    "baa",
    "bbaab",
    "bbb"
]

for s in test_strings:
    if fsa_ends_with_ab(s):
        print(f"{s} --> Accepted")
    else:
        print(f"{s} --> Rejected")