from parameters import *



# def fragment_alignment(fragment_sequences)

fragSeq = {}

# create dictionary
for line in open(fragment_sequences, "r").readlines():

	line = line.replace("\n", "").split("\t")
	key = line[0] 
	# replace _ with :
	key = key.split("_")
	key = key[0] + "_" + key[1] + ":" + key[2]
	seq = line[1]

	fragSeq[key] = seq

print(fragSeq)
		# return 





