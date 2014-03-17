class Solution:
    # @param A, a list of integer
    # @return an integer
#    def __init__(self, A):
 #       print A

    def singleNumber(self, A):
        testvalue=0
        for number in A:
            testvalue^=number
        return testvalue
