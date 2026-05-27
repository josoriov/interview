"""
LeetCode 12. Integer to Roman

Approach:
- Greedy algorithm: iterate through value-symbol pairs from largest to
  smallest, including subtractive cases (CM, CD, XC, XL, IX, IV).
- For each value, append its symbol as many times as it fits into the
  remaining number, then subtract.

Time: O(1) — the number of entries is fixed (13)
Space: O(1)
"""


def intToRoman(num: int) -> str:
    value_symbols = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
        (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
        (1,    "I"),
    ]

    remaining = num
    roman_number = ""

    for value, symbol in value_symbols:
        while remaining >= value:
            roman_number += symbol
            remaining -= value

    return roman_number