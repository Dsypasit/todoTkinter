# importing tkinter module and Widgets
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from tkcalendar import DateEntry # pip install tkcalendar

# Creating App class which will contain
class App:
    def __init__(self, master) -> None:
        # Instantiating master i.e toplevel Widget
        self.master = master
        # Setting the title of the window
        self.master.title('TODODO')

        # FUNCTIONS
        def delete_item():
                listbox.delete(ANCHOR)
                # label status len(list)
                text_status = Label(mframe3, text ="have "+ str(listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')

        def check_item():
                try :
                        index = int(listbox.curselection()[0])
                        # not done
                        if listbox.itemcget(index, "fg") == "#ffa364":
                                listbox.itemconfig(
                                        listbox.curselection(),
                                        fg='#21130d')
                                # get rid of selection bar
                                listbox.select_clear(0, END)
                        
                        # done
                        listbox.itemconfig(
                                listbox.curselection(),
                                fg='#ffa364')
                        # get rid of selection bar
                        listbox.select_clear(0, END)
                except: pass


        def del_alldone():
                count = 0
                while count < listbox.size():
                        if listbox.itemcget(count, "fg") == '#ffa364':
                                listbox.delete(listbox.index(count))
                        count +=1
                text_status = Label(mframe3, text ="have "+ str(listbox.size()) + " list ")
                text_status.grid(row=0, column=0, sticky='w')


        def donothing():
                filewin = Toplevel(root)
                button = Button(filewin, text="Do nothing button")
                button.pack()

        # messagebox
        def popup():
                messagebox.askyesno("Application","Got it?")

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
        account_menu.add_command(label="Open", command=donothing)
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

        # container: master(frame1)
        mframe1 = Frame(self.master)  
        mframe1.pack(padx=10, fill=BOTH, expand=True)      
        mframe1.columnconfigure(0,weight=1)
        mframe1.rowconfigure(0,weight=1) 

        # label
        acc = Label(mframe1, text ="Guest", font=('Helvetica 11 bold'))
        acc.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # button check
        btn_add = Button(mframe1,text ="check", command=check_item)
        btn_add.grid(row=0, column=1)

        # container: master(frame2)
        mframe2 = Frame(self.master)                                 
        mframe2.pack(padx=10, fill=BOTH, expand=True)  
        mframe2.columnconfigure(0,weight=1)
        mframe2.rowconfigure(0,weight=1)

        # create a listbox widget
        global listbox
        listbox=Listbox(mframe2, 
                        font=list_font,
                        bg='#FFFFFF',
                        bd=0,
                        fg='#21130d',
                        highlightthickness=0,
                        selectbackground='#EB6424',
                        activestyle='none')    
        listbox.grid(row=0,column=0,sticky='nsew')
        # create scrollbar
        scrollbar = Scrollbar(mframe2)
        scrollbar.grid(row=0,column=1,sticky='nsew')
        # set scroll to listbox
        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=listbox.yview)
        #listbox.bind('<<ListboxSelect>>', check_item) #Select click
        listbox.bind('<Double-1>', 
                lambda e: editWindow(self.master)) #double click

        separator = ttk.Separator(self.master, orient='horizontal')
        separator.pack(fill='x')

        # container: master(frame3)
        global mframe3
        mframe3 = Frame(self.master)                                 
        mframe3.pack(padx=10,pady=10, fill=BOTH, expand=True) 
        mframe3.columnconfigure(0,weight=1)
        mframe3.rowconfigure(0,weight=1) 

        # button add
        btn_add = Button(mframe3,text ="+")
        btn_add.bind("<Button>",
                lambda e: addWindow(self.master))
        btn_add.grid(row=0, column=1)

        # list in listbox
        self.list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]
        for item in range(len(self.list)): 
	        listbox.insert(END, self.list[item]) 

        # label status len(list)
        text_status = Label(mframe3, text ="have "+ str(len(self.list)) + " list ")
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
                str_date = date_text
                print(str_date)

                # update count list
                text_status = Label(mframe3, text ="have "+ str(listbox.size()) + " list ")
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
        date_text = cal.get_date()

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
        detail_entry.grid(row=1, sticky='nswe')

        # container: addWindow(frame3)
        frame3 = Frame(self)  
        frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        frame3.columnconfigure(0,weight=1)
        frame3.rowconfigure(0,weight=1)

        # add button
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

        def setTextInput(text, entry):
                entry.delete(0,"end")
                entry.insert(0, text)

        def update_listbox(index, updated_item):
                listbox.delete(listbox.index(index))
                listbox.insert(index, updated_item)

        def edit_list():
                try :
                        index = int(listbox.curselection()[0])
                        print(index)

                        # string to entry
                        value = listbox.get(index)      # text selection form listbox
                        #setTextInput(value, title_entry)
                        # date
                        cal = DateEntry(self, selectmode = 'day',
                                        year = 2020, month = 5,
                                        day = 22)
                        cal.grid(row=0, column=3, padx=10, sticky='w')
                        # detail
                        #setTextInput(value, detail_entry)

                        # string form entry
                        str_title = title_text.get()
                        print(str_title)
                        str_detail = detail_text.get()
                        print(str_detail)
                        str_date = date_text
                        print(str_date)

                        # update_listbox
                        update_listbox(index, str_title)

                        #self.destroy()
                except: pass


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
        date_text = cal.get_date()

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
        detail_entry.grid(row=1, sticky='nswe')

        # container: addWindow(frame3)
        frame3 = Frame(self)  
        frame3.grid(row=2, column=0, columnspan=4, padx=10, pady=10)      
        frame3.columnconfigure(0,weight=1)
        frame3.rowconfigure(0,weight=1)

        # add button
        btn_done = Button(frame3, text ="Done", command=edit_list)
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