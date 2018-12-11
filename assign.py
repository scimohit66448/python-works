#ques6
f2=open(input(),'w')
tf=1
with open(input()) as f:
      while True:
        c = f.read(1)
        if c.isdigit()==True:
            c='('+c+')'
        if tf==1:
            c=c.upper()
            tf=0
        if c=='.':
              tf=1
        if not c:
            break
        f2.write(c)
f2.close()
#ques5
with open(input(),'r+') as  f:
    with open(input(),'r+') as f1:
        a=f.read()
        f.seek(0)
        b=f1.read()
        f1.seek(0)
        f.write(b)
        f1.write(a)
#ques4
f2=open(input(),'w')
tf=1
with open(input()) as f:
      while True:
        c = f.read(1)
        c=c.upper()
        if c=='.':
              c=','
        if not c:
            break
        f2.write(c)
f2.close()
#ques1
with open(input(),'r') as f1:
    with open(input(),'w') as f2:
        f2.write(f1.read().upper())
#ques2
import sys
with open(sys.argv[1]) as f:
	with open(sys.argv[2])as f2:
		with open(sys.argv[3],'w') as f3:
			f3.write(f.read())
			f3.write(f2.read())
#ques3
fname=input('enter the file name :')
t=int(input("1.add new record\n2.delete a record\n3.edit a record\n4.dsplay record:"))
if t==1:
    with open(fname,'a')as f:
        f.write(input())
if t==2:
    with open(fname,'r+') as f:
        x=input('record to delete:')
        a=f.read()
        a=a.replace(x,'')
        f.seek(0)
        f.write(a)
        
if t==3:
    with open(fname,'r+') as f:
        x=input('record to delete:')
        a=f.read()
        a=a.replace(x,'')
        f.seek(0)
        f.write(a)
        
if t==4:
    with open(fname) as f:
        print(f.read())
else:
    print('enter valid menu')
        
