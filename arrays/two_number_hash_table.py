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
    The problem comes down to this : targetsum = x+y 
    So, since I know the tragetsum, I am trying ot find out the value of x 
    which can be formed into a equation 'x = targetsum-y'
    
    
    What really happens lets explain with an example 
    
    array = [3,7,1,9]
    
    During the first iteration, when the iteration is 3, then potential match is to be 7. 
    However, it is seen the dict does'nt have 7 yet. During the next iteration you would
    get potential value to be as 3 that is when the target sum is made. 
    
    However the limitation of the problem is it will return the first match. If there multiple matches then it would not.
    
    """
    nums={}
    for num in array:
        potentialMatch = targetSum-num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
    
    

if __name__ == '__main__':
    #array = [3,5,-4, 8, 11, 1, -1, 6]
    array = [3,7,-4, 8, 11, 1, -1, 6]
    targetsum = 10
    output = twoNumberSum(array, targetsum)
    print(output)


