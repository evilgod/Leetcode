class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        
        if x < 2 :return x
        
        left=1
        right=x/2
        
        while left<=right:
            mid = (left+right)/2
            
            if x > mid*mid:
                left=mid+1
                mid_pivot = mid
            elif x < mid*mid:
                right=mid-1
            else:
                return mid
        return mid_pivot


if __name__== "__main__":

    print Solution().sqrt(6)