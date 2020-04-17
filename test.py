# sq=[i*i for i in range(10)]
# print(sq)
# sq2=["({} , {})".format(i,j) for i in range(10) for j in range(0,10,2) if i*j%4 is not 0 ]
# print("\n".join(sq2))

myTuple=1,2

def f():
    return myTuple

a=f()
a[0]=10
