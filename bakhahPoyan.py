p=int(input())
d=int(input())
i=1
r=d%p

while r > p/2 :
    D=i*d;
    i=i+1;
    r=D%p
    pass
print(D)
