import os
from typing import final

import mysql.connector
import bcrypt
from cryptography.fernet import Fernet


class DataBase:

    db = None

    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2137",
                database="paladin"
            )
        except mysql.connector.Error as err:
            print(f"Błąd połączenia z bazą: {err}")
            self.db = None

        self.create_user_table()
        self.create_passwords_table()



    def create_user_table(self):

        with self.db.cursor() as cursor:
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL
                )
                ''')
                self.db.commit()

    def create_passwords_table(self):

        with self.db.cursor() as cursor:
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER NOT NULL,
                service_name VARCHAR(255) UNIQUE NOT NULL,
                password TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
                ''')
                self.db.commit()

    def create_account(self,login,password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt=salt)
        try:
            with self.db.cursor() as cursor:
                print(f"{login} , {hashed}")
                cursor.execute("INSERT INTO users (username, hashed_password) VALUES (%s, %s)",(login, hashed))
                self.db.commit()
                print("Account created successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def try_loging_in(self, login, password):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT hashed_password, id FROM users WHERE username = %s", (login,))
                result = cursor.fetchone()
                if bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                    user_id = result[1]
                    return True, user_id
                else:
                    return False, 0
        except Exception as e:
            print(f"problem z baza")
            return False, 0


    def create_password(self, name, login, password, id):
        key = os.getenv("ENCRYPTION_KEY")
        cipher = Fernet(key.encode())
        encrypted_password = cipher.encrypt(password.encode())
        try:
            with self.db.cursor() as cursor:
                cursor.execute("INSERT INTO passwords (user_id, service_name, password, login)  VALUES(%s, %s, %s, %s)", ( id, name, encrypted_password, login))
                self.db.commit()



        except Exception as e:
            print(e)

    def get_logins(self, id):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT service_name FROM passwords WHERE user_id = %s",(id,))
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"problem z baza")
            return 0



    def get_password(self, id, name):
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT login, password FROM passwords WHERE user_id = %s AND service_name = %s",(id,name))
                result = cursor.fetchall()

            login, encrypted_password = result[0]

            key = os.getenv("ENCRYPTION_KEY")
            cipher = Fernet(key.encode())

            password = cipher.decrypt(encrypted_password.encode()).decode()

            return login, password
        except Exception as e:
            print(f"problem z baza")
            return 0

    def get_database(self):
        return self.db













