import os
def explore(pf,add):
    pf = '.'+pf
    tmp=os.walk(add)
    tmp = list(tmp)
    ls={}

    for i in tmp:
        c=0
        for j in i[2]:
            if pf in j:
                c=c+1
        if c != 0:
            ls[i[0]]=c
        c=0
    return ls 
    pass

