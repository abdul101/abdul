def getNum():
    do = True
    inpStr ="Enter number: "
    while do:
        num = raw_input(inpStr)
        if num.isdigit() and int(num) >= 1:
            return int(num)
        else:
            inpStr = "Error enter number >= 1"
            

def dispNum(num):
    print "the first %d items in the sequence are:" % num
    if num == 1:
        print num
    else:
        addTwo=True
        sum =1
        print sum
        for i in range(1,num):
            if addTwo:
                sum += 2
                addTwo = False      
            else:
                sum += 3
                addTwo = True
            print sum


###Main

dispNum(getNum())        