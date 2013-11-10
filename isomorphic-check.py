import sys

a="deepak"
b="cantab"

cache=[]
lcache=[]
char_cache=[]
res_neg="Not Isomorphic"
res_pos="Isomorphic" 

if len(a)!=len(b):
    print res_neg

for i,x in enumerate(b):
    if a[i] in char_cache:
        continue
    if x in lcache:
        cache.append((i,x))
        continue
    lcache.append(x)
    tmp=''
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
    char_cache.append(a[i])
if a==b:
    print res_pos
else:
    print res_neg