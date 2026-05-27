"""
LeetCode 14. Longest Common Prefix

Approach:
- Find the shortest string in the list (the longest possible prefix
  cannot exceed its length).
- For each prefix length from 1 to len(shortest), check whether every
  string in the list starts with that prefix.
- Keep track of and return the longest prefix that matches all strings.

Time: O(n * m) where n = len(strs), m = len(shortest string)
Space: O(1)
"""


def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    small = min(strs, key=len)
    small_len = len(small)
    array_len = len(strs)
    for i in range(1, small_len + 1):
        prefix = small[:i]
        if array_len == sum([prefix == x[:i] for x in strs]):
            result = prefix

    return result

test = ["flower","flow","flight"]
longestCommonPrefix(test)