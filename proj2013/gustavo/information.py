# reads information from file and transfer it to a list
# also gets Helix,Sheet,Title and chain info
import menus
import funct

def Main_information(lstFile,fileName):
    dicHelix={}
    dicSheet={}
    dicDBref={}
    strTitle=''
    dicChain={}
    dicChainSize={}

    
    
    for line in lstFile:
        if line[:6].strip()== 'HELIX':      #gets Helix infomation from file
            if len(dicHelix) == 0:
                key=1
            else:
                key = len(dicHelix) + 1
                
            dicHelix[key]=line[7:10].strip(),line[11:14].strip(),line[15:18].strip(),line[19].strip(),line[21:25].strip(),line[25].strip(),line[27:30].strip(),line[31].strip(),line[33:37].strip(),line[37].strip(),line[38:40].strip(),line[40:70].strip(),line[71:76].strip()
            
        if line[:5].strip() == 'SHEET':    #gets sheet iformation from file
            if len(dicSheet) == 0:
                key=1
            else:
                key = len(dicSheet) + 1
                
            dicSheet[key]=line[7:10].strip(),line[11:14].strip(),line[14:16].strip(),line[17:20].strip(),line[21].strip(),line[22:26].strip(),line[26].strip(),line[28:31].strip(),line[32].strip(),line[33:37].strip(),line[37].strip(),line[38:40].strip(),line[41:45].strip(),line[45:48].strip(),line[49].strip(),line[50:54].strip(),line[54].strip(),line[56:60].strip(),line[60:63].strip(),line[64].strip(),line[65:69].strip(),line[69].strip()
                            
            
        if line[:5].strip()=='TITLE':       #gets title information
            strTitle += line[10:80].strip() + " "
            
        if line[:6].strip()=='SEQRES':      #gets Chain information
            newCodonStr=''
            codonStr=''
            codonStr=line[19:70].strip().split()
            for i in codonStr:          
                newCodonStr += funct.getCodon(i)    #conerts 3 letter codon string to 1 letter
            if dicChain.has_key(line[11]):
                dicChain[line[11]] += newCodonStr    
            else:
                dicChain[line[11]] = newCodonStr
                dicChainSize[line[11]] = line[13:17].strip()
             
        if line[:5].strip()== 'DBREF':      #gets DBREF info
            previousEndseq=0
            previousStartseq=0
            if len(dicDBref) == 0:
                key=1
                dicDBref[key]= line[7:11].strip(),line[12],line[14:18].strip(),line[20:24].strip()
            else:
                key = len(dicDBref) + 1
                lst = dicDBref[key-1]
                previousChain=lst[0]
                previousStartseq=lst[1]
                previousEndseq=lst[2]
                
                if int(line[14:18].strip())- int(previousEndseq) == 1 and previousChain ==line[12]:
                    dicDBref[key-1]= line[7:11].strip(),previousChain,previousStartseq,line[20:24].strip()
                else:
                    dicDBref[key]= line[7:11].strip(),line[12],line[14:18].strip(),line[20:24].strip()
        
                    
            
    
        
    for i in dicChain:      #strores sizes of aequences in each chan
        dicChain[i]= dicChain[i],dicChainSize[i]
     
    return dicHelix,dicSheet,dicChain,strTitle,dicDBref
        