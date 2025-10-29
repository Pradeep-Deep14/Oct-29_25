from collections import defaultdict
d=defaultdict(int)
for i in [1,2,1,3]:
    d[i]+=1
print(d[1],d[2],d[3])

