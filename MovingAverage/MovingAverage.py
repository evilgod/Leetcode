class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.data=[]
        self.window_size=size

    def next(self, val):
        if len(self.data)<self.window_size:
            self.data.append(val)
        else:
            self.data=self.data[1:self.window_size]
            self.data.append(val)
            
        return sum(self.data)/float(len(self.data))
        

if __name__=="__main__":
    m=MovingAverage(3)
    print m.next(1)
    print m.next(10)
    print m.next(3) 
    print m.next(5)