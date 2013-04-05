# this is the main module which calls all the other modules.
#this program uses a number of individual modules to achieve task ie add/del/displ helix/sheet
import menus            #display menus
import information      #gets info from file and transfer it to a list
import funct            #validates user input
import infoDisplay      #info display
import histogram        #display histogram
import secondStruct     #display secondary structure
import globalVar        #used to store global variableso

import newEdit          #main edit module
import saveFile         #export file


dicHelix={}         #dictionary for storing helix information
dicSheet={}         #dictionary for storing sheetinformation 
dicChain={}         #dictionary for storing cain information
dicDBref={}         #dictionary for storing DBREF information


#display the menu
def menu():
    
    do = True
    errStr=''
    while do:
        menus.dispMainMenu()        #calls module menus to display menu
        menus.footerMainMenu(globalVar.fileName) #display footer section in main menu
        
        if errStr != '':
            print errStr
            
        selection = raw_input(":")
        if selection.upper() in ['O','I','H','S','M','X','Q'] :      #validates user inputs
            if selection.upper() == 'O' or selection.upper() == 'Q' :
                return selection.upper()
            elif globalVar.fileName != 'None':
                return selection.upper()        
                     
            else:
                errStr= "Error - select a file first."   
                    
        else:
            
            errStr="Error - invalid option selected."
                      
    
#main program which display menus
def mainProgram():

    
    do=True
    while do:
        selection=menu().upper()
        if selection == 'O':                        #user wants to select input file
            
            lstFile,fileName,path=funct.fileNameMenu()
            if lstFile != None:
                globalVar.lstFile =lstFile          #stores variable in module to give it global scope
                globalVar.fileName=fileName
                globalVar.path=path
                
                #gets information from File
                dicHelix,dicSheet,dicChain,strTitle,dicDBref = information.Main_information(globalVar.lstFile,globalVar.fileName)
                       
        elif selection ==  'I':                     #dislay inofrmation
                                
            infoDisplay.Display(dicHelix,dicSheet,dicChain,strTitle,globalVar.fileName)
                    
        elif selection ==  'H':                     #display histogram
                
            histogram.histoMain(dicChain)
                    
        elif selection  ==  'S':                    #display secondary structure
                
                 
            secondStruct.disp2Struct(dicChain, dicHelix, dicSheet, dicDBref)
                    
        elif selection ==  'M':                     #display edit menu
           
            newEdit.mainEdit()
    
        elif selection ==  'X':                     #export file
                
            saveFile.exportMain()
           
           
        else:                                       #exits and confiirms whether to save changes
            selection = funct.saveExit()
            if selection.upper() == "E":
                    funct.exit()
            
                                        
            
                
       
            



#initiates the program, calls menu
mainProgram()