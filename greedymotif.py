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
moti = []
for x in mot:
    moti.append(x.strip('\n'))


def scorekmer(kmer,profile,charm):
    prob = 1
    for i in range(len(kmer)):
        prob = prob*profile[charm[kmer[i]],i]
    if prob == 0:
        return 0
    else:
        ent = prob*math.log(prob,2)
        return ent

def mlk(dna,k,prof,cmap):
    bestkmer = ''
    smax = math.inf
    for x in range(len(dna)-k+1):
        score = scorekmer(dna[x:x+k],prof,cmap)
        if score < smax:
            smax = score
            bestkmer = dna[x:x+k]
    return bestkmer

def buildprofile(motifs,k,t,cmap):
    pmat = torch.zeros([4,k])
    for x in motifs:
        for j,y in enumerate(x):
            pmat[cmap[y],j]+=1
    for i,x in enumerate(pmat):
        for j,y in enumerate(x):
            pmat[i,j] = pmat[i,j]/t
    return pmat

def pscore(profile):
    p = 1
    for x in range(k):
        colent = 0
        for y in range(4):
            if profile[y][x] > colent:
                colent = profile[y][x]
        p = p*colent
    return p



chmap = {'A':0,'C':1,'G':2,'T':3}
motifs = []
for x in range(len(moti[0])-k+1):
    m = [moti[0][x:x+k]]
    seed = buildprofile(m,k,t,chmap)
    for y in range(1,t):
        m.append(mlk(moti[y],k,seed,chmap))
        seed = buildprofile(m,k,t,chmap)
    motifs.append((seed,m))

mscore = 0
motyboy = []
for x in motifs:
    if mscore < pscore(x[0]):
        mscore = pscore(x[0])
        motyboy = x[1]
print(mscore,motyboy)

out = ''
for x in motyboy:
    out = out + x + '\n'
write.write(out)

    