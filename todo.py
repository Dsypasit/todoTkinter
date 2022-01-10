class todo:
    
    def __init__(self):
        self.topic = new Topic()
        self.orderList = 0
        self.importance = 0
        self.endDate = 0
        self.checkDone = False

    def getDate(self):
        return self.endDate

    def getOrderList(self):
        return self.orderList

    def getDone(self):
        return self.checkDone

    def setDate(self):
        pass

    def setOrderList(self):
        pass

    def setDone(self):
        pass

class topic:
    def __init__(self):
        self.topic = ""
        self.checkList = []

    def getTopic(self):
        return self.topic

    def setTopic(self, text):
        self.topic = text

    def getDiscription(self):
        return self.checkList

    def setCheckList(self):
        checkList.append(text)
