#program prints sequences and the number of bases in each sequenc
import question2        #used for input and counting base sequence


#changes the format of sequence and prints sequence and base count
def printSeq(seq,base_counts,seqno=0,gcratio=-1):
    
    format_seq = seq[:]
    format_seq= format_seq.replace('g','G')
    format_seq= format_seq.replace('c','C')
    format_seq= format_seq.replace('A','a')
    format_seq= format_seq.replace('T','t')
        
    if gcratio ==-1:
       print "SEQUENCE %d: %s " % (seqno,format_seq)
    else:
       print "GC Ratio: %.2f  SEQUENCE %d: %s " % (gcratio,seqno,format_seq)   
    
    print 'A | ',base_counts[0]
    print '-------'
    print 'T | ',base_counts[1]
    print '-------'
    print 'G | ',base_counts[2]
    print '-------'
    print 'C | ',base_counts[3]
    print '-------'
    print '* | ',base_counts[4]
    print
    


#prints list of sequences 
def Main(lst_sequences,lst_bases_count):    
    seqno=1
    for i in range(len(lst_sequences)):
        printSeq(lst_sequences[i],lst_bases_count[i],seqno)
        seqno +=1 

