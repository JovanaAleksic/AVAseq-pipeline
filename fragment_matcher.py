from parameters import *
from Bio.Align import PairwiseAligner, MultipleSeqAlignment
import time
import random


# execution time
# start_time = time.time()



# def fragment_alignment(fragment_sequences)
aligner = PairwiseAligner(match_score=1.0)
fragSeq = {}

# create dictionary
for line in open(fragment_sequences, "r").readlines():

	line = line.replace("\n", "").split("\t")
	key = line[0] 
	# replace _ with :
	key = key.split("_")
	key = key[0] + "_" + key[1] + ":" + key[2]
	seq = line[1][0:75]  # important to not provide the whole sequence

	fragSeq[seq] = key

list_of_sequences = list(fragSeq.keys())
print(len(list_of_sequences))


# test and time
counter = 0
start_time = time.time()


for i in range(1000000):

	seqq = random.choice(list_of_sequences)
	query = "ABCF" + seqq[4:50] + "GXHJS" + seqq[55:75]
	real_fragment = fragSeq[seqq]

	score = 0
	matched_fragment=''

	for seq in list_of_sequences:
		# print(fragSeq[seq])
		temp_score = aligner.score(query, seq)
		# print(temp_score)
		if temp_score >= score:
			score = temp_score
			matched_fragment = fragSeq[seq]

	if real_fragment==matched_fragment:
		counter+=1




print(f"It takes {time.time() - start_time} secs")
print(f"We got {counter} correct")
