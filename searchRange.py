class Solution:
    def searchRange(self, nums, target):

        if len(nums) == 0:
            return [-1, -1]

        index = self.binary_search(nums, target, 0, len(nums) - 1)

        if index is None:
            return [-1, -1]

        start = index
        end = index

        for i in range(index, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break

        for i in range(index, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break

        return [start, end]

    def binary_search(self, nums, target, left, right):

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if left > right:
            return None

        if target < nums[mid]:
            return self.binary_search(nums, target, left, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, right)


solution = Solution()

# print(solution.searchRange([5, 7, 7, 8, 8,  10], 8))
#
# print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
#
# print(solution.searchRange([], 0))

print(solution.searchRange([1, 1, 2], 1))

# class Solution:
#     def searchRange(self, nums, target):
#
#         start = -1
#         end = -1
#
#         for i in range(0, len(nums)):
#             if nums[i] == target:
#                 start = i
#                 break;
#
#         if start == -1:
#             return [start, end]
#
#         for i in range(start, len(nums)):
#             if (nums[i] == target):
#                 end = i
#
#         return [start, end]
