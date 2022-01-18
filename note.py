from todo import TodoList
from user import User
import json
from datetime import datetime
from time import strftime
class NoteManager:
    def __init__(self):
        self.todoAll = []
        self.user = User()
        self.userTodo = {}
        self.todoCompleted = []
        self.todoIncompleted = []
        self.filename = "data_file.json"

    def createTodo(self, title, date, detail, time):      # create Todo
        todo = TodoList()
        todo.setTitle(title)
        todo.setDate(date)
        todo.setDetail(detail)
        todo.setTime(time)
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
        self.sortTodo()
    
    def getTodoCompleted(self):
        return self.todoCompleted

    def getTodoCompletedTitle(self):
        return [i['title'] for i in self.todoCompleted]

    def getTodoIncompleted(self):
        return self.todoIncompleted

    def getTodoIncompletedTitle(self):
        return [i['title'] for i in self.todoIncompleted]

    def getTodos(self):
        self.checkUser(self.user.getName())    # chack current user
        return self.todoAll

    def sortTodo(self):
        self.todoCompleted.sort( key=lambda a:(datetime.strptime(a['endDate'], "%Y-%m-%d"), datetime.strptime(a['timeEnd'], "%H:%M")) )
        self.todoIncompleted.sort( key=lambda a:(datetime.strptime(a['endDate'], "%Y-%m-%d"), datetime.strptime(a['timeEnd'], "%H:%M")))
        self.todoAll.sort( key=lambda a:(datetime.strptime(a['endDate'], "%Y-%m-%d"), datetime.strptime(a['timeEnd'], "%H:%M")))

    def updateCurrentUser(self):
        self.userTodo[self.user.getName()] = self.todoCompleted + self.todoIncompleted
    
    def toJson(self):
        with open(self.filename, "w") as write_file:     # convert dict to json file
            json.dump(self.userTodo, write_file)

    def loadJson(self, name=""):
        with open(self.filename, "r") as read_file:  # convert json file to dict
            self.userTodo = json.load(read_file)
        user_all = list(self.userTodo.keys())
        if len(name)>0:
            self.checkUser(name)
        elif(len(user_all)>0):
            self.checkUser(user_all[0])
        else:
            self.checkUser(self.user.getName())
            self.toJson()
        self.separateTodo()
        return self.userTodo
        
    def checkUser(self, user):
        self.user.changeName(user)
        if user in self.userTodo:       # if self.userTodo have username, it's will use todo in userTodo
            self.todoAll = self.userTodo[user]      
        else:
            self.userTodo[user] = []
            self.todoAll = []   # else create emty list
        self.separateTodo()
        return self.todoAll
    
    def getAccout(self):
        return list(self.userTodo.keys())
    
    def load_file(self, filename):
        self.filename = filename
        self.loadJson()
    
    def delete_user(self, name):
        del self.userTodo[name]
        self.toJson()
        self.user.changeName(self.getAccout()[0])
    
    def export_file(self, path):
        self.filename = path
        self.toJson()


            
if __name__ == "__main__":
    no = NoteManager()
    no.createTodo("cooking", "2011-1-2", "hi1", strftime("13:%M"))
    no.createTodo("รดน้ำต้นไม่", "2011-1-3", "hihi", strftime("15:%M"))
    no.createTodo("daily", "2011-1-14", "hihi", strftime("%H:%M"))
    no.createTodo("math", "2011-2-3", "hihi", strftime("%H:%M"))
    no.checkUser("ong")
    no.createTodo("anime", "2011-1-3", "hellow", strftime("%H:%M"))
    no.createTodo("serie", "2011-1-3", "hhhhh", strftime("%H:%M"))
    no.toJson()
    a = no.loadJson()
    no.checkUser('user1')
    no.sortTodo()
    print(no.getTodos())