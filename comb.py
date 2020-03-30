def fac(a):
    i=1
    if a<2 :
        return i
        pass

    for c in range(2,a+1):
        i = i*c
        pass
    return i
    pass

def comb(n,k):
    ans=fac(n) // ( fac(k) * fac(n-k) )
    return ans
    pass

print(comb(10,0))
