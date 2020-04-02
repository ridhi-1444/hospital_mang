from tkinter import *
from tkinter import messagebox as msg
from PIL import ImageTk,Image
from datetime import datetime as dt
import sqlite3
from scrolling_area import Scrolling_Area, Table
from tkinter import filedialog, PhotoImage
import os
import tkinter.messagebox 
root=Tk()
root.title('HOSPITAL MANAGEMENT SYSTEM')
root.geometry('1366x768')
frame=Frame(root,width=1366,height=768)
frame.place(x=0,y=0)
doc_id=''
#MAIN
def main(root,frame):
    img=ImageTk.PhotoImage(Image.open('E:\programming\hosp mgmt\hospital images\hosp196.jpg'))
    L1=Label(frame,image=img)
    L1.place(x=0,y=0)
    L2=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L2.place(x=0,y=50)
    B1=Button(frame,text='REGISTER',font=('arial',20),fg='white',bg='grey',width=12,bd=10,command=lambda:register(root,frame))
    B1.place(x=950,y=200)

    L3=Label(frame,text='LOGIN AS',font=('arial',30),fg='white',bg='deep sky blue',width=10,bd=10)
    L3.place(x=0,y=200)
    
    img1=ImageTk.PhotoImage(Image.open('hospital images\hosp36.png'))
    L5=Label(frame,image=img1)
    L5.place(x=185,y=400)
    B2=Button(frame,text='ADMIN',font=('arial',20),fg='white',bg='deep sky blue',width=12,bd=10,command=lambda:admin_login(root,frame))
    B2.place(x=150,y=550)

    img2=ImageTk.PhotoImage(Image.open('hospital images\hosp37.png'))
    L4=Label(frame,image=img2)
    L4.place(x=535,y=400)
    B3=Button(frame,text='RECEPTIONIST',font=('arial',20),fg='white',bg='deep sky blue',width=12,bd=10,command=lambda:reception_login(root,frame))
    B3.place(x=500,y=550)

    img3=ImageTk.PhotoImage(Image.open('hospital images\hosp39.png'))
    L5=Label(frame,image=img3)
    L5.place(x=885,y=400)
    B4=Button(frame,text='DOCTOR',font=('arial',20),fg='white',bg='deep sky blue',width=12,bd=10,command=lambda:doctor_login(root,frame))
    B4.place(x=850,y=550)
    frame.mainloop()


#REGISTER
def register(root,frame):
    global picture_file
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)

    conn=sqlite3.connect('myproject_1.db')
    conn.execute('''create table if not exists DOCTORS
            (NAME TEXT  NOT NULL,
            ID TEXT PRIMARY KEY NOT NULL,
            DESIGNATION TEXT,
            SPECIALISATION TEXT,
            MOBILE_NO INT(10),
            EMAIL TEXT,
            PASSWORD TEXT,
            PICTURE BLOB,
            TYPE TEXT,
            FILE_NAME TEXT);''')
    

    def select_file():
        global picture_file
        #conn = create_or_open_db('myproject_1.db')
        picture_file = filedialog.askopenfilename()
        return picture_file
        #insert_picture(conn, picture_file)
        #conn.close()

    def insert_picture(conn, picture_file):
        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base=os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            sql = '''INSERT INTO DOCTORS
            (PICTURE, TYPE, FILE_NAME)
            VALUES(?, ?, ?);'''
            conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
            conn.commit()
            conn.close()
    
    def write(root,frame):
        global picture_file
        txt2=E2.get()
        txt3=E3.get()
        txt4=E4.get()
        txt5=E5.get()
        txt6=E6.get()
        txt7=E7.get()
        txt8=E8.get()
        print(txt2)
        print(txt3)
        print(txt4)
        print(txt5)
        print(txt6)
        print(txt7)
        print(txt8)
        print()
        ans=msg.askquestion('Registration Successful','Do You Want To Proceed')
        if ans=='yes':
            conn=sqlite3.connect('myproject_1.db')
            with open(picture_file, 'rb') as input_file:
                ablob = input_file.read()
                base=os.path.basename(picture_file)
                afile, ext = os.path.splitext(base)
                conn.execute("INSERT INTO DOCTORS (NAME,ID,DESIGNATION,SPECIALISATION,MOBILE_NO,EMAIL,PASSWORD,PICTURE, TYPE, FILE_NAME)\
                VALUES(?,?,?,?,?,?,?,?,?,?);",[txt2,txt3,txt4,txt5,int(txt6),txt7,txt8,sqlite3.Binary(ablob), ext, afile])
                conn.commit()
            
                cursor=conn.execute('select * from DOCTORS')
                for row in cursor:
                    print('NAME=',row[0])
                    print('ID=',row[1])
                    print('DESIGNATION=',row[2])
                    print('SPECIALISATION=',row[3])
                    print('MOBILE_NO=',row[4])
                    print('EMAIL=',row[5])
                    print('PASSWORD=',row[6])
                conn.commit()
                #insert_picture(conn, picture_file)
                conn.close()    
                register(root,frame)
            
    
        else:
            conn.close()    
            register(root,frame)
    
    img=ImageTk.PhotoImage(Image.open('hospital images\HOSP21.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L0=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L0.place(x=0,y=50)

    L1=Label(frame,text="DOCTOR'S REGISTRATION PANEL",font=('arial',30),fg='white',bg='deep sky blue',width=30)
    L1.place(x=0,y=150)

    L2=Label(frame,text='NAME',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L2.place(x=50,y=250)
    E2=Entry(frame,width=30,bd=3,font=('arial',17))
    E2.place(x=300,y=250)

    L3=Label(frame,text='ID',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L3.place(x=50,y=310)
    E3=Entry(frame,width=30,bd=3,font=('arial',17))
    E3.place(x=300,y=310)
    
    L4=Label(frame,text='DESIGNATION',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L4.place(x=50,y=370)
    E4=Entry(frame,width=30,bd=3,font=('arial',17))
    E4.place(x=300,y=370)

    L5=Label(frame,text='SPECIALISATION',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L5.place(x=50,y=430)
    E5=Entry(frame,width=30,bd=3,font=('arial',17))
    E5.place(x=300,y=430)

    L6=Label(frame,text='MOBILE NO.',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L6.place(x=50,y=500)
    E6=Entry(frame,width=30,bd=3,font=('arial',17))
    E6.place(x=300,y=500)

    L7=Label(frame,text='E-MAIL',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L7.place(x=50,y=560)
    E7=Entry(frame,width=30,bd=3,font=('arial',17))
    E7.place(x=300,y=560)

    L8=Label(frame,text='PASSWORD',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L8.place(x=50,y=620)
    E8=Entry(frame,show='*',width=30,bd=3,font=('arial',17))
    E8.place(x=300,y=620)

    B1=Button(frame,text='ATTACH PHOTO',font=('arial',15),fg='white',bg='grey',width=14,bd=15,command=lambda:select_file())
    B1.place(x=900,y=175)

    B2=Button(frame,text='SUBMIT',font=('arial',15),fg='white',bg='grey',width=14,bd=15,command=lambda:write(root,frame))
    B2.place(x=900,y=300)
    
    B3=Button(frame,text='RESET',font=('arial',15),fg='white',bg='grey',width=14,bd=15,command=lambda:register(root,frame))
    B3.place(x=900,y=425)

    B4=Button(frame,text='BACK',font=('arial',15),fg='white',bg='grey',width=14,bd=15,command=lambda:main(root,frame))
    B4.place(x=900,y=550)
    frame.mainloop()

#DOCTOR LOGIN

def after_doctorsuccess(root,frame,doc_id):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\doctor.jpeg'))
    L4=Label(frame,image=img)
    L4.place(x=0,y=0)
    L5=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L5.place(x=0,y=50)
    L6=Label(frame,text="WELCOME TO DOCTOR'S PORTAL",font=('arial',30),fg='white',bg='deep sky blue',width=30)
    L6.place(x=0,y=150)
    B3=Button(frame,text='APPOINTMENTS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda:doc_appointments(root,frame,doc_id))
    B3.place(x=100,y=250)
    B4=Button(frame,text='PATIENT DETAILS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda:doc_pat_details(root,frame))
    B4.place(x=500,y=250)
    B5=Button(frame,text='VIEW REPORTS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15)
    B5.place(x=100,y=400)
    B6=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda:doctor_login(root,frame))
    B6.place(x=500,y=400)
    frame.mainloop()

def doctor_login(root,frame):
    def doctorlogin_success(root,frame):
        txt2=E2.get()
        txt3=E3.get()
        conn=sqlite3.connect('myproject_1.db')
        cursor=conn.execute('Select EMAIL,PASSWORD,ID from DOCTORS')
        for row in cursor:
            if row[0]==txt2 and row[1]==txt3:
                print('Login Successful')
                doc_id=row[2]
                print(doc_id)
                ans=msg.askquestion('Ask Question','Do You Want To Proceed')
                print(ans)
                if ans=='yes':
                    print('yes pressed')
                    conn.close()
                    after_doctorsuccess(root,frame,doc_id)
                else:
                    print('no pressed')
                    conn.close()
                    doctor_login(root,frame)
                
                return doc_id
        else:
            msg.showwarning('Login Failed','Invalid User Name or Password')
            conn.close()
            doctor_login(root,frame)
            
    
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp52.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    L0=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L0.place(x=0,y=50)
    
    L1=Label(frame,text="DOCTOR'S LOGIN PANEL",font=('arial',30),fg='white',bg='deep sky blue',width=25)
    L1.place(x=0,y=200)
    
    L2=Label(frame,text='E-MAIL',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=10)
    L2.place(x=50,y=350)
    L3=Label(frame,text='PASSWORD',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=10)
    L3.place(x=50,y=450)
    E2=Entry(frame,width=25,bd=10,font=('arial',20))
    E2.place(x=350,y=350)
    E3=Entry(frame,show='*',width=25,bd=10,font=('arial',20))
    E3.place(x=350,y=450)
    
    B1=Button(frame,text='LOGIN',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:doctorlogin_success(root,frame))
    B1.place(x=100,y=575)
    B2=Button(frame,text='BACK',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:main(root,frame))
    B2.place(x=400,y=575)
    frame.mainloop()
    
#RECEPTION LOGIN
def after_receptionsuccess(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp58.jpg'))
    L4=Label(frame,image=img)
    L4.place(x=0,y=0)
    L5=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L5.place(x=0,y=50)
    L6=Label(frame,text="WELCOME TO RECEPTIONIST'S PORTAL",font=('arial',30),fg='white',bg='deep sky blue',width=35)
    L6.place(x=0,y=150)
    B3=Button(frame,text='PATIENT REGISTRATION',font=('arial',20),fg='deep sky blue',bg='white',width=22,bd=15,command=lambda:register_1(root,frame))
    B3.place(x=100,y=250)
    B4=Button(frame,text='APPOINTMENTS',font=('arial',20),fg='deep sky blue',bg='white',width=22,bd=15,command=lambda:appointments_details(root,frame))
    B4.place(x=900,y=250)
    B5=Button(frame,text='DOCTOR DETAILS',font=('arial',20),fg='deep sky blue',bg='white',width=22,bd=15,command=lambda:doc_details(root,frame))
    B5.place(x=100,y=510)
    B6=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=22,bd=15,command=lambda: reception_login(root,frame))
    B6.place(x=900,y=510)
    #B7=Button(frame,text='UPDATE APPOINTMENTS',font=('arial',20),fg='deep sky blue',bg='white',width=22,bd=15)
    #B7.place(x=500,y=380)
    frame.mainloop()
def reception_login(root,frame):
    def receptionlogin_success(root,frame):
        txt2=E2.get()
        txt3=E3.get()
        conn=sqlite3.connect('myproject_3.db')
        cursor=conn.execute('Select EMAIL,PASSWORD from RECEPTIONIST')
        for row in cursor:
            if row[0]==txt2 and row[1]==txt3:
                print('Login Successful')
                ans=msg.askquestion('Ask Question','Do You Want To Proceed')
                print(ans)
                if ans=='yes':
                    print('yes pressed')
                    conn.close()
                    after_receptionsuccess(root,frame)
                else:
                    print('no pressed')
                    conn.close()
                    reception_login(root,frame)
                
                return
        else:
            msg.showwarning('Login Failed','Invalid User Name or Password')
            conn.close()
            reception_login(root,frame)
            

    
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp41.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    L0=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L0.place(x=0,y=50)

    L1=Label(frame,text="RECEPTIONIST'S LOGIN PANEL",font=('arial',30),fg='white',bg='deep sky blue',width=28)
    L1.place(x=0,y=200)
    
    L2=Label(frame,text='E-MAIL',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=10)
    L2.place(x=50,y=350)
    L3=Label(frame,text='PASSWORD',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=10)
    L3.place(x=50,y=450)
    E2=Entry(frame,width=20,bd=10,font=('arial',20))
    E2.place(x=350,y=350)
    E3=Entry(frame,show='*',width=20,bd=10,font=('arial',20))
    E3.place(x=350,y=450)
    
    B1=Button(frame,text='LOGIN',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:receptionlogin_success(root,frame))
    B1.place(x=100,y=575)
    B2=Button(frame,text='BACK',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:main(root,frame))
    B2.place(x=400,y=575)
    frame.mainloop()

#ADMIN LOGIN

def after_adminsuccess(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp53.jpg'))
    L4=Label(frame,image=img)
    L4.place(x=0,y=0)
    L5=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L5.place(x=0,y=50)
    L6=Label(frame,text="WELCOME TO ADMIN'S PORTAL",font=('arial',30),fg='white',bg='deep sky blue',width=30)
    L6.place(x=0,y=150)
    B3=Button(frame,text='DOCTOR DETAILS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda:admin_doc_details(root,frame))
    B3.place(x=100,y=250)
    B4=Button(frame,text='PATIENT DETAILS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda:admin_appointments_details(root,frame))
    B4.place(x=500,y=400)
    #B5=Button(frame,text='SUBMIT REPORTS',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15)
    #B5.place(x=900,y=400)
    B6=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=18,bd=15,command=lambda: admin_login(root,frame))
    B6.place(x=900,y=550)
    frame.mainloop()

'''def extract_picture(cursor, picture_id):
    sql = ("SELECT PICTURE, TYPE, FILE_NAME FROM DOCTORS WHERE ID = %s"%picture_id)
    #param = {'id': picture_id}
    cursor.execute(sql)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename'''

def extract_picture(cursor, picture_id):
    sql = ("SELECT PICTURE, TYPE, FILE_NAME FROM 'DOCTORS' where ID='%s'"%picture_id)
    #param = {'ID': picture_id}
    x=cursor.execute(sql)
    ablob, ext, afile = x.fetchone()
    filename = afile + ext
    print('her1')
    print(filename)
    with open(filename, 'wb') as output_file:
       output_file.write(ablob)
    return filename
        
def show_img(root,frame,var1):
            frame.destroy()
            frame1=Frame(root, width=2000,height=1000)
            frame1.place(x=0,y=0)
            conn = create_or_open_db('picture_db.db')
            cur = conn.cursor()
            filename = extract_picture(cur,var1)
            print(filename)
            cur.close()
            conn.close()
            
            img=ImageTk.PhotoImage(Image.open(filename))
            #img = PhotoImage(file=filename)
            L1=Label(frame1,image=img)
            L1.place(x=900,y=170)
            #L1.pack()
            frame1.mainloop()
    
def admin_doc_details(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img1=ImageTk.PhotoImage(Image.open('hospital images\HOSP21.jpg'))
    L4=Label(frame,image=img1)
    L4.place(x=0,y=0)
    L5=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L5.place(x=0,y=25)
    L6=Label(frame,text="ENTER DOCTOR'S ID",font=('arial',17),fg='deep sky blue',bg='white',width=20)
    L6.place(x=50,y=150)
    E6=Entry(frame,width=30,bd=3,font=('arial',17))
    E6.place(x=350,y=150)
    
    B6=Button(frame,text='SEARCH',font=('arial',15),fg='white',bg='grey',width=15,bd=5,command=lambda:after_a_d_details(root,frame))
    B6.place(x=800,y=150)

    B7=Button(frame,text='BACK',font=('arial',15),fg='white',bg='grey',width=15,bd=5,command=lambda:after_adminsuccess(root,frame))
    B7.place(x=1000,y=150)

    def after_a_d_details(root,frame):
        txt1=E6.get()
        conn = sqlite3.connect("myproject_1.db")
        cur = conn.cursor()
        cur.execute(" select NAME,ID,DESIGNATION,SPECIALISATION,MOBILE_NO,EMAIL,PICTURE, TYPE, FILE_NAME from DOCTORS where ID = '%s'"%(txt1))
        
        for row in cur:
            name_0=row[0]
            print(name_0)
            id_1=row[1]
            print(id_1)
            desig_2=row[2]
            print(desig_2)
            spec_3=row[3]
            print(spec_3)
            mob_4=row[4]
            print(mob_4)
            email_5=row[5]
            print(email_5)
            
        filename = extract_picture(cur,txt1)
        print(filename)
        img=ImageTk.PhotoImage(Image.open(filename))
        img = PhotoImage(file=filename)
        L1=Label(frame,image=img)
        L1.image=img
        L1.place(x=900,y=370)    

            
        L7=Label(frame,text='NAME',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L7.place(x=50,y=250)

        E7=Entry(frame,width=30,bd=3,font=('arial',17))
        E7.place(x=350,y=250)
        E7.insert(END, str(name_0))
        
        L8=Label(frame,text='ID',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L8.place(x=50,y=310)

        E8=Entry(frame,width=30,bd=3,font=('arial',17))
        E8.place(x=350,y=310)
        E8.insert(END, str(id_1))

        L9=Label(frame,text='DESIGNATION',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L9.place(x=50,y=370)

        E9=Entry(frame,width=30,bd=3,font=('arial',17))
        E9.place(x=350,y=370)
        E9.insert(END, str(desig_2))

        L10=Label(frame,text='SPECIALISATION',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L10.place(x=50,y=430)

        E10=Entry(frame,width=30,bd=3,font=('arial',17))
        E10.place(x=350,y=430)
        E10.insert(END, str(spec_3))

        L11=Label(frame,text='MOBILE NO.',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L11.place(x=50,y=500)

        E11=Entry(frame,width=30,bd=3,font=('arial',17))
        E11.place(x=350,y=500)
        E11.insert(END, str(mob_4))

        L12=Label(frame,text='E-MAIL',font=('arial',17),fg='deep sky blue',bg='white',width=15)
        L12.place(x=50,y=560)

        E12=Entry(frame,width=30,bd=3,font=('arial',17))
        E12.place(x=350,y=560)
        E12.insert(END, str(email_5))

        B8=Button(frame,text='UPDATE',font=('arial',15),fg='white',bg='grey',width=15,bd=5,command=lambda:update_db(root,frame))
        B8.place(x=800,y=600)

        B9=Button(frame,text='DELETE',font=('arial',15),fg='white',bg='grey',width=15,bd=5,command=lambda:delete_db(root,frame))
        B9.place(x=1000,y=600)

        def update_db(root,frame):
            # declaring the variables to update
            var1 = E7.get() #updated name
            var2 = E8.get() #updated id
            var3 = E9.get() #updated designation
            var4 = E10.get() #updated specialisation
            var5 = E11.get() #updated phone
            var6 = E12.get() #updated email

            query = "UPDATE DOCTORS SET NAME=?, ID=?, DESIGNATION=?, SPECIALISATION=?, MOBILE_NO=?, EMAIL=? WHERE ID LIKE ?"
            cur.execute(query, (var1,var2,var3,var4,var5,var6, txt1))
            conn.commit()
            tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

        def delete_db(root,frame):
            # delete the appointment
            cur.execute("DELETE FROM DOCTORS WHERE  ID = '%s'" %(txt1))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Deleted Successfully")
            L7.destroy()
            E7.destroy()
            L8.destroy()
            E8.destroy()
            L9.destroy()
            E9.destroy()
            L10.destroy()
            E10.destroy()
            L11.destroy()
            E11.destroy()
            L12.destroy()
            E12.destroy()
                    
    frame.mainloop()
    
    
def admin_login(root,frame):
    def adminlogin_success(root,frame):
        txt2=E2.get()
        txt3=E3.get()
        conn=sqlite3.connect('myproject_2.db')
        cursor=conn.execute('Select EMAIL,PASSWORD from ADMIN')
        for row in cursor:
            if row[0]==txt2 and row[1]==txt3:
                print('Login Successful')
                ans=msg.askquestion('Ask Question','Do You Want To Proceed')
                print(ans)
                if ans=='yes':
                    print('yes pressed')
                    after_adminsuccess(root,frame)
                else:
                    print('no pressed')
                    admin_login(root,frame)
                conn.close()
                return
        else:
            msg.showwarning('Login Failed','Invalid User Name or Password')
            admin_login(root,frame)
            conn.close()
        
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp40.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    
    L0=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L0.place(x=0,y=50)

    L1=Label(frame,text="ADMIN'S LOGIN PANEL",font=('arial',30),fg='white',bg='deep sky blue',width=25)
    L1.place(x=0,y=200)
    
    L2=Label(frame,text='E-MAIL',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=15)
    L2.place(x=350,y=350)
    L3=Label(frame,text='PASSWORD',font=('arial',20),fg='deep sky blue',bg='white',width=10,bd=15)
    L3.place(x=350,y=450)
    E2=Entry(frame,width=20,bd=15,font=('arial',20))
    E2.place(x=650,y=350)
    E3=Entry(frame,show='*',width=20,bd=15,font=('arial',20))
    E3.place(x=650,y=450)
    
    B1=Button(frame,text='LOGIN',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:adminlogin_success(root,frame))
    B1.place(x=400,y=575)
    B2=Button(frame,text='BACK',font=('arial',20),fg='white',bg='grey',width=12,bd=15,command=lambda:main(root,frame))
    B2.place(x=700,y=575)
    frame.mainloop()


def register_1(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)

    conn=sqlite3.connect('myproject_5.db')
    conn.execute('''create table if not exists PATIENTS
            (DATE TEXT,
            TIME TEXT,
            PID TEXT PRIMARY KEY NOT NULL,
            PNAME TEXT NOT NULL,
            DISEASE TEXT,
            MOBILE_NO INT(10),
            DOCTAR_NAME TEXT,
            DOCTAR_ID TEXT  NOT NULL,
            GENDER TEXT,
            D_O_B TEXT,
            AGE TEXT,
            BD_GROUP TEXT);''')
    def write_1(root,frame):
        txt12=E12.get()
        txt13=E13.get()
        txt14=E14.get()
        txt15=E15.get()
        txt16=E16.get()
        txt17=E17.get()
        txt18=E18.get()
        txt19=E19.get()
        txt20=E20.get()
        txt21=E21.get()
        txt22=E22.get()
        txt23=E23.get()
        print(txt12)
        print(txt13)
        print(txt14)
        print(txt15)
        print(txt16)
        print(txt17)
        print(txt18)
        print(txt19)
        print(txt20)
        print(txt21)
        print(txt22)
        print(txt23)
        print()
        ans=msg.askquestion('Registration Successful','Do You Want To Proceed')
        if ans=='yes':
            conn=sqlite3.connect('myproject_5.db')
            conn.execute("INSERT INTO PATIENTS (DATE,TIME,PID,PNAME,DISEASE,MOBILE_NO,DOCTAR_NAME,DOCTAR_ID,GENDER,D_O_B,AGE,BD_GROUP)\
            VALUES('%s','%s','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s')"%(txt12,txt13,txt14,txt15,txt16,int(txt17),txt18,txt19,txt20,txt21,txt22,txt23))
            cursor1=conn.execute('select * from PATIENTS')
            for row in cursor1:
                print('DATE=',row[0])
                print('APPOINTMENT TIME=',row[1])
                print('ID=',row[2])
                print('NAME=',row[3])
                print('DISEASE=',row[4])
                print('MOBILE_NO=',row[5])
                print('DOCTAR_NAME=',row[6])
                print('DOCTAR_ID=',row[7])
                print('GENDER=',row[8])
                print('D_O_B=',row[9])
                print('AGE=',row[10])
                print('BD_GROUP=',row[11])
            conn.commit()
            conn.close()
            register_1(root,frame)
            
    
        else:
            register_1(root,frame)

    img=ImageTk.PhotoImage(Image.open('hospital images\hosp48.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L10=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L10.place(x=0,y=50)

    L11=Label(frame,text="PATIENT'S REGISTRATION PANEL",font=('arial',30),fg='white',bg='deep sky blue',width=30)
    L11.place(x=0,y=150)
    date=StringVar()
    now=dt.now()
    d=now.strftime('%d-%m-%y')
    date.set(d)
    L12=Label(frame,text='DATE',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L12.place(x=50,y=250)
    E12=Entry(frame,textvariable=date,width=20,bd=3,font=('arial',17))
    E12.place(x=300,y=250)

    L13=Label(frame,text='APPOINTED TIME',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L13.place(x=50,y=305)
    E13=Entry(frame,width=20,bd=3,font=('arial',17))
    E13.place(x=300,y=305)
    
    L14=Label(frame,text='ID',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L14.place(x=50,y=360)
    E14=Entry(frame,width=20,bd=3,font=('arial',17))
    E14.place(x=300,y=360)

    L15=Label(frame,text='NAME',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L15.place(x=620,y=250)
    E15=Entry(frame,width=30,bd=3,font=('arial',17))
    E15.place(x=870,y=250)

    L16=Label(frame,text='PROBLEM',font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L16.place(x=620,y=305)
    E16=Entry(frame,width=30,bd=3,font=('arial',17))
    E16.place(x=870,y=305)

    L17=Label(frame,text="MOBILE NO.",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L17.place(x=50,y=415)
    E17=Entry(frame,width=20,bd=3,font=('arial',17))
    E17.place(x=300,y=415)
    
    L18=Label(frame,text="DOCTOR'S NAME",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L18.place(x=620,y=360)
    E18=Entry(frame,width=30,bd=3,font=('arial',17))
    E18.place(x=870,y=360)

    L19=Label(frame,text="DOCTOR'S ID",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L19.place(x=620,y=415)
    E19=Entry(frame,width=30,bd=3,font=('arial',17))
    E19.place(x=870,y=415)

    L20=Label(frame,text="GENDER",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L20.place(x=50,y=470)
    E20=Entry(frame,width=20,bd=3,font=('arial',17))
    E20.place(x=300,y=470)

    L21=Label(frame,text="D.O.B",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L21.place(x=620,y=470)
    E21=Entry(frame,width=30,bd=3,font=('arial',17))
    E21.place(x=870,y=470)

    L22=Label(frame,text="AGE",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L22.place(x=50,y=525)
    E22=Entry(frame,width=20,bd=3,font=('arial',17))
    E22.place(x=300,y=525)

    L23=Label(frame,text="BLOOD GROUP",font=('arial',17),fg='deep sky blue',bg='white',width=15)
    L23.place(x=620,y=525)
    E23=Entry(frame,width=30,bd=3,font=('arial',17))
    E23.place(x=870,y=525)
    
    B11=Button(frame,text='SUBMIT',font=('arial',17),fg='white',bg='grey',width=15,bd=10,command=lambda:write_1(root,frame))
    B11.place(x=100,y=600)
    
    B12=Button(frame,text='RESET',font=('arial',17),fg='white',bg='grey',width=15,bd=10,command=lambda:register_1(root,frame))
    B12.place(x=500,y=600)

    B13=Button(frame,text='BACK',font=('arial',17),fg='white',bg='grey',width=15,bd=10,command=lambda:after_receptionsuccess(root,frame))
    B13.place(x=900,y=600)
    frame.mainloop()



def doc_details(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('hospital images\hosp60.jpg'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L10=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L10.place(x=0,y=50)

    name = StringVar
    scrolling_area = Scrolling_Area(frame, height=400)
    scrolling_area.place(x=0,y=120)
    
    table = Table(scrolling_area.innerframe,
                  ["ID", "NAME", "DESIGNATION","SPECIALISATION","MOBILE_NO","EMAIL"],
                  column_minwidths=[50, 250, 250,250,250,250],height=650)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)

      
    
    conn = sqlite3.connect("myproject_1.db")
    cur = conn.cursor()
    cur.execute("select ID,NAME,DESIGNATION,SPECIALISATION,MOBILE_NO,EMAIL from DOCTORS ")  

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
    conn.commit()

    B1=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=12,bd=15,command=lambda:after_receptionsuccess(root,frame))
    B1.place(x=900,y=575)
    frame.mainloop()

def appointments_details(root,frame):
    frame.destroy()
    frame=Frame(root, width=2000,height=1500)
    frame.pack()

    img=ImageTk.PhotoImage(Image.open('hospital images\HOSP63.png'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L10=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L10.place(x=0,y=50)
    
    name = StringVar
    scrolling_area = Scrolling_Area(frame, height=400)
    scrolling_area.place(x=0,y=120)
    
    table = Table(scrolling_area.innerframe,
                  ["PID", "NAME", "DOCTOR_ID","APPOINTMENT TIME","APPOINTMENT DATE"],
                  column_minwidths=[250, 300, 250,300,220],height=600)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)

      
    
    conn = sqlite3.connect("myproject_5.db")
    cur = conn.cursor()
    cur.execute("select PID,PNAME,DOCTAR_ID,TIME,DATE from PATIENTS")

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
    conn.commit()

    B1=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=12,bd=15,command=lambda:after_receptionsuccess(root,frame))
    B1.place(x=900,y=575)
    frame.mainloop()
    
def doc_appointments(root,frame,doc_id):
    frame.destroy()
    frame=Frame(root, width=2000,height=1500)
    frame.pack()

    img=ImageTk.PhotoImage(Image.open('hospital images\HOSP63.png'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L10=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L10.place(x=0,y=50)
    print(doc_id)
    
    name = StringVar
    scrolling_area = Scrolling_Area(frame, height=400)
    scrolling_area.place(x=0,y=120)
    
    table = Table(scrolling_area.innerframe,
                  ["DATE","PID", "NAME","APPOINTMENT TIME","MOBILE_NO","PROBLEM"],
                  column_minwidths=[200,120,280,270,170,280],height=600)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)

      
    
    conn = sqlite3.connect("myproject_5.db")
    cur = conn.cursor()
    cur.execute("select DATE,PID,PNAME,TIME,MOBILE_NO,DISEASE from PATIENTS where DOCTAR_ID = '%s'"%(doc_id))

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
    conn.commit()

    B1=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=12,bd=15,command=lambda:after_doctorsuccess(root,frame,doc_id))
    B1.place(x=900,y=575)
    frame.mainloop()


def admin_appointments_details(root,frame):
    frame.destroy()
    frame=Frame(root, width=2000,height=1500)
    frame.pack()

    img=ImageTk.PhotoImage(Image.open('hospital images\HOSP63.png'))
    L=Label(frame,image=img)
    L.place(x=0,y=0)
    L10=Label(frame,text='HOSPITAL MANAGEMENT SYSTEM',font=('arial',40),fg='white',bg='deep sky blue',width=50)
    L10.place(x=0,y=50)
    
    name = StringVar
    scrolling_area = Scrolling_Area(frame, height=400)
    scrolling_area.place(x=0,y=120)
    
    table = Table(scrolling_area.innerframe,
                  ["DATE","TIME","PID","NAME","PROBLEM","MOBILE_NO","DOCTOR_NAME","DOCTOR_ID"],    #DATE,TIME,PID,PNAME,DISEASE,MOBILE_NO,DOCTAR_NAME,DOCTAR_ID
                  column_minwidths=[150,100,100,205,250,200,200,110],height=600)
    table.pack(expand=True, fill=X)

    table.on_change_data(scrolling_area.update_viewport)

      
    
    conn = sqlite3.connect("myproject_5.db")
    cur = conn.cursor()
    cur.execute("select DATE,TIME,PID,PNAME,DISEASE,MOBILE_NO,DOCTAR_NAME,DOCTAR_ID from PATIENTS")

    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
    conn.commit()

    B1=Button(frame,text='BACK',font=('arial',20),fg='deep sky blue',bg='white',width=12,bd=15,command=lambda:after_adminsuccess(root,frame))
    B1.place(x=900,y=575)
    frame.mainloop()






#BACK
def back(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    main(root,frame)
   
    
    
main(root,frame)

