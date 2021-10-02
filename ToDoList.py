from Task import Task

class ToDoList:
    def __init__(self, name):
        self.name = name
        self.list = []
        self.completedList = []

    def addToList(self, taskName):
        self.list.append(Task(taskName))

    def tickOffTask(self, itemNo):
        self.completedList.append(self.list[int(itemNo)])
        del self.list[int(itemNo)]

    def printList(self, width):
        print("-" * width)
        print((" " * int((width - len(self.name)) / 2)), self.name)
        print("-" * width)

        for x in range(len(self.list)):
            if self.list[x].important == True:    
                print("* " , self.list[x].name, end="")
            else:    
                print("- " , self.list[x].name, end="")

            if self.list[x].dueDateIsSet():
                print("  (", self.list[x].dueDay, "/", self.list[x].dueMonth, ")")
            else:
                print()
            
        print()

    def printCompletedList(self, width):
        print("-" * width)
        print((" " * int((width - len(self.name)) / 2)), self.name)
        print("-" * width)

        for x in range(len(self.completedList)):
            if self.completedList[x].important == True:    
                print("* " , self.completedList[x].name, end="")
            else:    
                print("- " , self.completedList[x].name, end="")

            if self.completedList[x].dueDateIsSet():
                print("  (", self.completedList[x].dueDay, "/", self.completedList[x].dueMonth, ")")
            else:
                print()
            
        print()
        




