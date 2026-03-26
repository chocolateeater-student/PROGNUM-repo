class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    fib=[0,1]
    def __init__(self,N=1000):
        self.N=N
        for i in range(N):
            self.fib.append(self.fib[i+1]+self.fib[i])
        print("I created fibonacci")
    def find(self,n):
        self.n=int(n)
        return self.fib[n-1]
    def div(self,n,m):
        self.n=int(n)
        self.m=m
        r=[]
        for j in self.fib:
            if j<self.fib[n-1] and j%m==0:
                r.append(j)            
        return r
        