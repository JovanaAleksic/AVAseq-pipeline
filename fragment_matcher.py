from parameters import *
from Bio.Align import PairwiseAligner



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

list_of_sequences = fragSeq.keys()


# test it
for seqq in list_of_sequences:
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

	print(real_fragment)
	print(matched_fragment)
	print(score)





