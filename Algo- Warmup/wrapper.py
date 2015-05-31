k = int(raw_input())

def wrapper(n,m):
    return n/m
    
    
for i in range(k):
    a,b,c = map(int, raw_input().strip().split(" "))
    count=wrapper(a,b)  #number of chocolates
    orig_count=count
    d=0
    extra=0
    while (count+d)/c>=1:
        	#print "Count+d..",count+d
            extra+=(count+d)/c
            #print "Extra..",extra
            d=(count+d)%c
            #print "d...",d
            count=count/c
        	#print "count..",count

    print extra+orig_count
