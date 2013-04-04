#adds new helix

import validation
import funct
import globalVar

#gets helix number
def helixNumber(dicHelix):
    return len(dicHelix)+ 1


#gets inputs to add helix
def addHelix(dicHelix,dicSheet,dicChain):
    
    helixNo = helixNumber(dicHelix)        #gets helix no

    newChainID=validation.chainValid('None',dicChain)   #gets chain id
    
    initSeqNum=validation.initSeqNumValid_H(helixNo, dicHelix, dicSheet,  newChainID, dicChain)   #gets init seq number
    
    endSeqNum=validation.endSeqNumValid_H(helixNo, dicHelix, dicSheet, newChainID, dicChain,initSeqNum)    #end seq num

    helixClass =validation.helixClassValid(helixNo, dicHelix)   #helix class
    
    comment =validation.comment_H(helixNo, dicHelix)  #comment
    
    
    lstChain= dicChain[newChainID]
    initResName=funct.getCodon(lstChain[0][initSeqNum])
    endResName=funct.getCodon(lstChain[0][endSeqNum])
    
    line =('HELIX  %3s %3s %3s %1s %4s%1s %3s %1s %4s%1s%2s%30s %5s\n') % (str(helixNo),str(helixNo),initResName,newChainID,initSeqNum,"",endResName,newChainID,endSeqNum,"",helixClass,comment,(int(endSeqNum)-int(initSeqNum)+1))
    
    return line,helixNo
        
#add helix to list which which was used to read file        
def addHelixFileLst(line,dicHelix):
    index=1
    if len(dicHelix)!=0:
        for i in range(len(globalVar.lstFile)):
            if globalVar.lstFile[i][0:6].strip()=='HELIX':
                index =i
    else:
        index = 3
    try:
    
        globalVar.lstFile.insert(index+1,line)
    except:
        return "Error adding helix"
    
    return None


        
        
#main program   
def mainAddHelix(dicHelix,dicSheet,dicChain):
    
    line,helixNo = addHelix(dicHelix,dicSheet,dicChain)      #gets helix details

    strAdd = addHelixFileLst(line,dicHelix)                  #updates main file list
    if strAdd == None:
        print
        print 'The Helix %d has been successfully created. ' % helixNo  
        print
    else:
        print strAdd
        
        
    
    
    
          