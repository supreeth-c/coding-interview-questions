"""
Rule : You can't add a single integer to itself in order to obtain the traget sum
    Background: There will be atmost one pair of numbers summing up to the traget sum.

- Given: A non-empty array of distinct integers.
- When : Any two numbers in the input array sum up to target sum
- Then:  The writen function should return the numbers in an array of any order.
- But : No Numbers sum up to the target sum, the function should return empty array
"""


def twoNumberSum_s1(array, targetSum):
    """
    Time Complexity : O(n^2)
    Space Complexity : O(1)
    
    When going with the approch of having two for loops, the confusing part is what are th conditions
    for the loop.
    
    The trick lies here, vola ! 
    Two arrays, its obvious from the above Rule that we are non't add a single integer to itself by
    which it means the first iterator [i] will be at 0th position and the second iterator would be 
    j=[i+1]. 
    
    Great, know we know the start, how about till when do we do it ? 
    When [i] is @ 0th posting which means he would have to only go till length-1th position.
    
    Wondering why ? 
    If [i] is at last position, then j=i+1. This is where we get array out of bound exeception. 
    
    
    In order to avoid the above problem. 
    The first iteration should stop at length-1 postion and second iteration can stop at the length exactly.
    """
    for i in range(len(array)-1):
        firstnumber = array[i]
        for j in range(i+1, len(array)):
            secondnumber = array[j]
            if firstnumber+secondnumber == targetSum:
                return firstnumber, secondnumber
    return []

if __name__ == "__main__":
    array = [3,5,-4, 8, 11, 1, -1, 6]
    targetsum = 10
    output = twoNumberSum_s1(array, targetsum)
    print(output)
    
