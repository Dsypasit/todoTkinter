# importing tkinter module and Widgets
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from note import NoteManager
from tkcalendar import DateEntry # pip install tkcalendar
from datetime import datetime, date
from time import strftime

# Creating App class which will contain
class App:
    def __init__(self, master) -> None:
        # Instantiating master i.e toplevel Widget
        self.master = master
        self.note = NoteManager()
        self.mlist = []
        self.clist = []
        self.todo = []
        self.tasklist =[]
        self.account = []
        self.last_index = 0
        self.last_task_index = 0
        self.check_com = False
        # Setting the title of the window
        self.master.title('TODODO')

        def find_todo(title):
                for n in self.todo:
                        if n['title'] == title:
                                return n

        def fetch_listbox():
                mlist = self.note.getTodoIncompleted()
                clist = self.note.getTodoCompleted()
                main_listbox.delete(0, END)
                clistbox.delete(0, END)
                for item in mlist:
                        main_listbox.insert(END, item['title'])
                for item in clist:
                        clistbox.insert(END, item['title'])

        def fetch_data():
                self.note.loadJson(account_str.get())
                self.note.checkUser(account_str.get())
                self.todo = self.note.getTodos()
                self.mlist = []
                self.clist = []
                self.account = self.note.getAccout()
                for n in self.todo:
                        if n['completed']:
                                self.clist.append(n['title'])
                        else:
                                self.mlist.append(n['title'])

        def update_json():
                self.note.updateCurrentUser()
                self.note.toJson()
                fetch_data()
        
        # self.account = ["Guest", "user1", "user2"]
        # self.mlist = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]

        #///////////////////////////
        self.note.loadJson()
        self.account = self.note.getAccout()


        # FUNCTIONS
        def new_account():      # window for input text
                global add_acc_win
                add_acc_win = Toplevel(self.master)
                add_acc_win.title('New Account')

                add_acc_Label = Label(add_acc_win,text='Account')
                add_acc_Label.grid(row=0,column=0,padx=10,pady=10)

                global text_new_account
                text_new_account = StringVar()
                add_acc_entry = Entry(add_acc_win,textvariable=text_new_account)
                add_acc_entry.grid(row=0,column=1,columnspan=1,padx=10,pady=10,sticky='w')

                separator = ttk.Separator(add_acc_win, orient='horizontal')
                separator.grid(row=1,columnspan=2,sticky="ew")

                add_acc_btn = Button(add_acc_win, text="Done", command=add_account)
                add_acc_btn.grid(row=2,column=0,padx=10,pady=10)
                btn_cancel = Button(add_acc_win, text="Cancel", command=add_acc_win.destroy)
                btn_cancel.grid(row=2,column=1,padx=10,pady=10)

        def add_account():      # add new account in combo box
                self.account.append(text_new_account.get())
                self.note.checkUser(text_new_account.get())
                update_json()
                #text_new_account.get()
                combox["values"] = self.account
                combox.current(END)
                add_acc_win.destroy()
                refresh()
                
        def delete_account():
                ask = messagebox.askokcancel("Are you sure?","Are you sure to delete \"{}\" account".format(account_str.get()))
                if ask:
                        self.note.delete_user(account_str.get())
                        self.account.remove(account_str.get())
                        combox["values"] = self.account
                        combox.current(0)
                        refresh()
                        fetch_data()
                        fetch_listbox()

        def changeAccount(event):
                refresh()
                self.note.checkUser(account_str.get())
                fetch_data()
                fetch_listbox()
                
        def refresh():
                clear_all_listbox()
                # show title 
                main_title_text.set('')
                # show date
                main_cal = DateEntry(detail_frame1)
                main_cal.grid(row=0, column=3, padx=10, sticky='w') 
                # show detail
                main_detail_text.set('')
                # set time
                value_time = strftime('%H:%M:%S')
                main_time_text.set(value_time)  # adding time to Entry

                # status len(list)
                text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')
                # status task
                task_text.set('')       # empty entry
                task_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
                task_status.grid(row=0, column=0, sticky='w')

        def clear_all_listbox():
                main_listbox.delete(0,END)
                clistbox.delete(0,END)
                task_listbox.delete(0,END)

        def delete_item():
                self.note.todoIncompleted.pop(int(main_listbox.curselection()[0]))
                main_listbox.delete(ANCHOR)
                update_json()
                # update status 
                text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')

        def changePage():
                index=notebook.index(notebook.select())
                if index == 0:
                        # button check
                        btn_add = Button(mframe1,text ="check", command=check_item)
                        btn_add.grid(row=0, padx=10, pady=10, column=1, sticky='ew')
                elif index == 1:
                        # button check
                        btn_add = Button(mframe1,text ="uncheck", command=check_item)
                        btn_add.grid(row=0, padx=10, pady=10, column=1, sticky='ew')
        
        global click_check
        def click_check():
                # try :   
                        self.last_task_index = int(task_listbox.curselection()[0])
                        # not done
                        if task_listbox.itemcget(self.last_task_index, "fg") == "#ffa364":
                                task_listbox.itemconfig(
                                        self.last_task_index,
                                        fg='#21130d')
                                # get rid of selection bar
                                task_listbox.select_clear(0, END)
                                if self.check_com:
                                        self.note.todoCompleted[self.last_index]['task'][self.last_task_index]['completed'] = False
                                else:
                                        self.note.todoIncompleted[self.last_index]['task'][self.last_task_index]['completed'] = False
                                update_json()
                                # print(task_listbox.curselection())
                                return
                        # done
                        task_listbox.itemconfig(
                                self.last_task_index,
                                fg='#ffa364')
                        # get rid of selection bar
                        task_listbox.select_clear(0, END)
                        if self.check_com:
                                self.note.todoCompleted[self.last_index]['task'][self.last_task_index]['completed'] = True
                        else:
                                self.note.todoIncompleted[self.last_index]['task'][self.last_task_index]['completed'] = True
                        update_json()
                # except: pass

        def check_item():
                try :
                        today = date.today().strftime("%Y-%m-%d")
                        if self.check_com:
                                self.note.todoCompleted[self.last_index]['completed'] = False
                                self.note.todoCompleted[self.last_index]['dateCompleted'] = None
                                
                        else:
                                self.note.todoIncompleted[self.last_index]['completed'] = True
                                self.note.todoIncompleted[self.last_index]['dateCompleted'] = today
                                
                        update_json()
                        fetch_listbox()
                        
                        # update status 
                        text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                        text_status.grid(row=0, column=0, sticky='w')

                except: pass

        def click_item_show(listbox, index_in):
                # try : 
                        global main_listbox, clistbox
                        fetch_data()
                        task_listbox.delete(0,END)    
                        task_text.set('')       # empty entry 

                        if len(listbox.curselection()): # ()
                                self.last_index = int(listbox.curselection()[0])

                        if listbox == clistbox:
                                self.check_com = True
                                #set index
                                if index_in == None:
                                        index = int(listbox.curselection()[0])
                                else:
                                        index = index_in
                                value_title = listbox.get(index)      # text selection form listbox

                                task_listbox.bind('<<ListboxSelect>>', 
                                        lambda e: click_check()) #Select click

                                value = self.note.todoCompleted[index] 
                                # show title 
                                main_title_text.set(value['title'])
                                # show date
                                selection_date = value['endDate']
                                main_cal.set_date(datetime.strptime(selection_date, "%Y-%m-%d"))
                                main_cal.grid(row=0, column=3, padx=10, sticky='w') 
                                # show detail
                                value_detail = value['detail']
                                main_detail_text.set(value_detail)
                                # set time
                                value_time = strftime('%H:%M:%S')
                                main_time_text.set(value['timeEnd'])  # adding time to Entry

                                # set task
                                for n, i in enumerate(value['task']):
                                        task_listbox.insert(END, u'\u2022 '+i['title'])
                                        task_listbox.itemconfig(
                                                n,
                                                fg='#ffa364' if i['completed'] else '#21130d')
                                        # get rid of selection bar

                                # status 
                                task_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
                                task_status.grid(row=0, column=0, sticky='w')
                                pass
                                
                        elif listbox == main_listbox:
                                self.check_com = False
                                # enable btn_addtask & btn_del 
                                btn_add = Button(detail_frame3,text ="+")
                                btn_add.bind("<Button>",
                                        lambda e: addtask())
                                btn_add.grid(row=0, column=6, sticky='e')
 
                                btn_del = Button(detail_frame1,text ="Delete List", command=delete_item)
                                btn_del.grid(row=2,column=3,pady=10, sticky='ew')
                                
                                #set index
                                if index_in == None:
                                        index = int(listbox.curselection()[0])
                                else:
                                        index = index_in
                                value_title = listbox.get(index)      # text selection form listbox

                                task_listbox.bind('<<ListboxSelect>>', 
                                        lambda e: click_check()) #Select click

                                value = self.note.todoIncompleted[index] 
                                # show title 
                                main_title_text.set(value['title'])
                                # show date
                                selection_date = value['endDate']
                                main_cal.set_date(datetime.strptime(selection_date, "%Y-%m-%d"))
                                main_cal.grid(row=0, column=3, padx=10, sticky='w')
                                # show detail
                                value_detail = value['detail']
                                main_detail_text.set(value_detail)
                                # set time
                                value_time = strftime('%H:%M:%S')
                                main_time_text.set(value['timeEnd'])  # adding time to Entry
                                # set task
                                for n, i in enumerate(value['task']):
                                        task_listbox.insert(END, u'\u2022 '+i['title'])
                                        task_listbox.itemconfig(
                                                n,
                                                fg='#ffa364' if i['completed'] else '#21130d')

                                # status 
                                task_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
                                task_status.grid(row=0, column=0, sticky='w')

                # except: pass

        def del_alldone():
                clistbox.delete(0,END)
                self.note.todoCompleted = []
                update_json()

        def donothing():
                filewin = Toplevel(root)
                button = Button(filewin, text="Do nothing button")
                button.pack()
                ask = messagebox.askokcancel("Are you sure?","Are you sure to delete all complete")
                if ask:
                        clistbox.delete(0,END)  

        def addtask():
                global main_listbox
                task_listbox.insert(END, u'\u2022 '+task_text.get())
                print(main_listbox.curselection())
                self.note.todoIncompleted[self.last_index]['task'].append({'title': task_text.get(), 'completed': False})
                update_json()
                task_text.set('')
                # status 
                task_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
                task_status.grid(row=0, column=0, sticky='w')
                task_listbox.select_clear(0, END)


        #///////////////////////////

        # define list font
        list_font = Font(
                family='Browallia new',
                size=20) 

        # create menu bar
        menubar = Menu(self.master)
        # create account menu
        account_menu = Menu(menubar, tearoff=0)
        account_menu.add_command(label="New",  command=new_account)
        account_menu.add_command(label="Delete", command=delete_account)

        account_menu.add_separator()
        account_menu.add_command(label="Exit", command=self.master.quit)

        menubar.add_cascade(label="Account", menu=account_menu)
        # create edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Update",  command= lambda: editWindow(self.master))
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete All Complete",  command=del_alldone)

        menubar.add_cascade(label="Edit", menu=edit_menu)

        #///////////////////////////

        separator = ttk.Separator(self.master, orient='vertical')
        separator.grid(row=0,column=1,rowspan=3,sticky="ns")

        # frame detail
        global detail_frame
        detail_frame = ttk.Frame(self.master)
        detail_frame.grid(row=0,column=2,rowspan=3, padx=10, sticky='nswe')

        # container: detail_frame(frame1)
        global main_title_label ,detail_frame1, main_date_label, main_cal
        detail_frame1 = Frame(detail_frame)  
        detail_frame1.grid(row=0, padx=10, pady=10, sticky='nsew')      
        detail_frame1.columnconfigure(0,weight=0)
        detail_frame1.rowconfigure(0,weight=0) 

        #title
        main_title_label = Label(detail_frame1,text="Title :",font=('Helvetica 11 bold'))
        main_title_label.grid(row=0, column=0,sticky='w', pady=10)
        main_title_text= StringVar()
        title_show  = Entry(detail_frame1,textvariable=main_title_text,
                        font=('Helvetica 11'),state='disabled')
        title_show.grid(row=0,column=1,padx=10, sticky='w')

        # date
        main_date_label = Label(detail_frame1, text ="Date :")
        main_date_label.grid(row=0, column=2,sticky='w')
        main_cal = DateEntry(detail_frame1, selectmode = 'day',
                        year = 2020, month = 5,
                        day = 22)
        main_cal.grid(row=0, column=3, padx=10, sticky='w') 
        date_text = main_cal.get_date()

        # detail
        main_detail_text= StringVar()
        main_detail_label = Label(detail_frame1, text='Detail')
        main_detail_label.grid(row=1, column=0, sticky='w')
        main_detail_show = Entry(detail_frame1,textvariable=main_detail_text, state=DISABLED)
        main_detail_show.grid(row=2,column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

        # time
        main_time_text= StringVar()
        main_time_label = Label(detail_frame1,  text='Time :' ) 
        main_time_label.grid(row=1,column=2,sticky='w') 
        # set time
        main_time_string = strftime('%H:%M:%S')
        main_time_text.set(main_time_string)  # adding time to Entry
        main_time_show = Label(detail_frame1, textvariable=main_time_text) #  Entry box
        main_time_show.grid(row=1,column=3,sticky='w') 

        # button delete
        btn_del = Button(detail_frame1,text ="Delete List", state= DISABLED)
        btn_del.grid(row=2,column=3,pady=10, sticky='ew')

        separator = ttk.Separator(detail_frame, orient='horizontal')
        separator.grid(row=1,columnspan=3,sticky="ew")

        # container: detail_frame(frame2)
        detail_frame2 = Frame(detail_frame)                                
        detail_frame2.grid(row=2, padx=10,pady=10, sticky='nsew') 
        detail_frame2.columnconfigure(0,weight=20) 

        # task list
        global task_listbox, task_scrollbar
        task_listbox = Listbox(detail_frame2,
                        font=list_font,
                        bg='SystemButtonFace',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')
        task_listbox.grid(row=0,column=0,columnspan=3,sticky='nsew')

        # create scrollbar
        task_scrollbar = Scrollbar(detail_frame2)
        task_scrollbar.grid(row=0,column=3,sticky='ns')
        # set scroll to listbox
        task_listbox.configure(yscrollcommand=task_scrollbar.set)
        task_scrollbar.configure(command=task_listbox.yview)
        separator.grid(row=1,columnspan=3,sticky="ew")

        # container: detail_frame(frame3)
        global detail_frame3
        detail_frame3 = Frame(detail_frame)                                 
        detail_frame3.grid(row=3, padx=10,pady=10, sticky='nsew') 
        detail_frame3.columnconfigure(1,weight=20)

        # status 
        task_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
        task_status.grid(row=0, column=0, sticky='w')

        # entry
        task_text = StringVar()
        detail_label = Label(detail_frame3, text='Add task')
        detail_label.grid(row=0, column=2, sticky='w', padx=10)
        detail_entry = Entry(detail_frame3, textvariable=task_text)
        detail_entry.grid(row=0,column=3,columnspan=3, pady=10, sticky='nswe')

        # button add
        btn_add = Button(detail_frame3,text ="+",state= DISABLED)
        btn_add.grid(row=0, column=6, sticky='e')

        #///////////////////////////

        # container: master(frame1)
        mframe1 = Frame(self.master)  
        mframe1.grid(row=0,column=0,padx=10, sticky='nswe')      
        mframe1.columnconfigure(0,weight=1)
        mframe1.rowconfigure(0,weight=1) 

        # combobox
        account_str=StringVar()        # get account_str
        combox = ttk.Combobox(mframe1, textvariable=account_str, 
                                state='readonly', font=('Helvetica 11 bold'))
        combox["values"] = self.account
        combox.current(0)
        combox.grid(row=0, column=0)

        combox.bind("<<ComboboxSelected>>", changeAccount)

        # button check
        btn_add = Button(mframe1,text ="check", command=check_item)
        btn_add.grid(row=0, padx=10, pady=10, column=1, sticky='ew')

        #///////////////////////////

        # List ToDo page :: notebook
        notebook = ttk.Notebook(self.master)
        notebook.grid(row=1, column=0,padx=10, sticky='nswe')
        # create page page 1 : main, page 2 : complete
        page1 = ttk.Frame(notebook, width=400, height=500)
        notebook.bind('<<NotebookTabChanged>>',lambda e :changePage())
        page2 = ttk.Frame(notebook, width=400, height=500)
        notebook.bind('<<NotebookTabChanged>>',lambda e :changePage())

        page1.pack(fill='both', expand=True)
        page2.pack(fill='both', expand=True)

        notebook.add(page1, text='TODO-List')
        notebook.add(page2, text='Complete')

        # container: TODOList(frame2)
        mframe2 = Frame(page1)                                 
        mframe2.pack(fill=BOTH, expand=True)  
        mframe2.columnconfigure(0,weight=1)
        mframe2.rowconfigure(0,weight=1)

        # create a listbox widget
        global main_listbox
        main_listbox=Listbox(mframe2, 
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')    
        main_listbox.grid(row=0,column=0,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(mframe2)
        scrollbar.grid(row=0,column=1,sticky='nsew')
        # set scroll to listbox
        main_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=main_listbox.yview)
        main_listbox.bind('<<ListboxSelect>>', 
                lambda e: click_item_show(main_listbox, int(e.widget.curselection()[0]))) #Select click
        main_listbox.bind('<Double-1>', 
                lambda e: editWindow(self.master, e, click_item_show, main_listbox, name=account_str.get())) #double click

        separator = ttk.Separator(mframe2, orient='horizontal')
        separator.grid(sticky="ew")

        # insert list in listbox
        for item in range(len(self.mlist)): 
	        main_listbox.insert(END, self.mlist[item]) 

        # container: Complete(frame2)
        cframe2 = Frame(page2)                                 
        cframe2.pack(fill=BOTH, expand=True)  
        cframe2.columnconfigure(0,weight=1)
        cframe2.rowconfigure(0,weight=1)

        # create a listbox widget
        global clistbox
        clistbox=Listbox(cframe2, 
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')    
        clistbox.grid(row=0,column=0,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(cframe2)
        scrollbar.grid(row=0,column=1,sticky='nsew')
        # set scroll to listbox
        clistbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=clistbox.yview)
        clistbox.bind('<<ListboxSelect>>', 
                lambda e: click_item_show(clistbox, int(e.widget.curselection()[0]))) #Select click
        
        separator = ttk.Separator(cframe2, orient='horizontal')
        separator.grid(sticky="ew")

        # insert list in listbox
        for item in range(len(self.clist)): 
	        clistbox.insert(END, self.clist[item]) 

        #///////////////////////////

        # container: master(frame3)
        global mframe3
        mframe3 = Frame(self.master)                                 
        mframe3.grid(row=2,column=0, padx=10,pady=10, sticky='nsew') 
        mframe3.columnconfigure(0,weight=1)
        mframe3.rowconfigure(0,weight=1) 

        # button add
        btn_add = Button(mframe3,text ="+")
        btn_add.bind("<Button>",
                lambda e: addWindow(self.master, name = account_str.get()))
        btn_add.grid(row=0, column=1)


        # self.list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]
        fetch_data()
        fetch_listbox()

        # label status len(list)
        text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
        text_status.grid(row=0, column=0, sticky='w')
        
        # config for menu
        self.master.config(menu=menubar)
        


#/////////////////////////////////////////////////////////////////////

# class for new window add
class addWindow(Toplevel):
     
    def __init__(self, master = None, name=None):
        # set self => master 
        super().__init__(master = master)
        self.title("Add List")
        self.note = NoteManager()
        self.mlist = []
        self.clist = []
        self.todo = []
        self.tasklist =[]
        self.name = name


        def add_list():
                # string form entry
                str_title = add_title_text.get()
                str_detail = add_detail_text.get()
                str_date = self.cal.get_date().strftime("%Y-%m-%d")
                str_time = add_time_text.get()
                self.note.createTodo(str_title, str_date, str_detail, str_time)
                main_listbox.insert(END, str_title)
                update_json()
                self.destroy()
                text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')

        def fetch_listbox():
                mlist = self.note.getTodoIncompletedTitle()
                clist = self.note.getTodoCompletedTitle()
                main_listbox.delete(0, END)
                clistbox.delete(0, END)
                for item in mlist:
                        main_listbox.insert(END, item)
                for item in clist:
                        clistbox.insert(END, item)

        def fetch_data():
                self.note.loadJson()
                self.note.checkUser(self.name)
                self.todo = self.note.getTodos()
                self.account = self.note.getAccout()
        
        def update_json():
                self.note.updateCurrentUser()
                self.note.toJson()
                fetch_data()
                fetch_listbox()

        fetch_data()

                

        # title
        add_title_text = StringVar()
        add_title_label = Label(self, text ="Title")
        add_title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        add_title_entry = Entry(self, textvariable=add_title_text)
        add_title_entry.grid(row=0, column=1, padx=10, pady=10)

        # date
        date_label = Label(self, text ="Date")
        date_label.grid(row=0, column=2,sticky='w')
        self.cal = DateEntry(self, locale='en_US') 
        self.cal.grid(row=0, column=3, padx=10, sticky='w')

        # container: addWindow(frame2)
        add_frame2 = Frame(self)  
        add_frame2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        add_frame2.columnconfigure(0,weight=1)
        add_frame2.rowconfigure(0,weight=0) 

        # detail
        add_detail_text = StringVar()
        add_detail_label = Label(add_frame2, text='Detail')
        add_detail_label.grid(row=0, column=0, sticky='w')
        add_detail_entry = Entry(add_frame2, textvariable=add_detail_text)
        add_detail_entry.grid(row=1, columnspan=4, pady=10, sticky='nswe')

        # time
        add_time_text= StringVar()
        add_time_label = Label(add_frame2,  text='Time' ) 
        add_time_label.grid(row=0,column=1,padx=10) 
        add_time_entry = Entry(add_frame2, textvariable=add_time_text,width=15) #  Entry box
        add_time_entry.grid(row=0,column=2) 
        # set time
        add_time_string = strftime('%H:%M:%S')
        add_time_text.set(add_time_string)  # adding time to Entry

        # container: addWindow(frame3)
        add_frame3 = Frame(self)  
        add_frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        add_frame3.columnconfigure(0,weight=1)
        add_frame3.rowconfigure(0,weight=1)

        # button
        add_btn_done = Button(add_frame3, text ="Done", command=add_list)
        add_btn_done.grid(row=0, column=0, sticky='e', padx=10)
        add_btn_add = Button(add_frame3, text ="Cancel", command=self.destroy)
        add_btn_add.grid(row=0, column=1, sticky='e', padx=10)
  
#/////////////////////////////////////////////////////////////////////

# class for new window update
class editWindow(Toplevel):
     
    def __init__(self, master, e, update_func=None, listbox=None, name=None):
        # set self => master 
        super().__init__(master = master)
        self.title("Update List")
        self.name = name
        self.note = NoteManager()
        self.todo = {}
        self.clist = []
        self.mlistTodo = []
        self.mlist = []
        self.update_func = update_func
        self.index = int(e.widget.curselection()[0])
        self.listbox = listbox
        # index of selection
        index = int(main_listbox.curselection()[0])

        def setTextInput(text, entry):
                entry.delete(0,"end")
                entry.insert(0, text)

        def update_listbox(index, updated_item):
                main_listbox.delete(main_listbox.index(index))
                main_listbox.insert(index, updated_item)

        def edit_list():
                # try :
                        # string form entry
                        str_title = edit_title_entry.get()
                        str_detail = edit_detail_entry.get()
                        str_date1 = self.edit_cal.get_date().strftime("%Y-%m-%d")

                        todo = self.note.getTodoIncompleted()
                        todo[self.index]['title'] = str_title
                        todo[self.index]['endDate'] = str_date1
                        todo[self.index]['detail'] = str_detail
                        update_json()
                        self.update_func(listbox, index)
                        self.destroy()

                        # update_listbox
                        # update_listbox(self.index, str_title)

                        #self.destroy()
                # except: pass
        
        def fetch_listbox():
                mlist = self.note.getTodoIncompletedTitle()
                clist = self.note.getTodoCompletedTitle()
                main_listbox.delete(0, END)
                clistbox.delete(0, END)
                for item in mlist:
                        main_listbox.insert(END, item)
                for item in clist:
                        clistbox.insert(END, item)

        def fetch_data():
                self.note.loadJson()
                self.note.sortTodo()
                self.note.checkUser(self.name)
                self.todo = self.note.getTodos()
                self.mlistTodo = self.note.getTodoIncompleted()
                self.account = self.note.getAccout()

        def update_json():
                self.note.updateCurrentUser()
                self.note.toJson()
                fetch_data()
                fetch_listbox()

        fetch_data()

        # index = int(listbox.curselection()[0])


        # title
        edit_title_text = StringVar()
        edit_title_label = Label(self, text ="Title")
        edit_title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        edit_title_entry = Entry(self, textvariable=edit_title_text)
        edit_title_entry.grid(row=0, column=1, padx=10, pady=10)
        # string to entry
        value = main_listbox.get(index)      # text selection form listbox
        setTextInput(self.mlistTodo[self.index]['title'], edit_title_entry)

        # date
        edit_date_label = Label(self, text ="Date")
        edit_date_label.grid(row=0, column=2,sticky='w')
        # select_date = self.mlistTodo[self.index]['endDate'].split("-")
        select_date = self.mlistTodo[self.index]['endDate']
        self.edit_cal = DateEntry(self, locale='en_US') 
        self.edit_cal.set_date(datetime.strptime(select_date, "%Y-%m-%d"))
        # self.edit_cal = DateEntry(self, selectmode = 'day',
        #                                 year = int(select_date[0]), month = int(select_date[1]),
        #                                 day = int(select_date[2]))
        self.edit_cal.grid(row=0, column=3, padx=10, sticky='w') 
        
        # container: addWindow(frame2)
        edit_frame2 = Frame(self)  
        edit_frame2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        edit_frame2.columnconfigure(0,weight=2)
        edit_frame2.rowconfigure(0,weight=0) 

        # detail
        edit_detail_text = StringVar()
        edit_detail_label = Label(edit_frame2, text='Detail')
        edit_detail_label.grid(row=0, column=0, sticky='w')
        edit_detail_entry = Entry(edit_frame2, textvariable=edit_detail_text)
        edit_detail_entry.grid(row=1, columnspan=4, pady=10, sticky='nswe')
        # string to entry
        setTextInput(self.mlistTodo[self.index]['detail'], edit_detail_entry)

        # time
        edit_time_text= StringVar()
        edit_time_label = Label(edit_frame2,  text='Time' ) 
        edit_time_label.grid(row=0,column=1,padx=10) 
        edit_time_entry = Entry(edit_frame2, textvariable=edit_time_text,width=15) #  Entry box
        edit_time_entry.grid(row=0,column=2) 
        # set time
        edit_time_string = strftime('%H:%M:%S')
        edit_time_text.set(edit_time_string)  # adding time to Entry

        # container: addWindow(frame3)
        edit_frame3 = Frame(self)  
        edit_frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        edit_frame3.columnconfigure(0,weight=1)
        edit_frame3.rowconfigure(0,weight=1)

        # button
        edit_btn_done = Button(edit_frame3, text ="Done", command= lambda: edit_list())
        edit_btn_done.grid(row=0, column=0, sticky='e', padx=10)
        edit_btn_add = Button(edit_frame3, text ="Cancel", command=self.destroy)
        edit_btn_add.grid(row=0, column=1, sticky='e', padx=10)
  
#/////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
  
    # Instantiating top level
    root = Tk()
    # Calling our App
    app = App(root)

    root.mainloop()