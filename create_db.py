import sqlite3
import os 
def create_db():
    #con=sqlite3.connect('clinicd.db')

    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clinicdd.db")
    con = sqlite3.connect(db_path)

    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS xrays(address text,contact text,price text,state text,date text,age text,gender text,name text,cid INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS dental(address text,contact text,price text,state text,date text,age text,gender text,name text,cid INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS implant(cont text,con2 text,con1 text,con text,price text,type text,address text,contact text,date text,age text,gender text,name text,cid INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS press(cont text,con text,price text,type text,address text,contact text,date text,age text,gender text,name text,cid INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

create_db()

