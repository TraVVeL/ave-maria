import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_menu " + str(e))
        return []

    def add_product(self, name, description, quick_describe, weight, amount, price, url, filename):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM products WHERE url LIKE '{url}'")
            res = self.__cur.fetchone()

            if res['count'] > 0:
                print("A product with exact same url already exists")
                return False

            tm = math.floor(time.time())

            self.__cur.execute("INSERT INTO products VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (name,
                                description,
                                quick_describe,
                                weight,
                                amount,
                                price,
                                url,
                                filename,
                                tm))

            self.__db.commit()
        except sqlite3.Error as e:
            print("Error adding a product to the DB'\n'error comes from FDataBase | add_product " + str(e))
            return False

        return True

    def get_product(self, alias):
        try:
            self.__cur.execute(f"SELECT id, name, description, quick_describe, weight, amount, price, imgname "
                               f"FROM products WHERE url LIKE '{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_product " + str(e))

        return False, False

    def get_products_announce(self):
        try:
            self.__cur.execute(f"SELECT id, name, description, quick_describe, weight, amount, price, url, imgname "
                               f"FROM products ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_products_announce " + str(e))

        return []

    def add_user(self, name, email, hpsw, customer, phone, mail, receiver,
                 receiver_phone, city, street, building_address, entrance, floor, apartment):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("User with exact same email already exists")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (name, email, hpsw, customer, phone, mail, receiver,
                                receiver_phone, city, street, building_address, entrance, floor, apartment, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | add_user " + str(e))
            return False

        return True

    def get_user(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False

            return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_user " + str(e))

        return False

    def get_user_by_email(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False

            return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_user_by_email " + str(e))

        return False

    def user_autofill(self, user_id, customer, phone, mail, receiver, receiver_phone, city,
                      street, building_address, entrance, floor, apartment):
        try:
            self.__cur.execute(f"UPDATE users SET customer=?, phone=?, mail=?, receiver=?, receiver_phone=?, "
                               f"city=?, street=?, building_address=?, entrance=?, floor=?, "
                               f"apartment=? WHERE id =?",
                               (customer, phone, mail, receiver, receiver_phone, city,
                                street, building_address, entrance, floor, apartment, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | user_autofill " + str(e))
            return False
        return True

    def get_autofill(self, user_id):
        try:
            self.__cur.execute(f"SELECT customer, phone, mail, receiver, receiver_phone, city, "
                               f"street, building_address, entrance, floor, apartment "
                               f"FROM users WHERE id LIKE '{user_id}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Failed")
                return False
            return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_autofill " + str(e))

        return False


    def add_information(self, phone, mail, message, name, surname, color, price, viewed):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO contact VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (phone, mail, message, name, surname, color, price, viewed, tm))

            self.__db.commit()
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | add_information " + str(e))
            return False

        return True

    def get_information(self):
        try:
            self.__cur.execute(f"SELECT * FROM contact ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_information " + str(e))

        return []

    def get_order(self):
        try:
            self.__cur.execute(f"SELECT * FROM orders")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_order " + str(e))

        return []

    def list_user(self):
        try:
            self.__cur.execute(f"SELECT id, name, email FROM users")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from admin.py | user_list  " + str(e))

        return []

    # def user_information(self, name, phone, mail, secondary_name, secondary_phone, city, street, building_address,
    #                      entrance, floor, apartment, deliver, deliver_time, note, delivered, user_id):
    #     tm = math.floor(time.time())
    #     try:
    #         self.__cur.execute("INSERT INTO user_information VALUES"
    #                            "(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                            (name, phone, mail, secondary_name, secondary_phone,
    #                             city, street, building_address, entrance, floor,
    #
    #                             apartment, deliver, deliver_time, note, delivered, user_id, tm))
    #
    #         self.__db.commit()
    #     except sqlite3.Error as e:
    #         print("Error script getting data from DB'\n'error comes from FDataBase | user_information " + str(e))
    #         return False
    #
    #     return True

    def user_order(self, user_id, customer, phone, mail, receiver, receiver_phone, city, street, building_address,
                   entrance, floor, apartment, deliver, deliver_time, note, delivered, product_id, product_count,):
        tm = math.floor(time.time())
        try:
            self.__cur.execute("INSERT INTO user_order VALUES "
                               "(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (user_id, product_id, product_count, customer, phone, mail,
                                receiver, receiver_phone, city, street, building_address,
                                entrance, floor, apartment, deliver, deliver_time,
                                note, delivered, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | product_purchase " + str(e))
            return False
        return True

    def get_user_order(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM user_order WHERE user_id = {user_id} ")
            res = self.__cur.fetchall()
            if not res:
                print("Failed")
                return False
            return res
        except sqlite3.Error as e:
            print("Error script getting data from DB'\n'error comes from FDataBase | get_user_order " + str(e))

        return False
