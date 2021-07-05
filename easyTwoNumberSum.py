# bad approach
# O(n^2) time / O(1) space
# def two_numbers_sum(array, targetSum):
#     for i in range(len(array) - 1):
#         first_number = array[i]
#         for j in range(i + 1, len(array)):
#             second_number = array[j]
#             if first_number + second_number == targetSum:
#                 return first_number, second_number
#
#     return ()


# O(n) time / O(n) space
# def two_numbers_sum(array, targetSum):
#     nums = {}
#     for i in array:
#         potentialMatch = targetSum - i
#         if potentialMatch in nums.keys():
#             return i, potentialMatch
#         else:
#             nums[i] = True
#     return ()


# O(n log(n)) time / O(1) space
def two_numbers_sum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        potentialMatchPair = array[left] + array[right]
        if potentialMatchPair == targetSum:
            return array[left], array[right]
        elif potentialMatchPair > targetSum:
            right -= 1
        else:
            left += 1
    return ()

print(two_numbers_sum([2,4,-3,5,7,10], 2))