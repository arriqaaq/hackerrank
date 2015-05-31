import math
a = int(raw_input())

for x in range(a):
    b=int(raw_input())
    maxi=0
    for i in range(1,b+1):
        for j in range(i,b+1):
            if i+j==b and i*j>maxi:
                #print i,j
                maxi=i*j

    maxi=math.ceil(b/2.0)*math.floor(b/2.0)
    print maxi
