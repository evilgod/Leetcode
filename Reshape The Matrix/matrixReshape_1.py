class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums)*len(nums[0])<>r*c: return nums
        
        M1=[x for row in nums for x in row]
        print M1
        M=[]
        for i in range(r):
            M.append(M1[:c])
            M1=M1[c:]
        return M

if __name__ == "__main__":
    A=[[1,2],[3,4]]
    r=1
    c=4
    print Solution().matrixReshape(A, r, c)