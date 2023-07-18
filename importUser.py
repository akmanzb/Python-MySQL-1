import mysql.connector
import os

os.system('clear') # Başlangıçta terminali temizliyor.

def importUser(username,password,auth):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql1234",
        database = "python-db"
    )
    
    cursor = connection.cursor()

    sql = "INSERT INTO Users(username,password,auth) VALUES (%s,%s,%s)"
    values = (username,password,auth)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} kullanıcı kaydı eklendi.")
        # print(f"Son eklenen kaydın ID'si : {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        # print("Database bağlantısı kapandı.")

username = input("Kullanıcı Adı: ")
password = input("Parola: ")
auth = input("Kullanıcı Yetkisi / Adminisrator (1), Normal User (2) : ")

while auth != "1" or auth != "2":
    if auth == "1" or auth == "2":
        importUser(username,password,auth)
        break
    auth = input("Yanlış yetki seçimi.! Kullanıcı Yetkisi / Adminisrator (1), Normal User (2) : ")