class Solution(object):
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MASK= 0xFFFFFFFF
        
        while (b != 0):
             sum = (a ^ b) & MASK
             b = ((a & b) << 1) & MASK
             a = sum
        if sum <= MAX:
            return sum 
        else:
            return ~(sum^MASK)
# if __name__== "__main__":
#     print Solution().getSum(-1,1)