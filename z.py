import sys
import datetime


read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

pat = read.readline()
pat = pat.rstrip('\n')
P = len(pat)
gen = read.readline()
for x in range(15):
    gen = gen + gen

t = pat + '$' + gen
found = []
T = len(t)
z = [0] * T
sax = 0
j = 0

then = datetime.datetime.now()
for i in range(1,T):
    if sax < i:
        l = 0
        while (i + l) < T and t[i + l] == t[l]:
            z[i]+=1
            l += 1  
        sax = i + z[i]
        j = i
        if z[i] == P:
            found.append(i)
    else:
        k = i - j 
        if (z[k]+i) < sax:
            z[i] = z[k]
            if z[i] == P:
                found.append(i)
        elif (z[k]+i) > sax:
            z[i] = sax - i 
            if z[i] == P:
                found.append(i)
        else:
            z[i] = sax - i
            l = z[i]
            while (i + l) < T and t[i + l] == t[l]:
                z[i]+=1
                l += 1
            sax = i+z[i]
            j = i
            if z[i] == P:
                found.append(i)
now = datetime.datetime.now()
print(now - then)
