class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


if __name__== "__main__":
    A=[1,4,3,2]
    print Solution().arrayPairSum(A)