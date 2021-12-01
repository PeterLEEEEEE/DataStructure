from typing import List  

def twoSum(nums: List[int], target: int) -> List[int]:
  hash_table = {}  
  
  for idx,num in enumerate(nums):
    match_num = target - num
    match_idx = hash_table.get(match_num)
    # print(hash_table)
    # print(match_num)
    if match_idx is not None:
      return [idx,match_idx]     
    
    hash_table[num] = idx

indices = twoSum(nums = [13,7,5,1,3,2],target=10)
print(indices)