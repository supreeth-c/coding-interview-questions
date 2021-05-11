"""
Rule : You can't add a single integer to itself in order to obtain the traget sum
    Background: There will be atmost one pair of numbers summing up to the traget sum.

- Given: A non-empty array of distinct integers.
- When : Any two numbers in the input array sum up to target sum
- Then:  The writen function should return the numbers in an array of any order.
- But : No Numbers sum up to the target sum, the function should return empty array
"""


def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num]= True
    return []


if __name__ == '__main__':
    array = [3,5,-4, 8, 11, 1, -1, 6]
    targetsum = 10
    output = twoNumberSum(array, targetsum)
    print(output)


