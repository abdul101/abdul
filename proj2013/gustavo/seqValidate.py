import funct

#validates start sequence of sheet
def seqStartSheet_H(seqNo,dicSheet,chainID):
    if seqNo <=0:
        return "Error, invalid sequence number: "

    for i in sorted(dicSheet):
        lstSheet= dicSheet[i]

        if (seqNo in range(int(lstSheet[5]),int(lstSheet[9])+1)) and chainID==lstSheet[4]:
            return "Error, sequence Number not available: "
    return None



#validates start sequence of helix
def seqStartHelix_H(seqNo,helixNo,dicHelix,chainID):
    for i in dicHelix:
        
        lstHelix= dicHelix[i]
        if int(lstHelix[0]) == helixNo:
            if seqNo >= int(lstHelix[8]):
                return "Error, sequence Number past end sequence"
            
        if int(lstHelix[0]) != int(helixNo):
            if (seqNo in range(int(lstHelix[4]),int(lstHelix[8])+1)) and chainID==lstHelix[3]:
                return "Error, sequence Number not available "
    return None


def initSeqNumValid_H(helixNo,dicHelix,dicSheet,chainID,dicChain):
    if helixNo >= len(dicHelix):        #use same function to add and edit helix, checks if adding helix
        inpStr ='initSeqNum: '          # when adding new helix there is no default number
    else:
        lstHelix=dicHelix[helixNo]
        inpStr='initSeqNum [%s]: ' % lstHelix[4]   #display defauly value when editing
        
    lstChain=dicChain[chainID]
        
    
    do = True
    while do:
    
        inp=raw_input(inpStr)
        if inp.isdigit() and  int(inp) < len(lstChain[0]):
            seqStr = seqStartHelix_H(int(inp),helixNo,dicHelix,chainID)
        
            if seqStr != None:
                inpStr = seqStr
            else:
                seqStr = seqStartSheet_H(int(inp),dicSheet,chainID)
                if seqStr != None:
                    inpStr = seqStr
                else:
                    lstChain = dicChain[chainID]
                            
                    inpStr = 'That position correspond to the amino acid %s.' % funct.getCodon(lstChain[0][int(inp)-1])
                    print inpStr
                    return int(inp)
        else:

            inpStr = 'Error- initSeqNum must be less than %s : ' % len(lstChain[0])