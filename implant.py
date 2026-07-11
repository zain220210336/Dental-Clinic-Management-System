from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import sys

# import shutil

# # مسار قاعدة البيانات في مجلد التثبيت (مع Inno)
# installed_db_path = os.path.join(os.path.dirname(__file__), "clinicd.db")

# # مسار القاعدة القابل للكتابة
# local_app_folder = os.path.join(os.getenv("LOCALAPPDATA"), "Clinic")
# writable_db_path = os.path.join(local_app_folder, "clinicd.db")

# # إذا لم تكن القاعدة موجودة في LocalAppData، انسخها من المجلد المثبت
# if not os.path.exists(writable_db_path):
#     os.makedirs(local_app_folder, exist_ok=True)
#     shutil.copyfile(installed_db_path, writable_db_path)

# # الآن افتح الاتصال على النسخة القابلة للكتابة
# con = sqlite3.connect(writable_db_path)


# # الحصول على مسار البرنامج
# if getattr(sys, 'frozen', False):
#     # إذا كان البرنامج يعمل كملف EXE
#     program_path = os.path.dirname(sys.executable)
# else:
#     # إذا كان البرنامج يعمل كملف بايثون عادي
#     program_path = os.path.dirname(os.path.abspath(__file__))

# # الآن يمكنك استخدام program_path للوصول إلى الملفات الأخرى
# database_path = os.path.join(program_path, 'database.db')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class implantClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("995x550+50+120")
        self.root.title("Tooth Implant")
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
        self.var_type=StringVar()
        self.var_price=StringVar()
        self.var_contact=StringVar()
        self.var_address=StringVar()
        self.var_con=StringVar()
        self.var_con1=StringVar()
        self.var_con2=StringVar()
        self.var_cont=StringVar()


        #=========searchframe===============
        SearchFrame=LabelFrame(self.root,text="Search",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE, bg="white")
        SearchFrame.place(x=365,y=1,width=600,height=70)
        
        #=========options===================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("tajwal",15),bg="lightyellow",justify=CENTER).place(x=200,y=10,width=210)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#005C78",fg="white",cursor="hand2").place(x=420,y=9,width=150,height=30)
        
        #============title=============
        title=Label(self.root,text=" Tooth Implant Details",
                    font=("goudy old style",15),bg="#005C78",
                    fg="white").place(x=340,y=85,width=645)
        
        #============ photo ===========
        self.Logo=Image.open(resource_path("images/b.png"))
        self.Logo=self.Logo.resize((325,200))
        self.Logo=ImageTk.PhotoImage(self.Logo)

        lbl1 = Label(self.root,image=self.Logo)
        lbl1.place(x=5,y=5,width=325,height=200)
        
        #============ entry ============
        lbl_name=Label(self.root,text="الاسم",font=("tajwal",12,'bold')
                       ,bg="white").place(x=940,y=125)
        lbl_gender=Label(self.root,text="الجنس",font=("tajwal",12,'bold')
                         ,bg="white").place(x=710,y=125)
        lbl_age=Label(self.root,text="العمر",font=("tajwal",12,'bold')
                      ,bg="white").place(x=500,y=125)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=770,y=130,width=150)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","ذكر","انثى"),state='readonly',justify=CENTER,font=("tajwal",15))
        cmb_gender.place(x=540,y=130,width=150)
        cmb_gender.current(0)
        txt_age=Entry(self.root,textvariable=self.var_age,font=("tajwal",15),
                      bg="lightyellow",justify=CENTER).place(x=345,y=130,width=150)
        
        lbl_date=Label(self.root,text="التاريخ",font=("tajwal",12,'bold'),
                       bg="white").place(x=940,y=170)
        lbl_contact=Label(self.root,text="الهاتف",font=("tajwal",12,'bold'),
                          bg="white").place(x=710,y=170)
        lbl_address=Label(self.root,text="العنوان",font=("tajwal",12,'bold'),
                          bg="white").place(x=495,y=170)
        
        txt_date=Entry(self.root,textvariable=self.var_date,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=770,y=175,width=150)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("tajwal",15),
                          bg="lightyellow",justify=CENTER).place(x=540,y=175,width=150)
        txt_address=Entry(self.root,textvariable=self.var_address,font=("tajwal",15),
                          bg="lightyellow",justify=CENTER).place(x=345,y=175,width=150)
        
        lbl_type=Label(self.root,text="نوع الزرعة",font=("arial",12,'bold'),
                       bg="white").place(x=922,y=210)
        lbl_price=Label(self.root,text="المبلغ المفرد",font=("arial",12,'bold'),
                        bg="white").place(x=688,y=210)
        lbl_con=Label(self.root,text="العدد",font=("arial",12,'bold'),
                      bg="white").place(x=500,y=210)
        
        txt_type=Entry(self.root,textvariable=self.var_type,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=770,y=210,width=150)
        txt_price=Entry(self.root,textvariable=self.var_price,font=("tajwal",15),
                        bg="lightyellow",justify=CENTER).place(x=540,y=210,width=150)
        txt_con=Entry(self.root,textvariable=self.var_con,font=("tajwal",15),
                      bg="lightyellow",justify=CENTER).place(x=345,y=210,width=150)

        lbl_con1=Label(self.root,text="قسط اول",font=("arial",12,'bold'),
                       bg="white").place(x=928,y=250)
        lbl_con2=Label(self.root,text="قسط ثاني",font=("arial",12,'bold'),
                       bg="white").place(x=700,y=250)
        lbl_cont=Label(self.root,text="الكلي",font=("arial",12,'bold'),
                       bg="white").place(x=500,y=250)
        
        txt_con1=Entry(self.root,textvariable=self.var_con1,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=770,y=250,width=150)
        txt_con2=Entry(self.root,textvariable=self.var_con2,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=540,y=250,width=150)
        txt_cont=Entry(self.root,textvariable=self.var_cont,font=("tajwal",15),
                       bg="lightyellow",justify=CENTER).place(x=345,y=250,width=150)

        #================ button ================ 
        btn_add=Button(self.root,text="اضافة",command=self.add,font=("goudy old style",15),bg="#005C78",fg="white",cursor="hand2").place(x=175,y=215,width=155,height=28)
        btn_update=Button(self.root,text="تعديل",command=self.update,font=("goudy old style",15),bg="#005C78",fg="white",cursor="hand2").place(x=5,y=215,width=155,height=28)
        btn_delete=Button(self.root,text="حذف",command=self.delete,font=("goudy old style",15),bg="#005C78",fg="white",cursor="hand2").place(x=5,y=250,width=155,height=28)
        btn_clear=Button(self.root,text="تفريغ",command=self.clear,font=("goudy old style",15),bg="#005C78",fg="white",cursor="hand2").place(x=175,y=250,width=155,height=28)
        
        #===========employee details===========

        imp_frame=Frame(self.root,bd=3,relief=RIDGE)
        imp_frame.place(x=0,y=290,relwidth=1,height=260)

        scrolly=Scrollbar(imp_frame,orient=VERTICAL)
        scrollx=Scrollbar(imp_frame,orient=HORIZONTAL)

        self.implantTable=ttk.Treeview(imp_frame,columns=("cont","con2","con1","con","price","type","address","contact","date","age","gender","name","cid"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.implantTable.xview)
        scrolly.config(command=self.implantTable.yview)


        self.implantTable.heading("address",text="العنوان")
        self.implantTable.heading("contact",text="الهاتف")
        self.implantTable.heading("price",text=" المبلغ مفرد")
        self.implantTable.heading("type",text="نوع الزرعة")
        self.implantTable.heading("con",text="العدد")
        self.implantTable.heading("con1",text="القسط الاول")
        self.implantTable.heading("con2",text="القسط ثاني")
        self.implantTable.heading("cont",text="الكلي")
        self.implantTable.heading("date",text="التاريخ")
        self.implantTable.heading("age",text="العمر")
        self.implantTable.heading("gender",text="الجنس")
        self.implantTable.heading("name",text="الاسم")
        self.implantTable.heading("cid",text="التسلسل")
        self.implantTable["show"]="headings"


        self.implantTable.column("cid",width=20,anchor=NE)
        self.implantTable.column("name",width=90,anchor=NE)
        self.implantTable.column("gender",width=30,anchor=NE)
        self.implantTable.column("age",width=30,anchor=NE)
        self.implantTable.column("date",width=50,anchor=NE)
        self.implantTable.column("contact",width=50,anchor=NE)
        self.implantTable.column("address",width=50,anchor=NE)
        self.implantTable.column("type",width=50,anchor=NE)
        self.implantTable.column("price",width=50,anchor=NE)
        self.implantTable.column("con",width=20,anchor=NE)
        self.implantTable.column("con1",width=50,anchor=NE)
        self.implantTable.column("con2",width=50,anchor=NE)
        self.implantTable.column("cont",width=40,anchor=NE)
        self.implantTable.pack(fill=BOTH,expand=1)
        self.implantTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def recorder_id(self,cur):
        con=sqlite3.connect(resource_path('clinicd.db'))

        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        cur.execute("""
        WITH RECURSIVE cte AS (
            SELECT ROW_NUMBER() OVER (ORDER BY cid) AS new_id, cid
            FROM implant
        )
        UPDATE implant
        SET cid = (SELECT new_id FROM cte WHERE cte.cid = implant.cid)
        """)
        con.commit()

    def add(self):
        con=sqlite3.connect(resource_path('clinicd.db'))

        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        if(self.var_cont.get()=="" or self.var_con2.get()=="" or self.var_con1.get()=="" or self.var_con.get()=="" or self.var_price.get()=="" or self.var_type.get()=="" or self.var_address.get()=="" or self.var_contact.get()=="" or self.var_date.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="" or self.var_name.get()==""):
           messagebox.showerror("خطأ","رجاء قم بمليء جميع الحقول")
        else:
            cur.execute("Insert into implant (cont ,con2 ,con1 ,con ,price ,type ,address ,contact ,date ,age ,gender ,name) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_cont.get(),
                                        self.var_con2.get(),
                                        self.var_con1.get(),
                                        self.var_con.get(),
                                        self.var_price.get(),
                                        self.var_type.get(),
                                        self.var_address.get(),
                                        self.var_contact.get(),
                                        self.var_date.get(),
                                        self.var_age.get(),
                                        self.var_gender.get(),
                                        self.var_name.get()
                                        
                    
                    ))            
            messagebox.showinfo("نجح","تم اضافة البيانات بنجاح",parent=self.root)
        con.commit()
        self.recorder_id(cur)
        self.show()
        self.clear()



    def show(self):
        con=sqlite3.connect(resource_path('clinicd.db'))

        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        try:
            cur.execute("select * from implant")
            rows=cur.fetchall()
            self.implantTable.delete(*self.implantTable.get_children())
            for row in rows:
                self.implantTable.insert('',END,values=row)
        except  Exception as ex:
            messagebox.showerror("Error",f"Erorr due to : {str(ex)}",parent=self.root)    



    def get_data(self,ev):
        f=self.implantTable.focus()
        content=(self.implantTable.item(f))
        row=content['values']
        #print(row)
        self.var_cont.set(row[0])
        self.var_con2.set(row[1])
        self.var_con1.set(row[2])
        self.var_con.set(row[3])
        self.var_price.set(row[4])
        self.var_type.set(row[5])
        self.var_address.set(row[6])
        self.var_contact.set(row[7])
        self.var_date.set(row[8])
        self.var_age.set(row[9])
        self.var_gender.set(row[10])
        self.var_name.set(row[11])
        self.var_id.set(row[12])
       

    def update(self):
        con=sqlite3.connect(resource_path('clinicd.db'))

        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        cur.execute("Update implant set cont=? ,con2=? ,con1=? ,con=? ,price=? ,type=? ,address=? ,contact=? ,date=? ,age=? ,gender=? ,name=? where cid=?",(
                                        
                                        self.var_cont.get(),
                                        self.var_con2.get(),
                                        self.var_con1.get(),
                                        self.var_con.get(),
                                        self.var_price.get(),
                                        self.var_type.get(),
                                        self.var_address.get(),
                                        self.var_contact.get(),
                                        self.var_date.get(),
                                        self.var_age.get(),
                                        self.var_gender.get(),
                                        self.var_name.get(),
                                        self.var_id.get(),
                                        
                                         
                    ))
        con.commit()
        self.recorder_id(cur)
        messagebox.showinfo("نجح","تم تحديث البيانات بنجاح",parent=self.root)
        self.show() 
        #self.clear()

    def delete(self):
        con=sqlite3.connect(resource_path('clinicd.db'))

        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        op=messagebox.askyesno("تاكيد","هل حقا تريد الحذف؟",parent=self.root)
        op==True
        cur.execute("delete from implant where cid=?",(self.var_id.get(),))
        con.commit()
        self.recorder_id(cur)
        messagebox.showinfo("حذف","تم الحذف بنجاح",parent=self.root)
        self.show()
        self.clear() 

    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_age.set("")
        self.var_date.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_type.set("")
        self.var_price.set("")
        self.var_con.set("")
        self.var_con1.set("")
        self.var_con2.set("")
        self.var_cont.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()     
    

    def search(self):
        con=sqlite3.connect(resource_path('clinicd.db'))
        #con = sqlite3.connect(writable_db_path)

        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("خطأ","اختر ليتم البحث",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("خطأ","للبحث ادخل القيمة",parent=self.root)
            else:    
                cur.execute("select * from implant where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                     self.implantTable.delete(*self.implantTable.get_children())
                     for row in rows:
                         self.implantTable.insert('',END,values=row)
                else:
                    messagebox.showerror("خطأ","لا يوجد!!!",parent=self.root)         
        except  Exception as ex:
            messagebox.showerror("Erorr",f"Erorr due to : {str(ex)}",parent=self.root)    
            
    
if __name__=="__main__":

    root=Tk()
    obj=implantClass(root)
    root.mainloop()              