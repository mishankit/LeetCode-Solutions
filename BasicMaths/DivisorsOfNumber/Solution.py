class Solution:
    def countFactors (self, n):
        factors = set()
        for i in range(1,int(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
                
        return len(factors)    
        # code here