from tkinter import *
from PIL import Image,ImageTk
import time
import os
import sys

#=========== imports pages ================
from xrays import xraysClass
from dental import dentalClass
from implant import implantClass
from press import pressClass

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




class CLINIC:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1200x650+50+20")
        self.root.resizable(False,False)
        self.root.title("Dental Clinic")
        self.root.config(bg="white")

        f2=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        f2.place(x=1,y=72,width=995,height=577)

        self.Logo=Image.open(resource_path("images/logo.png"))
        self.Logo=self.Logo.resize((995,577))
        self.Logo=ImageTk.PhotoImage(self.Logo)

        lbl1 = Label(f2,image=self.Logo)
        lbl1.place(x=0,y=0,width=995,height=577)

        #=============== title =================
        #title =Label(self.root,text="نظام ادارة عيادة اسنان\t\t Date: DD-MM-YYYY\t Time: HH:MM:SS",compound=LEFT,font=("times new roman",20,"bold") ,bg="#005C78", fg="white", anchor="w", padx=20)
        #title.place(x=0,y=0,relwidth=1,height=70)
        
        
        #=============clock==============
        self.lbl_clock =Label(self.root,text="نظام ادارة عيادة اسنان\t\t\t\t Date: DD-MM-YYYY\t\t\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"), bg="#005C78", fg="white")
        self.lbl_clock.place(x=0,y=0,relwidth=1,height=70)

        #============== frame ==================
        Menuf=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Menuf.place(x=998,y=70,width=200,height=579)

        #============== lable + button ==========
        self.MenuLogo=Image.open(resource_path("images/d.png"))
        self.MenuLogo=self.MenuLogo.resize((200,270))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        lbl_menuLogo=Label(Menuf,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)


        lbl_men=Label(Menuf,text="Menu", font=("times new roman",20),bg="white",
                      fg="#005C78",bd=2,relief=RIDGE).pack(fill=X)
        btn1=Button(Menuf,text="الاشعة",command=self.xrays,
                    font=("times new roman",20,"bold"),
                    bg="#005C78",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn2=Button(Menuf,text="الحجوزات",command=self.dental,font=("times new roman",20,"bold"),bg="#005C78",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn3=Button(Menuf,text="قسم الحشوات",command=self.implant,font=("times new roman",20,"bold"),bg="#005C78",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn4=Button(Menuf,text="زراعة الاسنان",command=self.press,font=("times new roman",20,"bold"),bg="#005C78",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(Menuf,text="Exit",command=root.quit,font=("times new roman",20,"bold"),bg="#005C78",fg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        self.timed()
          
    
    def xrays(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=xraysClass(self.new_win)

    #def xrays(self):
           # self.win = Toplevel()
            #self.newin = xraysClass(self.win)
            #self.root.withdraw()
            #self.win.deiconify()
     
    def dental(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=dentalClass(self.new_win)

    def implant(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=implantClass(self.new_win)
    
    def press(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=pressClass(self.new_win)

    
    def timed(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"نظام ادارة عيادة اسنان\t\t\t\t Date: {str(date_)}\t\t\t\t Time: {str(time_)}")
        self.lbl_clock.after(1000,self.timed)
            
    
    
if __name__=="__main__":

    root=Tk()
    obj=CLINIC(root)
    root.mainloop()        
