import mysql.connector
import os

connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql1234",
        database = "python-db"
    )

os.system('clear') # It cleans the terminal at startup.

def userLogin():
    
    print("Program Login\n-------------")
    username = input("Username : ")
    password = input("Password : ")
    
    cursor = connection.cursor()

    sql = "SELECT * FROM Users WHERE username=%s AND password=%s"
    values = (username,password)

    cursor.execute(sql,values)
    try:
        result = cursor.fetchone()
        if result == None:
            print("You entered your login information incorrectly.! Please try again.\n")
            userLogin()
        elif result[1]==username and result[2]==password:
            menu(username)
    except mysql.connector.Error as err:
        print("error: ", err)
    finally:
        connection.close()

def menu(username):
    os.system('clear')
    print(f"Welcome {username}.\n\nTransaction Options\n-------------------")
    print("1.| Student List\t|")
    print("2.| Add Student\t\t|")
    print("3.| Edit Student\t|")
    print("4.| Delete Student\t|")
    print("5.| Authorized List\t|")
    print("6.| Add Authorized\t|")
    print("7.| Edit Authorized\t|")
    print("8.| Delete Authorized\t|")
    print("9.| Exit\t\t|")
    choice = int(input("\nPlease select the transaction number you want to make : "))

def addUser():

    username = input("Username: ")
    password = input("Password: ")
    auth = input("User Authority / Adminisrator (1), Normal User (2) : ")

    while auth != "1" or auth != "2":
        if auth == "1" or auth == "2":
            break
        auth = input("Wrong choice of authority.! User Authority / Adminisrator (1), Normal User (2) : ")

    cursor = connection.cursor()

    sql = "INSERT INTO Users(username,password,auth) VALUES (%s,%s,%s)"
    values = (username,password,auth)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} user registration added.")
        # print(f"Son eklenen kaydın ID'si : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        # print("Database bağlantısı kapandı.")

# User Login
userLogin()