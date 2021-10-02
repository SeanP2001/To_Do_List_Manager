from ToDoList import ToDoList
import pickle

# --------------------------------------------------------------- V A R I A B L E S ---------------------------------------------------------------
displayWidth = 40                                    # The char width that lists will be printed at
toDoLists = []                                       # The list where to do list objects are stored

saveFile = "lists.dat"                               # The file where the to do lists are saved

# --------------------------------------------------------------- F U N C T I O N S ---------------------------------------------------------------
def loadLists():                                                   # load the lists stored in the file
    try:                                                           # try to open the file (Read) 
        with open(saveFile, "rb") as f: 
            toDoLists = pickle.load(f)                             # and load the to do lists into the "toDoLists" list 
    except:                                                        # If that fails
        toDoLists = []                                             # continue with no to do lists
    return toDoLists 

def saveLists(data):                                               # save the to do lists to the file
    with open(saveFile, "wb") as f:                                # open the file (Write)
        pickle.dump(data, f)                                       # and dump the to do lists into the file

def printAllLists():                                               # Prints all lists
    for x in range(len(toDoLists)):                                # Go through all to do lists
        toDoLists[x].printList(displayWidth)                       # and for each one, print the list

def printAllCompleteLists():                                       # Prints all of the lists' completed tasks
    for x in range(len(toDoLists)):                                # Go through all lists
        toDoLists[x].printCompletedList(displayWidth)              # and print out all of it's completed tasks

def printListNames():                                              # Print the names of all of the lists e.g. "1) Work"
    for x in range(len(toDoLists)):                                # Go through all lists
        print(x, ") ", toDoLists[x].name)                          # and print out the list number followed by the name 

def printTaskNames(selectedList):                                  # Print the names of all of the tasks in a selected list e.g. "1) Follow up Emails"
    for x in range(len(toDoLists[int(selectedList)].list)):        # Go through all of the tasks in the selected list
        print(x, ") ", toDoLists[int(selectedList)].list[x].name)  # and print out the task number followed by the name

def selectList():                                                  # Print the list names and return the number of the list selected
    printListNames()                                               # Print the names of all of the lists e.g. "1) Work"       
    selectedList = input("Please Select: ")                        # and ask which one they want to select
    return selectedList                                            # return the selected list

# -------------------------------------------------------------------- M A I N --------------------------------------------------------------------
toDoLists = loadLists()                                            # Load any saved lists

while(1): 
    printAllLists()                                                # Print all to do lists
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

    userInput = input("Please Select (1-8): ")                     # Ask for user selection

# ------------------------------------------------------ C R E A T E   A   N E W   L I S T ------------------------------------------------------
    if (userInput == "1"):                                                                  # When the user selects "Create a New List"
        newListName = input("What would you like to name your new list? ")                  # Get the name of the new task
        toDoLists.append(ToDoList(newListName))                                             # Add the new list to the page
        print(newListName, "has been created")                                              # Notify the user that thier new list has been made

# ---------------------------------------------------------- D E L E T E   A   L I S T ----------------------------------------------------------
    elif (userInput == "2"):                                                                # When the user selects "Delete a List"     
        selectedList = selectList()                                                         # Find out which list the user wants to select
        del toDoLists[int(selectedList)]                                                    # and delete that list

# ------------------------------------------------------------- A D D   A   T A S K -------------------------------------------------------------
    elif (userInput == "3"):                                                                # When the user selects "Add a Task"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        newTaskName = input("What would you like to name your new task? ")                  # Get the name of the new task
        toDoLists[int(selectedList)].addToList(newTaskName)                                 # Add the task to the end of the selected list
        print(newTaskName, "has been added to ", toDoLists[int(selectedList)].name)         # Notify the user that their new task has been added to the list

# -------------------------------------------------------- T I C K   O F F   A   T A S K --------------------------------------------------------
    elif (userInput == "4"):                                                                # When the user selects "Tick off a Task"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to tick off the list? ")            # and ask which one they want to tick off
        toDoLists[int(selectedList)].tickOffTask(selectedTask)                              # Remove the item from the list and add it to the completed list

# ----------------------------------------------- M A R K   A   T A S K   A S   I M P O R T A N T -----------------------------------------------
    elif (userInput == "5"):                                                                # When the user selects "Mark a Task as Important"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to mark as important? ")            # and ask which one they want to mark as important
        toDoLists[int(selectedList)].list[int(selectedTask)].markAsImportant()              # and mark that item as important

# ---------------------------------------------------- A D D / C H A N G E   D U E   D A T E ----------------------------------------------------
    elif (userInput == "6"):                                                                # When the user selects "Add/Change Due Date"
        selectedList = selectList()                                                         # Find out which list the user wants to select
        printTaskNames(selectedList)                                                        # Print the task names for the selected list
        selectedTask = input("Which task would you like to set a due date for? ")           # and ask which one they want to set a due date for
        dueMonth = input("What month is this task due? ")                                   # Ask what month
        dueDay = input("What day is this task due? ")                                       # and day the task is due
        toDoLists[int(selectedList)].list[int(selectedTask)].setDueDate(dueDay, dueMonth)   # Then set the due date

# --------------------------------------------------- S H O W   C O M P L E T E D   T A S K S ---------------------------------------------------         
    elif (userInput == "7"):                                                                # When the user selects "Show Completed Tasks"
        print("\033[1;32;40m Completed Tasks\n")                                            # change terminal text colour to green
        printAllCompleteLists()                                                             # print out all of the completed tasks
        input("Press enter to return to viewing the current tasks... ")                     # and day the task is due
        print("\033[1;37;40m")                                                              # change terminal colour back to white

# ---------------------------------------------------------- S A V E   A N D   E X I T ----------------------------------------------------------         
    elif (userInput == "8"):                                                                # When the user selects "Save and Exit"
        saveLists(toDoLists)                                                                # Save the lists
        quit()                                                                              # and quit the program

# ---------------------------------------------------------- I N V A L I D   I N P U T ----------------------------------------------------------
    else:                                                                                   # Any other input is not valid
        print("Please enter a valid input")