#display the program main menu

def dispMainMenu():
    print '********************************************************************************'
    print '* PDB FILE ANALYZER                                                            *'
    print '********************************************************************************'
    print '* Select an option from below:                                                 *'
    print '*                                                                              *'
    print '*      1) Open a PDB File                        (O)                           *' 
    print '*      2) Information                            (I)                           *'
    print '*      3) Show histogram of amino acids          (H)                           *' 
    print '*      4) Display Secondary Structure            (S)                           *' 
    print '*      5) Manipulate Helix or Sheet              (M)                           *' 
    print '*      6) Export PDB File                        (X)                           *' 
    print '*      7) Exit                                   (Q)                           *' 
    print '*                                                                              *'


#display footer section of main menu
def footerMainMenu(fileName):
    label = 'Current PDB: %s *' % (fileName)
    print '*',label.rjust(78)                                                                
    print '********************************************************************************'   

    
