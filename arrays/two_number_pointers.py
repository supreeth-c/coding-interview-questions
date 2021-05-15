"""
Rule : You can't add a single integer to itself in order to obtain the traget sum
    Background: There will be atmost one pair of numbers summing up to the traget sum.

- Given: A non-empty array of distinct integers.
- When : Any two numbers in the input array sum up to target sum
- Then:  The writen function should return the numbers in an array of any order.
- But : No Numbers sum up to the target sum, the function should return empty array
"""


def twoNumberSum(array, targetSum):
    """
    This works completely on pointers, here we are having two pointers
    One is left pointer and another being right pointer
    idea here is to have left+right=sum, this can have three outcomes
    1. First outcome
        targetsum = sum
    2. Second outcome 
        targetsum > sum 
        reduce the value of right which intially is at length of array -1 , but now it
        is going to be lenght of array -2
        
    3. Third outcome
        targetsum < sum
        increase the value of left whose intiall value was at 0. Now it will be at 1
    
    """
    array.sort()
    left = 0
    right = len(array)-1
    while (left < right):
        currentSum = array[left]+array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
        
    return []

if __name__ == '__main__':
    array = [3,7,-4, 8, 11, 1, -1, 6]
    targetsum = 10
    output = twoNumberSum(array, targetsum)
    print(output)


