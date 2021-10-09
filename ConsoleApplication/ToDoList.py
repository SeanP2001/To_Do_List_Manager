from Task import Task

class ToDoList:
    def __init__(self, name):                                                                           # Each to do list
        self.name = name                                                                                # has a name
        self.list = []                                                                                  # a list of tasks
        self.completedList = []                                                                         # and a list of completed tasks
      
    def addToList(self, taskName):                                                                      # adds the task to the list of tasks
        self.list.append(Task(taskName))                                                                # appends the task to the end of the list

    def tickOffTask(self, itemNo):                                                                      # Tick the task off the list
        self.completedList.append(self.list[int(itemNo)])                                               # Add the task to the list of completed tasks
        del self.list[int(itemNo)]                                                                      # and remove it from the list of current tasks

    def printList(self, width):                                                                         # Prints the title and full list of tasks
        print("-" * width)                                                                              # prints a line across the set width
        print((" " * int((width - len(self.name)) / 2)), self.name)                                     # prints the to do list title in the centre
        print("-" * width)                                                                              # prints a line across the set width

        for x in range(len(self.list)):                                                                 # For each task on the list
            if self.list[x].important == True:                                                          # if the task is important 
                print("* " , self.list[x].name, end="")                                                 # print a * bullet point
            else:                                                                                       # for regular tasks
                print("- " , self.list[x].name, end="")                                                 # print a - bullet point

            if self.list[x].dueDateIsSet():                                                             # If the task has a due date set
                print("  (", self.list[x].dueDay, "/", self.list[x].dueMonth, ")")                      # print out the date after the task e.g. ( 25 / 12 )
            else:                                                                                       # if there is no due date
                print()                                                                                 # move to a new line
            
        print()                                                                                         # After all of the tasks have been printed, print a blank line

    def printCompletedList(self, width):                                                                # Prints the title and full list of tasks which have been completed
        print("-" * width)                                                                              # prints a line across the set width 
        print((" " * int((width - len(self.name)) / 2)), self.name)                                     # prints the to do list title in the centre
        print("-" * width)                                                                              # prints a line across the set width

        for x in range(len(self.completedList)):                                                        # For each task on the completed list
            if self.completedList[x].important == True:                                                 # if the task was important 
                print("* " , self.completedList[x].name, end="")                                        # print a * bullet point
            else:                                                                                       # for regular tasks
                print("- " , self.completedList[x].name, end="")                                        # print a - bullet point

            if self.completedList[x].dueDateIsSet():                                                    # If the task had a due date set
                print("  (", self.completedList[x].dueDay, "/", self.completedList[x].dueMonth, ")")    # print out the date after the task e.g. ( 25 / 12 )
            else:                                                                                       # if there was no due date
                print()                                                                                 # move to a new line
            
        print()                                                                                         # After all of the tasks have been printed, print a blank line
        




