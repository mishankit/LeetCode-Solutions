Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1


Approach : 

res = 0, 
Extract the last digit with digit = x % 10
Pre-check if res * 10 would overflow (by comparing with INT_MAX/10 or INT_MIN/10)
divide by 10 (do not use module)
Update result: res = res * 10 + digit
Return 0 if any step overflows

O(1) space and O(log |x|) time , mod x as x can be -ive as well

digit = int(x % 10) if x > 0 else int(x % -10)
x = int(x / 10) 

Why Check res > INT_MAX // 10?
If res > INT_MAX // 10, then multiplying res by 10 (i.e., res * 10) would already exceed INT_MAX (about 2.14 billion), regardless of the next digit—even before adding it.

Directly writing res * 10 > INT_MAX would itself cause an overflow during evaluation, which makes the check useless. Instead, by dividing the limit (INT_MAX) by 10 first, we avoid overflow and still guarantee safety:

If res > INT_MAX // 10, then res * 10 + digit must exceed the 32-bit limit → return 0 safely.

Note in py :
x = - 13
print(x% 10) # 7
print(x // 10) # -2

 = - 13
print(x% -10) # -3
print(x // 10) # -2

x =  13

print(x% 10) # 3
print(x // 10) # 1

x =  13

print(x% -10) # -7
print(x // 10) # 1