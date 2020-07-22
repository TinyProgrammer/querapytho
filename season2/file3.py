import datetime
import os
import sys

tmp,src,dst = sys.argv

if not os.path.isdir(dst):
    os.mkdir(dst)

AFD = list(os.walk(src))
#All Files and Directories

DateDic = {}
IMAGE_FORMATS=['jpg','jpeg','png']
VIDEO_FORMATS=['mp4','avi','3gp','mpeg','mkv','wmv','mov']


def indtype(name):
    for i in IMAGE_FORMATS:
        i='.'+i
        if (i) in name.lower()[-1*(len(i)+1):]:
            return 'photos'

    for i in VIDEO_FORMATS:
        if (i) in name.lower()[-1*(len(i)+1):]:
            return 'videos'
    pass

def cp(src,dst):
    with open(src,'rb') as s:
        data = s.read()
        with open(dst,'wb') as d:
            d.write(data)
    pass

for i in AFD:
    for f in i[2]:
        #file path
        p=os.path.join(i[0],f)
        y=(datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime('%Y'))
        try:
            DateDic[y].add(p)
        except:
            DateDic[y]=set()
            DateDic[y].add(p)

for i in DateDic:
    D=os.path.join(dst,i)
    if not os.path.isdir(D):
        os.mkdir(D)
        
    for add in DateDic[i]: 

        name=os.path.basename(add)
        ftype=indtype(name)
        
        if ftype == None:
            continue

        Df=os.path.join(D,ftype)

        if not os.path.isdir(Df):
            os.mkdir(Df)

        cp(add,os.path.join(Df,name))

    pass







