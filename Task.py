class Task:
    def __init__(self, name):
        self.name = name
        self.important = False
        self.dueDay = 0
        self.dueMonth = 0

    def markAsImportant(self):
        self.important = True

    def setDueDate(self, day, month):
        self.dueDay = day
        self.dueMonth = month

    def dueDateIsSet(self):
        if self.dueDay != 0:
            return True
        else:
            False
