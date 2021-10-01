class ToDoList:
    def __init__(self, name):
        self.name = name
        self.list = []
        self.completedList = []

    def addToList(self, item):
        self.list.append(item)

    def tickOffTask(self, item):
        self.completedList.append(self.list[int(item)])
        del self.list[int(item)]

    def printList(self, width):
        print("-" * width)
        print((" " * int((width - len(self.name)) / 2)), self.name)
        print("-" * width)

        for x in range(len(self.list)):
            print("- " , self.list[x])
            
        print()
        




