#program uses a module to input sequences and question 1 to count the bases

import seq_input         #gets users input
import question1        # counts the bases in sequence

        
#gets users input, count bases in sequence
def getSeqCounts():
    lst_base_count=[]
    seq_count=[]
    lst_seq=seq_input.get_input()
    lst_base_count = question1.list_counts(lst_seq)
    return lst_seq,lst_base_count




    



 


    

 
       
       
    