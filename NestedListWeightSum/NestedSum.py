class NestedInteger(object):#object implement
    def __init__(self, nestedlist):
        self.data=nestedlist
        
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return (type(self.data)==int)
        
    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if (type(self.data)==int):
            return self.data
        else:
            return None
        
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if (type(self.data)==int):
            return None
        else:
            return self.data
        
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        
    
        return self.DFS(nestedList,0)
    
    def DFS(self, data, depth):
            
        sum=0
            
        for x in data:
            if x.isInteger():
                sum+=x.getInteger()*(depth+1)
            else:
                sum+=self.DFS(x.getList(),depth+1)
        return sum
    
if __name__== "__main__":
    #data=[[1,1],2,[1,1]]
    net2Int=NestedInteger(2)
    net1Int=NestedInteger(1)
    net4Int=NestedInteger(4)
    net6Int=NestedInteger(6)
    netInt=NestedInteger([net1Int,net1Int])
    
    #data=[netInt, net2Int, netInt]
    data=[net1Int,NestedInteger([net4Int,NestedInteger([net6Int])])]
    
    print net1Int.getInteger()
    print net1Int.getList()
    print net2Int.getInteger()
    print netInt.getList()
    print Solution().depthSum(data)