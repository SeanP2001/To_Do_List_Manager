from ToDoList import ToDoList
import pickle

displayWidth = 30
toDoLists = []

saveFile = "lists.dat"

def printAllLists():
    for x in range(len(toDoLists)):
        toDoLists[x].printList(displayWidth)

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

toDoLists = loadLists()                                                         # Load any saved lists

while(1): 
    printAllLists()                                                             # Print all to do lists
                                                                                # Print Main Menu
    print("""                                                                     
    1) Create a New List
    2) Select a List (to add or tick off a task)
    3) Save and Exit
    """)

    userInput = input("Please Select: ")                                        # Ask for user selection

    if (userInput == "1"):                                                      # When the user selects "Create a New List"
        newListName = input("What would you like to name you new list? ")       # Get the name of the new task
        toDoLists.append(ToDoList(newListName))                                 # Add the new list to the page
        print(newListName, "has been created")                                  # Notify the user that thier new list has been made

    elif (userInput == "2"):                                                    # When the user selects "Select a List"
        for x in range(len(toDoLists)):                                         # Print out the names of all of the lists
            print(x, ") ", toDoLists[x].name)
            
        listSelection = input("Please Select: ")                                # and ask which one they want to select

        selected = True                                                         # Mark that the user has selected a list

        while(selected):                                                                        # while selected
            toDoLists[int(listSelection)].printList(displayWidth)                               # Print the selected list
                                                                                                # and print the menu of possible actions
            print("""                                                           
            1) Create a New Task
            2) Tick off a Task
            3) Return to All Tasks
            """)

            listAction = input("Please Select: ")                                               # Ask which action the user wants to do

            if (listAction == "1"):                                                             # When the user selects "Create a New Task"
                newTaskName = input("What would you like to name you new task? ")               # Get the name of the new task
                toDoLists[int(listSelection)].addToList(newTaskName)                            # Add the task to the end of the selected list
                print(newTaskName, "has been added to ", toDoLists[int(listSelection)].name)    # Notify the user that their new task has been added to the list

            elif (listAction == "2"):                                                           # When the user selects "Tick off a Task" 
                for i in range(len(toDoLists[int(listSelection)].list)):                        # Print out the names of all of the tasks
                    print(i, ") ", toDoLists[int(listSelection)].list[i])
            
                tickTask = input("Which task would you like to tick off the list? ")            # and ask which one they want to tick off
                toDoLists[int(listSelection)].tickOffTask(tickTask)                             # Remove the item from the list and add it to the completed list

            elif (listAction == "3"):                                                           # When the user selects "Return to All Tasks"
                selected = False                                                                # deselect the selected list

            else:                                                                               # Any other input is not valid
                 print("Please enter a valid input")
            
    elif (userInput == "3"):                                                        # When the user selects "Save and Exit"
        saveLists(toDoLists)                                                        # Save the lists
        quit()                                                                      # and quit the program


    else:                                                                           # Any other input is not valid
        print("Please enter a valid input")