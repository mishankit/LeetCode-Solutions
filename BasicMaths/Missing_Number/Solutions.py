class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = (n * (n + 1) ) // 2
        sum = 0
        for i in nums:
            sum += i
            
        return result - sum 
            