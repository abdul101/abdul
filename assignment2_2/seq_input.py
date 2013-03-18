def get_input():
    do = True
    lst_input=[]
    while do:
        inp = raw_input("enter sequence: ")
        if inp == "":
            do = False
        else:
            lst_input.append(inp)  
            
    return lst_input