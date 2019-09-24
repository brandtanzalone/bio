import sys
import torch
import math

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

text = read.readlines()

k = text[0].strip('\n')
km = []
for x in k.split(' '):
    km.append(int(x))

k = km[0]
t = km[1]

mot = text[1:]
for x in mot:
    x.strip('\n')

chmap = {'A':0,'C':1,'G':2,'T':3}
pmat = torch.zeros([4,k])
print(pmat)
for x in range(len(mot)):
    #compute matrix of everything else
    pmat = torch.zeros([4,k])
    e = mot[:x] + mot[x+1:]
    for x in e:
        for y in range(k):
            pmat[chmap[x[y]],y]+=1
    print(pmat)
    for y in range(len(x) - k):
