from collections import*
from tkinter import*
from tkinter import ttk
from tkinter.ttk import*
from tkinter import messagebox
w = Tk()
w.geometry('600x400')
w.title('دفترچه تلفن')
w.config(bg='pink')
w.config(cursor='hand2')
## exchange , hand1 , hand2 ,dot,...
#w.withdraw()          مخفي کردن پنجره
icon=PhotoImage(file='icon.png')
w.iconphoto(True,icon)

#توابع
##def messag_box():
    


# واسه فريم 3تابع اضافه کردن
def show_add_form():
    w = Tk()
#فريم ها 
    lf=Frame(w)
    lf.pack(side=LEFT, padx=20,pady=5)
    rf=Frame(w)
    rf.pack(side=LEFT, padx=20,pady=5)
    fnf=Frame(lf)
    fnf.pack(side=TOP, padx=20,pady=5)
    lnf=Frame(lf)
    lnf.pack(side=TOP, padx=20,pady=5)
    mf=Frame(lf)
    mf.pack(side=LEFT, padx=20,pady=5)

    global a11
    global a33
    global a55
    a11=StringVar(fnf)
    a33=StringVar(fnf)
    a55=StringVar(fnf)
    
    a=Label(fnf,text="اسم",font=('arial', 15, 'bold'))
    a.pack(side=LEFT )
    a1=Entry(fnf,textvariable=a11)
    a1.pack(side=LEFT)
    a2=Label(fnf,text="فاميل",font=('arial', 15, 'bold'))
    
    a2.pack(side=LEFT)
    a3=Entry(fnf,textvariable=a33)
    a3.pack(side=LEFT)
    a4=Label(fnf,text="شماره",font=('arial', 15, 'bold'))
    a4.pack(side=LEFT)
    a5=Entry(fnf,textvariable=a55)
    a5.pack(side=LEFT)
    #
    a6=Button(rf,text="اضافه",command=save)
    a6.pack(side=TOP)           
    w.mainloop()
def show(tree,contacts):
   # for contact in contacts():
        tree.insert('',END,values=(a11.get(),a33.get(),a55.get()))
def save ():
    contact=Contact(a11.get(),a33.get(),a55.get())
    contacts.append(contact)
   # refresh_list(contacts)
##    print (contacts[0].lname)
    show(tree,contact)
    messagebox.showinfo('افزودن مخاطب',' :) مخاطب شما با موفقيت افزوده شد ')
def filter_contacts():
    result=[]
    for c in range (len(contacts)):
        print(4)
        if c.fname==ss.get() :
            result.append(c)
    print(result)
    return result
def delete_form():
    messagebox.showwarning('حذف','آيا از حذف مخاطب اطمينان داريد ؟')
    selected_item = tree.selection()[0] ## بدست آوردن آيتم انتخاب شده
    tree.delete(selected_item)
def edit_form():
    curr = tree.focus()
    print(tree[curr])
   # if '' == curr: return

    #    treeView.delete(curr)
   # selected_item = tree.selection()['values']
    #tree1.item(selected_item)['values']
    #x = tree.get_children()
 #   print(selected_item)


#فريم 1(جستجو)
search = Frame(w)
search.pack(side = TOP, padx=20,pady=20)
ss=StringVar(search)
s1=Entry(search,textvariable=ss)
s1.pack(side = LEFT)
s2=Button(search,text="search",command=filter_contacts)
s2.pack(side=LEFT)
#فريم2(مخاطبين)
liste = Frame(w)
'''st=ttk.Style()
st.configure("mystyle",font=('Calibri',15,'bold'))
'''
liste.pack(side=TOP, padx=20,pady=20)
tree=Treeview(liste,columns=('fname','lname','mobile'))

tree.column('#0',width=0)
#tree.column('#0',width=0,style="mystyle")
tree.heading('fname',text='First Name')
tree.heading('lname',text='Last name')
tree.heading('mobile',text='phone')

tree.config(height=10)
#tree.config(width=25)

Contact=namedtuple("Contact","fname lname mobile")

contacts = []

#show(tree,contacts)
tree.pack()

#فريم3
addition=Frame(w)
addition.pack(side=TOP, padx=20,pady=20)
a1=Button(addition,text="addition",command=show_add_form)
a1.pack(side=LEFT)
a2=Button(addition,text="Delete",command=delete_form)
a2.pack(side=LEFT)
a3=Button(addition,text="Edit",command=edit_form)
##a3.fg='black')
a3.pack(side=LEFT)
#



w.mainloop()

#https://www.aparat.com/v/0P83w
