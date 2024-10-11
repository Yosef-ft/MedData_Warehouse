import psycopg2
import os 

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

class DbConn:

    def __init__(self):
        self.conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        
    
    def insert_data(self, Channel_Title, Channel_Username, ID, Message, Date, Media_Path):
        try:
            cur = self.conn.cursor()
            query = """
                INSERT INTO RawData (Channel_Title, Channel_Username, ID, Message, Date, Media_Path) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(query, (Channel_Title, Channel_Username, ID, Message, Date, Media_Path))
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")