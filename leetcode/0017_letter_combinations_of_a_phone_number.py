"""
LeetCode 17. Letter Combinations of a Phone Number

Approach:
- Map each digit to its corresponding list of letters.
- Collect the letter lists for every digit in the input, then compute
  the Cartesian product of those lists with itertools.product.
- Join each resulting tuple into a string.

Time: O(4^n * n) — at most 4 letters per digit, n digits
Space: O(4^n * n) — number of combinations times string length
"""


def letterCombinations(digits: str) -> list[str]:
    from itertools import product
    conversion = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "0": []
    }

    # digits_split = list(digits)
    list_to_combine = []
    for i in digits:
        list_to_combine.append(conversion[i])

    result = [''.join(comb) for comb in product(*list_to_combine)]
    return result