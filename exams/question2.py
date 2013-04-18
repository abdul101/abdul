def getPoints(list_X):
    tupTeamRes=()
    listResult=[]

    for i in list_X:
        if i[2]==i[3]:
            tupTeamRes = i[0],1
            listResult.append(tupTeamRes)
            tupTeamRes = i[1],1
            listResult.append(tupTeamRes)
        elif [2] >= i[3]:
            tupTeamRes = i[0],3
            listResult.append(tupTeamRes)
            tupTeamRes = i[1],0
            listResult.append(tupTeamRes)
        else:
            tupTeamRes = i[1],0
            listResult.append(tupTeamRes)
            tupTeamRes = i[0],3
            listResult.append(tupTeamRes)    
    
    
    
    return listResult 
 
    
    
    
list_X = [ ('PSG','Barcelona',2,2),('Bayern Munchen','Juventes',2,0),('Malaga','Borussia Dort',0,0),('Real Madrid','Gelat',3,0)]
results= getPoints(list_X)
print results
