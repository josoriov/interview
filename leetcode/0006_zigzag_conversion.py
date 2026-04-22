"""
LeetCode 6. Zigzag Conversion

Approach:
- Simulate the zigzag by walking through the rows one character at a time.
- Append each character to the current row, then move either downward or
  upward depending on the current direction.
- Once all characters are placed, concatenate the rows from top to bottom.

Time: O(n)
Space: O(n)
"""


def convert(s: str, numRows: int) -> str:
    """
    Build the zigzag row by row and then read the rows in order.

    The key idea is to keep track of:
    - the current row
    - whether we are moving down or up through the rows

    Edge case:
    - If there is only one row, the zigzag is identical to the original string.
    """
    if numRows == 1:
        return s

    rows = {}
    actual_row = 1
    desc = True

    for i in s:
        # Add the current character to the row we are currently visiting.
        rows[actual_row] = rows.get(actual_row, "") + i

        # move to the next row
        if desc == True:
            actual_row += 1
        else:
            actual_row -= 1

        # check and update the direction
        if actual_row == numRows:
            desc = False
        elif actual_row == 1:
            desc = True

    # Read the stored rows from top to bottom to build the final string.
    return "".join(rows.values())
