import sys

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

gen = read.read()
skew = 0
ds = {}
for i,x in enumerate(gen):
    oldskewl = skew
    if x == 'G':
        skew += 1
    if x == 'C':
        skew -= 1
    if oldskewl <= skew:
        if oldskewl not in ds:
            ds[oldskewl] = [i]
        else:
            ds[oldskewl].append(i)

m = sorted(ds.keys())
for x in ds[m[0]]:
    write.write(str(x) + ' ')