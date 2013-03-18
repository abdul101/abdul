#program counts the number of bases in a given sequence




#for an individual sequence counts the number of a,c,g,t and "other" bases
def count_bases(seq):
	count_a=0
	count_c=0
	count_g=0
	count_t=0
	count_x=0
	count_seq=()

	count_a=seq.lower().count('a')
	count_c=seq.lower().count('c')
	count_g=seq.lower().count('g')
	count_t=seq.lower().count('t')
	x_count=len(seq)- (count_a+count_c+count_g+count_t)
	count_seq = (count_a,count_t,count_g,count_c,x_count)
		
	return count_seq



#counts the number of bases in a list of sequences
def list_counts(lst_sequences):
	lst_base_counts=[]
	for sequences in lst_sequences:
		lst_base_counts.append(count_bases(sequences))
	return lst_base_counts

#Main	
#print list_counts(nucleotides)
	




	
	
	