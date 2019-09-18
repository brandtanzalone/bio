import sys

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

found = []
pat = read.readline()
pat = pat.rstrip('\n')
gen = read.readline()

for x in range(len(gen)-len(pat)):
    print(gen[x:x+len(pat)],pat)
    if gen[x:x+len(pat)] == pat:
        found.append(x)

for x in found:
    write.write(str(x) + ' ')