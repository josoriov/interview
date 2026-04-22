"""
LeetCode 10. Regular Expression Matching

Approach:
- Use dynamic programming to track whether prefixes of s and p match.
- Treat '.' as a wildcard that matches any single character.
- Treat '*' as matching zero or more occurrences of the previous pattern
  character.
- The answer is whether the full string matches the full pattern.

Time: O(m * n), where m is the length of s and n is the length of p.
Space: O(m * n)
"""


def isMatch(s: str, p: str) -> bool:
    """
    Return whether the entire string matches the given pattern.

    The pattern supports:
    - '.' to match any single character.
    - '*' to match zero or more of the previous pattern character.

    Args:
        s: Input string to match.
        p: Pattern containing lowercase letters, '.', and '*'.

    Returns:
        True if the whole string matches the whole pattern, otherwise False.
    """
    m, n = len(s), len(p)

    # cache[i][j] = whether s[:i] matches p[:j].
    cache = [[False] * (n + 1) for _ in range(m + 1)]
    cache[0][0] = True

    # Initialize patterns that can match the empty string, such as:
    # "a*", "a*b*", or ".*".
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            cache[0][j] = cache[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                cache[i][j] = cache[i - 1][j - 1]

            elif p[j - 1] == "*":
                # Zero occurrences: ignore the previous char and '*'.
                cache[i][j] = cache[i][j - 2]

                # One or more occurrences: if the previous pattern char matches
                # the current string char, consume one char from s and keep the
                # same pattern because '*' can be reused.
                prev = p[j - 2]
                if prev == "." or prev == s[i - 1]:
                    cache[i][j] = cache[i][j] or cache[i - 1][j]

    return cache[m][n]


if __name__ == "__main__":
    assert isMatch("aab", "c*a*b") is True
    assert isMatch("aa", "a") is False
    assert isMatch("aa", "a*") is True
    assert isMatch("ab", ".*") is True
