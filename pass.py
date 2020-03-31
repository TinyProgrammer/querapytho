n=int(input())
password=input()
total=0

for i in range(1,n+1):
    ring=input()
    index=ring.find(password[i-1])
    if index<5:
        # print(index)
        total = total+index
        pass
    else:
        # print(9-index)
        total = total-index+9
        pass

    pass
print(total)
