"""
LeetCode 11. Container With Most Water

Approach:
- Use two pointers starting at both ends of the array.
- At each step compute the area formed by the two lines; update the
  maximum if the current area is larger.
- Move the pointer pointing to the shorter line inward — the wider
  container can only hold more water if a taller wall is found.
- Repeat until the two pointers meet.

Time: O(n)
Space: O(1)
"""


def maxArea(height: list[int]) -> int:
    curr_max = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Update curr_max
        volume = min(height[left], height[right]) * (right - left)
        if volume > curr_max:
            curr_max = volume

        # update pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return curr_max