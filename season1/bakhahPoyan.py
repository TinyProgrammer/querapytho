p ,d = input().split()
p=int(p)
d=int(d)
D=d
i=1
r=d%p

while r > p/2 :
    D=i*d;
    i=i+1;
    r=D%p
    pass
print(D)
