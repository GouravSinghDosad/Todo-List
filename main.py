

def addTask(taskName, taskList):
    taskList.append(taskName)


def allTasks(taskList):
    for i in range(len(taskList)):
            print(taskList[i])
            # print("\n")


taskList = []

while True:

    print("\n")
    print("=====TODO LIST APP===== \n")
    print("Press: 1 -> If you want to add a task")
    print("Press: 2 -> If you want to view tasks")
    print("Press: 3 -> If you want to remove a task")
    print("Press: 5 -> Want to create a new TO-DO LIST")
    print("Press: 4 -> Exit from the TODO LIST APP \n")

    choice = int(input("Enter your choice: "))



    if(choice == 1):

        print()
        print("OK. So, you chose 1 well then--- \n")
        taskName = input("Name of the task: ")
        addTask(taskName, taskList)
        print("Task Added Succesfully \n")

    elif(choice == 2):

        print("Here's the list of the tasks----- \n")

        allTasks(taskList)

    elif(choice == 3):

        print("So you wanted to remove a task---- \n")
        print(" Here's the list of the tasks from list:")

        allTasks(taskList)

        task = input("Enter the task you want to be deleted: ")
        print("\n")

        taskList.remove(task)

        print("Here's the tasks present in TODO LIST---- \n")

        allTasks(taskList)

    elif(choice == 4):
        print("See you again, GOODBYE!!!!!")
        break
    else:
        print("You made the WRONG choice!!!!!!!!!!")

    