class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list=list(s)
        for i in range(len(s)/2):
            s_list[i],s_list[-(i+1)]=s_list[-(i+1)],s_list[i]
        return ''.join(s_list)
    def reverseString2(self, s):

        return s[::-1]

if __name__ == "__main__":
    
    print (Solution().reverseString("string"))
    print (Solution().reverseString2('hello'))