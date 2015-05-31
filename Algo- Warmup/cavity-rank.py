def cavity(l,n):
    for i in xrange(1,n-1):
        for j in xrange(1,n-1):
            if l[i-1][j]!='X' and l[i][j-1]!='X' and l[i+1][j]!='X' and l[i][j+1]!='X' and l[i][j]>l[i-1][j] and l[i][j]>l[i+1][j] and l[i][j]>l[i][j-1] and l[i][j]>l[i][j+1]:
                l[i][j]='X'

if __name__ == '__main__':
    n = input()
     
    p = []
     
    for _ in xrange(n):
        line = list(raw_input())
        p.append(line)
         
    cavity(p, n)
     
    for line in p:
        print ''.join(line)
