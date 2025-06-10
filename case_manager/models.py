from database import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            client TEXT,
            date_opened TEXT,
            status TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
