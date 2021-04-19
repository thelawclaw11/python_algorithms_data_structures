def next_permutation(nums):
    k = None
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            k = i
            break

    if k is None:
        nums.sort()
        return True

    l = None
    for i in range(k, len(nums)):
        if nums[i] > nums[k]:
            l = i

    nums[k], nums[l] = nums[l], nums[k]

    i = k + 1
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return False


def generate_permutations(nums):
    permutations = []

    stop = False

    while stop is False:
        permutations.append(nums.copy())
        stop = next_permutation(nums)

    return permutations




# print(solution.nextPermutation([1, 2, 3, 4]))

a = [1, 2, 3]

print(generate_permutations(a))

# n = [1, 2, 3, 4, 5, 6]
# solution.reverse(n)
# print(n)
