import sys

a="deepak"
b="cantab"

cache=[]
lcache=[]
converted_cache=[]
res_neg="Not Isomorphic"
res_pos="Isomorphic" 

if len(a)!=len(b):
    print res_neg

for i,x in enumerate(b):
    if x in lcache:
        cache.append((i,x))
        continue
    lcache.append(x)
    tmp=''
    if a[i] in converted_cache:
        continue
    converted_cache.append(a[i])
    for j,y in enumerate(a):
        if (j,y) not in cache:
            if a[i]==y:
                tmp+=x
                cache.append((i,x))
            else:
                tmp+=y
        else:
            tmp+=y
    a=tmp
if a==b:
    print res_pos
else:
    print res_neg