def p(n):
    return n==n[::-1]
x=int(raw_input())

for i in range(x):
    s=raw_input()
    if p(s):
        print 0
    else:
        q=s[::-1]
        count=0
        if len(s)%2==0:
            length=len(s)/2
        else:
            length=len(s)/2+1
            
        for i in range(length):
            if s[i]!=s[-i-1]:
                if ord(s[i])>ord(s[-i-1]):
                                 count+=ord(s[i])-ord(s[-i-1])
                else:
                                 count+=ord(s[-i-1])-ord(s[i])
        print count
                             
            
