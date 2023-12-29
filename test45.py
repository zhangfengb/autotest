"""并查集"""

class UnionFindSet:
    def __init__(self,n):
        self.fa = [i for i in range(n)]
        self.count = n

    def find(self,x):
        if x != self.fa[x]:
            x = self.find(self.fa[x])
            return self.fa[x]
        return x

    def union(self,x,y):
        x_fa = self.find(x)
        y_fa = self.find(y)
        if x_fa != y_fa:
            self.fa[y_fa] = x_fa
            self.count -= 1