import mysql.connector 
from mysql.connector import Error

while True:
    try:
        connection=mysql.connector.connect( host='localhost',database='Education',user='sujan',password='password')
        n=int(input("1.insert \t2.search \t3.display \t4.exit"))
        if(n==1):
            lst=[]
            lst.append(input("Enter reg no:"))
            lst.append(input("Enter name :"))
            lst.append(input("Enter age:"))
            lst.append(input("Enter gender:"))
            lst.append(input("Enter community:"))
            lst.append(input("Enter mobile no:"))
            lst.append(input("Enter email:"))
            lst.append(input("Enter cgpa:"))
            t1=tuple(lst)

            query="""insert into STUDENT  (regNo,Name,age,gender,community,mobileNo,email,cgpa) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor=connection.cursor()
            cursor.execute(query,t1)
            connection.commit()
            print('Record inserted')   
        elif(n==2):
            search=input("Enter regno:")
            query="select * from STUDENT where regNo="+search+";"
            cursor=connection.cursor()    
            cursor.execute(query)
            record=cursor.fetchall()
            for row in record:
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                print(row[5])
                print(row[6])
                print(row[7])
        elif(n==3):
            query="select * from STUDENT;"
            cursor=connection.cursor()    
            cursor.execute(query)
            record=cursor.fetchall()
            for row in record:
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                print(row[5])
                print(row[6])
                print(row[7])
        else:
            break
    except Error as e:
        print(e)
    finally:
        if connection.is_connected:
            connection.close()
            cursor.close()

