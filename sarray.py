import sys

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

text = read.readlines()
ntext = ''
for x in text[1:]:
    x = x.strip('\n')
    ntext = ntext + x
t = ntext
T = len(t)
sp = [0] * T
sax = 0
j = 0
for i in range(1,T):
    c = 0
    l = 0
    if sax <= i:
        while  (i + l) < T and t[i+l] == t[l]:
            c+=1 
            sp[i+l] = c
            l+=1
        sax = i + l 
        j=i
    else:
        k = i - j
        if sp[k] != 0:
            while (i + l ) < T and t[i+l] == t[l]:
                c+=1
                if sp[i+l] == 0:
                    sp[i+l] = c
                l+=1
            sax = i + l 
            j = i
print(sp)
s = ''
for x in sp:
    s = s + ' ' +str(x)
s = s.strip()
write.write(s)
    
