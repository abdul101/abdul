
def addDict(firstProt,secondProt,dic):
    if firstProt in dic.keys():
        list = dic[firstProt]
        if  secondProt not in list:
            dic[firstProt] = list + [secondProt]
    else:
        dic[firstProt] = [secondProt]


    if secondProt in dic.keys():
        list = dic[secondProt]
        if  firstProt not in list:
            dic[secondProt] = list + [firstProt]
    else:
        dic[secondProt ] = [firstProt]
    
    return dic


def getProt():
    index=0
    firstProt=''
    secondProt=''
    dict={}
    do = True
    inpStr ="Enter input an interaction: "
    while do:
        inp = raw_input(inpStr)
        if inp == "":
            return dict
        if ',' in inp:
            index = inp.find(',')
            firstProt=inp[:index]
            secondProt=inp[index+1:]
            dict=addDict(firstProt,secondProt,dict)
            
        else:
            print "ERROR: The input text is not in the correct format: P1,P2"
            
            
            
            
def queryProt(dic):
    do = True
    while do:
        inp = raw_input("Which protein do you want to query?: ")
        if inp == "":
            return
        if inp in dic.keys():
            list = dic[inp]
            print 'The interactions with %s are: ' % inp.upper()

            for i in list:
                print i
            print
        else:
            print 'The protein %s doesn"t have interactions registered in the system.' % inp.upper() 
            

#main
dict=getProt()
queryProt(dict)