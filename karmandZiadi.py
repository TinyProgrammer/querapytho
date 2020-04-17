n=int(input())
colors=0
names={} #create na empty dict not set
for i in range(n):
    name=input()
    name=name[0:name.index(' ')]
    names[name]=names.get(name,0)+1

print(sorted(names.values())[-1])
