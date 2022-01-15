# importing tkinter module and Widgets
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from turtle import st
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

        # FUNCTIONS
        def delete_item():
                main_listbox.delete(ANCHOR)
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

        def check_item():
                try :
                        index = int(main_listbox.curselection()[0])
                        value_title = main_listbox.get(index)      # text selection form listbox

                        clistbox.insert(END, value_title) 

                        main_listbox.delete(ANCHOR)
                        # update status 
                        text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                        text_status.grid(row=0, column=0, sticky='w')

                except: pass

        def click_item_show(listbox):
                try :
                        btn_del = Button(detail_frame1,text ="Delete", state= NORMAL, command=delete_item)
                        btn_del.grid(row=2,column=3,pady=10, sticky='ew')

                        index = int(listbox.curselection()[0])
                        value_title = listbox.get(index)      # text selection form listbox

                        # show title 
                        main_title_text.set(value_title)
                       
                        # show date
                        main_cal = DateEntry(detail_frame1, selectmode = 'day',
                        year = 2020, month = 5,
                        day = 22)
                        main_cal.grid(row=0, column=3, padx=10, sticky='w') 

                        # show detail
                        value_detail = ''
                        main_detail_text.set(value_detail)

                        # set time
                        value_time = strftime('%H:%M:%S')
                        main_time_text.set(value_time)  # adding time to Entry
                        
                except: pass

        def del_alldone():
                count = 0
                while count < main_listbox.size():
                        if main_listbox.itemcget(count, "fg") == '#ffa364':
                                main_listbox.delete(main_listbox.index(count))
                        count +=1
                # update status 
                text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')

        def donothing():
                filewin = Toplevel(root)
                button = Button(filewin, text="Do nothing button")
                button.pack()

        # combo box
        def changeAccount(event):
                pass

        #///////////////////////////

        # define list font
        list_font = Font(
                family='Browallia new',
                size=20) 

        # create menu bar
        menubar = Menu(self.master)
        # create account menu
        account_menu = Menu(menubar, tearoff=0)
        account_menu.add_command(label="New",  command=donothing)
        account_menu.add_command(label="Delete", command=donothing)
        account_menu.add_command(label="Save", command=donothing)

        account_menu.add_separator()
        account_menu.add_command(label="Exit", command=self.master.quit)

        menubar.add_cascade(label="Account", menu=account_menu)
        # create edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Update",  command= lambda: editWindow(self.master))
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete All Done",  command=del_alldone)

        menubar.add_cascade(label="Edit", menu=edit_menu)

        #///////////////////////////

        separator = ttk.Separator(self.master, orient='vertical')
        separator.grid(row=0,column=1,rowspan=3,sticky="ns")

        # frame detail
        global detail_frame
        detail_frame = ttk.Frame(self.master, width=250)
        detail_frame.grid(row=0,column=2,rowspan=3, padx=10, sticky='nswe')

        # container: detail_frame(frame1)
        detail_frame1 = Frame(detail_frame)  
        detail_frame1.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        detail_frame1.columnconfigure(0,weight=2)
        detail_frame1.rowconfigure(0,weight=0) 

        #title
        main_title_label = Label(detail_frame1,text="Title :",font=('Helvetica 11 bold'))
        main_title_label.grid(row=0, column=0,sticky='w', pady=10)
        main_title_text= StringVar()
        title_show  = Entry(detail_frame1,textvariable=main_title_text,font=('Helvetica 11'))
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
        main_detail_show = Label(detail_frame1,textvariable=main_detail_text)
        main_detail_show.grid(row=2,column=0, columnspan=3, pady=10, sticky='nswe')

        # button delete
        btn_del = Button(detail_frame1,text ="Delete", state= DISABLED)
        btn_del.grid(row=2,column=3,pady=10, sticky='ew')

        # time
        main_time_text= StringVar()
        main_time_label = Label(detail_frame1,  text='Time :' ) 
        main_time_label.grid(row=1,column=2,sticky='w') 
        # set time
        main_time_string = strftime('%H:%M:%S')
        main_time_text.set(main_time_string)  # adding time to Entry
        main_time_show = Label(detail_frame1, textvariable=main_time_text) #  Entry box
        main_time_show.grid(row=1,column=3,sticky='w') 

        # container: detail_frame(frame2)
        detail_frame2 = Frame(detail_frame)                                 
        detail_frame2.grid(row=2,column=0,columnspan=3, padx=10,pady=10, sticky='nsew')  
        detail_frame2.columnconfigure(0,weight=0)
        detail_frame2.rowconfigure(0,weight=0)

        task_listbox = Listbox(detail_frame2,
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')
        task_listbox.grid(row=0,column=0,columnspan=3,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(detail_frame2)
        scrollbar.grid(row=0,column=3,sticky='nsew')
        # set scroll to listbox
        task_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=task_listbox.yview)
        task_listbox.bind('<<ListboxSelect>>', 
                lambda e: click_check()) #Select click

        separator = ttk.Separator(detail_frame2, orient='horizontal')
        separator.grid(row=1,columnspan=3,sticky="ew")

        # container: detail_frame(frame3)
        global detail_frame3
        detail_frame3 = Frame(detail_frame)                                 
        detail_frame3.grid(row=3, padx=10,pady=10, sticky='nsew') 
        detail_frame3.columnconfigure(0,weight=1)
        detail_frame3.rowconfigure(0,weight=1) 

        # button add
        btn_add = Button(detail_frame3,text ="+")
        btn_add.bind("<Button>",
                lambda e: addWindow(self.master))
        btn_add.grid(row=0, column=1, sticky='e')

        # update status 
        text_status = Label(detail_frame3, text ="have "+ str(task_listbox.size()) + " task ")
        text_status.grid(row=0, column=0, sticky='w')

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
                lambda e: click_item_show(main_listbox)) #Select click
        main_listbox.bind('<Double-1>', 
                lambda e: editWindow(self.master)) #double click

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
                lambda e: click_item_show(clistbox)) #Select click
        
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
                lambda e: addWindow(self.master))
        btn_add.grid(row=0, column=1)

        # label status len(list)
        text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
        text_status.grid(row=0, column=0, sticky='w')
        
        # config for menu
        self.master.config(menu=menubar)


#/////////////////////////////////////////////////////////////////////

# class for new window add
class addWindow(Toplevel):
     
    def __init__(self, master = None):
        # set self => master 
        super().__init__(master = master)
        self.title("Add List")

        def add_list():
                # string form entry
                str_title = title_text.get()
                print(str_title)
                str_detail = detail_text.get()
                print(str_detail)
                str_date = cal.get_date()
                print(str_date)

                main_listbox.insert(END, str_title) 

                # update count list
                text_status = Label(mframe3, text ="have "+ str(main_listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')

                self.destroy()
                

        # title
        title_text = StringVar()
        title_label = Label(self, text ="Title")
        title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        title_entry = Entry(self, textvariable=title_text)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        # date
        date_label = Label(self, text ="Date")
        date_label.grid(row=0, column=2,sticky='w')
        cal = DateEntry(self, locale='en_US') 
        cal.grid(row=0, column=3, padx=10, sticky='w')

        # container: addWindow(frame2)
        frame2 = Frame(self)  
        frame2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        frame2.columnconfigure(0,weight=1)
        frame2.rowconfigure(0,weight=0) 

        # detail
        detail_text = StringVar()
        detail_label = Label(frame2, text='Detail')
        detail_label.grid(row=0, column=0, sticky='w')
        detail_entry = Entry(frame2, textvariable=detail_text)
        detail_entry.grid(row=1, columnspan=4, pady=10, sticky='nswe')

        # time
        time_text= StringVar()
        time_label = Label(frame2,  text='Time' ) 
        time_label.grid(row=0,column=1,padx=10) 
        time_entry = Entry(frame2, textvariable=time_text,width=15) #  Entry box
        time_entry.grid(row=0,column=2) 
        # set time
        time_string = strftime('%H:%M:%S %p')
        time_text.set(time_string)  # adding time to Entry

        # container: addWindow(frame3)
        frame3 = Frame(self)  
        frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        frame3.columnconfigure(0,weight=1)
        frame3.rowconfigure(0,weight=1)

        # button
        btn_done = Button(frame3, text ="Done", command=add_list)
        btn_done.grid(row=0, column=0, sticky='e', padx=10)
        btn_add = Button(frame3, text ="Cancel", command=self.destroy)
        btn_add.grid(row=0, column=1, sticky='e', padx=10)
  
#/////////////////////////////////////////////////////////////////////

# class for new window update
class editWindow(Toplevel):
     
    def __init__(self, master = None):
        # set self => master 
        super().__init__(master = master)
        self.title("Update List")

        # index of selection
        index = int(main_listbox.curselection()[0])
        print(index)

        def setTextInput(text, entry):
                entry.delete(0,"end")
                entry.insert(0, text)

        def update_listbox(index, updated_item):
                main_listbox.delete(main_listbox.index(index))
                main_listbox.insert(index, updated_item)

        def edit_list(index):
                # string form entry
                str_title = title_text.get()
                print(str_title)
                str_detail = detail_text.get()
                print(str_detail)
                str_date = date_text
                print(str_date)

                # update_listbox
                update_listbox(index, str_title)

                self.destroy()

        # title
        title_text = StringVar()
        title_label = Label(self, text ="Title")
        title_label.grid(row=0, column=0,sticky='w', padx=10, pady=10)
        title_entry = Entry(self, textvariable=title_text)
        title_entry.grid(row=0, column=1, padx=10, pady=10)
        # string to entry
        value = main_listbox.get(index)      # text selection form listbox
        setTextInput(value, title_entry)

        # date
        date_label = Label(self, text ="Date")
        date_label.grid(row=0, column=2,sticky='w')
        cal = DateEntry(self, selectmode = 'day',
                        year = 2020, month = 5,
                        day = 22)
        cal.grid(row=0, column=3, padx=10, sticky='w') 
        date_text = cal.get_date()
        print(date_text)
        
        # container: addWindow(frame2)
        frame2 = Frame(self)  
        frame2.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')      
        frame2.columnconfigure(0,weight=2)
        frame2.rowconfigure(0,weight=0) 

        # detail
        detail_text = StringVar()
        detail_label = Label(frame2, text='Detail')
        detail_label.grid(row=0, column=0, sticky='w')
        detail_entry = Entry(frame2, textvariable=detail_text)
        detail_entry.grid(row=1, columnspan=4, pady=10, sticky='nswe')
        # string to entry
        #setTextInput(value, detail_entry)

        # time
        time_text= StringVar()
        time_label = Label(frame2,  text='Time' ) 
        time_label.grid(row=0,column=1,padx=10) 
        time_entry = Entry(frame2, textvariable=time_text,width=15) #  Entry box
        time_entry.grid(row=0,column=2) 
        # set time
        time_string = strftime('%H:%M:%S')
        time_text.set(time_string)  # adding time to Entry

        # container: addWindow(frame3)
        frame3 = Frame(self)  
        frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        frame3.columnconfigure(0,weight=1)
        frame3.rowconfigure(0,weight=1)

        # button
        btn_done = Button(frame3, text ="Done", command= lambda: edit_list(index))
        btn_done.grid(row=0, column=0, sticky='e', padx=10)
        btn_add = Button(frame3, text ="Cancel", command=self.destroy)
        btn_add.grid(row=0, column=1, sticky='e', padx=10)
  
#/////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
  
    # Instantiating top level
    root = Tk()
    # Setting the geometry i.e Dimensions
    #root.geometry("350x350")
  
    # Calling our App
    app = App(root)

    root.mainloop()