Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


We can use two different approach to solve this:
1. Sum of First n Natural Numbers
    Calculate the sum if no numbers were missing: expected_sum = n*(n+1)/2.
    Calculate the actual sum of the numbers in the array.
    The missing number is expected_sum - actual_sum.
2. Bitwise XOR

    XORing a number with itself results in 0, and XORing a number with 0 results in the number itself.
    We can use this property to find the missing number by XORing all the numbers in the range [0, n] and all the numbers in the array. 
    Initialize a variable missing to 0.
    XOR missing with all numbers from 0 to n.
    XOR missing with all numbers in the array.
    The final value of missing will be the missing number.
    
    For nums = [3, 0, 1], n = 3.
    XOR all numbers from 0 to 3: 0 ^ 1 ^ 2 ^ 3.
    XOR all numbers in the array: 3 ^ 0 ^ 1.
    Combine these: (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) = 2.

