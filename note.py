from todo import TodoList
from user import User
import json
class Note:
    def __init__(self):
        self.todoAll = []
        self.user = User()
        self.userTodo = {}

    def createTodo(self, title, date):
        todo = TodoList()
        todo.setTitle(title)
        todo.setDate(date)
        self.todoAll.append(todo.to_dict())
        self.updateCurrentUser()

    def getTodos(self):
        self.changeUser(self.user.getName())
        return self.todoAll

    def alarmTodo(self):
        pass

    def sortTodo(self):
        pass

    def updateCurrentUser(self):
        self.userTodo[self.user.getName()] = self.todoAll
    
    def toJson(self):
        self.updateCurrentUser()
        with open("data_file.json", "w") as write_file:     # convert dict to json file
            json.dump(self.userTodo, write_file)

    def loadJson(self):
        with open("data_file.json", "r") as read_file:  # convert json file to dict
            self.userTodo = json.load(read_file)
        return self.userTodo
        
    def changeUser(self, user):
        self.user.changeName(user)
        if user in self.userTodo:
            self.todoAll = self.userTodo[user]
        else:
            self.todoAll = []
        return self.todoAll

            
if __name__ == "__main__":
    no = Note()
    no.createTodo("hi", "2011/1/2")
    no.createTodo("hi2", "2011/1/3")
    no.changeUser("ong")
    no.createTodo("hi2", "2011/1/3")
    no.createTodo("hi2", "2011/1/3")
    no.toJson()
    print(no.userTodo)
    a = no.loadJson()
    print(a.keys())
