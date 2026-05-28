"""
LeetCode 16. 3Sum Closest

Approach:
- Sort the array so the two-pointer technique can be applied and
  duplicate first elements can be skipped.
- For each unique first element, use left and right pointers to find
  the sum closest to target, updating the best match whenever a
  nearer distance is found.
- Move pointers inward based on whether the current sum is too small
  or too large; return immediately if the sum exactly equals target.

Time: O(n^2)
Space: O(1)
"""


def threeSumClosest(nums: list[int], target: int) -> int:
    closest = float("inf")
    closest_dist = float("inf")
    nums_sorted = sorted(nums)
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            sum_3 = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            dist = abs(sum_3 - target)
            # update the closest
            if dist < closest_dist:
                closest = sum_3
                closest_dist = dist
            # update the pointers
            if sum_3 < target:
                left += 1
            elif sum_3 > target:
                right -= 1
            else:
                return sum_3

    return int(closest)


nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))