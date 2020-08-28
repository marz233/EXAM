class n_num():
    def __init__(self,num,n):
        self.num = num
        self.rev_d = str(num)[::-1] # 将输入逆序
        self.radix = n # 进制数
        self.dec = 0
        self.res = ''
        self.n2dec()
        
    def n2dec(self): # n进制转十进制
        for i,d in enumerate(self.rev_d):
            self.dec += int(d)*self.radix**i
            
    def dec2n_gen(self,_n): # 十进制转n进制(整数) 生成器
        while self.dec != 0:
            yield self.dec % _n
            self.dec //= _n
            
    def dec2n(self,_n):
        _list = [i for i in self.dec2n_gen(_n)][::-1]
        for i in _list:
            self.res += str(i)
        return self.res
if __name__ == "__main__":
    n1 = n_num(1012,3)
    n2 = n_num(2012,3)
    n3_dec = n1.dec + n2.dec
    n3 = n_num(n3_dec,10)
    print(n1.dec,n2.dec,n3.dec,n3.dec2n(3))
