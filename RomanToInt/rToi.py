class Solution:
    # @return an integer
    def romanToInt(self, s):
        self.pre = ""
        self.result = 0
        for ix in range(len(s)):
            if s[ix]=="": return self.result
            if s[ix]=="M" and self.pre !="C" : self.result+=1000
            if s[ix]=="M" and self.pre =="C" : self.result+=800
            if s[ix]=="C" and self.pre !="X" : self.result+=100
            if s[ix]=="C" and self.pre =="X" : self.result+=80
            if s[ix]=="X" and self.pre !="I" : self.result+=10
            if s[ix]=="X" and self.pre =="I" : self.result+=8
            if s[ix]=="I": self.result+=1
            if s[ix]=="D" and self.pre !="C" : self.result+=500
            if s[ix]=="D" and self.pre =="C" : self.result+=300
            if s[ix]=="L" and self.pre !="X" : self.result+=50
            if s[ix]=="L" and self.pre =="X" : self.result+=30
            if s[ix]=="V" and self.pre !="I" : self.result+=5
            if s[ix]=="V" and self.pre =="I" : self.result+=3
            self.pre =s[ix]
        return self.result

if __name__=="__main__":

    rom="DCXXI"
    print Solution().romanToInt(rom)