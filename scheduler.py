import csv
import os
import datetime
import time

#os.chdir("D:/schedule/task-scheduler")
lst = []
file = "data.csv"
status = {'-1':"Missed",'0':"Not yet completed",'1':"Completed"}

def currents():#
    d = list(map(str,datetime.datetime.today().strftime("%Y/%m/%d").split('/')))
    t=list(map(str,datetime.datetime.now().strftime(("%H:%M:%S")).split(":")))
    return [d[0],d[1],d[2],t[0],t[1],t[2]]
    

def getfiledata():#
    f = open(file,"r",newline='\n',encoding="utf8")    
    re = csv.reader(f,delimiter=',')
    return list(re)

def alreadyexists(a):#
    for i in lst:
        if i[:5] == a[:5]:
            return 0
    lst.append(a)
    return 1


def addtosched():#
    dd,mm,yyyy = list(map(str,input("Enter the completion date (dd/mm/yyyy) :").split("/")))

    task_name = input("Enter the task name : ")
    task_description = input("Enter the description : ")

    add,amm,ayy,ahr,amin,asec = currents()

    task = [yyyy,mm,dd,task_name,task_description,add,amm,ayy,ahr,amin,asec,'0']

    if not alreadyexists(task):
        print("TASK ALREADY EXISTS...")
        return
    
    lst.sort()
    lstwrite()
    print("Added successfully...")
    

def gettodaysched():#
    temp = []
    now = [int(x) for x in currents()[:3]]
    for val in lst:
        t = [int(x) for x in val[:3]]
        if t==now:
            temp.append(val)
    if len(temp)>0:
        print(f"\nTODAY'S SCHEDULE ({now[0]}/{now[1]}/{now[2]})....")
        for ind,j in enumerate(temp):
            
            i=j
            print(f"""\nTask {ind+1} : \nTask name : {i[3]}\nTask Description : {i[4]}""")
            print(status[j[-1]])
    return temp


def getallsched():#
    temp = lst
    if len(temp)>0:
        print("\nALL SCHEDULE...")
        for ind,i in enumerate(temp):
            if i[-1]=='-1':
                continue  #missed
            print(f"\nTask {ind+1} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]}\nTask name : {i[3]}\nTask Description : {i[4]}")
            print(status[str(i[-1])])

    return temp
    

def getmissedsched():#
    num=1
    temp = []
    print("Missed Tasks....")
    for i in lst:
        if i[-1]=='-1':
            print(f"\nTask {num} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]} \nTask name : {i[3]}\nTask Description : {i[4]}\nTask Added Date-Time : {i[5]}/{i[6]}/{i[7]} {i[8]}:{i[9]}:{i[10]}")
            num+=1
            temp.append(i)
    return temp



def history():#
    print("HISTORY...\n")
    for ind,i in enumerate(lst):
        print(f"""\nTask {ind+1} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]} \nTask name : {i[3]}\nTask Description : {i[4]}\nTask Added Date-Time : {i[5]}/{i[6]}/{i[7]} {i[8]}:{i[9]}:{i[10]}\nTask Status : {status[str(i[-1])]}""")

def menu():#
    missedassign()
    print("....MY TASK SCHEDULER....")
    print("1. ADD TASK")
    print("2. VIEW TODAY\'S TASKS")
    print("3. VIEW ALL TASKS")
    print("4. VIEW MISSED TASKS")
    print("5. HISTORY")
    print("6. FINISH")
    print("7. DELETE TASK")
    print("8. VIEW FINISHED TASKS")
    print("9. EXIT")

    opt = int(input("Enter the option : "))
    if opt>8 or opt<1:
        print("Invalid OPTION")
        opt=menu()
        if len(lst)==0 and opt>1:
            return 0
    return opt

def lstwrite():#
    f = open(file,"w",newline='\n',encoding="utf8")    
    wr = csv.writer(f)
    wr.writerows(lst)
    f.close()

def finish():#
    print("Enter '1' if the task is scheduled today otherwise enter '2'...")
    opt1 = int(input("1. GetTodaySchedule\n2. GetAllSchedule\nEnter option : "))
    if opt1==1:
        templst = [x for x in gettodaysched() if x[-1]!='1']
        if len(templst)>0:
            ans = int(input("Enter finished task number : "))-1
            for ind,i in enumerate(templst):
                if ind==ans:
                    index = lst.index(i)
                    lst[index][-1]='1'
                    lstwrite()
                    print(f"\nTask '{lst[index][3]}' is finished...")
                    return

    elif opt1==2:
        templst = [x for x in getallsched() if x[-1]!='1']
        if len(templst)>0:
            ans = int(input("Enter finished task number : "))-1
            for ind,i in enumerate(templst):
                if ind==ans:
                    index = lst.index(i)
                    lst[index][-1]='1'
                    lstwrite()
                    print(f"\nTask '{lst[index][3]}' is finished...")
                    return

    else:
        print("Entered wrong option...")
        time.sleep(3)


def missedassign():#
    for ind,i in enumerate(lst):
        if i[:3]<i[5:8]:
            lst[ind][-1]='-1'
    lstwrite()

def delete():
    opt1 = int(input("1. GetTodaySchedule\n2. GetAllSchedule\nEnter option : "))
    if opt1==1:
        templst = [x for x in gettodaysched() if x[-1]!='1']
        if len(templst)>0:
            ans = int(input("Enter task number to delete : "))-1
            for ind,i in enumerate(templst):
                if ind==ans:
                    print(f"Task deleted...")
                    lst.remove(i)
                    lstwrite()
                    time.sleep(3)
                    return


    elif opt1==2:
        templst = [x for x in getallsched() if x[-1]!='1']
        if len(templst)>0:
            ans = int(input("Enter task number to delete : "))-1
            for ind,i in enumerate(templst):
                if ind==ans:
                    print(f"Task deleted...")
                    lst.remove(i)
                    lstwrite()
                    time.sleep(3)
                    return

    else:
        print("Entered wrong option...")
        time.sleep(3)

def finishedtoday():
    temp = []
    now = [int(x) for x in currents()[:3]]
    for val in lst:
        t = [int(x) for x in val[:3]]
        if t==now:
            temp.append(val)
    templst = [x for x in gettodaysched() if x[-1]=='1']
    return templst

def finishedall():
    temp = []
    for i in lst:
        if i[-1]=='1':
            temp.append(i)
    return temp
    

def finishedtasks():
    opt1 = int(input("1. GetTodaySchedule\n2. GetAllSchedule\nEnter option : "))
    if opt1==1:
        temp = finishedtoday()
        if len(temp)>0:
            print("TODAY'S FINISHED TASKS...")
            for ind,i in enumerate(temp):
                print(f"""\nTask {ind+1} : \nTask name : {i[3]}\nTask Description : {i[4]}\n""")
        else:
            print("NO FINISHED TASKS FOR TODAY....")


    elif opt1==2:
        temp = finishedall()
        if len(temp)>0:
            print("\nALL FINISHED TASKS...")
            for ind,i in enumerate(temp):
                print(f"\nTask {ind+1} : \nCompletion Date : {i[0]}/{i[1]}/{i[2]}\nTask name : {i[3]}\nTask Description : {i[4]}\n")      
        else:
            print("YOU HAVEN'T FINISHED ANY TASKS YET...")


    else:
        print("Entered wrong option...")
        time.sleep(3)

def lstempty():
    print("No tasks are available...\nAdd new tasks to do any operations...")
    time.sleep(2)

if __name__=="__main__":

    if os.path.exists(file):
        lst = getfiledata()

    while 1:
        try:  
            opt = menu()
            os.system("cls")
            if opt==0:
                lstempty()
            elif opt==1:
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
            elif opt==7:
                delete()
            elif opt==8:
                finishedtasks()
            else:
                print("Exiting....")
                time.sleep(1)
                break
        except:
            print("Error...")
            time.sleep(1)

        input("\nPress ENTER to continue...")
        os.system("cls")
