import mysql.connector
from mysql.connector import Error

while True:
        
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Education',
                                            user='sujan',
                                            password='password')
        
    
        n=int(input("1.Insertion \n2.Search \n3.Display  \nEnter choice:"))
        print()
        if n == 1:
            t1=[]
            t=input("Enter regNo: ")
            t1.append(t)
            t=input("Enter name: ")
            t1.append(t)
            t=input("Enter age:")
            t1.append(t)
            t=input("Enter gender:")
            t1.append(t)
            t=input("Enter community:")
            t1.append(t)
            t=input("Enter mobile No:")
            t1.append(t)
            t=input("Enter email :")
            t1.append(t)
            t=input("Enter cgpa:")
            t1.append(t)
            t2=tuple(t1)
            mySql_insert_query = """INSERT INTO STUDENT(RegNo,Name,Age,Gender,Community,MobileNO,Email,CGPA) 
                                    VALUES 
                                    (%s,%s,%s,%s,%s,%s,%s,%s)

                                """
                                    
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query,t2)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into student table")
            cursor.close()
        elif n==2:
            reg=input("Enter regNo :")
            sql_select_Query = "select * from student where regNo ="+reg+" ;"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                print('Name :',row[1])
                print('Age :',row[2])
                print('Gender :',row[3])
                print('Community :',row[4])
                print('MobileNo :',row[5])
                print('email :',row[6])
                print('CGPA :',row[7],'\n\n')
                print("-----------------------------")
        
        elif n==3:
            sql_select_Query = "select * from student ;"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            for row in records:
                print('Reg No:',row[0])
                print('Name :',row[1])
                print('Age :',row[2])
                print('Gender :',row[3])
                print('Community :',row[4])
                print('MobileNo :',row[5])
                print('email :',row[6])
                print('CGPA :',row[7],'\n\n')
                print("-----------------------------")



        

    except Error as e:
        print("Error while connecting to MySQL",e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    exit=input("Try again? (y/n):")
    if exit not in ['y','Y']:
        break