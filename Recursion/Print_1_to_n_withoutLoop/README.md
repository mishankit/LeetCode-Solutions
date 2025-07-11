You are given an integer n. You have  to print all numbers from 1 to n.
Note: You must use recursion only, and print all numbers from 1 to n in a single line, separated by spaces.

Examples:

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Input: n = 5
Output: 1 2 3 4 5
Input: n = 1
Output: 1
Constraints:
1 ≤ n ≤ 103

Base Case Implicit: When n = 1, it just prints 1
Recursive Case:
First makes recursive call for n-1
Then prints the current number n
end=' ' keeps all numbers on the same line with spaces