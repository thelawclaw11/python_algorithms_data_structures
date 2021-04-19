import math


class Solution:
    def findMin(self, nums):

        if len(nums) == 1:
            return nums[0]

        index = find_pivot(nums)
        return nums[index]


def find_pivot(nums, left=None, right=None):
    if left is None:
        left = 0

    if right is None:
        right = len(nums) - 1

    if nums[left] < nums[right]:
        return left

    if right - left == 1 and nums[left] > nums[right]:
        return right

    mid = (left + right) // 2

    if nums[left] > nums[mid]:
        return find_pivot(nums, left, mid)
    else:
        return find_pivot(nums, mid, right)


solution = Solution()
print(solution.findMin([3, 4, 5, 1, 2]))
