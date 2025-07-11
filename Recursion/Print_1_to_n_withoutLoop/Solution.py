class Solution:    
    def printNos(self,n):
        if n == 1:
            return "1"
        return self.printNos(n-1) + " " + str(n)
            