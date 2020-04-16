m, n = input().split()
m=int(m)
n=int(n)
table=[]

def plist():
    for i in range(m):
        print(' '.join(str(x) for x in table[i]))
    pass


k = int(input())


for i in range(m):
    table.append([0]*n)

for it in range(k):
    i, j = input().split()
    i=int(i)-1
    j=int(j)-1
    table[i][j]='*'

    for I in range(3):
        for J in range(3):
            indexI=i+(I-1)
            indexJ=j+(J-1)

            if indexI >= 0 and indexJ>=0 :
                try:
                    table[indexI][indexJ]+=1
                except:
                    pass
plist()
