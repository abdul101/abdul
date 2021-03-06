#display histogram
import funct

#display histogram based on number in ascending 
def dispNoAsc(aaDic):
    for i in sorted(aaDic.items(), key=lambda t: t[1]):
        count = i[1]
        print i[0].title(), '(  %2s)  : %s' % (str(count),'*' * count)
        
        
    print

#display histogram based on number in descending 
def dispNoDesc(aaDic):
    for i in sorted(aaDic.items(), key=lambda t: t[1],reverse=True):
        count = i[1]
        print i[0].title(), '(  %2s)  : %s' % (str(count),'*' * count)
        
        
    print

#display histogram based on alpabetical order in ascending 
def dispAlpAsc(aaDic):
    for i in sorted(aaDic):
        count = aaDic[i]
        print i.title(),    '(  %2s)  : %s' % (str(count),'*' * count)
        
    print

#display histogram based on alpabetical order in ascending 
def dispAlpDesc(aaDic):
    for i in sorted(aaDic,reverse=True):
        count = aaDic[i]
        print i.title(),    '(  %2s)  : %s' % (str(count),'*' * count)
        
    print

#  join equences   
def joinSequences(dicChain):
    sequences = ''
    for i in dicChain:
        lstChain=dicChain[i]
        sequences += lstChain[0]
        
    return sequences

#count sequences
def aaCount(sequences):
    aaDic={}
    for i in range(len(sequences)):
        codon = funct.getCodon(sequences[i])
        if codon.capitalize() in aaDic:
            count = aaDic[codon.capitalize()]
            aaDic[codon.capitalize()] = count + 1
        else:
            
            aaDic[codon.capitalize()] = 1
    
       
    return aaDic


#display histograms menu
def histoMenu():
    strInput='order by: '
    do = True
    while do:
        print 'Choose an option to order by:'
        print '   number of amino acids - ascending  (an)'
        print '   number of amino acids - descending (dn)'
        print '   alphabetically - ascending         (aa)'
        print '   alphabetically - descending        (da)'
        selection = raw_input(strInput)
        print
    
        try:
            if selection.upper() in ['AN','DN','AA','DA']:
                return selection.lower()
            else:
                strInput = "error in valid option selected: "
        except:
                strInput = "error in valid option selected: "

#main section of histogram module
def histoMain(dicChain):
    aaDic={}
    seq=''
    seq=joinSequences(dicChain)
    aaDic=aaCount(seq)
    selection = histoMenu()
    
    if selection == 'an':
        dispNoAsc(aaDic)
        
    if selection == 'dn':
        dispNoDesc(aaDic)
        
    if selection == 'da':
        dispAlpDesc(aaDic)
        
    if selection == 'aa':
        dispAlpAsc(aaDic)
    
    
    
    
    