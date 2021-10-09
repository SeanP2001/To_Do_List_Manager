class Task:
    def __init__(self, name):                              # All tasks have a name which is set when they are initialised
        self.name = name                                   # The name is set by the constructor argument
        self.important = False                             # by default Tasks are not flagged as important
        self.dueDay = 0                                    # The due day 
        self.dueMonth = 0                                  # and due month are 0 by default (indicating they are not set)

    def markAsImportant(self):                             # Flags the task as important
        self.important = True       

    def setDueDate(self, day, month):                      # Sets the due date for the task
        self.dueDay = day                                  # Set the due day
        self.dueMonth = month                              # and due month 

    def dueDateIsSet(self):                                # Checks if the due date is set
        if (int(self.dueDay) and int(self.dueMonth)) != 0: # If both the due day and due month are set (Not 0)    
            return True                                    # then return that the date is set
        else:                                              # Otherwise
            False                                          # return that it is not set
