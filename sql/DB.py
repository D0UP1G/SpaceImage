import sqlite3

class BD:
    def __init__(self, name):
        self.con = sqlite3.connect(name)
        self.cursor = self.con.cursor()

    def first_user(self,id,username):
        try:
            self.cursor.execute("INSERT INTO Users (id, username) VALUES (?,?)",(id,username))
        except:
            pass
        return self.con.commit()

    def get_user(self,id):
        self.cursor.execute('SELECT * FROM Users WHERE id = ?', (id,))

        return self.cursor.fetchone()
    
    def update_uid(self, uid, id):
        self.cursor.execute('UPDATE Users SET uid = ? WHERE id = ?', (uid,id))
        return self.con.commit()
    
    def add_tourmantes(self, name, description, count, price, photo, admin):
        self.cursor.execute("""INSERT INTO Tournaments
                                  (name, description, count, price, photo, people, verified,admin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (name, description, count, price, photo, '{}', 0, admin))
        return self.con.commit()
    def get_tourmantes(self):
        self.cursor.execute('SELECT * FROM Tournaments WHERE verified = ? ', (0,))
        result = self.cursor.fetchall()
        return result
    def get_my_tournaments(self, id):
        print(id)
        self.cursor.execute('SELECT * FROM Tournaments WHERE admin = ? ', (id,))
        return self.cursor.fetchall()
    
    def verifired_tourmantes(self, id):
        self.cursor.execute('UPDATE Tournaments SET verified = ? WHERE id = ?', (1,id))
        self.con.commit()
        return 'done*'