#edit helix
import validation
import funct
import globalVar


#menu to get helix number to edit
def getHelixNo(dicHelix):
    inpStr='Enter Helix number to delete: '
    do = True
    while do:
        inp=raw_input(inpStr)
        if inp.isdigit():
            if inp in dicHelix.keys():
                return int(inp)
        else:
            inpStr = 'Error invalid entry: '
            


#update helix details
def editHelix(dicHelix,dicSheet,dicChain):
    
    helixNo,chainID=validation.helixNoValid_H(dicHelix)      #gets helixNo and chainID

    newChainID=validation.chainValid(chainID,dicChain)      #new chain ID
    
    initSeqNum=validation.initSeqNumValid_H(helixNo, dicHelix, dicSheet,  newChainID, dicChain)  #initial seq num
    
    endSeqNum=validation.endSeqNumValid_H(helixNo, dicHelix, dicSheet, newChainID, dicChain,initSeqNum)  #end seq num

    helixClass =validation.helixClassValid(helixNo, dicHelix)     #helix class
    
    comment =validation.comment_H(helixNo, dicHelix)  #comment
    
    
    lstHelix = dicHelix[helixNo]
    lstChain= dicChain[newChainID]
    initResName=funct.getCodon(lstChain[0][initSeqNum])
    endResName=funct.getCodon(lstChain[0][endSeqNum])
    
    line =('HELIX  %3s %3s %3s %1s %4s%1s %3s %1s %4s%1s%2s%30s %5s\n') % (str(helixNo),str(helixNo),initResName,newChainID,initSeqNum,"",endResName,newChainID,endSeqNum,"",helixClass,comment,(int(endSeqNum)-int(initSeqNum)+1))
    
    return line,helixNo
        
#updates changes in main file list       
def editHelixFileLst(line):
    
    for i in range(len(globalVar.lstFile)):
        a=globalVar.lstFile[i][7:10].strip()
        b=line[7:10].strip()
        if globalVar.lstFile[i][0:6].strip()=='HELIX':
            if line[7:10].strip()==globalVar.lstFile[i][7:10].strip():
                globalVar.lstFile[i]= line        
                return None
    
    return 'Error editing'


        
        
#man program    
def mainEditHelix(dicHelix,dicSheet,dicChain):
    
    line,helixNo = editHelix(dicHelix,dicSheet,dicChain)     #gets sheet details to update

    strEdit = editHelixFileLst(line)                         #updates  main file list
    if strEdit == None:
        print
        print 'The Helix %d has been successfully edited. ' % helixNo  
        print
    else:
        print strEdit
        
        
    
    
    
          