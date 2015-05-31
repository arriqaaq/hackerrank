a = int(raw_input())
b = map(int, raw_input().strip().split(" "))
x=0
while(x!=1):
    count=0
    small=min([x for x in b if x!=0])
    for i in range(len(b)):
        if b[i]!=0:
            b[i]-=small
            count+=1
    print count
    x=count

