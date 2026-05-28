"""
LeetCode 18. 4Sum

Approach:
- Sort the array so duplicates can be skipped and the two-pointer
  technique can be applied.
- Two nested outer loops fix the first two elements (i, j), then left
  and right pointers scan for the remaining two that hit the target.
- Dedup at every level — i, j, left, and right — to avoid returning
  duplicate quadruplets.

Time: O(n^3)
Space: O(1) (excluding output)
"""


def fourSum(nums: list[int], target: int) -> list[list[int]]:
    result = []
    nums_sorted = sorted(nums)
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums_sorted[j] == nums_sorted[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                sum_4 = (
                    nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right]
                )
                # update the pointers
                if sum_4 < target:
                    left += 1
                elif sum_4 > target:
                    right -= 1
                else:
                    result.append([
                        nums_sorted[i],
                        nums_sorted[j],
                        nums_sorted[left],
                        nums_sorted[right],
                    ])
                    left += 1
                    right -= 1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1

    return result



nums = [2,2,2,2,2]
target = 8
print(fourSum(nums, target))