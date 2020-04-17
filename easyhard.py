print(*sorted([int(it) for i,it in enumerate(input().split()) if (i+1)%6 is 0 and int(it)%6 is 0]))
