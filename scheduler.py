
import os,csv
os.chdir("D:\Subd\schedule")
"""
with open("schedule.csv","w") as csv_file:
    reader_csv = csv.reader(csv_file)
    reader_csv.writerow()
"""
lst=[["apple","apple"],["orange","orange"]]

def addtosched(newtask):
    f=open("schedule.csv",'w',newline='\n',encoding="utf8")
    w = csv.writer(f)
    lst.append(newtask)
    w.writerows(lst)    
    f.close()

def gettodaysched():
    pass

def getallsched():
    pass

def getmissedsched():
    pass

def getsched():

    date=list(map(int,input("Enter the date of task (dd-mm-yyyy) : ").split('-')))
    temp=input("Enter the time of task completion : ")
    time=list(map(int,temp.split(':'))) if temp!='' else ''
    return [date,time]
def menu():
    print("....MY TASK SCHEDULER....")
    print("1. ADD TASK")
    print("2. VIEW TODAY\'S TASKS")
    print("3. VIEW ALL TASKS")
    print("4. VIEW MISSED TASKS")
    opt = int(input("Enter the option : "))
    if opt>4 or opt<1:
        print("Invalid OPTION")
        opt=menu()
    return opt


if __name__=="1__main__":
    opt = menu()

    if opt==1:
        addtosched()
    elif opt==2:
        gettodaysched()
    elif opt==3:
        getallsched()
    else:
        getmissedsched()
