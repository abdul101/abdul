#deletes  a helix
import validation
import funct
import globalVar

#updates the indexes after deleting helix
def updateIndex():
    tmpDic={}
   
    for i in range(1,len(globalVar.lstFile)):
        if globalVar.lstFile[i][0:6].strip()=='HELIX':
            a= globalVar.lstFile[i][7:10].strip()
            index = int(globalVar.lstFile[i][7:10].strip())
            tmpDic[index]=(i,globalVar.lstFile[i])
            
            
    counter= len(tmpDic) + 1   

    for i in range(1,counter):
        if i not in (tmpDic):
            lst=tmpDic[i+1]
            line = lst[1]
            newLine =('HELIX %3s %3s %s') % (str(i),str(i),line[14:76])
            tmpDic[i]=(lst[0],newLine)
            tmpDic.pop(i+1)
            popIndex = lst[0]
    
    for i in tmpDic:
        lst=tmpDic[i]
        globalVar.lstFile[lst[0]]=lst[1]+'\n'

   

#gets helix number to delete
def menuHelixNoDel(dicHelix):
    inpStr='Which Helix do you want to delete (1-%d): ' % len(dicHelix)
    do = True
    while do:
        inp=raw_input(inpStr)
        if inp.isdigit():
            
            if int(inp) not in range(1,len(dicHelix) + 1):
                inpStr = 'select helix in range (1-%s): ' % (len(dicHelix))
                
            else:
                return int(inp)
    


#deletes helix from file list    
def delHelixFileLst(helixNo):
    for i in range(len(globalVar.lstFile)):
        a=globalVar.lstFile[i][0:6].strip()
        if globalVar.lstFile[i][0:6].strip()=='HELIX'and helixNo== int(globalVar.lstFile[i][7:10].strip()):
            globalVar.lstFile.pop(i)     
            return None
    return 'Error deleting Helix %s' % helixNo


# display and confirms deletes of helix   
def menuConf(helixNo,dicHelix):
    lst = dicHelix[helixNo]
    print 'Are you sure do you want to delete the helix?'
  #  print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (lst[0:6],lst[7:10],lst[11:14],lst[15:18],lst[19],lst[21:25],lst[27:30],lst[31])
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('HELIX',lst[0],lst[1],lst[2],lst[3],lst[4],lst[6],lst[7],lst[8],lst[10])
    do = True
    inpStr='Y/N? '
    while do:
        inp = raw_input(inpStr)
        if inp.upper() == 'Y' or inp.upper()=='N':
            return inp.upper()
        else:
            inpStr = ' Error - Enter Y/N: '

#main program      
def mainDelHelix(dicHelix):
    helixNo = menuHelixNoDel(dicHelix)     #helix number to delete
    strConf= menuConf(helixNo,dicHelix)    #confirmation
    if strConf =='Y':
        strDel = delHelixFileLst(helixNo) #deletes from main file list

        
        if strDel == None:
            updateIndex()
            print
            print 'The Helix %d has been successfully removed. ' % helixNo  
            print 'All the serial numbers have been updated.'
            print
        else:
                print strDel 
        
  

    
  