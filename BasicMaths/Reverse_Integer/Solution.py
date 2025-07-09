class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
    
        while x != 0:
            digit = int(x % 10) if x > 0 else int(x % -10)
            x = int(x / 10)
            
            if res > INT_MAX // 10 or res < INT_MIN // 10:
                return 0
            
            res = res * 10 + digit
        
        return res
