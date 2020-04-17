jadvalzarb=[[x for x in range(0,y*10+1,y) if x is not 0] for y in range(1,11)]

def plist():
    for i in jadvalzarb:
        print(*[str(j) for j in i])
        #like ' '.join(...)
plist()
