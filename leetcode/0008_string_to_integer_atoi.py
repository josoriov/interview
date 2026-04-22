"""
LeetCode 8. String to Integer (atoi)

Approach:
- Strip leading whitespace before processing the meaningful characters.
- Check the first remaining character for an optional '+' or '-' sign.
- Collect consecutive digits until a non-digit character is reached.
- Convert the collected digits, apply the sign, and clamp the result to the
  32-bit signed integer range.

Time: O(n)
Space: O(1)
"""


def myAtoi(s: str) -> int:
    """
    Convert a string to a 32-bit signed integer following atoi rules.

    Leading whitespace is ignored. After that, the function accepts one optional
    sign character, parses the consecutive digit characters that follow, and
    stops as soon as another character appears. If no digits are found, it
    returns 0.

    Args:
        s: Input string to parse.

    Returns:
        The parsed integer clamped to the range [-2^31, 2^31 - 1].
    """
    max_int = 2**31 - 1
    min_int = -2**31
    is_neg = False
    s = s.lstrip()
    to_convert = ""
    digits = "0123456789"

    # Check that it is signed
    if s == "":
        pass
    elif s[0] == "-":
        is_neg = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    else:
        pass
    
    # Add digits to the string to convert
    for i in s:
        if i not in digits:
            break
        to_convert += i

    if to_convert == "":
        return 0
    unbounded = -1*int(to_convert) if is_neg else int(to_convert)

    return max(min(max_int, unbounded), min_int)
