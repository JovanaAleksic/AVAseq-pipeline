from parameters import *
import time
import random
import numpy as np
from sequence_aligner import match_seq



def align_score(str1, str2):
	count = 0
	for i in range(75):
		if str1[i] == str2[i]:
			count += 1
	return count


fragSeq = {}

# create dictionary
for line in open(fragment_sequences, "r").readlines():

	line = line.replace("\n", "").split("\t")
	key = line[0]   # key used in a wrong way, sequences are keys
	# replace _ with :
	key = key.split("_")
	key = key[0] + "_" + key[1] + ":" + key[2]
	seq = line[1][0:75]  # important to not provide the whole sequence

	fragSeq[seq] = key

list_of_sequences = list(fragSeq.keys())


for j in range(6000):
	invented_key = ''.join(random.choices(['A', 'C', 'T', 'G'], k=75))
	invented_fragment = random.choices(list(fragSeq.values()))[0]
	fragSeq[invented_key] = invented_fragment

total_time = 0
counter = 0

for i in range(100):

	seqq = random.choice(list_of_sequences)
	query = "ATTT" + seqq[4:50] + "GGGGG" + seqq[55:75]
	real_fragment = fragSeq[seqq]


	start_time = time.time()
	matched_fragment = match_seq(query, fragSeq)
	total_time += time.time() - start_time


	if real_fragment==matched_fragment:
		counter+=1




print(f"It took: {total_time} seconds with built in aligner")
print(f"We got {counter} correct")
