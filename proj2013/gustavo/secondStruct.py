#display the secondary strcuture
def pdbID(dicDBref):
    for i in dicDBref:
        lst=dicDBref[i]
        return lst[0]

#gets seq start no    
def seqStartNum(dicDBref,chain):
    for i in dicDBref:
        lst=dicDBref[i]
        if lst[1] == chain:
            return lst[2]
            
    

def seqEndNum(dicDBref,chain):
    for i in dicDBref:
        lst=dicDBref[i]
        if lst[1] == chain:
            seqNum =lst[3]
            
    return seqNum

#main program to display secondary structure
def disp2Struct(dicChain,dicHelix,dicSheet,dicDBref):
    
    try:
        print 'Secondary Structure of the PDB id %s:' % pdbID(dicDBref)
        seq=''
        secondStructLst=[]
        secondLabelsList=[]
        for chain in sorted(dicChain):
            
            seqStartNo= int(seqStartNum(dicDBref,chain))
            seqEndNo=int(seqEndNum(dicDBref,chain))
            lstChain= dicChain[chain]
            seq = lstChain[0]
            
            secondStructLst= list('-' * (len(seq)))
            secondLabelsList = list(" " * (len(seq)))
            if len(dicHelix) >=1:
                for i in sorted(dicHelix):
                    lstHelix = dicHelix[i]
                    if lstHelix[3] == chain:
                        for index in range((int(lstHelix[4])-1),int(lstHelix[8])):
                            if seqStartNo == 1:
                                secondStructLst[index]='/'
                            else:
                                secondStructLst[index-seqStartNo]='/'
                                
                        if seqStartNo == 1:
                            secondLabelsList[(int(lstHelix[4])-1):(int(lstHelix[4])+len(lstHelix[0]))]=lstHelix[0]
                        else:
                            secondLabelsList[(int(lstHelix[4])-1)-seqStartNo:int(lstHelix[4])+len(lstHelix[0])-seqStartNo +1]=lstHelix[0]
                            
            if len(dicSheet) >= 1:                            
                for i in dicSheet:
                    lstSheet = dicSheet[i]
                    if lstSheet[4] == chain:
                        
                        for index in range((int(lstSheet[5])-1),int(lstSheet[9])):
                            if seqStartNo == 1:
                                secondStructLst[index]= '|'
                            else:
                                secondStructLst[index-seqStartNo]='|'
                            
                        
                        if seqStartNo == 1:
                            secondLabelsList[int(lstSheet[5])-1:(int(lstSheet[5])-1)+len(lstSheet[0])]=lstSheet[0]
                            secondLabelsList[int(lstSheet[5]):int(lstSheet[5])+len(lstSheet[1])]=lstSheet[1]
                        else:
                            secondLabelsList[(int(lstSheet[5])-1)-seqStartNo:int(lstSheet[5])+len(lstSheet[0])-seqStartNo +1]= lstSheet[0]
                            secondLabelsList[(int(lstSheet[5]))-seqStartNo:int(lstSheet[5])+len(lstSheet[1]-seqStartNo +1)]= lstSheet[1]
                    
            
            
            
            structStr=''
            structLabel=''
            seqStr=''
            structStr="".join(secondStructLst)
            structLabelStr ="".join(secondLabelsList)
            struct=''
            labels=''
            
            print 'Chain %s:' % chain
            print '(%s)' % seqStartNo
            index =0
            while index<len(seq):
                
                seqStr = seq[index:index+80]
                struct = structStr[index:index+80]
                labels = structLabelStr[index:index+80]
                print seqStr
                print struct
                print labels
                index +=80
                
                    
            print        
            print '(%s)' % seqEndNo
            print 

    except:
            print 'ERROR - INVALID FILE'    