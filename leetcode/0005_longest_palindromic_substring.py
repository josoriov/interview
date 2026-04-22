"""
LeetCode 5. Longest Palindromic Substring

Approach:
- Treat each index as a possible center.
- Expand outward for both odd-length and even-length palindromes.
- Keep track of the longest palindrome found so far.

Time: O(n^2)
Space: O(1)
"""


def longestPalindrome(s: str) -> str:
    # Store the best palindrome seen so far.
    result = ""
    max_length = 0
    str_len = len(s)

    for i in range(str_len):
        # Odd-length palindromes have one character at the center.
        l, r = i, i
        while l >= 0 and r < str_len and s[l] == s[r]:
            current_length = r - l + 1
            if current_length > max_length:
                result = s[l : r + 1]
                max_length = current_length

            l -= 1
            r += 1

        # Even-length palindromes have a center between two characters.
        l, r = i, i + 1
        while l >= 0 and r < str_len and s[l] == s[r]:
            current_length = r - l + 1
            if current_length > max_length:
                result = s[l : r + 1]
                max_length = current_length

            l -= 1
            r += 1

    return result
