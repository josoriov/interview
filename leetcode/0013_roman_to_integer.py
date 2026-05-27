"""
LeetCode 13. Roman to Integer

Approach:
- Map each Roman character to its integer value.
- Traverse the string comparing each adjacent pair; when the previous
  value is smaller than the current one, it signals a subtractive
  pattern (e.g. IV, IX) so subtract it, otherwise add it.
- After the loop add the very last character's value.

Time: O(n)
Space: O(1)
"""


def romanToInt(s: str) -> int:
    conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    i = 1
    result = 0
    while i < len(s):
        prev = s[i - 1]
        curr = s[i]
        # if the prev is less is subtracting
        if conversion[prev] < conversion[curr]:
            result -= conversion[prev]
        # if prev is bigger or equal it adds
        else:
            result += conversion[prev]

        i += 1
    result += conversion[s[i-1]]
    return result

test = "LVIII"
romanToInt(test)