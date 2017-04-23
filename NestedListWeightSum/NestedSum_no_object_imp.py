class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def DFS(data, depth):
            
            sum=0
       
            if type(data)==int:
                return data*depth
            
            localdepth=depth+1
            for x in data:
                sum+=DFS(x,localdepth)
            return sum
    
        return DFS(nestedList,0)
    
if __name__== "__main__":
    #data=[[1,1],2,[1,1]]
    data=[1,[4,[6]]]
    print Solution().depthSum(data)