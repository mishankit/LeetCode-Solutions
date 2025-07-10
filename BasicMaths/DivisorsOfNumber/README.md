Find the number of factors for a given integer n.

 Examples:

Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5
Input: n = 25
Output: 3
Explanation: 25 has 3 factors 1, 5, 25


Need to check from 1 to n**0.5 , for each number that divides n evenly, you can find its pair factor , 
by n % i == 0 the pair will be i and n // i

Complexity O(n ** 0.5)