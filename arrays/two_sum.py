"""
Input: nums = [3,3], target = 6
Output: [0,1]

"""
from operator import index
from typing import List, Dict

from attr import has


def twoSum_hash(nums: List[int], target: int) -> List[int]:
    hash_map: Dict[int, int] = {}
    for i in range(len(nums)):
        reminder = target - nums[i]
        if reminder in hash_map:
            return [i, hash_map[reminder]]
        hash_map[nums[i]] = i

def twoSum_loop(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
            
            
            
            
            
if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(twoSum_hash(nums, target))
    print(twoSum_loop(nums, target))
    