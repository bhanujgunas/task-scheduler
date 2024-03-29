import csv,os,datetime
os.chdir("D:/schedule/task-scheduler")
lst = []
file = "data.csv"

def currents():
    d = list(map(int,datetime.datetime.today().strftime("%d/%m/%Y").split('/')))
    t=list(map(int,datetime.datetime.now().strftime(("%H:%M:%S")).split(":")))
    return [d[0],d[1],d[2],t[0],t[1],t[2]]

def getfiledata():
    f = open(file,"r",newline='\n',encoding="utf8")    
    re = csv.reader(f,delimiter=',')
    return list(re)

def alreadyexists(a):
    #global lst
    for i in lst:
        if i[:8] == a[:8]:
            return 0
    lst.append(a)
    return 1
'''
def existscan():
    global lst
    temp = []
    for i,j in enumerate(lst):
        for k,l in enumerate(lst):
            if i==k:
                continue
            else:
                if j[:8]==l[:8]:
                    temp.append(j)
    return temp
'''

def sortlst():
    # sort the list and write it to the file
    pass

def addtosched():
    #global lst
    dd,mm,yyyy = list(map(str,input("Enter the completion date (dd/mm/yyyy) :").split("/")))

    hr,min,sec = list(map(str,input("Enter the completion time (hr:min:sec) (24hrs) : ").split(":")))

    task_name = input("Enter the task name : ")
    task_description = input("Enter the description : ")

    add,amm,ayy,ahr,amin,asec = currents()

    task = [dd,mm,yyyy,hr,min,sec,task_name,task_description,add,amm,ayy,ahr,amin,asec]

    if not alreadyexists(task):
        print("TASK ALREADY EXISTS...")
        return

    f = open(file,"a",newline='\n',encoding="utf8")    
    wr = csv.writer(f)
    wr.writerow(task)
    f.close()
    print("Added successfully...")
    sortlst()

def gettodaysched():
    #global lst
    temp = []
    now = currents()[:3]
    for i in lst:
        t = [int(x) for x in i[:3]]
        if t==now:
            temp.append(i)
    print(f"\nTODAY'S SCHEDULE ({now[0]}/{now[1]}/{now[2]})....")
    for ind,i in enumerate(temp):
        print(f"\nTask {ind+1} : \nCompletion Time : {i[3]}:{i[4]}:{i[5]}\nTask name : {i[6]}\nTask Description : {i[7]}")


def getallsched():
    #global lst
    for ind,i in enumerate(lst):
        print(f"\nTask {ind+1} : \nCompletion Date-Time : {i[0]}/{i[1]}/{i[2]} {i[3]}:{i[4]}:{i[5]}\nTask name : {i[6]}\nTask Description : {i[7]}\nTask Added Date-Time : {i[8]}/{i[9]}/{i[10]} {i[11]}:{i[12]}:{i[13]}")

def getmissedsched():
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

    if os.path.exists(file):
        lst = getfiledata()

    while 1:

        opt = menu()
        os.system("cls")
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
            print("Exiting....")
            break
        input("\nPress ENTER to continue...")
        os.system("cls")
