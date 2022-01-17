import pendulum
from task import Task

class TodoList(Task):
    def __init__(self):
        self.title = ""
        self.pinned = False
        self.completed = False
        self.dueDate = 0
        self.detail = ""
        self.task = []

    def to_dict(self):      # change attribute to dict
        return {'title': self.title,
                'endDate': self.getDateString(),
                'completed': self.completed,
                'pinned': self.pinned,
                'detail': self.detail,
                'task': self.task}

    def getDate(self):
        return self.dueDate     # return pendulum date

    def getDateString(self):
        return self.dueDate.to_date_string()    # return a string date

    def getComplete(self):
        return self.orderList

    def setDetail(self, de):
        self.detail = de

    def setDate(self, dt):
        date = pendulum.from_format(dt, 'YYYY-MM-DD')   # specify date formate
        self.dueDate = date

    def setTitle(self, title):
        if(not isinstance(title, str)):     # if other than integer raise TypeError
            raise TypeError
        self.title = title

    def setComplete(self, order):
        if(not isinstance(order, int)):     # if other than integer raise TypeError
            raise TypeError
        self.completed = order
            
    def setPinned(self, pin):
        if(not isinstance(pin, bool)):     # if other than boolean raise TypeError
            raise TypeError
        self.pinned = pin
    
    def addTask(self, task):
        self.task.append(task)
    
    def removeTask(self, index):
        self.task.pop(index)


if __name__ == "__main__":
    t = TodoList()
    t.setDate('2021-1-10')
    print(type(t.getDate()))
    print(t.getDateString())
