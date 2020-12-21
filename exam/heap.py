#max heap
class heap:
    def __init__(self,a):
        self.item=[]
        for i in a:
            self.add(i)

    def swap(self,i,j):
        c=self.item[i]
        self.item[i]=self.item[j]
        self.item[j]=c

    def add(self,a):
        self.item.append(a)
        self.sort(sp=len(self.item)-1)
        

    def sort(self,sp=0):
        n=len(self.item)
        pp,c1,c2=(sp+1)//2,(sp+1)*2,(sp+1)*2 +1
        if pp and (self.item[sp] > self.item[pp-1]):
            self.swap(sp,pp-1)
            return self.sort(sp=pp-1)
        if c2 <=n and max(self.item[c1-1:c2]) > self.item[sp]  :
            k=c1-1 if self.item[c1-1] > self.item[c2-1] else c2-1
            self.swap(sp,k)
            return self.sort(sp=k)
        if c1 <= n and self.item[c1-1] >self.item[sp]:
            self.swap(sp,c1-1)
            return self.sort(sp=c1-1)

    def get(self):
        c=self.item[0]
        self.swap(0,-1)
        self.item=self.item[:-1]
        self.sort()
        return c


    def show(self):
        def ckl(l):
            n,s=0,0
            while s >= l:
                s+=2**n
                n+=1
            return 2**n
        p=ckl(len(self.item))
        n,s=0,0
        cmd=''
        for i,j in enumerate(self.item):
            if i < (s+ 2**n):
                cmd+=f' {j}[{i}] '
            else:
                icmd=cmd.center(100,' ')
                print(icmd)
                if len(cmd) > 100: break
                cmd=f' {j}[{i}] '
                s+=2**n
                n+=1
        icmd=cmd.center(100,' ')
        print(icmd)

 
