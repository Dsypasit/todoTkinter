from todo import TodoList
from user import User
import json
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np

class NoteManager:
    def __init__(self):
        self.todoAll = []
        self.user = User()
        self.userTodo = {}
        self.todoCompleted = []
        self.todoIncompleted = []
        self.filename = "data_file.json"
        self.size = (500, 400)

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
    
    def toJson(self, path=""):
        if len(path)>0:
            with open(path, "w") as write_file:     # convert dict to json file
                json.dump(self.userTodo, write_file)
        else:
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
        # self.filename = path
        self.updateCurrentUser()
        self.toJson(path)

    def graph_pie(self):
        name = self.user.getName()
        c, i = len(self.getTodoCompleted()), len(self.getTodoIncompleted())
        y = [c, i]
        label = ['completed', 'incompleted']
        plt.title('Amount todo of '+ name)
        plt.pie(y, labels=label, autopct=lambda x:f"{x:.2f} %")
        plt.savefig(f'pie_{name}.png', dpi=200)
        plt.close()

    def graph_complete(self):
        name = self.user.getName()
        l = self.getTodoCompleted()
        result = {}
        for i in l:
            date = i['dateCompleted']
            if date in result:
                result[date] += 1
            else:
                result[date] = 1
        k = list(result.keys())
        k = sorted(k, key=lambda a: datetime.strptime(a, "%Y-%m-%d"))
        v = [result[i] for i in k]
        plt.title('Amout complete of '+ name)
        plt.ylim(0, 10)
        plt.yticks(np.arange(0, 10, 1))
        plt.plot(k, v, 'bo', k, v, 'k--')
        plt.savefig(f'plot_completed_{name}.png', dpi=200)
        plt.close()

    def graph_incomplete(self):
        name = self.user.getName()
        l = self.getTodoIncompleted()
        result = {}
        for i in l:
            date = i['endDate']
            if date in result:
                result[date] += 1
            else:
                result[date] = 1
        k = list(result.keys())
        k = sorted(k, key=lambda a: datetime.strptime(a, "%Y-%m-%d"))
        v = [result[i] for i in k]
        plt.title('Amout incomplete of '+ name)
        plt.ylim(0, 10)
        plt.yticks(np.arange(0, 10, 1))
        plt.plot(k, v, 'ro', k, v, 'k--')
        plt.savefig(f'plot_incompleted_{name}.png', dpi=200)
        plt.close()

    def graph(self):
        self.graph_pie()
        self.graph_complete()
        self.graph_incomplete()
    
    def get_pie(self):
        name = self.user.getName()
        return ImageTk.PhotoImage(Image.open(f"pie_{name}.png").resize(self.size))

    def get_completed(self):
        name = self.user.getName()
        return ImageTk.PhotoImage(Image.open(f"plot_completed_{name}.png").resize(self.size))

    def get_incompleted(self):
        name = self.user.getName()
        return ImageTk.PhotoImage(Image.open(f"plot_incompleted_{name}.png").resize(self.size))


            
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