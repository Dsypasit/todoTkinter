from todo import Todo
import json
class Note:
    def __init__(self):
        self.todoAll = []
        self.user = "user1"
        self.userTodo = {}

    def createTodo(self, topic, desc, date):
        todo = Todo()
        todo.setTopic(topic)
        todo.setDescription(desc)
        todo.setDate(date)
        self.todoAll.append(todo.to_dict())

    def getTodos(self):
        return self.todoAll

    def alarmTodo(self):
        pass

    def sortTodo(self):
        pass

    def updateCurrentUser(self):
        self.userTodo[self.user] = self.todoAll
    
    def toJson(self):
        self.updateCurrentUser()
        with open("data_file.json", "w") as write_file:     # convert dict to json file
            json.dump(self.userTodo, write_file)

    def loadJson(self):
        with open("data_file.json", "r") as read_file:  # convert json file to dict
            self.userTodo = json.load(read_file)

    def changeUser(self, user):
        self.updateCurrentUser()
        if user in self.userTodo:
            self.user = user
            self.todoAll = self.userTodo[user]
        else:
            self.user = user
            self.todoAll = []
            
if __name__ == "__main__":
    no = Note()
    no.createTodo("hi", "hello", "2011/1/2")
    no.createTodo("hi2", "hello2", "2011/1/3")
    no.changeUser("ong")
    no.createTodo("hi2", "hello2", "2011/1/3")
    no.createTodo("hi2", "hello2", "2011/1/3")
    no.toJson()
    print(no.userTodo)
    no.loadJson()
    print(no.userTodo)
