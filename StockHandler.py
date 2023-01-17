from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import datetime
import pymysql
import os


class bill_app:
  def __init__(self,root):
      self.root=root #initialize root
      self.root.geometry("1365x700+0+0")#giving geomtry size of tkinter window frame
      self.root.title("Stock Handler")
      bg_color="SANDYBROWN"
      title=Label(self.root,text="THERMEX ENGINEERS  Stock  Assistant",bd=10,relief=GROOVE,fg="DARKMAGENTA",bg=bg_color,font=("copperplate",30,"bold"),pady=2).pack(fill=X)#adding properties to title block

      #===================================================varaibles======================================================================================
      #==================ITEM & information===================
      self.item=StringVar()
      self.size=StringVar()
      self.hsn=StringVar()
      self.where=StringVar()
      #=================Quantity & information================
      self.added=IntVar()
      self.deduct=IntVar()
      self.quantity=IntVar()
      self.quant=IntVar()
      #================searching vaiable======================
      self.combo_search=StringVar()
      self.search=StringVar()




      #=============================================clock area===========================================================================================

      self.lbl_hr=Label(self.root,font=("lucida bright",50,"bold"),bg="chocolate",fg="darkslategray")
      self.lbl_hr.place(x=0,y=581,relwidth=0.14,relheight=0.12)
      self.lbl_hr2=Label(self.root,text="Hours",font=("lucida bright",25,"bold"),bg="chocolate",fg="darkslategray")
      self.lbl_hr2.place(x=0,y=668,relwidth=0.14,relheight=0.046)


      self.lbl_min=Label(self.root,font=("lucida bright",50,"bold"),bg="goldenrod",fg="royalblue")
      self.lbl_min.place(x=190,y=581,relwidth=0.14,relheight=0.12)
      self.lbl_min2=Label(self.root,text="Minutes",font=("lucida bright",25,"bold"),bg="goldenrod",fg="royalblue")
      self.lbl_min2.place(x=190,y=668,relwidth=0.14,relheight=0.046)



      self.lbl_sec=Label(self.root,font=("lucida bright",50,"bold"),bg="dimgray",fg="lawngreen")
      self.lbl_sec.place(x=381,y=581,relwidth=0.14,relheight=0.12)
      self.lbl_sec2=Label(self.root,text="Seconds",font=("lucida bright",25,"bold"),bg="dimgray",fg="lawngreen")
      self.lbl_sec2.place(x=381,y=668,relwidth=0.14,relheight=0.046)
      self.clock()

      #=================================================ITEM DETAIL FRAME=================================================================================
      F1=LabelFrame(self.root,bd=5,relief=GROOVE,text="Item Details",font=("times new roman",19,"bold"),fg="midnight blue",bg="cyan")
      F1.place(x=0,y=70,relwidth=0.42,relheight=0.36)#item frame in which all is written
      #======Sr. No.=========
      hsn_label=Label(F1,text="Sr. No.",bg="cyan",fg="firebrick",font=("lucida bright",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
      hsn_txt=Entry(F1,textvariable=self.hsn,width=35,font="monaco",bd=4).grid(row=0,column=1,padx=6,pady=5)#hsn entry
      #======item=========
      item_label=Label(F1,text="Particular",bg="cyan",fg="firebrick",font=("lucida bright",14,"bold")).grid(row=1,column=0,padx=20,pady=5)
      item_txt=Entry(F1,textvariable=self.item,width=35,font="monaco",bd=4).grid(row=1,column=1,padx=6,pady=5)#item entry
      #======item=========
      size_label=Label(F1,text="Size",bg="cyan",fg="firebrick",font=("lucida bright",14,"bold")).grid(row=2,column=0,padx=20,pady=5)
      size_txt=Entry(F1,width=35,textvariable=self.size,font="monaco",bd=4).grid(row=2,column=1,padx=6,pady=5)#size entry
      #======location=========
      where_label=Label(F1,text="Location",bg="cyan",fg="firebrick",font=("lucida bright",14,"bold")).grid(row=3,column=0,padx=20,pady=5)
      where_txt=Entry(F1,textvariable=self.where,width=35,font="monaco",bd=4).grid(row=3,column=1,padx=6,pady=5)#location entry
      #======location=========
      qt_label=Label(F1,text="Quantity",bg="cyan",fg="firebrick",font=("lucida bright",14,"bold")).grid(row=4,column=0,padx=20,pady=5)
      qt_txt=Entry(F1,textvariable=self.quantity,width=35,font="monaco",bd=4).grid(row=4,column=1,padx=6,pady=5)#location entry

      #=================================================BUTTON FRAME=================================================================================
      F2=LabelFrame(self.root,bd=5,relief=GROOVE,font=("times new roman",19,"bold"),fg="midnight blue",bg="cyan") #button frame
      F2.place(x=0,y=318,relwidth=0.42,relheight=0.1)#button frame in which button is made
      ADD= Button(F2,command=self.add,text="ADD", fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold",width=11,height=1).grid(row=0,column=1,padx=4,pady=7)
      UPDATE= Button(F2,command=self.update,text="UPDATE", fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold",width=11,height=1).grid(row=0,column=2,padx=5,pady=7)
      DELETE= Button(F2,command=self.delete,text="DELETE", fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold",width=11,height=1).grid(row=0,column=3,padx=4,pady=7)
      clear= Button(F2,command=self.clear,text="CLEAR", fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold",width=11,height=1).grid(row=0,column=4,padx=4,pady=7)

      #===================================================quantity handler frame=====================================================================
      F3=LabelFrame(self.root,bd=5,text="Quantity Handling",relief=GROOVE,font=("times new roman",19,"bold"),fg="midnight blue",bg="cyan") #quantity handler  frame
      F3.place(x=0,y=385,relwidth=0.42,relheight=0.28)#button frame in which button is made
      #======ADD TO STOCK=========
      inc_label=Label(F3,text="Purchased",bg="cyan",fg="darkslategray",font=("lucida bright",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
      inc_txt=Entry(F3,textvariable=self.added,width=15,font="monaco",bd=4).grid(row=0,column=1,padx=6,pady=5)#item entry
      #======DEDUCT FROM STOCK=========
      dec_label=Label(F3,text="Sold",bg="cyan",fg="darkslategray",font=("lucida bright",14,"bold")).grid(row=1,column=0,padx=20,pady=5)
      dec_txt=Entry(F3,textvariable=self.deduct,width=15,font="monaco",bd=4).grid(row=1,column=1,padx=6,pady=5)#size entry
      #======NOW AVAILABLE QUANTITY=========
      qt_label=Label(F3,text="QUANTITY",bg="cyan",fg="darkslategray",font=("lucida bright",17,"bold")).grid(row=2,column=0,padx=20,pady=5)
      qt_txt=Entry(F3,width=15,textvariable=self.quantity,font="arial 15",bd=4).grid(row=2,column=1,padx=6,pady=5)

      submit= Button(F3,command=self.change,text="SUBMIT", fg="beige",bg="cornflowerblue",bd=7,relief=GROOVE,font="arial 12 bold",width=13,height=2).grid(row=1,column=5,padx=34,pady=5)

      #====================================================  search bar handler =========================================================================
      F4=LabelFrame(self.root,bd=4,relief=GROOVE,text="Search Bar",font=("times new roman",19,"bold"),fg="midnight blue",bg="cyan")
      F4.place(x=576,y=70,relwidth=0.59,relheight=0.12)#declaring frame

      search_label=Label(F4,text="Search By",bg="cyan",fg="darkslategray",font=("lucida bright",13,"bold")).grid(row=0,column=0,padx=5,pady=5)

      combo_search=ttk.Combobox(F4,textvariable=self.combo_search,width=10,font=("times new roman",13,"bold"),state="readonly")


      combo_search['values']=("Sr. No.","Particular")#making combobox for searching category


      combo_search.grid(row=0,column=1,padx=2,pady=5)

      srch_label=Label(F4,text="Search:",bg="cyan",fg="darkslategray",font=("lucida bright",13,"bold")).grid(row=0,column=2,padx=15,pady=5)
      srch_txt=Entry(F4,width=29,textvariable=self.search,font="arialnarrow",bd=2).grid(row=0,column=3,padx=3,pady=5)#making search entry place

      search= Button(F4,command=self.search_data,text="SEARCH", fg="beige",bg="cornflowerblue",bd=1,relief=GROOVE,font="arial 12 bold",width=8,height=1).grid(row=0,column=4,padx=2,pady=5)
      show_all= Button(F4,text="SHOW ALL",command=self.fetch_data, fg="beige",bg="cornflowerblue",bd=1,relief=GROOVE,font="arial 11 bold",width=9,height=1).grid(row=0,column=5,padx=3,pady=5)
      #====================================================  stock showing area =========================================================================
      F5=Frame(self.root,bd=4,relief=GROOVE,bg="cyan")
      F5.place(x=576,y=156,relwidth=0.577,relheight=0.777)

      scroll_x=Scrollbar(F5,orient=HORIZONTAL)
      scroll_y=Scrollbar(F5,orient=VERTICAL)#making scroll bars

      self.Stock_Table=ttk.Treeview(F5,columns=("HSN","Particular","Size","Location","Quantity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_x.config(command=self.Stock_Table.xview)
      scroll_y.config(command=self.Stock_Table.yview)

      self.Stock_Table.heading("Particular",text="PARTICULAR")
      self.Stock_Table.heading("HSN",text="Sr. No.")
      
      self.Stock_Table.heading("Size",text="SIZE")
      self.Stock_Table.heading("Location",text="LOCATION")
      self.Stock_Table.heading("Quantity",text="QUANTITY")

      self.Stock_Table['show']="headings"

      self.Stock_Table.column("HSN",width=130)
      self.Stock_Table.column("Size",width=130)
      self.Stock_Table.column("Location",width=130)
      self.Stock_Table.column("Quantity",width=130)

      self.Stock_Table.pack(fill=BOTH,expand=1)
      self.Stock_Table.bind("<ButtonRelease-1>",self.get_cursor)
      self.fetch_data()



  #===========to add data to database==================================
  def add(self):
     if self.item.get()==""or self.hsn.get()=="":
         messagebox.showerror("Error","Please fill the missing Feild!!!!")
     else:
       try:
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into stock1 values(%s,%s,%s,%s,%s)",(self.hsn.get(),self.item.get(),self.size.get(),self.where.get(),self.quantity.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
       except pymysql.err.IntegrityError:
        messagebox.showerror("Error","Can't add new item with same \'Sr. No.\'")
        pass
        
 #==============to fetch data from database & display in showing area=========================
  def fetch_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("select * from stock1")
      rows=cur.fetchall()
      if len(rows)!=0:
          self.Stock_Table.delete(*self.Stock_Table.get_children())
          for row in rows:
              self.Stock_Table.insert('',END,values=row)
          con.commit()
      con.close()
#========================to clear entry fields=============================================
  def clear(self):
        self.item.set("")
        self.size.set("")
        self.hsn.set("")
        self.where.set("")
        self.combo_search.set("")
        self.search.set("")
        self.added.set(0)
        self.deduct.set(0)
        self.quantity.set(0)
#========================to show selected entry from showing area to entry fiels============
  def get_cursor(self,ev):
      cursor_row=self.Stock_Table.focus()
      contents=self.Stock_Table.item(cursor_row)
      row=contents['values']
      
      try:
          self.hsn.set(row[0])
          self.item.set(row[1])
          self.size.set(row[2])
          self.where.set(row[3])
          self.quantity.set(row[4])
      except IndexError:
          pass
#======================update items & other info============================================
  def update(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("update stock1 set Particular=%s,Size=%s,Location=%s,Quantity=%s where HSN=%s",(self.item.get(),self.size.get(),self.where.get(),self.quantity.get(),self.hsn.get()))
      con.commit()
      self.fetch_data()
      self.clear()
      con.close()
#======================change quantity=====================================================
  def change(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      #===========performing calculation======================================
      self.quant=self.quantity.get()+self.added.get()-self.deduct.get()
      self.quantity.set(self.quant)
      #=======================================================================
      cur.execute("update stock1 set Particular=%s,Size=%s,Location=%s,Quantity=%s where HSN=%s",(self.item.get(),self.size.get(),self.where.get(),self.quantity.get(),self.hsn.get()))
      con.commit()
      self.fetch_data()

      con.close()
#========================delete=============================================================
  def delete(self):
       con=pymysql.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       cur.execute("delete from stock1 where HSN=%s",(self.hsn.get()))
       con.commit()
       con.close()
       self.fetch_data()
       self.clear()
#=========================searchbar handler=================================================
  def search_data(self):
      con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      cur=con.cursor()
      cur.execute("select * from stock1 where "+str(self.combo_search.get()) +" LIKE \'%" +str(self.search.get()) +"%\'")
      rows=cur.fetchall()
      if len(rows)!=0:
          self.Stock_Table.delete(*self.Stock_Table.get_children())
          for row in rows:
              self.Stock_Table.insert('',END,values=row)
          con.commit()
      con.close()
#=============================clock working===================================================
  def clock(self):
      h=(time.strftime("%H"))
      m=(time.strftime("%M"))
      s=(time.strftime("%S"))
      if int(h)>12:
          h=str(int(h)-12)
      self.lbl_hr.config(text=h)
      self.lbl_min.config(text=m)
      self.lbl_sec.config(text=s)
      strTime = datetime.datetime.now().strftime("%I:%M:%S")
      hrs=str(strTime[:2])
      minu=str(strTime[3:5])
      self.lbl_hr.after(200,self.clock)

file="D://project/StockManager/xamp/xampp-control.exe"
os.startfile(file)
time.sleep(6)
root=Tk()
obj=bill_app(root)
root.mainloop()
