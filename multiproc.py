def avr(a):
    t=0.0
    for i in a:
        t+=i
    return t/len(a)

def mia(a):
    if len(a)%2 is 0:
        return avr(a[len(a)//2-1:len(a)//2+1])
    return a[(len(a))//2]

def calc(a):
    a.sort()
    return (avr(a),mia(a),a[-1])

print(calc([2, 20, 30, 29]))
