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

def scorekmer(kmer,profile,charm):
    prob = 0
    for i in range(len(kmer)):
        prob = prob*profile[charm[kmer[i]],i]
        print(prob)
    ent = prob*math.log(prob,2)
    return ent

def mlk(dna,k,prof,cmap):
    bestkmer = ''
    smax = 0
    for x in range(len(dna)-k):
        score = scorekmer(dna[x:x+k],prof,cmap)
        if score > smax:
            smax = score
            bestkmer = dna[x:x+k]
    return bestkmer

def buildprofile(motifs,k,t,cmap):
    pmat = torch.zeros([4,k])
    for x in motifs:
        for y in range(k):
            pmat[cmap[x[y]],y]+=1
    for i,x in enumerate(pmat):
        for j,y in enumerate(x):
            pmat[i,j] = pmat[i,j]/t
    return pmat

def pscore(profile):
    print(profile)
    cmax = 0
    p = 0
    # for x in range(k):
    #     for y in range(4):



chmap = {'A':0,'C':1,'G':2,'T':3}
motifs = []
for x in range(len(mot[0]) - k):
    m = [mot[0][x:x+k]]
    seed = buildprofile(m,k,t,chmap)
    for y in range(1,t):
        m.append([mlk(mot[y],k,seed,chmap)])
        seed = buildprofile(m,k,t,chmap)
    motifs.append((seed,m))

mscore = 0
for x in motifs:
    print(pscore(x[0]))
    