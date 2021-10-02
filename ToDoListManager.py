from ToDoList import ToDoList
import pickle

displayWidth = 40
toDoLists = []

saveFile = "lists.dat"

def loadLists():
    try:
        with open(saveFile, "rb") as f:
            toDoLists = pickle.load(f)
    except:
        toDoLists = []
    return toDoLists 

def saveLists(data):
    with open(saveFile, "wb") as f:
        pickle.dump(data, f)

def printAllLists():
    for x in range(len(toDoLists)):
        toDoLists[x].printList(displayWidth)

def printListNames():
    for x in range(len(toDoLists)):                           # Print out the names of all of the lists
        print(x, ") ", toDoLists[x].name)

def printTaskNames(selectedList):
    for i in range(len(toDoLists[int(selectedList)].list)):         # Print out the names of all of the tasks in the selected list
        print(i, ") ", toDoLists[int(selectedList)].list[i].name)

def selectList():
    printListNames()                                                        # Print out the names of all of the lists       
    selectedList = input("Please Select: ")                                # and ask which one they want to select
    return selectedList

# -------------------------------------------------------------------- M A I N --------------------------------------------------------------------
toDoLists = loadLists()                                                         # Load any saved lists

while(1): 
    printAllLists()                                                             # Print all to do lists
                                                                                # Print Main Menu
    print("""                                                                     
    1) Create a New List
    2) Delete a list
    3) Add a Task
    4) Tick off a Task
    5) Mark a Task as Important
    6) Add/Change Due Date
    7) Show Completed Tasks
    8) Save and Exit
    """)

    userInput = input("Please Select (1-8): ")                                              # Ask for user selection

    if (userInput == "1"):                                                                  # When the user selects "Create a New List"
        newListName = input("What would you like to name your new list? ")                  # Get the name of the new task
        toDoLists.append(ToDoList(newListName))                                             # Add the new list to the page
        print(newListName, "has been created")                                              # Notify the user that thier new list has been made

    elif (userInput == "2"):                                                                # When the user selects "Delete a List"     
        selectedList = selectList()                                                         # Find out which list the user wants to select
        del toDoLists[int(selectedList)]                                                    # and delete that list

    elif (userInput == "3"):                                                                # When the user selects "Add a Task"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        newTaskName = input("What would you like to name your new task? ")                  # Get the name of the new task
        toDoLists[int(selectedList)].addToList(newTaskName)                                 # Add the task to the end of the selected list
        print(newTaskName, "has been added to ", toDoLists[int(selectedList)].name)         # Notify the user that their new task has been added to the list

    elif (userInput == "4"):                                                                # When the user selects "Tick off a Task"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to tick off the list? ")            # and ask which one they want to tick off
        toDoLists[int(selectedList)].tickOffTask(selectedTask)                              # Remove the item from the list and add it to the completed list

    elif (userInput == "5"):                                                                # When the user selects "Mark a Task as Important"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to mark as important? ")            # and ask which one they want to mark as important
        toDoLists[int(selectedList)].list[int(selectedTask)].markAsImportant()              # and mark that item as important

    elif (userInput == "6"):                                                                # When the user selects "Add/Change Due Date"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to set a due date for? ")           # and ask which one they want to set a due date for
        dueMonth = input("What month is this task due? ")                                   # Ask what month
        dueDay = input("What day is this task due? ")                                       # and day the task is due
        toDoLists[int(selectedList)].list[int(selectedTask)].setDueDate(dueDay, dueMonth)   # Then set the due date
         
    elif (userInput == "8"):                                                                # When the user selects "Save and Exit"
        saveLists(toDoLists)                                                                # Save the lists
        quit()                                                                              # and quit the program

    else:                                                                                   # Any other input is not valid
        print("Please enter a valid input")