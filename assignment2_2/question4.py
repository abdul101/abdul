#program gets input of sequences,counts the bases,GC ratio and average GC for all sequences
#Prints the sequences, counts of bases, GC Ratio for each sequence and average GC ratio for all sequence
import question2        #used for counting
import question3        #used for printing


#calculates gc ratio for a sequence
def calcGCratio(bases_count):
    if len(bases_count)==0:
        return 0
    else:
        return float(bases_count[2]+bases_count[3])/sum(bases_count)
    
            
#calculates gc ratio for all sequences    
def GC_ratio():
    lst_ratio_seq_count =[]
    ratio_seq_count=()
    lst_sequences,lst_bases_count=question2.getSeqCounts()              #gets the sequences and base counts
    
    for i in range(len(lst_bases_count)):
        gcratio = calcGCratio(lst_bases_count[i])                       #calculates gc ratio for sequence
        ratio_seq_count=gcratio,lst_sequences[i],lst_bases_count[i]     #creates a tuple (gc_ratio,sequence,base counts)
        lst_ratio_seq_count.append(ratio_seq_count)                     #creates list of tuple above
         
        
    return lst_ratio_seq_count                                          #returns list of [{(gc_ratio,sequence,base_counts)]

#prints sequence,base counts, ordered according to gc ratio
def  print_ratio_seq(lst_ratio_seq_count):
    seqNo=1
    for i in sorted(lst_ratio_seq_count):                               #orders list in ascending order according to gc ratio
               
        question3.printSeq(i[1],i[2],seqNo,i[0])                        #prints sequence,base counts,gc ratio
        seqNo +=1
        
#calculates average GC ratio for all sequences        
def calc_globalGC(lst_ratio_seq_count):
    totalGC=0.0   
    count = 0.1
    for i in lst_ratio_seq_count:
        totalGC +=i[0]
        count +=1
    return float(totalGC)/count
    
    



def dispMenu():
    choice =''
    choice = raw_input('To input sequences,calculate GC ratio, press any key !! , type "quit" to exit: ')
    return choice 
        



#Main program,display menu,gets user inputs,prints sequences,bases counts and gc ratio for each sequence and average GC ratio for all sequences
do = True
while do:
    lst_ratio_seq_count=[]
    userInp=dispMenu()
    if userInp != 'quit':
        lst_ratio_seq_count = GC_ratio()
        print_ratio_seq(lst_ratio_seq_count)
        print 'the average GC ratio for all sequences is: %.2f ' % (calc_globalGC(lst_ratio_seq_count))
    else:
        do = False   
        
    