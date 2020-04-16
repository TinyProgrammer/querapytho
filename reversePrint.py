list=[]
list.append(input())

while list[-1] != '0':
    list.append(input())

list.pop()
list.reverse()
print('\n'.join(list))
