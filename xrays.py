from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class xraysClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("995x550+50+120")
        self.root.title("X-rays")
        self.root.config(bg="white")
        self.root.resizable(False,False)
        
        #========= varibale ================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_age=StringVar()
        self.var_date=StringVar()
        self.var_state=StringVar()
        self.var_price=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()

        #=========searchframe===============
        SearchFrame=LabelFrame(self.root,text="Search X-rays",
                               font=("goudy old style",12,"bold"),bd=2,relief=RIDGE, bg="white")
        SearchFrame.place(x=370,y=20,width=600,height=70)
        
        #=========options===================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,
                                values=("Select","Name","contact"),state='readonly',
                                justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        self.txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,
                              font=("tajwal",15),bg="lightyellow",
                              justify=CENTER).place(x=200,y=10,width=210)
        self.btn_search=Button(SearchFrame,text="Search",command=self.search,
                               font=("goudy old style",15),bg="#005C78",fg="white",
                               cursor="hand2").place(x=420,y=9,width=150,height=30)
        
        #============title=============
        self.title=Label(self.root,text="X-rays Details",font=("goudy old style",15),
                         bg="#005C78",fg="white").place(x=340,y=100,width=645)
        
        #============ photo ===========
        self.Logo=Image.open(resource_path("images/a.png"))
        self.Logo=self.Logo.resize((325,200))
        self.Logo=ImageTk.PhotoImage(self.Logo)

        lbl1 = Label(self.root,image=self.Logo)
        lbl1.place(x=5,y=5,width=325,height=200)

        #============ entry ============

        lbl_name=Label(self.root,text="الاسم",font=("tajwal",15),bg="white").place(x=940,y=145)
        lbl_gender=Label(self.root,text="الجنس",font=("tajwal",15),bg="white").place(x=710,y=150)
        lbl_age=Label(self.root,text="العمر",font=("tajwal",15),bg="white").place(x=500,y=150)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=780,y=150,width=150)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,
                                values=("Select","ذكر","انثى"),state='readonly',
                                justify=CENTER,font=("tajwal",15))
        cmb_gender.place(x=550,y=150,width=150)
        cmb_gender.current(0)
        txt_age=Entry(self.root,textvariable=self.var_age,font=("tajwal",15),
                      bg="lightyellow",justify=CENTER).place(x=350,y=150,width=150)

        lbl_date=Label(self.root,text="التاريخ",font=("tajwal",15),bg="white").place(x=940,y=200)
        lbl_state=Label(self.root,text="الحالة",font=("tajwal",15),bg="white").place(x=710,y=200)
        lbl_price=Label(self.root,text="المبلغ",font=("tajwal",15),bg="white").place(x=500,y=200)
        
        txt_date=Entry(self.root,textvariable=self.var_date,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=780,y=200,width=150)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("tajwal",15),
                        bg="lightyellow",justify=CENTER).place(x=550,y=200,width=150)
        txt_price=Entry(self.root,textvariable=self.var_price,font=("tajwal",15),
                        bg="lightyellow",justify=CENTER).place(x=350,y=200,width=150)
        
        lbl_contact=Label(self.root,text="الهاتف",font=("tajwal",15),bg="white").place(x=940,y=250)
        lbl_address=Label(self.root,text="العنوان",font=("tajwal",15),bg="white").place(x=701,y=250)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("tajwal",15),
                          bg="lightyellow",justify=CENTER).place(x=780,y=250,width=150)
        txt_address=Entry(self.root,textvariable=self.var_address,font=("tajwal",15),
                          bg="lightyellow",justify=CENTER).place(x=350,y=250,width=350)
        
        #================ button ================#005C78  
        btn_add=Button(self.root,text="اضافة",command=self.add,font=("goudy old style",15),
                       bg="#005C78",fg="white",cursor="hand2").place(x=175,y=215,width=155,height=28)
        btn_update=Button(self.root,text="تعديل",command=self.update,font=("goudy old style",15),
                          bg="#005C78",fg="white",cursor="hand2").place(x=5,y=215,width=155,height=28)
        btn_delete=Button(self.root,text="حذف",command=self.delete,font=("goudy old style",15),
                          bg="#005C78",fg="white",cursor="hand2").place(x=5,y=250,width=155,height=28)
        btn_clear=Button(self.root,text="تفريغ",command=self.clear,font=("goudy old style",15),
                         bg="#005C78",fg="white",cursor="hand2").place(x=175,y=250,width=155,height=28)
        
        #===========employee details===========

        xray_frame=Frame(self.root,bd=3,relief=RIDGE)
        xray_frame.place(x=0,y=290,width=995,height=260)

        scrolly=Scrollbar(xray_frame,orient=VERTICAL)
        scrollx=Scrollbar(xray_frame,orient=HORIZONTAL)

        self.XraysTable=ttk.Treeview(xray_frame,columns=("address","contact","price","state","date","age","gender","name","cid"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.XraysTable.xview)
        scrolly.config(command=self.XraysTable.yview)
        
        self.XraysTable.heading("address",text="العنوان")
        self.XraysTable.heading("contact",text="الهاتف")
        self.XraysTable.heading("price",text="المبلغ")
        self.XraysTable.heading("state",text="الحالة")
        self.XraysTable.heading("date",text="التاريخ")
        self.XraysTable.heading("age",text="العمر")
        self.XraysTable.heading("gender",text="الجنس")
        self.XraysTable.heading("name",text="الاسم")
        self.XraysTable.heading("cid",text="التسلسل")
        
        self.XraysTable["show"]="headings"

        self.XraysTable.column("cid",width=20,anchor=NE) # NE => North East
        self.XraysTable.column("name",width=100,anchor=NE)
        self.XraysTable.column("gender",width=40,anchor=NE)
        self.XraysTable.column("age",width=30,anchor=NE)
        self.XraysTable.column("date",width=100,anchor=NE)
        self.XraysTable.column("state",width=100,anchor=NE)
        self.XraysTable.column("price",width=50,anchor=NE)
        self.XraysTable.column("contact",width=100,anchor=NE)
        self.XraysTable.column("address",width=100,anchor=NE)
        self.XraysTable.pack(fill=BOTH,expand=1)
        self.XraysTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def recorder_id(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()

        cur.execute("""
        WITH RECURSIVE cte AS (
            SELECT ROW_NUMBER() OVER (ORDER BY cid) AS new_id, cid
            FROM xrays
        )
        UPDATE xrays
        SET cid = (SELECT new_id FROM cte WHERE cte.cid = xrays.cid)
        """)
        #بعد انشاؤ cte يتم تحديث الجدول xrays 
        #يتم تعيين قيمة xid الى القيمة الجديده new_id المستخرجة من cte
        #يتم مطابقة الصفوف القديمة والجديده باستخدام الشرط where للxid
        con.commit()



    def add(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()
        
        if(self.var_address.get()=="" or self.var_contact.get()=="" or self.var_price.get()=="" or self.var_state.get()=="" or self.var_date.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="" or self.var_name.get()==""):
           messagebox.showerror("Error","Please Enter All The Data.")
        else:
            cur.execute("Insert into xrays (address,contact,price,state,date,age,gender,name) values(?,?,?,?,?,?,?,?)",(
                                        self.var_address.get(),
                                        self.var_contact.get(),
                                        self.var_price.get(),
                                        self.var_state.get(),
                                        self.var_date.get(),
                                        self.var_age.get(),
                                        self.var_gender.get(),
                                        self.var_name.get(),                                
                   ))
            
            messagebox.showinfo("Success","Xrays Add Successfully",parent=self.root)
        con.commit()
        self.recorder_id()
        self.show()
        self.clear()
    

    def show(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()
        try:
            cur.execute("select * from xrays")
            rows=cur.fetchall()# لاعادة جميع الصفوف المسترجعة بشكل قائمة
            self.XraysTable.delete(*self.XraysTable.get_children())
            for row in rows:
                self.XraysTable.insert('',END,values=row)
        except  Exception as ex:
            messagebox.showerror("Error",f"Erorr due to : {str(ex)}",parent=self.root)    
        

    def get_data(self,ev):#ev تمثل حدث مثل نقرة زر او اختيار عنصر
        f=self.XraysTable.focus()#للحصول ع عنصر معين تم تحديده
        content=(self.XraysTable.item(f))#   للحصول ع محتوى الصف المحدد
        row=content['values']#استخراج القيم من الصف باستخدام المفتاح values
        #print(row)
        self.var_address.set(row[0])
        self.var_contact.set(row[1])
        self.var_price.set(row[2])
        self.var_state.set(row[3])
        self.var_date.set(row[4])
        self.var_age.set(row[5])
        self.var_gender.set(row[6])
        self.var_name.set(row[7])
        self.var_id.set(row[8])
    
        
    def update(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()
        cur.execute("Update xrays set address=?,contact=?,price=?,state=?,date=?,age=?,gender=?,name=? where cid=?",(
                                        
                                        self.var_address.get(), 
                                        self.var_contact.get(), 
                                        self.var_price.get(),
                                        self.var_state.get(),
                                        self.var_date.get(),
                                        self.var_age.get(),
                                        self.var_gender.get(),
                                        self.var_name.get(),
                                        self.var_id.get(),
                                               
                    ))
        con.commit()
        self.recorder_id()
        messagebox.showinfo("Success","xrays Update Successfully",parent=self.root)
        self.show() 
        self.clear()

    def delete(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()
        op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
        op==True
        cur.execute("delete from xrays where cid=?",(self.var_id.get(),))
        con.commit()
        self.recorder_id()
        messagebox.showinfo("Delete","xrays Delete Successfully",parent=self.root)
        self.show()
        self.clear() 

    # def delete():
    #     con = sqlite3.connect('clinicd.db')
    #     cur = con.cursor()
    #     op = messagebox.askyesno("confirm","do you want to delete")
    #     if op:  # إذا كان op == True (أي النقر على "Yes")، يتم الحذف
    #         cur.execute("delete from xray where cid=?",(self.var_id.get(),))
    #         con.commit()
    #         self.recorder_id()
    #         messagebox.showinfo("Delete","xrays Delete Successfully",parent=self.root)
    #         self.show()
    #         self.clear()    
                           
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_age.set("")
        self.var_date.set("")
        self.var_state.set("")
        self.var_price.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show() 
    
    def search(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("خطأ","اختر ليتم البحث",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("خطأ","للبحث ادخل القيمة",parent=self.root)
            else:    
                cur.execute("select * from xrays where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                #like تستخدم للبحث عن القيم للنص المدخل
                rows=cur.fetchall()#يسترجع جميع الصفوف الناتجة عن الاستعلام
                if len(rows)!=0:#اذا كانت هناك نتائج
                     self.XraysTable.delete(*self.XraysTable.get_children())
                     #يتم حذف جميع العناصر الحالية في الجدول
                     #ثم يتم ادراج الصفوف الجديده من قاعره البيانات
                     for row in rows:
                         self.XraysTable.insert('',END,values=row)
                else:
                    messagebox.showerror("خطأ","لا يوجد!!!",parent=self.root) 
                    #اذا لم توجد نتائج تظهر رساله لا توجد نتائج        
        except  Exception as ex:
            messagebox.showerror("Erorr",f"Erorr due to : {str(ex)}",parent=self.root)    
            
    
        
if __name__=="__main__":

    root=Tk()
    obj=xraysClass(root)
    root.mainloop()        
    