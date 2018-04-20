from tkinter import *
root=Tk()
count=0
def addrec():
    f=open('opendb.txt','a')
    name=s1.get()
    age=s2.get()
    dob=s3.get()
    salary=s4.get()
    yoe=s5.get()
    f.writelines(name.ljust(20)+age.ljust(10)+dob.ljust(30)+salary.ljust(15)+yoe.ljust(15)+"\n")
    f.close()
def nextrec():
    i=0
    f=open('opendb.txt','r')
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    count=count+1
    f.close()
def prev():
    f=open('opendb.txt','r')
    i=0
    global count
    count=count-1
    while(i<=count-1):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    
    f.close()  
def update():
    name=s1.get()
    age=s2.get()
    dob=s3.get()
    salary=s4.get()
    yoe=s5.get()
    f=open("opendb.txt","r")
    h=f.readlines()
    f.close()
    f=open("opendb.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=name):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
        else :
            f.writelines(name.ljust(20)+age.ljust(10)+dob.ljust(30)+salary.ljust(15)+yoe.ljust(15)+"\n")
            flag=1
    f.close()
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("opendb.txt","r")
    h=f.readlines()
    f.close()
    f=open("opendb.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
    f.close()
def search():
    k=s1.get()
    f=open("opendb.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
def lr():
    
    f=open('opendb.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[a-1].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
def fr():
    f=open('opendb.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    l1=l[0].split()
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l0=Label(root,text="MNC")
l1=Label(root,text="Name")
l2=Label(root,text="Age")
l3=Label(root,text="DOB")
l4=Label(root,text="Salary")
l5=Label(root,text="Years of Experience")
t1=Entry(root,textvariable=s1)
t2=Entry(root,textvariable=s2)
t3=Entry(root,textvariable=s3)
t4=Entry(root,textvariable=s4)
t5=Entry(root,textvariable=s5)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1=Button(root,text="Next", command=nextrec)
b2=Button(root,text="Add", command=addrec)
b3=Button(root,text="Delete", command=delete)
b4=Button(root,text="Search", command=search)
b5=Button(root,text="Update", command=update)
b7=Button(root,text="Last Record", command=lr)
b6=Button(root,text="First Record", command=fr)
b8=Button(root,text="Previous", command=prev)
b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=1)
b7.grid(row=7,column=2)
b8.grid(row=7,column=3)
root.mainloop()
