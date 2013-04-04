#add new sheet
import validation
import funct
import globalVar

#gets sheet ID
def sheetID(ID):
    dicAlpha = {
        'A': 1,'B':2,'C': 3,'D':4,'E': 5,'F':6,'G': 7,'H':8,'I': 9,'J':10,'K': 11,'L':12,'M': 13,'N':14,
        'O': 15,'P':16,'Q': 17,'R':18,'S': 19,'T':20,'U': 21,'V':22,'W': 23,'X':24,'Y': 25,'Z':26
        }
    index = dicAlpha[ID]
    for i in dicAlpha:
        if dicAlpha[i] == index + 1:
            return i
    
    return 'A'
    
    
#gets strand no
def getStrandNoSheetID(dicSheet):
    
    if len(dicSheet) != 0:
        
        lstSheet = dicSheet[len(dicSheet)]
        strandNo = lstSheet[0]
        sheetid = lstSheet[1]
        numStrands = lstSheet[2]
        
        if (int(numStrands) - int(strandNo)) >=1:
            return int(strandNo)+1,sheetID,numStrands
        else:
            numStrands = validation.numStrands()
            return 1,sheetID(sheetid),numStrands,0
        
    
    
#gets sheet info to add
def addSheet(dicHelix,dicSheet,dicChain):
    
    strandNo,sheetID,numStrands,sense = getStrandNoSheetID(dicSheet)    #strandNo, sheetID,NumberStrand, sense
    
    newChainID=validation.chainValid('None',dicChain)   #chain ID

    initSeqNum=validation.initSeqNumValid_S(dicHelix,dicSheet,newChainID,dicChain)   #init seq Num
    
    endSeqNum =validation.endSeqNumValid_S(dicHelix,dicSheet,newChainID,dicChain,initSeqNum) #end seq num
    
    
    if sense != 0:                          #updates sense
        sense = validation.getSense()
        
    curAtom = validation.currentAtom('None', dicSheet)
    
    curResName=validation.currentResName('None', dicSheet)
    
    curReSseq=validation.currentResSeq('None', dicSheet)

    prevAtom = validation.prevAtom('None', dicSheet)
    
    prevResName =validation.prevResName('None', dicSheet)
    
    prevChainID=validation.prevChainId('None', dicSheet,dicChain)
    
    prevResSeq= validation.prevResSeq('None', dicSheet)
    
    lstChain= dicChain[newChainID]
    initResName=funct.getCodon(lstChain[0][int(initSeqNum)])
    endResName=funct.getCodon(lstChain[0][int(endSeqNum)])

    line = ('%6s %3s %3s%2s %3s %1s%4s%1s %3s %1s%4s%1s%2s %4s%3s %1s%4s%1s %4s%3s %1s%4s%1s\n') %('SHEET ',strandNo,sheetID,numStrands,initResName,newChainID,initSeqNum,"",endResName,newChainID,endSeqNum,"",sense,curAtom,curResName,newChainID,curReSseq, "",prevAtom,prevResName,prevChainID,prevResSeq,"")                                               
    
    return line
        
   
    
# adds sheet to file list
def addSheetFileLst(line,dicSheet):
    index=1
    if len(dicSheet)!=0:
        for i in range(len(globalVar.lstFile)):
            if globalVar.lstFile[i][0:6].strip()=='SHEET':
                index =i
    else:
        index = 3
    try:
    
        globalVar.lstFile.insert(index+1,line)
    except:
        return "Error adding sheet"
    
    return None

    
    

#man program
def mainAddSheet(dicHelix,dicSheet,dicChain):
    
    line = addSheet(dicHelix,dicSheet,dicChain)   #gets sheet details

    strAdd = addSheetFileLst(line,dicSheet)       #updates main file list
    if strAdd == None:
        print 'sheet  has been successfully created. '  
    else:
        print strAdd
        
  