n=int(input())
max=0
alphabet='abcdefghijklmnopqrstuvwxyz'
for i in range(1,n+1):
    counter=0
    name=input()
    for j in list(alphabet):
        if j in name:
            counter=counter+1
            pass
        pass
    if counter > max:
        max=counter
        pass
    pass

print(max)
