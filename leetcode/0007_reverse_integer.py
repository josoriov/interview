"""
LeetCode 7. Reverse Integer

Approach:
- Work with the absolute value of the input so the digit reversal is easier.
- Reverse the digits using string slicing.
- Reapply the original sign and return 0 if the result is outside the 32-bit
  signed integer range.

Time: O(d), where d is the number of digits in the integer.
Space: O(d)
"""


def reverse(x: int) -> int:
    """
    Reverse the digits of an integer while preserving its sign.

    This implementation converts the absolute value to a string, reverses its
    characters, converts it back to an integer, and then reapplies the sign.
    If the final value is outside the 32-bit signed integer range, return 0.
    """

    # Remember whether the original number was negative.
    is_neg = True if x < 0 else False

    # Reverse the digits of the absolute value.
    rev = str(abs(x))[::-1]

    # Restore the sign after the digits have been reversed.
    rev = "-"+rev if is_neg else rev
    rev = int(rev)

    # The problem requires returning 0 when the result overflows 32-bit range.
    if -(2**31) <= rev <= 2**31-1:
        return rev
    else:
        return 0

x = -123

print(reverse(x))
