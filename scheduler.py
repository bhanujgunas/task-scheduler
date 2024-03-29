def addtosched(newtask):
    pass

def gettodaysched():
    pass

def getallsched():
    pass

def getmissedsched():
    pass

def getsched():
    pass

def history():
    pass

def menu():
    print("....MY TASK SCHEDULER....")
    print("1. ADD TASK")
    print("2. VIEW TODAY\'S TASKS")
    print("3. VIEW ALL TASKS")
    print("4. VIEW MISSED TASKS")
    print("5. HISTORY")
    print("6. EXIT")

    opt = int(input("Enter the option : "))
    if opt>6 or opt<1:
        print("Invalid OPTION")
        opt=menu()
    return opt


if __name__=="__main__":
    
    while 1:

        opt = menu()
        
        if opt==1:
            addtosched()
        elif opt==2:
            gettodaysched()
        elif opt==3:
            getallsched()
        elif opt==4:
            getmissedsched()
        elif opt==5:
            history()
        else:
            break
