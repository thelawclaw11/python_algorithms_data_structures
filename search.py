class Solution:
    def search(self, nums, target):

        pivot_index = 0

        if len(nums) == 1:
            pivot_index = 0
        else:
            pivot_index = find_pivot(nums)

        index = -1

        if nums[pivot_index] <= target <= nums[len(nums) - 1]:
            index = binary_search(nums, target, pivot_index, len(nums) - 1)
        elif nums[0] <= target <= nums[pivot_index - 1]:
            index = binary_search(nums, target, 0, pivot_index - 1)

        return index

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


def binary_search(nums, target, left, right):
    mid = (left + right) // 2

    if target == nums[mid]:
        return mid

    if left > right:
        return -1

    if target < nums[mid]:
        return binary_search(nums, target, left, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, right)


solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(solution.search([1], 0))

# print(find_pivot([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# print(find_pivot([9, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(find_pivot([8, 9, 1, 2, 3, 4, 5, 6, 7]))
# print(find_pivot([7, 8, 9, 1, 2, 3, 4, 5, 6]))
# print(find_pivot([6, 7, 8, 9, 1, 2, 3, 4, 5]))
# print(find_pivot([5, 6, 7, 8, 9, 1, 2, 3, 4]))
# print(find_pivot([4, 5, 6, 7, 8, 9, 1, 2, 3]))
# print(find_pivot([3, 4, 5, 6, 7, 8, 9, 1, 2]))
# print(find_pivot([2, 3, 4, 5, 6, 7, 8, 9, 1]))

# print(find_pivot([1, 2, 3, 4, 5, 6, 7, 8, 9]))
