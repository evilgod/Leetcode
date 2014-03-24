class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i=0
        j=0
        
        while i< m and j<n :
            if A[i]>=B[j]:
                A.insert(i, B[j])
                i=i+1
                j=j+1
                m=m+1
            else:
                i=i+1
        if i==m:
        
            #A = A+B[j:]
            for num in B[j:]:
                A[m:]=B[j:]
            
                
   
                    
                
        