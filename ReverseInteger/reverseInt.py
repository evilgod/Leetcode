class Solution:
    # @return an integer
    def reverse(self, x):
        
        result = ""
        if x == 0: return 0
        if x < 0: 
            result = "-"
            x = abs(x)
        while x > 0:
            p = x%10
            q = x/10
            result = result + str(p)
            x=q
        r = int(result)
        return r
        
        #return result /return a string if need 021 instead of 21
  