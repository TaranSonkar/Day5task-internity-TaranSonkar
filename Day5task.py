#DATA HANDLING WITH WRITE A FILE

'''It contains text file data to stroe the data with different approches
file data it can store the some specifice data or minimum amount of data.'''

#Normal file:
# binary files:--unddrstand by only computer
#ex-mp3,img,video file, etc

#text file:- data must be in the form of text data.
#ex- .txt,.py,.java.html,there is no pic and all.

#3 step to perform opretion

#open the file : open()
#read():--to read the data
#read.Line()
#write()-- to write the data
#append the data with the help of write()

#once the opretion is done close the file
#close()

#note : the defult opretion is read()

#mode
# read mode --r
# write mode--w
# append mode--a

#note--to read the data file is mendatory

######################################################################

#Question 1

#write the data and create the file

f=open("C:\\Users\\Taran\\Desktop\\python file\\hii.txt","w")
f.write("hii taran\n")
f.close()
print("opretion success")


#output--opretion success

#create the txt file on your loction and print write statement
#output is hii taran

# #Question 2

#read the data

f=open("C:\\Users\\Taran\\Desktop\\python file\\hii.txt","r")
data=f.read()
print(data)
f.close()
print("success")

#output--hii taran
#success

# #Question 3

#append the data

f=open("C:\\Users\\Taran\\Desktop\\python file\\hii.txt","r")
print(f.read())
f.close()
print("file success")

#output--hii taran
#hii sir 
# how are you 
 #welcome to saurabh sir
#file success

# #Question 4

#readline data

f=open("C:\\Users\\Taran\\Desktop\\python file\\hii.txt","r")
print(f.read(8))
f.close()
print("file success")

#output--hii tara

#file success

#Question 4

#seek the data

f=open("C:\\Users\\Taran\\Desktop\\python file\\hii.txt","r")
print(f.read(8))
f.seek(3)
print(f.read(6))
f.close()

print("success")

#output--hii tara
#taran
#success

#Question 5

#readlines()

f=open("C:\\Users\\Taran\\Desktop\\python file\\new.txt","r")
print(f.read())
print(f.tell())
f.seek(0)
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readlines())
f.close()
print("okay")

#output--hii sir
'''hii sir
hii sir

27
hii sir

9
['hii sir\n', 'hii sir\n', 'hii sir\n']
okay
​'''


#Question 6

try:
    f=open("sample.txt","r")
    data=f.read()
    print(data)
    f.close()
    print("success")
except IO Error as a:
    print('error',a)
print('opretion successfully')

#output--
'''hii good morninggood
success
opretion sucessfully'''

#Question 6

f=open("saurabh.txt","w");
f.write("hello")

print(f)
print(f.name);
print(f.mode);
print(f.closed);
f.close();
print(f.closed)

#output--

'''<_io.TextIOWrapper name='saurabh.txt' mode='w' encoding='cp1252'>
saurabh.txt
w
False
True'''


#Question 7

#overriding

f=open('new.txt','r')
f=open('hi.txt','r')
print(f.read())
f.close()
print('success')

#Question 7

#use tell()

f=open('new.txt','r')
print(f.read())
f.tell()
f.close()
#output--27 #count index

#############################################################################################

#r+--read file
#w+--write file
#a+--append file

#Question 

f=open('saurabh.txt','r+')
print(f.read())
f.close()
print('success')

#Question2

f=open('saurabh.txt','w+')
f.write('welcome to datalove')
f.close()
print('complete')

#Question3

f=open('hii.txt','a+')
f.write('vsics')
f=open('case.txt','a+')
f.write('hii sir')

#read the data old file and copy the new file

#Question

f=open('hii.txt','r')
f2=open('new.txt','w')
for x in f:
    f2.write(x)
f.close()
f2.close()
print('file success')

##########################################################################################################################



#Data Base connectivity

#MySql

#pip install mysql-connector in cmd

#open client window
#enter password

#mysql>
#find connecton id

#mysql>status


import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='your password',database='DB0')

#check connection

print(a.connection_id)

#create Database

#checkdatabase
#mysql>show database

#create database

cur=a.cursor()
cur.execute("CREATE DATABASE DB0")
s='CREATE TABLE BOOK(bookid integer(4),title varchar(20),price float(5,2))'
cur.execute(s)

#mysql>show table
#mysql> desc book

#show table

#inserting data in database

s='INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)'
b=(0,'Python',345)
cur.execute(s,b)
a.commit()#save changes
#mysql>select *from book

# show data

#second method

#creat sql data sheet

import mysql.connector
a=mysql.connector.connect(host='localhost',user='root',password='your password',database='internity')

cur=a.cursor()
cur.execute("select * from student")

for i in cur:
    print(i)

#output is print all in datasent student table

#######################################################################################################

                            #Day5task completed internity -Taran Sonkar
#Date-11/June/2021










