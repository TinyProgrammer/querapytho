import re
ans=''

try:
    while True:
        I=input()

        Regex="((\+|-)|())(\d+)(((.)(\d+))|())((E|e)((\+|-)|())(\d+)|())"

        #four main group in Regex are:
        #1.sign OR nothing  2.digit   3.dot and digit OR nothing
        #4.'e' or 'E' AND sign or nothing AND digit OR nothing

        obj=re.search(Regex,I)

        if obj is None: # to avoid Non-pointer Exeption
            ans=ans+"ILLEGAL\n"
        elif obj.group() == I :
            ans=ans+"LEGAL\n"
        else :
            ans=ans+"ILLEGAL\n"
except:
    print(ans)
