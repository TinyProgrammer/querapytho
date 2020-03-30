import math
x=int(input())
ans=math.gcd(math.ceil(math.pow(x,5/3) + math.tan(math.radians(x))),math.floor(math.pow(math.pi,2+math.atan(math.pow(math.sin(math.radians(x)),2)))))
print(ans)
