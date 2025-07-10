class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        res = 0
        orig = x
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        while x !=0:
            digit = x % 10 
            x = int(x / 10)

            if res > INT_MAX // 10 or res < INT_MIN // 10:
                return 0

            res = res * 10 + digit 
         
        return True if res == orig else False

        