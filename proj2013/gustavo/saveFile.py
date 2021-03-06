#modules allows user to export changes or save current file as a new file
import globalVar
import funct
import os.path
import time


#gets filename and path
def getFile(filename):
    try:
        index =filename.index('/')          #used to trigger excption, find returns -1 which could indicate last position
        index =filename.rfind('/')
        path = filename[:index +1] 
        filename = filename[index+1:]
        

        if os.path.isfile(path + filename):
            return path+filename,filename,path
        
        elif os.path.isfile(path + filename  +'.pdb'):
            return path+filename,filename  +'.pdb',path
        
        elif os.path.isfile(path + filename  +'.PDB'):
            return path+filename,filename  +'.PDB',path
        else:
            return None,None,None
        
        
    except:
        path = os.getcwd()
        if path[-1] != '/':
            path = path +'/'
            
        tupFnameExt = os.path.splitext(filename)
        if tupFnameExt[1] == '.pdb' or tupFnameExt[1] == '.PDB':
            if os.path.isfile(filename):
                return True,path+filename
            else:
                return False,path+filename
            
            
        
        
        if os.path.isfile(path + filename):
            return True,path + filename
        
        elif os.path.isfile(path + filename  +'.pdb'):
            return True,path + filename  +'.pdb'
        
        elif os.path.isfile(path + filename  +'.PDB'):
            return True,path + filename  +'.PDB'
        else:
            return False,path + filename  +'.pdb'
        
        
#display file exist and ask user for new file name or over write existing file
def dispFileExists(fileName):
    inpStr='The file %s already exist, to overwrite file press "Y" or enter a new name: ' % fileName
    do = True
    while do:
        inp = raw_input(inpStr)
        return inp

        

#display menu
def getMenuFileName(inpStr):
    inp = raw_input(inpStr)
    return inp

#gets filename and path
def getPath():
    fileNameAndPath =''
    inpStr='File path: '
    fileN = getMenuFileName(inpStr)
    do = True
    while do:
        if fileN in ['y','Y'] and fileNameAndPath != "":
            return fileNameAndPath 
        
        if fileN =='':
            fileN = os.getcwd()

        validDir,path = funct.validDirectory(fileN)
        if validDir:
            fileNameAndPath = path + 'new.pdb'
            if os.path.isfile(fileNameAndPath) == False:
                return fileNameAndPath
            else:
                strConf= dispFileExists(fileNameAndPath)
                if strConf.upper() =='Y':
                    return fileNameAndPath
            
                
                          
        else:
            fileExist,fileNameAndPath = getFile(fileN)
            if fileExist == False:
                return fileNameAndPath
            

            else:
                fileN= dispFileExists(fileNameAndPath)
                if fileN in ['y','Y'] :
                    return fileNameAndPath
                


# creates output file
def writeFile(path):   
    try: 
        f= open(path,'w')
        for line in globalVar.lstFile:
            f.write(line )
        
        f.close()
        return None
    except:
        return "Error wrting file."

#update file header            
def updateHeader():
    line = globalVar.lstFile[0]
    newLine ='HEADER    %40s%9s   %4s\n' % (line[10:50],time.strftime("%d-%b-%y"),line[62:66]) 
    globalVar.lstFile[0]=newLine
                       
#main program                    
def exportMain():
        fileName = getPath()
        updateHeader()
        strWrite= writeFile(fileName)
        if strWrite == None:
            print 'FILE SAVED.'
        else:
            print strWrite
        raw_input("Press [enter] to go back to the main menu.")
        