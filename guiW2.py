from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from tkcalendar import DateEntry # pip install tkcalendar
from time import strftime

# Creating App class which will contain
class App:
    def __init__(self, master) -> None:
        # Instantiating master i.e toplevel Widget
        self.master = master
        # Setting the title of the window
        self.master.title('TODODO')

        self.account = ["Guest", "user1", "user2"]
        self.mlist = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]
        self.clist = []
        self.tasklist =[]
        self.last_index = 0
        self.last_task_index = 0


        #///////////////////////////

        # FUNCTIONS
        def new_account():      # window for input text
            add_account_win = Toplevel(self.master)
            add_account_win.title('New Account')

            add_account_Label = Label(add_account_win,text='Account')
            add_account_Label.grid(row=0,column=0,padx=10,pady=10)

            global text_new_account
            text_new_account = StringVar()
            add_account_entry = Entry(add_account_win,textvariable=text_new_account)
            add_account_entry.grid(row=0,column=1,columnspan=1,padx=10,pady=10,sticky='w')

            separator = ttk.Separator(add_account_win, orient='horizontal')
            separator.grid(row=1,columnspan=2,sticky="ew")

            add_account_btn = Button(add_account_win, text="Done", command= lambda: add_account(add_account_win))
            add_account_btn.grid(row=2,column=0,padx=10,pady=10)
            btn_cancel = Button(add_account_win, text="Cancel", command=add_account_win.destroy)
            btn_cancel.grid(row=2,column=1,padx=10,pady=10)

        def add_account(root):      # add new account in combo box
            self.account.append(text_new_account.get())
            #text_new_account.get()
            combox["values"] = self.account
            combox.current(END)
            root.destroy()
            refresh()
                
        def delete_account():
            ask = messagebox.askokcancel("Are you sure?","Are you sure to delete \"{}\" account".format(account_str.get()))
            if ask:
                self.account.remove(account_str.get())
                combox["values"] = self.account
                combox.current(0)
                refresh()

        def changeAccount(event):
            refresh()
            self.mlist
            self.clist
                
        def refresh():
            clear_all_listbox()
            # show title 
            detail_title_text.set('Title')
            # show date
            
            # show detail
            detail_detail_text.set('Detail')
            # set time
            value_time = strftime('%H:%M')
            detail_time_text.set(value_time)  # adding time to Entry

            # status len(list)
            list_status.configure(text = str(main_listbox.size()) + " list ")
            # status task
            task_text.set('')       # empty entry
            task_status.configure(text = str(task_listbox.size()) + " list ")

        def clear_all_listbox():
            main_listbox.delete(0,END)
            complete_listbox.delete(0,END)
            task_listbox.delete(0,END)

        def delete_list():
            main_listbox.delete(ANCHOR)
            # update status 
            list_status.configure(text = str(main_listbox.size()) + " list ")

        def changePage():
            # remove pointer main_listbox
            main_listbox.select_clear(0, END)
            
            index = notebook_left.index(notebook_left.select())
            if index == 0:      #'todo list page
                # button check
                btn_check.configure(text= 'Check')
                    
            elif index == 1:    #complete_list page
                # button check
                btn_check.configure(text= 'Uncheck')

        def click_check():
            try :   
                index = int(task_listbox.curselection()[0])
                # not done
                if task_listbox.itemcget(index, "fg") == "#ffa364":
                        task_listbox.itemconfig(
                                task_listbox.curselection(),
                                fg='#21130d')
                        # get rid of selection bar
                        task_listbox.select_clear(0, END)
                # done
                task_listbox.itemconfig(
                        task_listbox.curselection(),
                        fg='#ffa364')
                # get rid of selection bar
                task_listbox.select_clear(0, END)
            except: pass

        def check_list():
            try :
                index=notebook_left.index(notebook_left.select())
                if index == 0:
                        index = int(main_listbox.curselection()[0])
                        value_title = main_listbox.get(index)      # text selection form listbox

                        complete_listbox.insert(END, value_title) 

                        main_listbox.delete(ANCHOR)
                        # update status 
                        list_status.configure(text = str(main_listbox.size()) + " list ")
                elif index == 1:
                        index = int(complete_listbox.curselection()[0])
                        value_title = complete_listbox.get(index)      # text selection form listbox

                        main_listbox.insert(END, value_title) 

                        complete_listbox.delete(ANCHOR)
                        # update status 
                        list_status.configure(text = str(main_listbox.size()) + " list ")

            except: pass

        def show_detail_list(listbox, index_in):
            
            task_listbox.delete(0,END)    
            task_text.set('')       # clear entry add task
            
            if len(listbox.curselection()):
                self.last_index = int(listbox.curselection()[0])


            if listbox == complete_listbox:
                if index_in == None:
                        index = int(listbox.curselection()[0])
                else:
                        index = index_in

                value_title = listbox.get(index)      # text selection form listbox

                task_listbox.bind('<<ListboxSelect>>', 
                        lambda e: click_check()) #Select click

                # enable btn_addtask & btn_del
                detail_btn_add.configure(state= DISABLED)
                detail_btn_del.configure(state= DISABLED)

                value_title = listbox.get(index)      # text selection form listbox

                # show title 
                detail_title_text.set(value_title)
                # show date
                detail_date_text.set('date')
                # show detail
                value_detail = ''
                detail_detail_text.set(value_detail)
                # set time
                value_time = strftime('%H:%M')
                detail_time_text.set(value_time)  # adding time to Entry

                # status 
                task_status.configure(text = str(task_listbox.size()) + " list ")
                    
            elif listbox == main_listbox:
                if index_in == None:
                        index = int(listbox.curselection()[0])
                else:
                        index = index_in

                value_title = listbox.get(index)      # text selection form listbox

                task_listbox.bind('<<ListboxSelect>>', 
                        lambda e: click_check()) #Select click

                # enable btn_addtask & btn_del 
                detail_btn_add.configure(state=NORMAL)
                detail_btn_del.configure(state=NORMAL)

                # show title 
                detail_title_text.set(value_title)
                # show date
                detail_date_text.set('date') 
                # show detail
                value_detail = ''
                detail_detail_text.set(value_detail)
                # set time
                value_time = strftime('%H:%M')
                detail_time_text.set(value_time)  # adding time to Entry

                # task status 
                task_status.configure(text = str(task_listbox.size()) + " list ")
    



        def del_all():
                ask = messagebox.askokcancel("Are you sure?","Are you sure to delete all list")
                if ask:
                    clear_all_listbox() 
                    # list status
                    list_status.configure(text = str(main_listbox.size()) + " list ")
                        # task status 
                    task_status.configure(text = str(task_listbox.size()) + " list ")


        def add_task():
                # remove pointer main_listbox
                main_listbox.select_clear(0, END)

                task_listbox.insert(END, task_text.get())
                task_text.set('')
                # task status 
                task_status.configure(text = str(task_listbox.size()) + " list ")
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
        edit_menu.add_command(label="Import",  command= lambda: editWindow(self.master))
        edit_menu.add_command(label="Export",  command= lambda: editWindow(self.master))
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete All Complete",  command=del_all)

        menubar.add_cascade(label="Edit", menu=edit_menu)

        #///////////////////////////

        # frame for design
        main_frame = Frame(self.master)  
        main_frame.grid(row=0,rowspan=3,column=0,padx=10,pady=10, sticky='nswe') 
        main_frame.rowconfigure(1,weight=2)

        # container: master(frame1)
        main_frame1 = Frame(main_frame)  
        main_frame1.grid(row=0,column=0,padx=10, pady=10,sticky='nswe')      

        # combobox
        account_str=StringVar()        # get account_str
        combox = ttk.Combobox(main_frame1, textvariable=account_str,
                                state='readonly', font=('Helvetica 11 bold'))
        combox["values"] = self.account
        combox.current(0)
        combox.grid(row=0, column=0)

        combox.bind("<<ComboboxSelected>>", changeAccount)

        # button check
        btn_check = Button(main_frame1,text ="check", command=check_list)
        btn_check.grid(row=0, padx=10, pady=10, column=1, sticky='ew')

        #///////////////////////////

        # List ToDo page :: notebook left
        notebook_left = ttk.Notebook(main_frame)
        notebook_left.grid(row=1, column=0,padx=10, sticky='nswe')

        # create page page 1 : main, page 2 : complete
        notebook_left_page1 = ttk.Frame(notebook_left,width=400, height=500)
        notebook_left.bind('<<NotebookTabChanged>>',lambda e :changePage())
        notebook_left_page2 = ttk.Frame(notebook_left)
        notebook_left.bind('<<NotebookTabChanged>>',lambda e :changePage())

        notebook_left_page1.pack(fill='both', expand=True)
        notebook_left_page2.pack(fill='both', expand=True)

        notebook_left.add(notebook_left_page1, text='TODO-List')
        notebook_left.add(notebook_left_page2, text='Complete')

        #///////////////////////////

        # List ToDo page :: notebook right
        notebook_right = ttk.Notebook(self.master)
        notebook_right.grid(row=0,rowspan=3, column=2,padx=10,pady=10, sticky='nswe')
        # create page page 1 : main, page 2 : complete
        notebook_right_page1 = ttk.Frame(notebook_right)
        notebook_right_page2 = ttk.Frame(notebook_right)

        notebook_right_page1.pack(fill='both', expand=True)
        notebook_right_page2.pack(fill='both', expand=True)

        notebook_right.add(notebook_right_page1, text='Detail')
        notebook_right.add(notebook_right_page2, text='Graph')

        #///////////////////////////

        # container: TODOList(frame) use page1
        ToDoList_frame = Frame(notebook_left_page1)                                 
        ToDoList_frame.pack(fill=BOTH, expand=True)  
        ToDoList_frame.columnconfigure(0,weight=1)
        ToDoList_frame.rowconfigure(0,weight=1)

        # create a listbox widget
        global main_listbox
        main_listbox=Listbox(ToDoList_frame, 
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')    
        main_listbox.grid(row=0,column=0,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(ToDoList_frame)
        scrollbar.grid(row=0,column=1,sticky='nsew')
        # set scroll to listbox
        main_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=main_listbox.yview)
        main_listbox.bind('<<ListboxSelect>>', 
                lambda e: show_detail_list(main_listbox,
                            int(main_listbox.curselection()[0]))) #Select click
        main_listbox.bind('<Double-1>', 
                lambda e: editWindow(self.master)) #double click

        separator = ttk.Separator(ToDoList_frame, orient='horizontal')
        separator.grid(sticky="ew")

        # insert list in listbox
        for item in range(len(self.mlist)): 
	        main_listbox.insert(END, self.mlist[item]) 

        #///////////////////////////

        # container: Complete(frame) use page2
        CompeletList_frame = Frame(notebook_left_page2)                                 
        CompeletList_frame.pack(fill=BOTH, expand=True)  
        CompeletList_frame.columnconfigure(0,weight=1)
        CompeletList_frame.rowconfigure(0,weight=1)

        # create a listbox widget
        global complete_listbox
        complete_listbox=Listbox(CompeletList_frame, 
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')    
        complete_listbox.grid(row=0,column=0,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(CompeletList_frame)
        scrollbar.grid(row=0,column=1,sticky='nsew')
        # set scroll to listbox
        complete_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=complete_listbox.yview)
        complete_listbox.bind('<<ListboxSelect>>', 
                lambda e: show_detail_list(complete_listbox,
                            int(complete_listbox.curselection()[0]))) #Select click
        
        separator = ttk.Separator(CompeletList_frame, orient='horizontal')
        separator.grid(sticky="ew")

        # insert list in listbox
        for item in range(len(self.clist)): 
	        complete_listbox.insert(END, self.clist[item]) 

        #///////////////////////////

        # container: master(frame2)
        main_frame2 = Frame(main_frame)                                 
        main_frame2.grid(row=2,column=0, padx=10,pady=10, sticky='nsew') 
        main_frame2.columnconfigure(0,weight=1)
        main_frame2.rowconfigure(0,weight=1) 

        # button add
        btn_add = Button(main_frame2,text ="+")
        btn_add.bind("<Button>",
                lambda e: addWindow(self.master))
        btn_add.grid(row=0, column=1)

        # status list
        global list_status
        list_status = Label(main_frame2, text = str(main_listbox.size()) + " list ")
        list_status.grid(row=0, column=0, sticky='w')
        
        
        # config for menu
        self.master.config(menu=menubar)

        #///////////////////////////

        separator = ttk.Separator(self.master, orient='vertical')
        separator.grid(row=0,column=1,rowspan=3,sticky="ns")

        #///////////////////////////

        # container: Detail(frame) 
        global detail_frame
        detail_frame = ttk.Frame(notebook_right_page1)
        detail_frame.grid(row=0,column=2,rowspan=3, padx=10, sticky='nswe')

        # container: detail_frame(frame1)
        detail_frame1 = Frame(detail_frame)  
        detail_frame1.grid(row=0, padx=10, pady=10, sticky='nsew')      

        #title (frame1)
        detail_title_text = StringVar()
        detail_title_text.set('Title')
        detail_title_entry = Entry(detail_frame1,textvariable=detail_title_text,
                            font=('Helvetica 11 bold'),bg='#FFFFFF',bd=0,state= 'readonly')
        detail_title_entry.grid(row=0, column=0,columnspan=2 ,sticky='w', pady=10)
        detail_title_entry.columnconfigure(1,weight=30)

        # date (frame1)
        detail_date_text = StringVar()
        detail_date_label = Label(detail_frame1, text ="Date :")
        detail_date_label.grid(row=0, column=2,padx=10,sticky='w')
        detail_date_show = Label(detail_frame1, textvariable= detail_date_text)
        detail_date_show.grid(row=0, column=3, padx=10, sticky='w') 

        # detail (frame1)
        detail_detail_text= StringVar()
        detail_detail_label = Label(detail_frame1, text='Detail')
        detail_detail_label.grid(row=1, column=0, sticky='w')
        detail_detail_entry = Entry(detail_frame1,textvariable=detail_detail_label,bd=0,state='readonly')
        detail_detail_entry.grid(row=2,column=0, columnspan=3, pady=10, sticky='nswe')

        # time (frame1)
        detail_time_text= StringVar()
        detail_time_label = Label(detail_frame1,  text='Time :' ) 
        detail_time_label.grid(row=1,column=2,padx=10,sticky='w') 
        # set time
        detail_time_string = strftime('%H:%M')
        detail_time_text.set(detail_time_string)  # adding time to Entry
        detail_time_show = Label(detail_frame1, textvariable=detail_time_text) #  Entry box
        detail_time_show.grid(row=1,column=3,padx=10,sticky='w') 

        # button delete (frame1)
        detail_btn_del = Button(detail_frame1,text ="Delete List",state= DISABLED)
        detail_btn_del.grid(row=2,column=3,padx=10,pady=10, sticky='ew')
        detail_btn_del.bind("<Button>",lambda e: delete_list())


        separator = ttk.Separator(detail_frame, orient='horizontal')
        separator.grid(row=1,columnspan=3,sticky="ew")

        # container: detail_frame(frame2)
        detail_frame2 = Frame(detail_frame)                                
        detail_frame2.grid(row=2, padx=10,pady=10, sticky='nsew') 
        detail_frame2.columnconfigure(0,weight=20) 

        # task list (frame2)
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

        # create scrollbar (frame2)
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

        # status (frame3)
        task_status = Label(detail_frame3, text = str(task_listbox.size()) + " task ")
        task_status.grid(row=0, column=0, sticky='w')

        # entry (frame3)
        task_text = StringVar()
        detail_label = Label(detail_frame3, text='Add task')
        detail_label.grid(row=0, column=2, sticky='w', padx=10)
        detail_entry = Entry(detail_frame3, textvariable=task_text)
        detail_entry.grid(row=0,column=3,columnspan=3, pady=10, sticky='nswe')

        # button add
        detail_btn_add = Button(detail_frame3,text ="+", command= lambda e: click_check,state= DISABLED)
        detail_btn_add.grid(row=0, column=6, sticky='e')
        detail_btn_add.bind("<Button>",lambda e: add_task())

        #///////////////////////////

        

        #///////////////////////////


#/////////////////////////////////////////////////////////////////////

class addWindow(Toplevel):
     
    def __init__(self, master = None):
        # set self => master 
        super().__init__(master = master)
        self.title("Add List")

        def add_list():
                # string form entry
                str_title = add_list_title_text.get()   # data title
                str_detail = add_list_detail_text.get() # data detail
                str_date = add_list_date_text           # data date

                main_listbox.insert(END, str_title) 

                # list status
                list_status.configure(text = str(main_listbox.size()) + " list ")

                self.destroy()
                

        # title
        add_list_title_text = StringVar()
        add_list_title_label = Label(self, text ="Title")
        add_list_title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        add_list_title_entry = Entry(self, textvariable=add_list_title_text)
        add_list_title_entry.grid(row=0, column=1, padx=10, pady=10)

        # date
        add_list_date_label = Label(self, text ="Date")
        add_list_date_label.grid(row=0, column=2,sticky='w')
        add_list_cal = DateEntry(self, locale='en_US') 
        add_list_cal.grid(row=0, column=3, padx=10, sticky='w')
        add_list_date_text = add_list_cal.get_date()

        #///////////////////////////

        # container: addWindow(frame2)
        add_list_frame2 = Frame(self)  
        add_list_frame2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        add_list_frame2.columnconfigure(0,weight=1)
        add_list_frame2.rowconfigure(0,weight=0) 

        # detail
        add_list_detail_text = StringVar()
        add_list_detail_label = Label(add_list_frame2, text='Detail')
        add_list_detail_label.grid(row=0, column=0, sticky='w')
        add_list_detail_entry = Entry(add_list_frame2, textvariable=add_list_detail_text)
        add_list_detail_entry.grid(row=1, columnspan=4, pady=10, sticky='nswe')

        # time
        add_list_time_text= StringVar()
        add_list_time_label = Label(add_list_frame2,  text='Time' ) 
        add_list_time_label.grid(row=0,column=1,padx=10) 
        add_list_time_entry = Entry(add_list_frame2, textvariable=add_list_time_text,width=15) #  Entry box
        add_list_time_entry.grid(row=0,column=2) 
        # set time
        add_list_time_string = strftime('%H:%M')
        add_list_time_text.set(add_list_time_string)  # adding time to Entry

        #///////////////////////////

        # container: addWindow(frame3)
        add_list_frame3 = Frame(self)  
        add_list_frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        add_list_frame3.columnconfigure(0,weight=1)
        add_list_frame3.rowconfigure(0,weight=1)

        # button
        add_btn_done = Button(add_list_frame3, text ="Done", command=add_list)
        add_btn_done.grid(row=0, column=0, sticky='e', padx=10)
        add_btn_add = Button(add_list_frame3, text ="Cancel", command=self.destroy)
        add_btn_add.grid(row=0, column=1, sticky='e', padx=10)
  
#/////////////////////////////////////////////////////////////////////

class editWindow(Toplevel):
     
    def __init__(self, master = None):
        # set self => master 
        super().__init__(master = master)
        self.title("Update List")

        # index of selection
        index = int(main_listbox.curselection()[0])

        def setTextInput(text, entry):
                entry.delete(0,"end")
                entry.insert(0, text)

        def update_listbox(index, updated_item):
                main_listbox.delete(main_listbox.index(index))
                main_listbox.insert(index, updated_item)

        def edit_list(index):
                # string form entry
                str_title = edit_title_text.get()   # data title
                str_detail = edit_detail_text.get() # data detail
                str_date = edit_date_text           # data date
  
                # update_listbox
                update_listbox(index, str_title)

                self.destroy()

        # title
        edit_title_text = StringVar()
        edit_title_label = Label(self, text ="Title")
        edit_title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        edit_title_entry = Entry(self, textvariable=edit_title_text)
        edit_title_entry.grid(row=0, column=1, padx=10, pady=10)
        # string to entry
        value = main_listbox.get(index)      # text selection form listbox
        setTextInput(value, edit_title_entry)

        # date
        edit_date_label = Label(self, text ="Date")
        edit_date_label.grid(row=0, column=2,sticky='w')
        edit_cal = DateEntry(self, selectmode = 'day',
                        year = 2020, month = 5,
                        day = 22)
        edit_cal.grid(row=0, column=3, padx=10, sticky='w') 
        edit_date_text = edit_cal.get_date()

        #///////////////////////////
        
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
        #setTextInput(value, detail_entry)

        # time
        edit_time_text= StringVar()
        edit_time_label = Label(edit_frame2,  text='Time' ) 
        edit_time_label.grid(row=0,column=1,padx=10) 
        edit_time_entry = Entry(edit_frame2, textvariable=edit_time_text,width=15) #  Entry box
        edit_time_entry.grid(row=0,column=2) 
        # set time
        edit_time_string = strftime('%H:%M')
        edit_time_text.set(edit_time_string)  # adding time to Entry

        #///////////////////////////

        # container: addWindow(frame3)
        edit_frame3 = Frame(self)  
        edit_frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        edit_frame3.columnconfigure(0,weight=1)
        edit_frame3.rowconfigure(0,weight=1)

        # button
        edit_btn_done = Button(edit_frame3, text ="Done", command= lambda: edit_list(index))
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