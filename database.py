import sqlite3


class Database(object):
    
    def __init__(self):
        self.database = sqlite3.connect(database="Hashes.db")
        self.cursor = self.database.cursor()
        
        
    def close(self):
        self.cursor.close()
        self.database.close()
        
    def insert_hash(self, hash_text):
        self.cursor.execute('''INSERT INTO hashes_table(HASH) VALUES(?)''', (hash_text,))
        self.database.commit()
        
    def check_hash(self, hash_text):
        return self.cursor.execute('''SELECT HASH FROM hashes_table WHERE HASH = ?''', (hash_text,)).fetchall()
        
        