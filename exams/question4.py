import os.path
import sys


def getHealthyFile():
    inpStr="Path of the expression levels for the healthy patients: "
    do = True
    while do:
        path = raw_input(inpStr)
        if path == "":
            path = os.getcwd() + '/healthy.txt'
        if os.path.isdir(path):
            if path[-1]=='/':
                filename= path + 'healthy.txt'
            else:
                filename= path + '/healthy.txt'
            if os.path.isfile(filename):
                return filename
        else:
            if os.path.isfile(filename):
                if 'healthy.txt' in filename:
                    return filename
       
        inpStr= 'Error invalid filename, enter path for healthy.txt: '
       
       
def getInfectedFile():      
    inpStr="Path of the expression levels for the infected patients: "
    do = True
    while do:
        path = raw_input(inpStr)
        if path == "":
            path = os.getcwd() + '/infected.txt'
        if os.path.isdir(path):
            if path[-1]=='/':
                filename= path + 'infected.txt'
            else:
                filename= path + '/infected.txt'
            if os.path.isfile(filename):
                return filename
        else:
            if os.path.isfile(filename):
                if 'infected.txt' in filename:
                    return filename
       
        inpStr= 'Error invalid filename, enter path for healthy.txt: '
 
 
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
    
 
       
def getList(fileName):
    f = openFileRead(fileName)
    if f == None:
        return "error opening file- %s " % fileName
    else:
        lstFile=f.readlines()
        if closeFile(f):
            return lstFile
        else:
            return None
    
    
def dispMenu():
    do = True
    while do:
        
        print 'Select an option:'
        print ' [T] Select a threshold value'
        print ' [D] Display categorized proteins ordered by delta'
        print ' [F] Create 3 files with the different categories'
        print ' [x] Exit'
        
        inp = raw_input(':')
        if inp.upper() in ['T','D','F','X']:
            return inp
        else:
            print 'Error - invalid selection'
    
    
    
def getThreshold():
    do = True
    while do:
        
        inp = raw_input("enter thershold value: ")
        if inp.isdigit():
            return float(inp)
        print 'Error enter valid number'
   
def overexpressed(listHealthy,listInfected,th):
    overExpressed=''
    for i in range (0,len(listHealthy)):
        proteinH= listHealthy[i][:6]
        proteinI= listInfected[i][:6]
        ave_H = float(listHealthy[i][7:11])+float(listHealthy[i][12:16])+float(listHealthy[i][17:21])
        ave_I = float(listInfected[i][7:11])+float(listInfected[i][12:16])
          
        if (ave_H + th) < ave_I:
            sum =ave_H 
            overExpressed +=  proteinH + "  " +sum +'\n'

def underexpressed(listHealthy,listInfected,th):
    underExpressed=''
    for i in range (0,len(listHealthy)):
        proteinH= listHealthy[i][:6]
        proteinI= listInfected[i][:6]
        ave_H = float(listHealthy[i][7:11])+float(listHealthy[i][12:16])+float(listHealthy[i][17:21])
        ave_I = float(listInfected[i][7:11])+float(listInfected[i][12:16])
          
        if (ave_H - th) >  ave_I:
            sum = ave_H 
            underExpressed +=  proteinH + "  " + sum +'\n'
                         
        
def normalexpressed(listHealthy,listInfected,th):
    normalExpressed=''
    for i in range (0,len(listHealthy)):
        proteinH= listHealthy[i][:6]
        proteinI= listInfected[i][:6]
        ave_H = float(listHealthy[i][7:11])+float(listHealthy[i][12:16])+float(listHealthy[i][17:21])
        ave_I = float(listInfected[i][7:11])+float(listInfected[i][12:16])
          
        if (ave_H - th) <  ave_I and (ave_H +th) > ave_I:
            sum = ave_H 
            normalExpressed +=  proteinH + "  " + sum +'\n'
                         
         

def dispProteins(th,hList,iList):
   
    oXpressed = overexpressed(hList,iList,th)
    nXpressed = normalexpressed(hList,iList,th)
    uXpressed = underexpressed(hList,iList,th)
    
    print "list using a threshold of ", th
    print 'Overexpressed proteins:'
    print oXpressed
     
    print 'Normally expressed proteins:'
    print nXpressed
     
    print 'Underexpressed proteins:'
    print uXpressed
     
    return oXpressed,nXpressed,uXpressed

# creates output file
def writeFile(path,expression):   
    try: 
        f= open(path,'w')
        f.writelines(expression )
        
        f.close()
        return None
    except:
        return "Error wrting file."   

def createOutFile(oXpressed,nXpressed,uXpressed):
    inp= raw_input("what is the predix of the files: ")
    error = writeFile(inp + '_OVER.txt',oXpressed)
    if error == None:
        print 'Error writing file'
        return
    error = writeFile(inp+ '_NORMAL.txt',nXpressed)
    if error == None:
        print 'Error writing file'
        return
    error = writeFile(inp+'_UNDER.txt',uXpressed)
    if error == None:
        print 'Error writing file'
        return
    print 'the files %s_OVER.txt ,%s_NORMAL.txt, %s_UNDER.txt have been succesfully created. ' % inp

def aveProtein_H(lst):                #assuming protein only occurs once in file
    for i in lst:
        print '%s  %f' % (i[:5],(float(i[7:11]) + float(i[12:16]) +  float(i[17:21])) / 3)
        
def aveProtein_I(lst):                #assuming protein only occurs once in file
    for i in lst:
        print '%s  %f' % (i[:5],(float(i[7:11]) + float(i[12:16]) ) / 2)
        
def aveProteinMany(lst):            #assuming many occurances of the same protein in file
    count = 1
    dic={}
    for i in list:
        if i in dic.keys():
            dic[i] =  dic[i] + 1
        else:
            dic[i] = 1
            
# print proteins
    print 'Average proteins'
    for i in dic:
        print i,'  ',dic[i]     
        
#calculate delat
def calcDelta(listHealthy,listInfected):
    print 'delta values for all proteins'
    for i in range (0,len(listHealthy)):
        ave_H = float(listHealthy[i][7:11])+float(listHealthy[i][12:16])+float(listHealthy[i][17:21])
        ave_I = float(listInfected[i][7:11])+float(listInfected[i][12:16])
        delta = ave_I - ave_H
        print listHealthy[i][:6] + "   " + delta
        

def dispDelta(healthyList,infectedList,th):
    ###
    return "not enough time !!! to do"
    
    
    
    
          
#main
oXpressed=''
nXpressed=''
uXpressed=''
thresholdValue=1.0
healthyFile=getHealthyFile()
infectedFile=getInfectedFile()
healthyList= getList(healthyFile)
infectedList=getList(infectedFile)
print 'Number of proteins in healthy file: %d' % len(healthyList)
print 'Number of proteins in infected file: %d' % len(infectedList)
print 'average protein in healthy list:'
aveProtein_H(healthyList)
print 'average protein in infected list:'
aveProtein_I(infectedList)


print 'average protein in healthy list:'
aveProteinMany(healthyList)

print 'average protein in infected list:'
aveProteinMany(infectedList)

print 'delta values for all proteins'
calcDelta(healthyList,infectedList)


dispDelta(healthyList,infectedList)
do = True
while do:
    inp= dispMenu()
    if inp == 'T':
        thresholdValue=getThreshold()
    elif inp== 'D':
        oXpressed,nXpressed,uXpressed=dispProteins(thresholdValue,healthyList,infectedList)
    elif inp == 'F':
        createOutFile(oXpressed,nXpressed,uXpressed)
    else:
        sys.exit()    

dispProteins(thresholdValue,healthyList,infectedList)

