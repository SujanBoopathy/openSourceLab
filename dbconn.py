import mysql.connector as mysql

conn = mysql.connect(host = "localhost", user = "sujan", password = "password", database = "registry")

print("Connection Established\n" if conn.is_connected() else "Connection Failed\n")

cursor = conn.cursor()

while True:
    choice = int(input("\t1 - INSERT\n\t2 - SELECT\n\t3 - UPDATE\n\t4 - DELETE\n\t5 - EXIT\nChoice: "))

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid Option")
        continue

    if choice == 1:
        sql = "INSERT INTO users(NAME, REG) VALUES(%s, %s)"
        name = str(input("\nEnter Name: "))
        reg = str(input("\nEnter Register: "))
        cursor.execute(sql, (name, reg))
        print("\nNew Row Created")
        conn.commit()
        continue

    if choice == 2:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
        continue

    if choice == 3:
        sql = "UPDATE users SET NAME = %s WHERE REG = %s"
        reg = str(input("\nEnter Register: "))
        name = str(input("\nEnter Name: "))
        cursor.execute(sql, (name, reg))
        print("\nRecord Changed")
        conn.commit()
        continue

    if choice == 4:
        sql = "DELETE FROM users WHERE REG = %s"
        reg = str(input("\nEnter Register: "))
        cursor.execute(sql, (reg, ))
        print("\nRow Deleted")
        conn.commit()
        continue

    if choice == 5:
        break

conn.close()