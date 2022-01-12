import pendulum
class Topic:
    def __init__(self):
        self.topic = ""
        self.description = ""

    def getTopic(self):
        return self.topic

    def setTopic(self, text):
        if(not isinstance(text, str)):     # if other than string raise TypeError
            raise TypeError
        self.topic = text

    def getDescription(self):
        return self.description

    def setDescription(self, text):
        if(not isinstance(text, str)):     # if other than string raise TypeError
            raise TypeError
        self.description = text

class Todo(Topic):
    def __init__(self):
        self.topic = Topic()
        self.orderList = 0
        self.importance = 0
        self.endDate = 0
        self.checkDone = False

    def to_dict(self):
        return {'topic': self.topic,
                'endDate': self.getDateString(),
                'checkDone': self.checkDone,
                'desc': self.description,
                'orderList': self.orderList}

    def getDate(self):
        return self.endDate     # return pendulum date

    def getDateString(self):
        return self.endDate.to_date_string()    # return a string date

    def getOrderList(self):
        return self.orderList

    def getDone(self):
        return self.checkDone

    def setDate(self, dt):
        date = pendulum.from_format(dt, 'YYYY/MM/DD')   # specify date formate
        self.endDate = date

    def setOrderList(self, order):
        if(not isinstance(order, int)):     # if other than integer raise TypeError
            raise TypeError
        self.orderList = order

    def setDone(self, done):
        if(not isinstance(done, bool)):     # if other than boolean raise TypeError
            raise TypeError
        self.checkDone = done


if __name__ == "__main__":
    t = Todo()
    t.setDate('2021/21-10')
    print(type(t.getDate()))
    print(t.getDateString())
