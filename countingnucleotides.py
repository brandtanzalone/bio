import sys

read = open(sys.argv[1],'r')
write = open(sys.argv[2],'w')

nucleotide_dict = {}
for s in read.read():
    if s not in nucleotide_dict:
        nucleotide_dict[s] = 1
    else:
        nucleotide_dict[s] += 1 
print(nucleotide_dict.keys())
write.write(str(nucleotide_dict['A']) + ' ' + str(nucleotide_dict['C']) + ' ' + str(nucleotide_dict['G']) +' ' + str(nucleotide_dict['T']))