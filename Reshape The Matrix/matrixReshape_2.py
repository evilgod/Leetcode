class Solution(object):
    def matrixReshape(self, nums, r, c):
        m=len(nums)
        n=len(nums[0])
        if m*n != r*c: return nums
        
#         flat=sum(nums, [])
#         print flat
        M=[[0 for i in range(c)] for j in range(r)]
        for i in range(r*c):
            M[i/c][i%c]=nums[i/n][i%n]
        return M

if __name__ == "__main__":
    A=[[1,2],[3,4]]
    r=1
    c=4
    print Solution().matrixReshape(A, r, c)