import pendulum

class TodoList:
    def __init__(self):
        self.title = ""
        self.pinned = False
        self.completed = False
        self.dueDate = 0

    def to_dict(self):      # change attribute to dict
        return {'topic': self.title,
                'endDate': self.getDateString(),
                'completed': self.completed,
                'pinned': self.pinned}


    def getDate(self):
        return self.dueDate     # return pendulum date

    def getDateString(self):
        return self.dueDate.to_date_string()    # return a string date

    def getComplete(self):
        return self.orderList

    def setDate(self, dt):
        date = pendulum.from_format(dt, 'YYYY/MM/DD')   # specify date formate
        self.dueDate = date

    def setTitle(self, title):
        if(not isinstance(title, str)):     # if other than integer raise TypeError
            raise TypeError
        self.orderList = title

    def setComplete(self, order):
        if(not isinstance(order, int)):     # if other than integer raise TypeError
            raise TypeError
        self.orderList = order
            
    def setPinned(self, pin):
        if(not isinstance(pin, bool)):     # if other than boolean raise TypeError
            raise TypeError
        self.pinned = pin


if __name__ == "__main__":
    t = TodoList()
    t.setDate('2021/21/10')
    print(type(t.getDate()))
    print(t.getDateString())
