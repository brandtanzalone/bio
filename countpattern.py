import sys
import datetime

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

found = []
pat = read.readline()
pat = pat.rstrip('\n')
gen = read.readline()
for x in range(15):
    gen = gen + gen
then = datetime.datetime.now()

for x in range(len(gen)-len(pat)):
    if gen[x:x+len(pat)] == pat:
        found.append(x)
now = datetime.datetime.now()
print(now-then)
for x in found:
    write.write(str(x) + ' ')