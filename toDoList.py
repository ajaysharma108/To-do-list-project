from tkinter import *
from tkcalendar import *
import datetime
from tkinter import ttk
from tkinter import messagebox
# Create app  window
app = Tk()
app.geometry('800x800')
app.title("To Do List application")
app.config(bg='grey66')
app.resizable(False, False) # Make the window non-
app_frame = Frame(app, bg='cornsilk4',bd=5,cursor="heart",relief=SOLID)
app_frame.place(x=0,y=0,height=70,width=800)
label = Label(app_frame,text='To Do List',bg='cornsilk4',fg='black',font=("Helvetica",30, 'bold'))
label.place(x=300,y=4)
#================Now make entries of our list=====================================

def addTask():
   task =  task_ent.get()
   
   if task !='':
       res_box.insert(END,task)
       task_ent.delete(0,END)
       res_box.itemconfig(END, fg='white')
   else:
       messagebox.showwarning(title='Attention',message='Please enter a Task!!')
      

def removeTask():
    try:
        selectedItem = res_box.curselection()[0]
        res_box.delete(selectedItem)
    except:
        messagebox.showwarning(title='Attention',message='Please select task !!')
   

def view():
    done_count=0
    total_count = res_box.size()
    for i in range(total_count):
        if res_box.itemcget(i,'fg') == 'green':
            done_count += 1
    messagebox.showinfo('Task Statistics',f"Total task: {total_count}\nCompleted task : {done_count} ")

def  markAsDone():
    selectedItems = res_box.curselection()
    if selectedItems:
        res_box.itemconfigure(selectedItems, fg='green')
  

ent_frame = Frame(app,bg='gainsboro',bd=5,relief='ridge')
ent_frame.place(x=5,y=75,height=150,width=790)
ent_label = Label(ent_frame,text='Please enter details',bg='grey',
                  font=('times',15,'bold'),fg='white')

##============================================================================
task = Label(ent_frame,text='Enter your task: ',bg='gainsboro',
             font=('arial',    12,'bold'))
task.place(x=50,y=47)

task_ent = Entry(ent_frame,bg='white',width=50,relief=FLAT,highlightthickness=0,font=('arial',10,'bold'),bd=5)
task_ent.insert(0,"Type here...")
task_ent.config(font=("Arial",14))
task_ent.bind('<FocusIn>' ,lambda e: task_ent.delete('0','end') )
task_ent.place(x=200,y=44)
#=============================================================================
add_btn = Button(ent_frame,text="Add",bg='green',fg='white',padx=2,pady=2,command=addTask)
add_btn.place(x=70,y=95,height=35,width=75)

delete_btn = Button(ent_frame,text="Delete",bg='red',fg='white',padx=2,pady=2,command=removeTask)
delete_btn.place(x=680,y=95,height=35,width=75)

done = Button(ent_frame,text="Done",bg='orange',fg='white',padx=2,pady=2,command=markAsDone)
done.place(x=250,y=95,height=35,width=75)

view = Button(ent_frame,text="View status",bg='orange',fg='white',padx=2,pady=2,command=view)
view.place(x=470,y=95,height=35,width=75)
##===============frame for showing task result=====================================
res_box = Listbox(app,bg='dark sea green',bd=5,relief='sunken',font=('arial',12),selectbackground='blue')
res_box.place(x =5,y=225,height=790,width=790)

scroll = Scrollbar(res_box)
scroll.pack(side=RIGHT,fill=Y)


res_box.config(yscrollcommand=scroll.set)
scroll.config(command=res_box.yview)
# ##
# ==============================Now make functions =============================


app.mainloop()