# this module mainly validates user inputs  and opening and closing files
#used by many other modules

import os.path
import sys

#confirms exit and save changes
def saveExit():
    inpStr='Do you want to exit(E) or do you want to go back to the menu (M): '
    do = True
    while do:
        print 
        selection = raw_input(inpStr)
        if selection.upper() in ['m','M','E','e']:
            return selection.upper()
        else:
            print
            inpStr = 'Error, enter M or E: '
            

#gets path and checks if valid path, returns filename            
def fileNameMenu():           
    path=raw_input('Enter a valid Path for a PDB File:  ')
    fileLst,fileName,path = fileOpen(path)
    if fileLst == None:
        return None,None,None
    else:
        if validpdbFile(fileLst):   
            print 'The file ',fileName, 'has been successfully loaded'
            return fileLst,fileName,path
        else:
            return None,None,None

#exit program        
def exit():
    sys.exit()


#open file
def fileOpen(fileN):
        if fileN =='':
            fileN = os.getcwd()

        validDir,path = validDirectory(fileN)
        if validDir:
            fileNameAndPath,fileName = getFileName(path)
                          
        else:
            fileNameAndPath,fileName,path = validFile(fileN)
            
        if fileNameAndPath == None:
            return None,None,None       
        f = openFileRead(fileNameAndPath)
        if f != None:
            lstFile=f.readlines()
            if closeFile(f):
                return lstFile,fileName,path

        
        return None,None,None     
            
         
    
#checks if valid PDB file
def validpdbFile(lstFile):
    if lstFile[0][:6] != 'HEADER':
        return False
    else:
        return True        

#checks valid directory
def validDirectory(path):
    if os.path.isdir(path):
        if path[-1] =='/':
            return os.path.isdir(path),path
        else:
            return os.path.isdir(path),path+'/'
    else:
        return False,""
    
    
    
    
# checks if valid file, returns path and file name  
def validFile(fileName):
    try:
        index =fileName.index('/')          #used to trigger excption, find returns -1 which could indicate last position
        index =fileName.rfind('/')
        path = fileName[:index +1] 
        filename = fileName[index+1:]
        

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
        if os.path.isfile(path + fileName):
            return path+fileName,fileName,path
        
        elif os.path.isfile(path + fileName  +'.pdb'):
            return path+fileName,fileName  +'.pdb',path
        
        elif os.path.isfile(path + fileName  +'.PDB'):
            return path+fileName,fileName  +'.PDB',path
        else:
            return None,None,None
        
        

             

#parse sequence, format sequence for printing
def parseSequence(sequence,numberperline):
    seq=""
    index=0
    while index<len(sequence):
        if index == 0:
            seq += sequence[index:index+numberperline] + "\n"
        else:
            seq += " "* 15 +sequence[index:index+numberperline] + "\n"
        index +=numberperline
    return seq
    
    
#gets filename
def getFileName(path):
    lstFileName= os.listdir(path)
    for i in lstFileName:
        if os.path.splitext(i)[1]=='.pdb':
            return os.path.join(path,i),i
    return None,None

#open file for writing
def openFileWrite(path):
    try:
        f = open(path,'w')
        return f
    except:
        return None
 
#open file for reading    
def openFileRead(path):
    try:
        f = open(path,'r')
        return f
    except:
        return None

#close file    
def closeFile(f):
    try:
        f.close()
        return True
    except:
        return False
    

#gets three or one letter codon    
def getCodon(codon):
    
    codon_table = {
      'ALA': 'A', 'VAL':'V', 'ILE':'I','LEU':'L','MET':'M', 'PHE':'F','TYR':'Y','TRP':'W',
      'LYS':'K','ARG':'R','HIS':'H','ASP':'D','GLU':'E','SER':'S','THR':'T','ASN':'N','GLN':'Q',
      'CYS':'C','GLY':'G','PRO':'P' }
    if len(codon)==1:
        for i in codon_table:
            if codon_table[i]==codon:
                return i
            
    else:
        for i in codon_table:
            if i==codon:
                return codon_table[i]
            
    return None