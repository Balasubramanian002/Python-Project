from tkinter import *
from tkinter import messagebox
from  tkinter import  ttk
import mysql.connector
import os


global  message;
global name
global contact
global email
global gender
global course
global dept
global user
global password
global cpassw


from PIL import Image, ImageTk

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

def on_ent(e):
    code.delete(0,'end')

def on_lea(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
def logo():
    loc = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\new2.png"))
    label = Label(root1, image = loc,bg='white').place(x=860,y=50)

#def GetValue(event):
    #user=user.get()
    #password=code.get()
    #user.delete(0, END)
    #code.delete(0, END)
    #user.insert(0,select['user'])
    #code.insert(0,select['password'])
def logged():
    root.destroy()

def des():
    root1.destroy()
def reg_des():
    reg_screen.destroy()

def prof():
    global name,fname,age,phone,email
    con=mysql.connector.connect(host="localhost",user="root",password='',database="test9")
    cursor=con.cursor(buffered=True)
    q='select name from new1 where user=%s'
    cursor.execute(q,[user])
    name=cursor.fetchone()
    name=str(name)
    name=name[2:-3:]
    q1='select course from new1 where user=%s'
    cursor.execute(q1,[user])
    course=cursor.fetchone()
    course=str(course)
    course=course[2:-3:]
    q2='select email from new1 where user=%s'
    cursor.execute(q2,[user])
    email=cursor.fetchone()
    email=str(email)
    email=email[2:-3:]
    q3='select contact from new1 where user=%s'
    cursor.execute(q3,[user])
    contact=cursor.fetchone()
    contact=str(contact)
    contact=contact[2:-3:]
    
    
    


    #q1="select name,contact,email,dept,course from new1 where user=%s "
        #cursor.execute(q1,user)
        #d=cursor.fetchall()
        #global name1,contact1,email1,dept1,course1
        #name1=d[0][0]
        #contact1=d[0][1]
        #email1=d[0][2]
        #dept1=d[0][3]
        #course1=d[0][4]
        #print(d)

    con.commit()
    cursor.close()
        #con.close()
        #except Exception as e:
    global root1
    
    #print(e)
    root1=Tk()
    root1.title("dashboard page")
    root1.geometry("1450x920")
    root1.configure(bg="white")
    
    from PIL import Image, ImageTk
        #logo
    #loc = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\new2.png"))
    #img = PhotoImage(file="C:\\Users\\sivam\\AppData\\Local\\Programs\\Python\\Python311\\new2.png")
    #label = Label(root1, image = img,bg='white').place(x=860,y=50)
    #logo()

        #green line
    Label(root1,width="1420",height="1",bg="green",fg="white").place(x=0,y=170)

        #heading
    Label(root1,width="200",text="MY DASHBOARD",font=("Wonderbar",30),bg="white",fg="red").place(x=-1650,y=200)

        #light green frame
    Frame(root1,width=1280,height=680,bg="#C1EFC2").place(x=250,y=300)


        #welcome string
        
    Label(root1,width="200",text="Welcome,  "+name,font=("Times new roman",30),bg="white",fg="black").place(x=-1250,y=300)
            

        #profle pic
    #loc2 = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\forbidden.png"))
    #label = Label(root1, image = loc2,bg='white').place(x=260,y=420)


        #Frame(root1,width=250,height=100,bg="white").place(x=410,y=420)
    Label(root1,width="14",text="Name",font=("Times new roman",25),bg="red",fg="yellow").place(x=300,y=437)
    Label(root1,width="14",text=name,font=("Times new roman",25),bg="white",fg="red").place(x=655,y=437)

        #Label(root1,width="15",bg="white").place(x=598,y=440)
        #course allocation logo
    #loc3 = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\courseall.png"))
    #label = Label(root1, image = loc3,bg='#C1EFC2').place(x=600,y=440)


        #course
    Label(root1,width="14",text="Course",font=("Times new roman",25),bg="red",fg="yellow").place(x=300,y=495)
    Label(root1,width="13",text=course,font=("Times new roman",25),bg="white",fg="red").place(x=655,y=495)

        #mail logo
    #loc4 = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\mailogo.png"))
    #label = Label(root1, image = loc4,bg='#C1EFC2').place(x=600,y=518)


        #email
    Label(root1,width="14",text="Email",font=("Times new roman",25),bg="red",fg="yellow").place(x=300,y=553)
    Label(root1,width="20",text=email,font=("Times new roman",25),bg="white",fg="red").place(x=655,y=553)


        #call logo
    #loc5 = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Desktop\\calllogo.png"))
    #label = Label(root1, image = loc5,bg='#C1EFC2').place(x=600,y=608)


        #phone number
    Label(root1,width="14",text="Phone",font=("Times new roman",25),bg="red",fg="yellow").place(x=300,y=611)
    Label(root1,width="13",text=contact,font=("Times new roman",25),bg="white",fg="red").place(x=655,y=611)

    reg=Button(root1,width=20,text='Logout',font=('arial',20),border=0,bg='orange',cursor='hand2',fg='blue',command=des).place(x=815,y=750)
                        #messagebox.showerror('Error','Invalid username or password')
    #else:
    reg_des
    root1.mainloop()
    
def admin():
    ad=Tk()
    ad.title("Admin page")
    ad.geometry("1450x920")
    ad.configure(bg="white")
    
    
    
def login():
    global user,password
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="test9")
    mycursor=mysqldb.cursor()
    q="use test9"
    mycursor.execute(q)
    user=user.get()
    password=code.get()

    if(user=='admin' and password=='admin'):
        query='select * from new1'
        mycursor.execute(query)
        admin()
        result=mycursor.fetchall()
        for row in result:
            print(row)
    else:
        try:
            query='select * from new1 where user=%s and password=%s'
            mycursor.execute(query,[(user),(password)])
            result=mycursor.fetchall()
            prof()
        except:
            messagebox.showerror("Sorry","Invalid username or password")
    #f   i in result:
        #logged()
        #break;
    
    #except Exception as e:
        #messagebox.showinfo("information", e)
            
    #except Exception as e:
        #print(e,1)
            #messagebox.showerror("Sorry","Database connection failed")
            #return

            
            


       
    
    #chek1="SELECT `user` AND `password` from `new1` where user=%s"
    #mycursor.execute(chek1,(uss,passs))
    #if not mycursor.fetchone():
    #    messagebox.showerror("Erorr","Please Register")
    #else:
        
     #   mycursor.close()
      #  mysqldb.close()
       # messagebox.showinfo("Sucessfull","Welcome,Login sucessful")
       # dash()
    
def dash():
    reg_des()
    login()
    

    #import mysql.connector
   # mysqldb=mysql.connector.connect(host="localhost",user="root",database="test")
    #mycursor=mysqldb.cursor()
    #sele="select * from student"
    #val1=(username,password)
   # s=mycursor.execute(sele,val1)
    #mysqldb.commit()
    #print(s)

    #mycursor.close()
    #mysqldb.close()
    
   


def GetValue(event):
    name.delete(0, END)
    contact.delete(0, END)
    email.delete(0, END)
    gender.delete(0, END)
    course.delete(0, END)
    dept.delete(0, END)
    user.delete(0, END)
    password.delete(0, END)
    cpassw.delete(0,END)
    name.insert(0,select['name'])
    contact.insert(0,select['contact'])
    email.insert(0,select['email'])
    gender.insert(0,select['gender'])
    course.insert(0,select['course'])
    dept.insert(0,select['dept'])
    user.insert(0,select['user'])
    password.insert(0,select['password'])

def submit():
    logged()
    global n,c,e,g,c,d,u,p,cp
    n=name.get()
    c=contact.get()
    e=email.get()
    g=gender.get()
    co=course.get()
    d=dept.get()
    u=user.get()
    p=password.get()
    cp=cpassw.get()
    if(p==cp):
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="")
        cursor=mysqldb.cursor()
        try:
            q="create database test9"
            cursor.execute(q)
            
            q1="create table new1(name varchar(20),contact varchar(20),email varchar(20),gender varchar(5),course varchar(20),dept varchar(40),user varchar(40),password varchar(40),primary key(user),unique(user))"
            cursor.execute(q1)
        except :
            try:
                q="use test9"
                cursor.execute(q)
                insert="insert into new1(name,contact,email,gender,course,dept,user,password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                vals = (n,c,e,g,co,d,u,p)
                cursor.execute(insert,vals)
                mysqldb.commit()
                Label(reg_screen, text="Registered successfully..",fg="green",font=('arial',25)).place(x=650,y=820)
                button=Button(reg_screen, text="Profile",bg="orange",fg='blue', command=prof).place(x=700,y=840)
                
                cursor.close()
                mysqldb.close()
                messagebox.showinfo("Sucessfull","Welcome,Register sucessful")
            except Exception as e:
                print(e)
                messagebox.showerror("fail","Connection failed")
    else:
        messagebox.showerror("Password","Password does not match")
            

        
                
            
           
        #else:

           # Label(reg_screen, text="password does not match..",fg="red",font=('arial',25)).place(x=670,y=820)
           # print("password does not match")
           

    #except:
       # print("error")
        
        #import log
        #loginform()
   



def registrationform():
    #loginform.quit()
    global reg_screen
    reg_screen=Tk()
    
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("1450x920")
    #declaring variable
    global  message;
    global name
    global contact
    global email
    global gender
    global course
    global dept
    global user
    global password
    global cpassw
   
    message=StringVar()
   
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="REGISTRATION PAGE",font=('arial',50),bg="orange",fg="white").pack()
    #name Label
    Label(reg_screen, text="Name * ",font=('arial',25)).place(x=600,y=150)
    #name textbox
    name=Entry(reg_screen, width=30)
    name.place(x=785,y=170)
    #contact Label
    Label(reg_screen, text="Contact * ",font=('arial',25)).place(x=600,y=220)
    #contact textbox
    contact=Entry(reg_screen, width=30)
    contact.place(x=785,y=240)

    # email Label
    Label(reg_screen, text="Email * ",font=('arial',25)).place(x=600, y=290)
    # email textbox
   
    email=Entry(reg_screen, width=30)
    email.place(x=785, y=310)

    # gender Label
    Label(reg_screen, text="Gender * ",font=('arial',25)).place(x=600, y=360)
    # gender radiobutton
    gender = ttk.Combobox(reg_screen, width=27)
    gender['values'] = ('Male','Female')
    gender.current()
    gender.place(x=785, y=380)
    # UserName Label
    Label(reg_screen, text="UserName *",font=('arial',25)).place(x=600,y=430)
    # UserName textbox
    user=Entry(reg_screen,width=30)
    user.place(x=785,y=450)
    # password Label
    Label(reg_screen, text="Password *",font=('arial',25)).place(x=600,y=500)
    # password textbox
    password=Entry(reg_screen,width=30)
    password.place(x=785,y=520)
    # confirm password Label
    Label(reg_screen, text="Confirm *",font=('arial',25)).place(x=600,y=570)
    # confirm password textbox
    cpassw=Entry(reg_screen,width=30)
    cpassw.place(x=785,y=590)
    # city Label
    Label(reg_screen, text="Course * ",font=('arial',25)).place(x=600, y=640)
    # city combobox
    course = ttk.Combobox(reg_screen, width=27)
    course['values'] = ('Data Science',
                              'Artificial Intelligence',
                              'Graphic Design',
                              'Cyber Security',
                              'Data Analytics',
                              'Digital Marketing',
                              'Social Media Marketing',
                              'Programming',
                              'Foreign Language',
                              'Web Development',)
    course.current()
    course.place(x=785,y=660)

    # state Label
    Label(reg_screen, text="Dept * ",font=('arial',25)).place(x=600, y=710)
    # state combobox
    dept = ttk.Combobox(reg_screen, width=27)
    dept['values'] = ('CSE','ECE','CIVIL','BIOTECH','BIOMEDICAL','MECH','EEE','AIDS',)
    dept.current()
    dept.place(x=785, y=730)
    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=900,y=600)
    #submit button
    Button(reg_screen, text="Submit",font=('arial',15), width=10, height=0, bg="orange",command=submit).place(x=700,y=780)
    reg_screen.mainloop()
   
   

def loginform():
   
    global root
    
    root=Tk()
    root.title('Login')
    root.geometry('1450x920')
    root.configure(bg="#fff")

    global user
    global code  
    global message;
    message=StringVar()
    user=StringVar()
    code=StringVar()
    
    Label(root,width="250", text="Online Course Reservation System",font=('WonderBar',45), bg="white",fg="green").pack()
    #image
    
    loc = ImageTk.PhotoImage(Image.open("C:\\Users\\sivam\\Downloads\\login.png"))
    label = Label(root, image = loc,bg='white').place(x=150,y=250)
    frame=Frame(root,width=600,height=600,bg="white")
    frame.place(x=820,y=310)
    heading=Label(frame,text='Sign in',fg='#c20078',bg='white',font=('Times new Roman',40,'bold'))
    heading.place(x=130,y=5)

    #username
    user=Entry(frame,textvariable=user,width=30,fg='#f783ac',border=0,bg="white",font=('Microsoft YaHei UI Light',25))
    
    user.place(x=30,y=135)
   
    user.insert(0,'username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=400,height=2,bg="#384B7A").place(x=25,y=180)


    #password
    code=Entry(frame,textvariable=code,width=30,fg='#f783ac',border=0,bg="white",font=('Microsoft YaHei UI Light',25))
    code.place(x=30,y=225)
    code.insert(0,'password')
    code.bind('<FocusIn>',on_ent)
    code.bind('<FocusOut>',on_lea)
    Frame(frame,width=400,height=2,bg="#384B7A").place(x=25,y=265)
    

    #Button
    Button(frame,width=39,pady=8,text='Login in',bg='#1F75FE',fg='white',font=('Microsoft YaHei UI Light',12),border=0,command=login).place(x=66,y=370)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',15))
    label.place(x=77,y=300)

    #label for message
    Label(root, text="",font=('arial',18),bg="white",fg="green",textvariable=message).place(x=1120,y=730)
    

   
    #Register
    reg=Button(frame,width=6,text='Register',font=('arial',10),border=0,bg='white',cursor='hand2',fg='red',command=registrationform)
    reg.place(x=315,y=306)
    root.mainloop()





  


#_---------------------------------------------------------------------------------------------------------------------
"""def openNewWindow():
    
        
    a1= Toplevel()
    sw=a1.winfo_screenwidth()
    sh=a1.winfo_screenheight()
    a1.geometry(f"{sw}x{sh}")    
    a1.title("LOGIN")
    frame=Frame(self.a1,width=f"{sw}",height=f"{sh}",bg="white")
    frame.pack()

    #entry
        
    entry2 = Entry(a1,font="sans-serif 12 bold",show='*',fg="#808080",bg='white',bd=0).place(x=570,y=250)
    limg1=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/wp6715186-indian-emblem-wallpapers.jpg"))
    l0=Label(a1,image=limg1)
    l0.place(x=0,y=0)

    L1 = Label(a1, text="User Name:",fg="white",bg="#808080",font="sans-serif 12 bold")
    L1.place(x=470,y=200)
    L2 = Label(a1, text="Password:",bg="#808080",fg="white",font="sans-serif 12 bold")
    L2.place(x=470,y=250)

    #button
    bimg1=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/icons8-macos-close-15 (1).png"))
    bimg2=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/icons8-macos-minimize-15 (1).png"))
    bimg3=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/icons8-macos-full-screen-15 (1).png")) 
    bimg4=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/icons8-back-arrow-30 (1).png"))
    bimg5=ImageTk.PhotoImage(Image.open("/Users/akash1304/Downloads/icons8-forward-button-30 (1).png"))
        
    
    #Database
    def check():
            global username1,password1
            username1=entry.get()
            password1=entry2.get()
            if username1=='' or password1=='':
                messagebox.showerror("Invalid","Enter all details")
            else:
                try:
                    con=db.connect(host="localhost",user="root",password='',port="3306",database="Passport Automation")
                    cursor=con.cursor()
                    q="SELECT Username AND Password from UserDetail WHERE username=%s AND Password = %s;"
                    cursor.execute(q,(username1,password1))
                        
                    
                except Exception as e:
                    print(e,1)
                    messagebox.showerror("Sorry","Database connection failed")
                    return
                if not cursor.fetchone():
                    messagebox.showerror("Erorr","Please Register")
                else:
                    cursor.close()
                    con.close()
                    messagebox.showinfo("Sucessfull","Welcome,Login sucessful")
                    self.loginpage2()
        

        
     #button
        
        
        b1=Button(self.a1,bd=0,command=check,text=",highlightthickness=0)
        b1.place(x=800,y=220)

        
        


        self.a1.mainloop()"""

    
loginform()

