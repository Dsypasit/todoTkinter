from todo import TodoList
from user import User
import json
from datetime import datetime
class Note:
    def __init__(self):
        self.todoAll = []
        self.user = User()
        self.userTodo = {}
        self.todoCompleted = []
        self.todoIncompleted = []

    def createTodo(self, title, date, detail):      # create Todo
        todo = TodoList()
        todo.setTitle(title)
        todo.setDate(date)
        todo.setDetail(detail)
        self.todoAll.append(todo.to_dict())
        self.todoIncompleted.append(todo.to_dict())
        self.updateCurrentUser()
    
    def separateTodo(self):
        self.todoIncompleted = []
        self.todoCompleted = []
        for todo in self.todoAll:
            if todo['completed']:
                self.todoCompleted.append(todo)
            else:
                self.todoIncompleted.append(todo)

    def findTodo(self, index, select):
        l = []
        if select == 'c':
            l = self.todoCompleted
        elif select == 'ic':
            l = self.todoIncompleted
        return l[index]
    
    def getTodoCompleted(self):
        return self.todoCompleted

    def getTodoCompletedTitle(self):
        return [i['title'] for i in self.todoCompleted]

    def getTodoIncompleted(self):
        return self.todoIncompleted

    def getTodoIncompletedTitle(self):
        return [i['title'] for i in self.todoIncompleted]
    
    def setTodoCompleted(self, l):
        self.todoCompleted = l
    
    def setTodoIncompleted(self, l):
        self.todoIncompleted = l

    def getTodos(self):
        self.checkUser(self.user.getName())    # chack current user
        return self.todoAll

    def alarmTodo(self):
        pass

    def sortTodo(self):
        self.todoCompleted.sort( key=lambda a:datetime.strptime(a['endDate'], "%Y-%m-%d") )
        self.todoIncompleted.sort( key=lambda a:datetime.strptime(a['endDate'], "%Y-%m-%d") )
        self.todoAll.sort( key=lambda a:datetime.strptime(a['endDate'], "%Y-%m-%d") )

    def updateCurrentUser(self):
        self.userTodo[self.user.getName()] = self.todoCompleted + self.todoIncompleted
    
    def toJson(self):
        self.updateCurrentUser()
        with open("data_file.json", "w") as write_file:     # convert dict to json file
            json.dump(self.userTodo, write_file)

    def loadJson(self):
        with open("data_file.json", "r") as read_file:  # convert json file to dict
            self.userTodo = json.load(read_file)
        self.checkUser(self.user.getName())
        self.separateTodo()
        self.sortTodo()
        return self.userTodo
        
    def checkUser(self, user):
        self.user.changeName(user)
        if user in self.userTodo:       # if self.userTodo have username, it's will use todo in userTodo
            self.todoAll = self.userTodo[user]      
        else:
            self.todoAll = []   # else create emty list
        self.separateTodo()
        return self.todoAll
    
    def getAccout(self):
        return list(self.userTodo.keys())

            
if __name__ == "__main__":
    no = Note()
    no.createTodo("cooking", "2011-1-2", "hi1")
    no.createTodo("รดน้ำต้นไม่", "2011-1-3", "hihi")
    no.createTodo("daily", "2011-1-14", "hihi")
    no.createTodo("math", "2011-2-3", "hihi")
    no.checkUser("ong")
    no.createTodo("anime", "2011-1-3", "hellow")
    no.createTodo("serie", "2011-1-3", "hhhhh")
    no.toJson()
    a = no.loadJson()
    no.checkUser('user1')
    no.sortTodo()
    print(no.getTodos())