import sys
import pandas as pd
import torch
import math

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

text = read.readlines()
t = text[0]
l = int(text[1])
its = len(t) - l
mprob = 'A' * l
pmat = text[2:6]
pmat = [x.strip('\n').split(' ') for x in pmat]

p =[]
for x in pmat:
    lp = []
    for y in x:
        lp.append(float(y))
    p.append(lp)
p = torch.tensor(p)
charm = {'A':0, 'C':1, 'G':2, 'T':3}

def scorekmer(kmer,p):
    prob = 0
    for i in range(len(kmer)):
        prob = prob + p[charm[kmer[i]],i]
    ent = prob*math.log(prob,2)
    return ent

smax = 0
bestkmer = ''
for x in range(len(t)-l):
    score = scorekmer(t[x:x+l],p)
    if score > smax:
        smax = score
        bestkmer = t[x:x+l]
print(smax)
print(bestkmer)
write.write(bestkmer)