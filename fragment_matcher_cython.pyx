# def cython_align_score(str seq1, str seq2):
# 	cdef int count = 0

# 	for i in range(75):
# 		if seq1[i] == seq2[i]:
# 			count += 1
# 	return count


def match_seq(str query, dict fragSeq):
	cdef int score = 0
	cdef str matched_fragment=''
	cdef int temp_score = 0


	for seq in list(fragSeq.keys()):
		# print(fragSeq[seq])
		
		temp_score = 0
		for i in range(75):
			if query[i] == seq[i]:
				temp_score += 1

		if temp_score==75:
			matched_fragment = fragSeq[seq]
			break

		# print(temp_score)
		elif temp_score >= score:
			score = temp_score
			matched_fragment = fragSeq[seq]	

	return matched_fragment