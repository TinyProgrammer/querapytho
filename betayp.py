inp=list(input())
out=[]
for i in inp:
    if(i is not '=') :
        out.append(i)
    else:
         try: out.pop()
         except: pass
print(''.join(out))
