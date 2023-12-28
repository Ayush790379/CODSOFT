
work_list=[]

def addtask():
    task=input("Enter the task\n")
    work_list.append(task)
def deltask():
    taskno=int(input("Enter the serial number of the task to be deleted\n  : "))

    if taskno<len(work_list):
        work_list.pop(taskno-1)
    else:
        print("Index out of range!\n")

def updatetask():
    taskno=int(input("Which serial number task do you want to update : "))
    if taskno<len(work_list):
        s = input("Enter the new task : ")
        work_list[taskno - 1] = s
    else:
        print("Index out of range!\n")

def displaytask():
    if len(work_list)==0:
        print("Your to-do list is empty")
    else:

        for i in range(0,len(work_list)):
            print(i+1,work_list[i])




#COMMAND LINE INTERFACE
cho="y"
while(cho=="y"):
    choice=int(input("Press 1 to add a task in to-do list.\nPress 2 to delete a task from to-do list.\nPress 3 to update a task in to-do list\nPress 4 to display your to-do list\n : "))
    if choice==1:
        addtask()
    elif choice==2:
        deltask()
    elif choice==3:
        updatetask()
    elif choice==4:
        displaytask()
    else:
        print("Please enter a valid choice (1/2/3/4)\n")




    cho=input("Do you wish to continue? (y/n)\n : ")
    print("--------------------------------------------------------------------------------------")










