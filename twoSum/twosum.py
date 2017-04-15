class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict1={}
        for i in range(len(num)):
            if dict1.get(target-num[i], "No") == "No":
            
                dict1[num[i]]=i
            else:
                return (dict1[target-num[i]]+1, i+1)
            
#if __name__== "__main__":

#    print Solution().twoSum([2, 7, 11, 15], 9)