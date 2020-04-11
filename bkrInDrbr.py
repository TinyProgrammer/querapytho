import re

def match(x,arg):

    x=re.split('#',x)
    # print("x = ",x," arg = ",arg)
    s=re.search(f'({x[0]})(\d*)({x[1]})',str(arg))
    if s is None: # to avoid Non-pointer Exeption
        return False
    s=s.group()

    return s==str(arg)
    pass

q=input()


x='' #majhol moadele ke b sorate (\d*)#(\d*) mibashad
evrthngOK=False #age formate moadele ba khoroji sedgh bokone True mishe

a=re.search('(\d*)(#*)(\d*)( \+)',q).group()[:-2]
b=re.search('(\+ )(\d*)(#*)(\d*)( =)',q).group()[2:-2]
c=re.search('( = )(\d*)(#*)(\d*)' , q).group()[3:]
if '#' in a:
    x=a
    a=int(c)-int(b)

    if match(x,a):
        evrthngOK=True
        pass

    pass
elif '#' in b:
    x=b
    b=int(c)-int(a)

    if match(x,b):
        evrthngOK=True
        pass

    pass
elif '#' in c:
    x=c
    c=int(a)+int(b)

    if match(x,c):
        evrthngOK=True
        pass
    pass


if evrthngOK:
    print(f'{a} + {b} = {c}')
    pass
elif x=='' and int(a)+int(b) == int(c):
    print(q)
    pass
else:
    print('-1')
    pass
