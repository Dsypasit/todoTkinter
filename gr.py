from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from note import NoteManager
from PIL import Image, ImageTk
import numpy as np
from datetime import datetime

def getCompleted(l):
    ans = {}
    for i in l:
        date = i['timeDate']
        if date in ans:
            ans[date] += 1
        else:
            ans[date] = 0
    return ans

def graph_pie(name):
    note.checkUser(name)
    c, i = len(note.getTodoCompleted()), len(note.getTodoIncompleted())
    y = [c, i]
    print(y)
    label = ['completed', 'incompleted']
    plt.title('Amount todo of '+ name)
    plt.pie(y, labels=label, autopct=lambda x:f"{x:.2f} %")
    plt.savefig(f'pie_{name}.png', dpi=200)
    plt.close()

def graph_incomplete(name):
    note.checkUser(name)
    l = note.getTodoCompleted()
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
    print(k)
    plt.title('Amout complete of '+ name)
    plt.ylim(0, 10)
    plt.yticks(np.arange(0, 10, 1))
    plt.plot(k, v, 'bo', k, v, 'k--')
    plt.savefig(f'plot_completed_{name}.png', dpi=200)
    plt.close()

def graph_complete(name):
    note.checkUser(name)
    l = note.getTodoCompleted()
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
    print(k)
    plt.title('Amout incomplete of '+ name)
    plt.ylim(0, 10)
    plt.yticks(np.arange(0, 10, 1))
    plt.plot(k, v, 'ro', k, v, 'k--')
    plt.savefig(f'plot_incompleted_{name}.png', dpi=200)
    plt.close()

def graph(name):
    graph_pie(name)
    graph_complete(name)
    graph_incomplete(name)

def change_acc(name):
    graph_pie(name)
    graph_complete(name)
    # time.sleep(0.5)
    img = ImageTk.PhotoImage(Image.open(f"pie_{name}.png").resize(size))
    label1.configure(image=img)
    label1.photo = img
    img2 = ImageTk.PhotoImage(Image.open(f"plot_completed_{name}.png").resize(size))
    label2.configure(image=img2)
    label2.photo = img2
    img3 = ImageTk.PhotoImage(Image.open(f"plot_incompleted_{name}.png").resize(size))
    label3.configure(image=img3)
    label3.photo = img3
    print('hello')

size = (500, 400)
root = Tk()
root.title('codemy')
root.geometry("500x900")

note = NoteManager()
note.loadJson()
account = note.getAccout()

n = StringVar()
combobox = ttk.Combobox(root, width = 27, textvariable=n)
combobox['values'] = account
combobox.current(0)
combobox.pack()

combobox.bind('<<ComboboxSelected>>', lambda e:change_acc(n.get()))

graph(n.get())
img = Image.open(f'pie_{n.get()}.png').resize(size)
img = ImageTk.PhotoImage(img)
label1 = Label(root, image=img)
label1.pack()
img2 = Image.open(f'plot_completed_{n.get()}.png').resize(size)
img2 = ImageTk.PhotoImage(img2)
label2 = Label(root, image=img2)
label2.pack()
img3 = Image.open(f'plot_incompleted_{n.get()}.png').resize(size)
img3 = ImageTk.PhotoImage(img3)
label3 = Label(root, image=img3)
label3.pack()

root.mainloop()