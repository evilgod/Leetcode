class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict1={}
        #result=[]
        for i in range(len(num)):
            #if dict1.get(target-num[i], "No") == "No":
            if (target-num[i]) not in dict1:
                dict1[num[i]]=i
            else:
                #result.append([dict1[target-num[i]]+1, i+1]) multiple pairs
                return (dict1[target-num[i]]+1, i+1)
        #return result
if __name__== "__main__":

    print (Solution().twoSum([2, 7, 5, 4], 9))