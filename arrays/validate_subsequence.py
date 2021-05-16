"""
- Given: Non empty array of integers
- When : second array is a subsequence of the first one
- Then:  return the first array is a valid subsequence
"""

def isValidSubsequence_for(array, sequence):
    """
    to find second array is subsequence of the first. One has to iterate through the first
    array. By which mean time complexity of the problem is going to be O(n) where n is the 
    lenght of the array. 
    During iteration, if the first element in the sequence matches the order in the array only 
    then seq_index is incremented and the process continues.
    """
    seq_index = 0
    
    for value in array:
        if value == sequence[seq_index]:
            seq_index+=1
        if seq_index == len(sequence):
            break
    return seq_index == len(sequence)
            
    

def isValidSubsequence_while(array, sequence):
    """
    In case of while loop, creat two index values one for sequence and another for array
    if idex of array and sequence matches then increment the sequence id.
    By default on each iteration increment the value of arridx from zero to n+1.
    till it returns length of sequence to be the seqidx
    """               
    seqidx = 0
    arridx = 0 
    while arridx < len(array) and seqidx < len(sequence):
        if array[arridx] == sequence[seqidx]:
            seqidx += 1
        arridx +=1
    return seqidx == len(sequence)
    
    
    
    
    

if __name__ == '__main__':
    array = [5,1,22,3,25,6,-1,10]
    sequence = [1,6,-1,10]
    print(isValidSubsequence_for(array,sequence))
    print(isValidSubsequence_while(array,sequence))
    