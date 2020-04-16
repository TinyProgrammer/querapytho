# list=['Mohammad',2,1,5,'is changed']
# for i,it  in enumerate(list) :
#     print(i+1,'line of the list is : ',it)

print('test zip abaility in python for loop :')

lista=[1,2,3,4,5]
listb=['a','b','c','d','e']
listc=['I','II','III','IV','V']

for a,b,c,d in zip(lista,listb,listc,range(2)):
    print('{}th alphabet or {} in greece is : {}'.format(a,c,d))
