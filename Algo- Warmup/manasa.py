# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())

for k in range(n):
    a=int(raw_input())
    b=int(raw_input())
    c=int(raw_input())
    s=''
    if b<c:
        mini=b
        maxi=c
    else:
        mini=c
        maxi=b
    for i in range(0,a):
        #print i
        z = (a-1-i)*mini + i*maxi
        if str(z) not in s:
            s+=str(z) + ' '         
    print s
