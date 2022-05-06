from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox


col0 = "#ffffff"
col1 = "#000000"
col2 = "#4456f0"

window = Tk()
window.title("")
window.geometry("485x450")
window.configure(background=col0)
window.resizable(width=False, height=False)

frameup  = Frame(window, width=500, height=50, bg=col2)
frameup.grid(row=0, column=0, padx=0,pady=1)

framed = Frame(window, width=500, height=250, bg=col0)
framed.grid(row=1, column=0, padx=0,pady=1)

framet  = Frame(window, width=500, height=150, bg=col0, relief="flat")
framet.grid(row=2,  column=0, columnspan=2, padx=10,pady=1, sticky=NW)

def show():
    global tree
    listheader = ["Name", "Gender","Telephone","Email"]
    dflist = view()
    
    # [["kene","m","080","qwerty@gmail.comm"]]
    tree = ttk.Treeview(framet, selectmode="extended", column=listheader, show="headings")
    vsb = ttk.Scrollbar(framet,orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(framet,orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0,row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0,row=1, sticky="ew")
    
    tree.heading(0, text="Name", anchor="nw")
    tree.heading(1, text="Gender", anchor="nw")
    tree.heading(2, text="Telephone", anchor="nw")
    tree.heading(3, text="Email", anchor="nw")
    
    tree.column(0,width=100, anchor="nw")
    tree.column(1,width=50, anchor="nw")
    tree.column(2,width=120, anchor="nw")
    tree.column(3,width=180, anchor="nw")

    for item in dflist:
        tree.insert("", "end", values=item)

show()

def insert():
    name = ename.get()
    gender = engender.get()
    telephone = ephone.get()
    email = epemail.get()
    
    data = [name, gender, telephone, email]
    if name == "" or gender == "" or telephone == "" or email == "":
        messagebox.showwarning("data","Please fill in all fields")
    else:
        add(data)
        messagebox.showinfo("data","data added successfuly")
        ename.delete(0, "end")
        engender.delete(0, "end")
        ephone.delete(0, "end")
        epemail.delete(0, "end")
        show()
        
def toupdate():
    try:
        tree_data = tree.focus()
        treedic = tree.item(tree_data)
        treelist = treedic["values"]
        
        name = str(treelist[0])
        gender = str(treelist[1])
        telephone = str(treelist[2])
        email = str(treelist[3])
        
        ename.insert(0, name)
        engender.insert(0, gender)
        ephone.insert(0, telephone)
        epemail.insert(0, email)
        
        def confirm():
            nname = ename.get()
            ngender = engender.get()
            ntelephone = ephone.get()
            nemail = epemail.get()
            
            data = [ntelephone, nname, ngender, ntelephone, nemail]
            
            update(data)
            
            messagebox.showinfo("success", "Update successful")
            
            ename.delete(0, "end")
            engender.delete(0, "end")
            ephone.delete(0, "end")
            epemail.delete(0, "end")
            
            for widget in framet.winfo_children():
                widget.destroy()
            b_confirm.destroy()
            show()
        b_confirm = Button(framed, text="Confirm", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=confirm)
        b_confirm.place(x=290, y =110)
    except IndexError:
        messagebox.showerror("Error", "select one the following")
def toremove():
    try:
        tree_data = tree.focus()
        treedic = tree.item(tree_data)
        treelist = treedic["values"]
        treetele = str(treelist[2])
        
        remove(treetele)
        for widget in framet.winfo_children():
                widget.destroy()  
        show()

    except:
        messagebox.showerror("Error", "select one the following")
def call():
        tree_data = tree.focus()
        treedic = tree.item(tree_data)
        treelist = treedic["values"]
        telephon = treelist[2]
        
        tocall(telephon)
        
        messagebox.showinfo("success", telephon)
def sende():
        tree_data = tree.focus()
        treedic = tree.item(tree_data)
        treelist = treedic["values"]
        email = treelist[3]
        
        tosende(email)
        
        messagebox.showinfo("success", "message sent")
        
    
def tosearch():
    telephone = btnsentry.get()
    data = search(telephone)
    def delete_command():
        tree.delete(*tree.get_children())
    delete_command()
    for item in data:
        tree.insert("","end", values=item)
    btnsentry.delete(0,"end")
appname = Label(frameup, text="PHONE BOOK", height=1, font=('verdana 17 bold '), bg=col2, fg=col0)
appname.place(x=5,y=0)

labname = Label(framed, text="Name", width=5, height=1, font=('ivy 10 '), bg=col2, fg=col0, anchor=NW)
labname.place(x=5,  y=5)

ename = Entry(framed, width=10, relief="solid", highlightthickness=1, justify="left")
ename.place(x=100, y=10)

labgender = Label(framed, text="Gender", width=5, height=1, font=('ivy 10 '), bg=col2, fg=col0, anchor=NW)
labgender.place(x=5,  y=55)

engender = ttk.Combobox(framed, width=10)
engender["values"] = ["", "F", "M"]
engender.place(x=100, y=55)

labphone = Label(framed, text="Phone", width=5, height=1, font=('ivy 10 '), bg=col2, fg=col0, anchor=NW)
labphone.place(x=5,  y=105)

ephone = Entry(framed, width=10, relief="solid", highlightthickness=1, justify="left")
ephone.place(x=100, y=105)

labemail = Label(framed, text="Email", width=5, height=1, font=('ivy 10 '), bg=col2, fg=col0, anchor=NW)
labemail.place(x=5,  y=150)

epemail = Entry(framed, width=10, relief="solid", highlightthickness=1, justify="left")
epemail.place(x=100, y=155)

btnsearch = Button(framed, text="Search", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=tosearch)
btnsearch.place(x=250, y =5)

btnsentry= Entry(framed, width=10, relief="solid", highlightthickness=1, justify="left")
btnsentry.place(x=360, y=5)

btnview = Button(framed, text="View", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=show)
btnview.place(x=250, y =50)

btncall = Button(framed, text="Make call", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=call)
btncall.place(x=250, y =108)

btnsendemail = Button(framed, text="Send email", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=sende)
btnsendemail.place(x=250, y =163)


btnadd = Button(framed, text="Add", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=insert)
btnadd.place(x=370, y =50)

btnupdate= Button(framed, text="Update", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=toupdate)
btnupdate.place(x=370, y =105)

btndelete = Button(framed, text="Delete", width =4, height=1, font=('ivy 8 bold'), bg=col2, fg=col0, command=toremove)
btndelete.place(x=370, y =160)

window.mainloop()