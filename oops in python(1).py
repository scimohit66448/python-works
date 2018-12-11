
# coding: utf-8

# In[1]:


class python_workshp: #define class
    def __init__(self,a,b): #default method to initialisze variables in class 
        self.a=a
        self.b=b
    def display(self): #method in class
        print("hello",self.a,self.b)
c=python_workshp("mohit singh",20) #creating an object of class
c.display() #call a fxn in  class


# In[12]:


class teacher:
    def getsal(self): #fuction to get the salary of the teacher
        self.sal=int(input("enter salary "))
    def display(self): #dispaly as 7th comm
        print("total salary of teacher :Rs",self.sal*.23+self.sal)
c=teacher()
#a=int(input("enter the salary of teacher"))
#c.getsal(a) -> passing salary taken as input 
c.getsal() #calling to take input 
c.display()


# In[41]:


class var:
    y=10 #class variable
    def __init__(self):
        self.x=10
    def modify(self):
        self.x+=1 v#using instance varibale i.e ob.var
        var.y+=1 #using a class varibale -> classname.var_name
    
v1=var()
v2=var()
v1.modify()
print(v1.y,v2.y,v1.x,v2.x)


# In[39]:


from datetime import * #to import datetime function
class computerscience:
    branch="CSE"
    def __init__(self):
        self.regmo=int(input("reg no"))
        self.name=input("name")
        self.dob=input("dob")
        #self.branch=input("branch")
    def display(self):
        today=datetime.today() #for curr date and time
        if today.month<int(self.dob[3:5]): #compute age if month is less tahn current month
                           self.age=today.year-int(self.dob[len(self.dob)-4:])-1
        else:
                           self.age=today.year-int(self.dob[len(self.dob)-4:]) #age if mont is greater than curr month
        print(self.regmo,self.name,computerscience.branch,self.dob,self.age)
    
c1=computerscience()
c2=computerscience()
c3=computerscience()
c4=computerscience()
print("Reg no","Name","Branch","dob","age")
c1.display()
c2.display()
c3.display()
c4.display()


# In[44]:


from datetime import *
today=datetime.today()
print(today)


# In[49]:


from datetime import * #to import datetime function
class computerscience:
    branch="CSE"
    n=0
    def __init(self):
        computerscience.n+=1
    def setdetails(self): #mutator 
        self.regmo=int(input("reg no"))
        self.name=input("name")
        self.dob=input("dob")
        #self.branch=input("branch")
    def getdetails(self): #accessor method
        today=datetime.today() #for curr date and time
        if today.month<int(self.dob[3:5]): #compute age if month is less tahn current month
                           self.age=today.year-int(self.dob[len(self.dob)-4:])-1
        else:
                           self.age=today.year-int(self.dob[len(self.dob)-4:]) #age if mont is greater than curr month
        print(self.regmo,self.name,computerscience.branch,self.dob,self.age,sep="\t")
    @staticmethod
    def y():
        print(computerscience.branch,computerscience.n)
    
c1=computerscience()
c2=computerscience()
c3=computerscience()
c4=computerscience()
#mutator method
c1.setdetails()
c2.setdetails()
c3.setdetails()
c4.setdetails()
print("Reg no","Name","Branch","dob","age",sep="\t")
#acessor method
c1.getdetails()
c2.getdetails()
c3.getdetails()
c4.getdetails()
computerscience.y() #static method 


# In[1]:


print("welcome back")


# In[6]:


class m:
    def getsal(self,sal):
        self.sal=sal
    def display(self):
        print(self.sal)
class k:
   # @staticmethod
    def z(self):
        self.sal+=1000
        self.display()
c1=m()
a=float(input())
c1.getsal(a)
c1.display()
k.z(c1) #passing instance of anoother class to a method of diffrent class 


# In[10]:


class adr:
    def setdetails(self):
        self.name=input("name")
        self.dob=input("dob")
        self.address=input("address")
    def getdata(self):
        print(self.name,self.dob,self.address,sep="\n")
class correction:
    @staticmethod
    def corr(self,a):
        self.address=a
        self.getdata()
c1=adr()
c2=adr()
c1.setdetails()
c2.setdetails()
c1.getdata()
c2.getdata()
b=input("customer name")
a=input("enter correct address")
correction.corr(c1,a)


# In[17]:


class teacher:
    def setid(self):
        self.id=int(input("id"))
    def setname(self):
        self.name=input("name")
    def setdob(self):
        self.dob=input("dob")
    def setaddress(self):
        self.address=input("address")
    def setsalary(self):
        self.salary=float(input("salary"))
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdob(self):
        return self.dob
    def getaddress(self):
        return self.address
    def getsalary(self):
        return self.salary
class student(teacher):
    def getmarks(self):
        self.marks=int(input("marks"))
        def getmarks(self):
            return self.marks
c1=teacher()
c1.setid()
c1.setname()
c1.setsalary()
print(c1.getid(),c1.getname(),c1.getsalary())
c2=student()
c2.setid()
c2.setname()
print(c2.getid,c2.getname())


   
        
   


# In[26]:


class central:
    def __init__(self):
        self.fund=int(input())
    def display(self):
        print(self.fund)
class state(central):
    def __init__(self):
        self.fund=int(input())
c1=central()
c1.display()
c2=state()
c2.display()
sum=(super().fund)+c2.fund
print("total fund of state n central",sum)


# In[38]:


class central:
    def __init__(self,prop):
        self.prop=prop
class state(central):
    def __init__(self,prop1,prop2):
        self.prop1=prop1
        super().__init__(prop2)
class display:
    @staticmethod
    def show(self):
        print("central:",self.prop,"state:",self.prop1,"sum of fund:",self.prop1+self.prop)
c=state(2000,5000)
display.show(c)
        


# # assignment 9 

# In[44]:


class teacher:
    def __init__(self,name,dob,address): #contructor overriding
        self.name=name
        self.dob=dob
        self.adress=address
    def display(self): 
        print("teacher detail->",self.name,self.dob,self.adress)
class student(teacher):
    def __init__(self,name,dob,address):#construcotr overridding
        self.name=name
        self.dob=dob
        self.adress=address
    def display(self): #method overriden
        print("student detail->",self.name,self.dob,self.adress)
c1=teacher("mks","29-09-98","varanasi") #initialization with constructor
c1.display()
c2=student("mohit","27-09-98","varanasi")
c2.display()
   


# In[1]:


class father:
    def height(self):
        print("6.0")
        super().height() #to check whether any further base class
class mother:
    def color(self):
        print("brown")
    def height(self):
        print("5.7")
    #super().height()
class child(father,mother): #multiple inheritence
    pass
c=child()
c.height()
c.color()
child.mro() #method resolution technique to know order of execution


# In[2]:


#example of multiple,multilevel programming along with daimond prblem
class livingbeing:
    def  eat(self):
        print("living bieng:I'm Eating")
        #super().eat()
    def breathe(self):
        print("living being:I'm breating")
       # super().breathe()
class animal(livingbeing): #single inheritence
    def  eat(self):
        print("animal:I'm Eating")
        super().eat()
    def breathe(self):
        print("animal:I'm breating")
        super().breathe()
class reptile(livingbeing):
    def  eat(self):
        print("reptile:I'm Eating")
        super().eat()
    def crawl(self):
        print("repltile:i crawl")
        #super().crawl()
class snake(animal,reptile): #multiple n multilevel inheritence
    def  eat(self):
        print("snake:I'm Eating")
        super().eat()
    def breathe(self):
        print("snake:I'm breating")
        super().breathe()
    def crawl(self):
        print("snake:i crawl")
        super().crawl()
c=snake()
c.eat()
c.breathe()
c.crawl()
snake.mro()
    


# In[7]:


class father:
    def __init__(self):
        self.prop=233000
    def display(self):
        print("father property:",self.prop)
class son(father):
    def __init__(self):
        self.prop1=87000
        super().__init__()    
    def display(self):
        print("child property:",self.prop1)
        super().display()
c=son()
c.display()
        


# In[25]:


class father:
    def __init__(self):
        self.fname=input("father's name ") #initailizing fathers name
        super().__init__()
    def height(self):
        self.h="6.0"
        return self.h
class mother:
    def __init__(self):
        self.mname=input("mother's name ") #initaializing mother's name
    def color(self):
        self.color1="fair"
        return self.color1
class son(father,mother):s
    def __init__(self):
        self.name=input("child name ")
        super().__init__()
        
    def display(self):
        print("father's name:{},mother's name:{},child name:{}\ninherited qualities\ncolor is:{}\nheightis:{}".format(self.fname,self.mname,self.name,super().color(),super().height(),sep="\n"))
c=son()
c.display()


# In[ ]:

#banking software as mini project
from datetime import *
class ICICI:
    ac_no=24000000
    def __init__(self):
        ICICI.interst()
        print("Welcome to ICICI Bank")
    def account_creation(self,cls):
        cls.ac_no+=1
        self.name=input("name of customer ")
        self.dob=input("dob in dd-mm/yyyy ")
        self.adress=input("adress")
        self.account=cls.ac_no
        self.bal=5000
    def ac_bal(self):
        print(self.bal)
    def deposit(self,a):
        xx=int(input("amount"))
        self.bal+=xx
    def withdrwal(self,a):
        w=int(input())
        if self.bal-w>=500:
            self.bal-=w
        else:
            print("not enough bal")
    def display(self):
        print(self.account,self.name,self.bal,self.adress)
    @staticmethod
    def interst(): 
        today=datetime.today()
        if today.day==30:
            if today.month==3:
                self.bal+=self.bal*.045
class HDFC(ICICI):
    ac_no=2800000
    def __init__(self):
        HDFC.interst1()
        print("welcome to HDFC bank")
    def withdrwal(self):
        w=int(input())
        if self.bal-w>=0:
            self.bal-=w
        else:
            print("not enough bal")
    @staticmethod
    def interst1(): 
        today=datetime.today()
        if today.day==30:
            if today.month==3:
                self.bal+=self.bal*.0478
l=[]
while(True):
    print("1. Create Account")
    print("2. Withdraw Money")
    print("3. deposit")
    print("4. Display by AccNo")
   
    ch = int(input("Enter your choice : "))
    if ch == 1:
        a = ICICI()
        l.append(a)
        a.account_creation(ICICI)
    elif ch == 2:
        acc = int(input("Enter account number : "))
        for a in l:
            if a.account == acc:
                a.withdrwal(a)
                break
    elif ch == 3:
        acc = int(input("Enter account number : "))
        for a in l:
            if a.account == acc:
                a.deposit()
    elif ch == 4:
        acc = int(input("Enter account number : "))
        for a in l:
            if a.ac_no == acc:
                a.display()
            print()
    elif ch == 5:
        for a in l:
                a.display()
    else:
        break


        


# In[67]:


class  staff:
       sitting_loc=10
       def availibility(self):
           print(staff.sitting_loc)
class typist(staff):
   def availibilty(self):
       super().avialibility()
class teacher(staff):
   sitting_loc=20
   def availibility(self):
       print(teacher.sitting_loc)
class officer(staff):
   sitting_loc=30
   def availibility(self):
       print(officer.sitting_loc)
c=staff()
c.availibility()
c1=officer()
c1.availibility()
c2=typist()
c2.availibility()
   


# In[ ]:


c=HDFC()
c.account_creation(HDFC)
c.deposit()
c.info()
c.withdrwal()
c.info()
c1=ICICI()
c1.account_creation(ICICI)
c1.deposit()
c1.info()
c1.withdrwal()
c1.info()
l=[]
print("enter 1:create account\n2:check balance\n3:deposit\n4:withdrawl")
a=int(input("enter choice"))
if a==1:
    x=ICICI()
    l.append(x)
    a.account_creation(ICICI)
if a==2:
    for ac in l:
        if 

