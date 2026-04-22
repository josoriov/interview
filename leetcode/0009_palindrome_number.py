"""
LeetCode 9. Palindrome Number

Approach:
- Reject negative numbers because the leading '-' cannot be mirrored.
- Compare the digits from both ends, either by reversing digits or by using a
  string representation.
- Return True only when the number reads the same forward and backward.

Time: O(d), where d is the number of digits in x.
Space: O(d) if using a string representation, or O(1) if reversing digits.
"""


def isPalindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome.

    Args:
        x: Integer to check.

    Returns:
        True if x reads the same forward and backward, otherwise False.
    """
    if str(x) == str(x)[::-1]:
        return True
    return False

