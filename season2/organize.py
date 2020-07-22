import datetime
import os
import sys

IMAGE_FORMATS=['jpg','jpeg','png']
VIDEO_FORMATS=['mp4','avi','3gp','mpeg','mkv','wmv','mov']


def indtype(name):
    for i in IMAGE_FORMATS:
        i='.'+i
        if (i) in name.lower():
            return 'photos'

    for i in VIDEO_FORMATS:
        i='.'+i
        if (i) in name.lower():
            return 'videos'
    pass
def cp(src,dst):
    with open(src,'rb') as s:
        data = s.read()
        with open(dst,'wb') as d:
            d.write(data)
    pass

tmp,src,dst = sys.argv

if not os.path.isdir(dst):
    os.mkdir(dst)

AFD = list(os.walk(src))
#All Files and Directories

DateDic = {}

for i in AFD:
    for f in i[2]: #just files
        p=os.path.join(i[0],f) #file path
        if indtype(os.path.basename(p))== None :
            continue
        y=(datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime('%Y'))

        try:
            DateDic[y].add(p)
        except:
            DateDic[y]=set()
            DateDic[y].add(p)
for key in DateDic:
    D=os.path.join(dst,key)
    if not os.path.isdir(D):
        os.mkdir(D)

    for add in DateDic[key]:

        name=os.path.basename(add)
        ftype=indtype(name)

        Df=os.path.join(D,ftype)

        if not os.path.isdir(Df):
            os.mkdir(Df)

        cp(add,os.path.join(Df,name))

    pass

