import sqlite3

DATABASE ="database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS rounds (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT
                   )
    """)

    conn.commit()
    conn.close()

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()
    return user

def create_round(name, description):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO rounds (name, description) VALUES (?, ?)",
        (name, description)
    )
    conn.commit()
    conn.close()


def get_all_rounds():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds")
    rounds = cursor.fetchall()
    conn.close()
    return rounds

def get_round_by_id(round_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds WHERE id = ?", (round_id,))
    round = cursor.fetchone()
    conn.close()
    return round
    