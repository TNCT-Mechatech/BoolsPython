class Bools(object):
    def __init__(self,n,args):
        self.n = n
        self.set_bits(args)
 
    def set_bits(self,args):
        self.m = len(args)
        # slice
        if self.m > self.n:
            self.index = self.n
        else:
            self.index = self.m
        self.bits = args[0 : self.index]

    def _get_bytes(self):
        ret = 0
        cnt = 0
        for i in self.bits:
            ret = ret | bin(i==0) << cnt
            cnt = cnt + 1
        return ret
    
    def _set_bytes(self,c):
        for i in range(self.n):
            self.bits[i] = (c >> i) & 0x01