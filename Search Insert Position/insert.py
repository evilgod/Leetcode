class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for ix in range(len(A)):
            if A[ix]>=target: return ix
            
        return len(A)