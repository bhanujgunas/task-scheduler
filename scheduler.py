import csv
import os
import datetime
import time

os.chdir("D:/schedule/task-scheduler")
lst = []
file = "data.csv"
status = {'-1':"Missed",'0':"Not yet completed",'1':"Completed"}

def currents():#
    d = list(map(int,datetime.datetime.today().strftime("%Y/%m/%d").split('/')))
    #t=list(map(int,datetime.datetime.now().strftime(("%H:%M:%S")).split(":")))
    #return [d[0],d[1],d[2],t[0],t[1],t[2]]
    return [d[0],d[1],d[2]]

def getfiledata():
    f = open(file,"r",newline='\n',encoding="utf8")    
    re = csv.reader(f,delimiter=',')
    return list(re)

def alreadyexists(a):
    #global lst
    for i in lst:
        if i[:5] == a[:5]:
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

def addtosched():#
    dd,mm,yyyy = list(map(str,input("Enter the completion date (dd/mm/yyyy) :").split("/")))

    #hr,min,sec = list(map(str,input("Enter the completion time (hr:min:sec) (24hrs) : ").split(":")))

    task_name = input("Enter the task name : ")
    task_description = input("Enter the description : ")

    add,amm,ayy,ahr,amin,asec = currents()

    #task = [dd,mm,yyyy,hr,min,sec,task_name,task_description,add,amm,ayy,ahr,amin,asec,0]
    #task = [yyyy,mm,dd,hr,min,sec,task_name,task_description,add,amm,ayy,ahr,amin,asec,0]
    task = [yyyy,mm,dd,task_name,task_description,add,amm,ayy,ahr,amin,asec,0]

    if not alreadyexists(task):
        print("TASK ALREADY EXISTS...")
        return

    f = open(file,"a",newline='\n',encoding="utf8")    
    wr = csv.writer(f)
    wr.writerow(task)
    f.close()
    print("Added successfully...")
    sortlst()

def gettodaysched():#
    #global lst
    temp = []
    now = currents()[:3]
    for val in lst:
        t = [int(x) for x in val[:3]]
        if t==now:
            temp.append(val)
    print(f"\nTODAY'S SCHEDULE ({now[0]}/{now[1]}/{now[2]})....")
    for ind,j in enumerate(temp):
        
        i=j
        print(f"""\nTask {ind+1} : \nTask name : {i[3]}\nTask Description : {i[4]}""")
        print(status[j[-1]])
    return temp


def getallsched():#
    temp = []
    now = currents()
    for val in lst:
        t = [int(x) for x in val[:3]]
        '''
        if t[2]==now[2]:
            if t[1]==now[1]:
                if t[0]>=now[0]:
                    temp.append(val)
            elif t[1]>now[1]:
                temp.append(val)
        elif t[2]>now[2]:
            temp.append(val)
        '''
    #print(f"\nSCHEDULE ON AND AFTER ({now[0]}/{now[1]}/{now[2]})....")
    print("\nALL SCHEDULE...")
    for ind,i in enumerate(temp):
        if i[-1]==-1:
            continue  #missed
        print(f"\nTask {ind+1} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]}\nTask name : {i[3]}\nTask Description : {i[4]}")
        print(status[j[-1]])

    return temp
    

def getmissedsched():#
    num=1
    temp = []
    print("Missed Tasks....")
    for i in lst:
        if i[-1]==-1:
            print(f"\nTask {num} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]} \nTask name : {i[3]}\nTask Description : {i[4]}\nTask Added Date-Time : {i[5]}/{i[6]}/{i[7]} {i[8]}:{i[9]}:{i[10]}")
            num+=1
            temp.append(i)
    return temp



def history():#
    print("HISTORY...\n")
    for ind,i in enumerate(lst):
        print(f"""\nTask {ind+1} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]} \nTask name : {i[3]}\nTask Description : {i[4]}\nTask Added Date-Time : {i[5]}/{i[6]}/{i[7]} {i[8]}:{i[9]}:{i[10]}\nTask Status : {status[i[-1]]}""")

def menu():#
    print("....MY TASK SCHEDULER....")
    print("1. ADD TASK")
    print("2. VIEW TODAY\'S TASKS")
    print("3. VIEW ALL TASKS")
    print("4. VIEW MISSED TASKS")
    print("5. HISTORY")
    print("6. FINISH")
    print("7. EXIT")

    opt = int(input("Enter the option : "))
    if opt>7 or opt<1:
        print("Invalid OPTION")
        opt=menu()
    return opt

def checkmissed():
    temp1 = currents()
    for i in lst:
        temp2=i
        if temp1>temp2:
            return 1
    return 0

def lstwrite():
    f = open(file,"w",newline='\n',encoding="utf8")    
    wr = csv.writer(f)
    wr.writerows(lst)
    f.close()

def finish():#
    opt1 = int(input("1. GetTodaySchedule\n2. GetAllSchedule\nEnter option : "))
    if opt1==1:
        templst = [x for x in gettodaysched() if x[-1]!=1]
        if len(templst)>0:
            ans = int(input("Enter finished task number : "))+1
            for ind,i in enumerate(templst):
                if ind==ans:
                    index = lst.index(i)
                    lst[index][-1]=1
                    lstwrite()
                    return

    elif opt1==2:
        templst = [x for x in getallsched() if x[-1]!=1]
        if len(templst)>0:
            ans = int(input("Enter finished task number : "))-1
            for ind,i in enumerate(templst):
                if ind==ans:
                    index = lst.index(i)
                    lst[index][-1]=1
                    lstwrite()
                    return

    else:
        print("Entered wrong option...")
        time.sleep(3)



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
        elif opt==6:
            finish()
        else:
            print("Exiting....")
            break
        input("\nPress ENTER to continue...")
        os.system("cls")
