import question1
#this module is to test question 1

nucleotides = [
    "tttacgatcgatgtATCATTgtgatcgtagcgatgtatTATggcggcc",
    "tttgggta",
    "tgactgtagcagtcaTATCGATG",
    "TTTTTGGTTGTGTGCAAGCTCGGCAGACTTt",
    "ACTGATCGTCGATGCATGTCAGTAGCTAGCCATGTCAGTCAT"]

#Main    

#prints the counts of the bases as a list of tuples
print question1.list_counts(nucleotides)