class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, values in enumerate(nums):
            dict[i] = values

        for i, num in dict.items(): 
            complement = target - num 
            if complement in dict.values():
                for key, val in dict.items(): 
                    if val == complement and key != i: 
                        return i, key