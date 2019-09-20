import sys

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

text = read.readlines()
ntext = ''
for x in text[1:]:
    x = x.strip('\n')
    ntext = x + ntext
t = ntext
t = 'CAGCATGGTATCACAGCAGAG'
T = len(t)
z = [0] * T
sax = 0
j = 0
for i in range(1,T):
    if sax < i:
        l = 0
        while (i + l) < T and t[i + l] == t[l]:
            z[i]+=1
            l += 1  
        sax = i + z[i]
        j = i
    else:
        k = i - j 
        if (z[k]+i) < sax:
            z[i] = z[k]
        elif (z[k]+i) > sax:
            z[i] = sax - i 
        else:
            z[i] = sax - i
            l = z[i]
            while (i + l) < T and t[i + l] == t[l]:
                z[i]+=1
                l += 1
            sax = i+z[i]
            j = i

