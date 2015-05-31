a = int(raw_input())

def inttolist(b):
    l=[]
    while(b!=0):
        l.append(b%10)
        b/=10
    return l

for i in range(a):
    b = int(raw_input())
    z=inttolist(b)
    count=0

    for j in range(len(z)):
        if z[j]!=0:
            if b%z[j]==0:
                count+=1
    print count
