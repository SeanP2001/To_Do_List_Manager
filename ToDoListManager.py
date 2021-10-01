from ToDoList import ToDoList

displayWidth = 30
toDoLists = []

def printAllLists():
    
    for x in range(len(toDoLists)):
        toDoLists[x].printList(displayWidth)

while(1):
    # print all to do lists
    printAllLists()

    print("""

    1) Create a New List
    2) Select a List (to add or tick off a task)
    3) Save and Exit

    """)

    userInput = input("Please Select: ")

    if (userInput == "1"):
        newListName = input("What would you like to name you new list? ")

        toDoLists.append(ToDoList(newListName))

        print(newListName, "has been created")

    elif (userInput == "2"):
        for x in range(len(toDoLists)):
            print(x, ") ", toDoLists[x].name)
            
        listSelection = input("Please Select: ")

        while(1):
            toDoLists[int(listSelection)].printList(displayWidth)

            print("""

            1) Create a New Task
            2) Tick off a Task
            3) Return to all tasks

            """)

            listAction = input("Please Select: ")

            if (listAction == "1"):
                newTaskName = input("What would you like to name you new task? ")

                toDoLists[int(listSelection)].addToList(newTaskName)

                print(newTaskName, "has been added to ", toDoLists[int(listSelection)].name)

            #elif (listAction == "2"):

            #elif (listAction == "3"): 

            else:
                 print("Please enter a valid input")
            
            
    else:
        print("Please enter a valid input")



"""
list1 = ToDoList("ICE-1001")
list2 = ToDoList("ICE-2003")

list1.addToList("Complete Assignment 1")
list1.addToList("Setup Software")
list1.addToList("Email Lecturer")

list2.addToList("Meeting at 9AM")
list2.addToList("Read Resources")
list2.addToList("Finish Write-up")

list1.printList(30)
list2.printList(30)

"""