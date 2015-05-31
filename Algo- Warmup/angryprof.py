a = int(raw_input())

for i in range(a):
    b,c=raw_input().split()
    b,c=int(b),int(c)
    d = map(int, raw_input().strip().split(" "))
    count=0

    for i in range(b):
        if d[i]<=0:
            count+=1

    if count>=c:
        print "No"
    else:
        print "Yes"

    
