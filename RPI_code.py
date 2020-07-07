import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import csv
import time

reader=SimpleMFRC522()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
 

f==open('details.csv','r')
reader=csv.reader(f)
e==open('details.csv','r')
read=csv.reader(e)


I="id"
N="Name"
A="Amount"
T="Time"
deatails={}
entry={}

for row in reader:
    details[row[0]]={N:row[1],A:row[2],T:row[3]}


for row in read:
    details[row[0]]={N:row[1],T:row[2]}

def ledon():
    GPIO.output(18,True)
    return

def ledoff():
    GPIO.output(18,False)
    return

def readcard():
    id,mon=reader.read()
    return(id,mon)
def writecard(arr):
    reader.write(arr)
    return

while(True):
    print("Register[1] or pay[2] or reacharge[3] or balance[4]")
    x=int(input())

if(x==1):
    print("How much money do you want to add")
    x=int(input())
    print("place the card")
    id,mon=readcard()
    mon=str(x)
 
    t=time.localtime()
    ct=time.strftime("%H:%M:%S",t)
    name=input("Enter your name")
    details[id]={N:name,A:mon,T:ct}
    writecard(mon)
    print(id)

elif(x==2):
    print("place the card")
    id,mon=readcard()
        
    if id in details:
        mon=int(mon)
        mon=mon-10
        details[id][A]=str(mon)
        writecard(str(mon))
        t=time.localtime()
        ct=time.strftime("%H:%M:%S",t)
        entry[id]={N:details[id][N],T:ct}

    else:
        print("Person not found")

elif(x==3):
    print("place the card")
    id,mon=readcard()
    if id in details:
        print("How much money do you want to add")
        x=int(input())
        mon=int(mon)
        mon=mon+x
        details[id][A]=str(mon)
        writecard(str(mon))
    else:
        print("Person not found")

elif(x==4):
    print("place card")
    id,mon=readcard()
    if id in details:
        print(mon)
    else:
        print("Person not found")

else:
    print("Invalid option")

with open("mycsv.csv",'w',newline='') as f: fieldnames=["id","Name","Amount","Time"]
csv_writer=DictWriter(f,fieldnames=fieldnames)
 
for hi in people: count=people[hi]


count["Name"]=hi
print(count)
csv_writer.writerow(count)
with open("entry.csv",'w',newline='') as f: fieldnames=["id","Name","Time"]
csv_writer=DictWriter(f,fieldnames=fieldnames)


for hi in people:
    count=people[hi]


count["Name"]=hi
print(count)
csv_writer.writerow(count)
