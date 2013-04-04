#display summary of file information
import funct
import textwrap


#display information
def Display(dicHelix,dicSheet,dicChain,strTitle,fileName):
    print 'PDB File:  ',fileName
    print textwrap.fill('Title: ' + strTitle,width=80)
    print 'CHAINS: ',chain_header(dicChain)
    for i in dicChain:
        lstChain= dicChain[i]
        seqStr=lstChain[0]
        print ' - Chain', i
        print '    Number of amino acids:',lstChain[1].rjust(5)
        print '    Number of helix:',str(noHelix(i,dicHelix)).rjust(11)
        print '    Number of sheet:',str(noSheet(i,dicSheet)).rjust(11)
        print '    Sequence: ',funct.parseSequence(seqStr,50)
        print
    
    

#counts no of Helix's    
def noHelix(chainID,dicHelix):
    count =0
    lstHelix=[]
    for i in dicHelix:
        lstHelix = dicHelix[i]
        if lstHelix[3]== chainID:
            count += 1
    return count

#count number of sheets
def noSheet(chainID,dicSheet):
    count =0
    for i in dicSheet:
        lstSheet=dicSheet[i]
        if lstSheet[4]== chainID:
            count += 1
    return count

#formats the chain header
def chain_header(dicChain):
    count = 1
    chainStr=''
    
    for key in dicChain:
        if len(dicChain)-count==1 or len(dicChain)-count ==0:
            if len(dicChain)-count==1:
                chainStr +=  key + ' AND '
            else:
                chainStr +=  key
                
        else:
            if len(dicChain.keys()) > 3:
                chainStr +=key +','
        count +=1           
    return chainStr