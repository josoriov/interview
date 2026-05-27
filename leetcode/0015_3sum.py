"""
LeetCode 15. 3Sum

Approach:
- Sort the array so duplicates can be skipped and the two-pointer
  technique can be applied.
- For each unique first element, use left and right pointers to find a
  complementary pair that sums to -nums[i].
- Skip duplicate values at every level (first element, left, right) to
  avoid returning duplicate triplets.
- Break early when nums[i] > 0 — no three positives can sum to zero.

Time: O(n^2)
Space: O(1) (excluding output)
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums_sorted = sorted(nums)
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
            continue
        if nums_sorted[i] > 0:
            break
        left = i + 1
        right = n - 1
        while left < right:
            sum_3 = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            if sum_3 < 0:
                left += 1
            elif sum_3 > 0:
                right -= 1
            else:
                result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                left += 1
                right -= 1
                while left < right and nums_sorted[left] == nums_sorted[left-1]:
                    left += 1
                while left < right and nums_sorted[right] == nums_sorted[right+1]:
                    right -= 1

    return result
