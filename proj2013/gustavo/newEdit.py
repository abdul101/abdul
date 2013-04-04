#main edit module
#allows to list/edit/del/add het/helix

import information
import globalVar
import validation
import editHelix
import editSheet
import addHelix
import addSheet
import delHelix
import delSheet

#list sheet
def listSheet(dicSheet):
    total = len(dicSheet)
    counter=1
    for i in sorted(dicSheet):
        lst = dicSheet[i]
        
        print 'Sheet %d of %d:' % (counter,total)
        print 'strand:      %s' % lst[0]
        print 'sheetID:     %s' % lst[1]
        print 'numStrands:  %s' % lst[2] 
        print 'initResName: %s' % lst[3] 
        print 'initChainID: %s' % lst[4] 
        print 'initSeqNum:  %s' % lst[5]
        print 'initICode:   %s' % lst[6]
        print 'endResName:  %s' % lst[7]
        print 'endChainID:  %s' % lst[8] 
        print 'endSeqNum:   %s' % lst[9] 
        print 'endICode:    %s' % lst[10]
        print 'sense:       %s' % lst[11]  
        print 'curAtom:     %s' % lst[12]
        print 'curResName:  %s' % lst[13]
        print 'curChainId:  %s' % lst[14]
        print 'curResSeq:   %s' % lst[15]
        print 'curICode:    %s' % lst[16]
        print 'prevAtom:    %s' % lst[17] 
        print 'prevResName: %s' % lst[18]
        print 'prevChainId: %s' % lst[19]
        print 'prevResSeq:  %s' % lst[20] 
        print 'prevICode:   %s' % lst[21] 
        
        counter +=1
         
    print
#list Helix
def listHelix(dicHelix):
    total = len(dicHelix)
    counter=1
    
    for i in sorted(dicHelix):
        lst = dicHelix[i]
 
        print 'Helix %d of %d:' % (counter,total)
         
        print 'serNum:      %s' % lst[0]
        print 'helixID:     %s' % lst[1]
        print 'initResName: %s' % lst[2]
        print 'initChainID: %s' % lst[3]
        print 'initSeqNum:  %s' % lst[4]
        print 'initICode:   %s' % lst[5]
        print 'endResName:  %s' % lst[6]
        print 'endChainID:  %s' % lst[7]
        print 'endSeqNum:   %s' % lst[8]
        print 'endICode:    %s' % lst[9]
        print 'helixClass:  %s' % validation.helixClass(int(lst[10]))
        print 'comment:     %s' % lst[11]
        print 'length:      %s' % lst[12]
        counter +=1
    print
    
    
#menu to chose helix or sheet
def menuHelixOrSheet(inpStr):
    
    do = True
    while do:
        selection = raw_input(inpStr)
        if selection.upper() == 'H'or selection.upper() == 'S' :
            return selection.upper()
        else:
            inpStr = 'Error, enter Helix(H) or Sheet(S): '
            

#main menu for editing
def mainMenu():
    do = True
    while do:
        selection =''
        print 'Choose one of the Manipulation Options:'
        print 'List(L)   Edit(E)   New(N)   Remove(R)     Main Menu(M)'
        selection = raw_input(':')
        if selection.upper() in ['L','E','N','R','M']:
            return selection.upper()

#main program            
def mainEdit():
    chain = ''
    do = True
    while do:
        #updates dictionaries
        dicHelix,dicSheet,dicChain,strTitle,dicDBref = information.Main_information(globalVar.lstFile,globalVar.fileName)  
        selection = mainMenu()
        if selection == 'L':        #list helix/sheet
            select=menuHelixOrSheet('Do you want to list the Helix (H) or the Sheet (S): ')
            if select.upper() == 'H':
                listHelix(dicHelix)
            else:
                listSheet(dicSheet)
                
        
                
        elif selection == 'E':      #edit helix/sheet              
            select = menuHelixOrSheet('Do you want to edit a Helix (H) or a Sheet (S): ')
            if select == 'H':
                editHelix.mainEditHelix(dicHelix, dicSheet, dicChain)
        
            else:
                editSheet.mainEditSheet(dicHelix,dicSheet,dicChain)
            
        elif selection == 'N':      #new helix/sheet
            select = menuHelixOrSheet('Do you want to add a Helix (H) or a Sheet (S): ')
            if select == 'H':
                addHelix.mainAddHelix(dicHelix,dicSheet,dicChain)
            else:
                addSheet.mainAddSheet(dicHelix,dicSheet,dicChain)
            
            
            
        elif selection == 'R':      #delete helix/sheet
            select = menuHelixOrSheet('Do you want to remove a Helix (H) or Sheet (S): ')
            if select == 'H':
                delHelix.mainDelHelix(dicHelix)
            else:
                delSheet.mainDelSheet(dicSheet)
    
        
        else:
            return()
    return None    