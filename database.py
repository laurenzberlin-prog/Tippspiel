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
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            creator_user_id INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            round_id INTEGER NOT NULL,
            match_date TEXT,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            actual_home_score INTEGER,
            actual_away_score INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS round_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            round_id INTEGER NOT NULL,
            UNIQUE(user_id, round_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            match_id INTEGER NOT NULL,
            predicted_home_score INTEGER NOT NULL,
            predicted_away_score INTEGER NOT NULL,
            UNIQUE(user_id, match_id)
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

def create_round(name, description, creator_user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO rounds (name, description, creator_user_id) VALUES (?, ?, ?)",
            (name, description, creator_user_id)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:        
        conn.close()


def get_all_rounds():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds")
    rounds = cursor.fetchall()
    conn.close()
    return rounds

def get_rounds_by_user_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT rounds.*
        FROM round_members
        JOIN rounds ON round_members.round_id = rounds.id
        WHERE round_members.user_id = ?
    """, (user_id,))
    
    rounds = cursor.fetchall()
    conn.close()
    return rounds

def create_match(round_id, match_date, home_team, away_team):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO matches (round_id, match_date, home_team, away_team) VALUES (?, ?, ?, ?)",
        (round_id, match_date, home_team, away_team)
    )
    conn.commit()
    conn.close()

def save_match_result(match_id, actual_home_score, actual_away_score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE matches
        SET actual_home_score = ?, actual_away_score = ?
        WHERE id = ?
        """,
        (actual_home_score, actual_away_score, match_id)
    )
    conn.commit()
    conn.close()

def delete_match(match_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM matches WHERE id = ?",
        (match_id,)
    )
    conn.commit()
    conn.close()

def get_matches_by_round_id(round_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM matches WHERE round_id = ? ORDER BY match_date ASC",
        (round_id,)
    )
    matches = cursor.fetchall()
    conn.close()
    return matches

def save_prediction(user_id, match_id, predicted_home_score, predicted_away_score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO predictions
        (user_id, match_id, predicted_home_score, predicted_away_score)
        VALUES (?, ?, ?, ?)
        """,
        (user_id, match_id, predicted_home_score, predicted_away_score)
    )
    conn.commit()
    conn.close()

def get_prediction_by_user_and_match(user_id, match_id):
    conn = get_connection ()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM predictions
        WHERE user_id = ? AND match_id = ?
        """,
        (user_id, match_id)
    )
    prediction = cursor.fetchone()
    conn.close()
    return prediction

def get_round_by_id(round_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds WHERE id = ?", (round_id,))
    round = cursor.fetchone()
    conn.close()
    return round

def get_round_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds WHERE name = ?", 
    (name,))
    round_data = cursor.fetchone()
    conn.close()
    return round_data

def add_user_to_round(user_id, round_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO round_members (user_id, round_id) VALUES (?, ?)",
        (user_id, round_id)
    )
    conn.commit()
    conn.close()

def remove_user_from_round(user_id, round_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM round_members WHERE user_id = ? AND round_id = ?",
        (user_id, round_id)
    )
    conn.commit()
    conn.close()
    
def get_users_by_round_id(round_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.id, users.username
        FROM round_members
        JOIN users ON round_members.user_id = users.id
        WHERE round_members.round_id = ?
    """, (round_id,))
    users = cursor.fetchall()
    conn.close()
    return users

def get_predictions_by_round_id(round_id):
    conn = get_connection ()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT predictions.*, users.username
        FROM predictions
        JOIN matches ON predictions.match_id = matches.id
        JOIN users ON predictions.user_id = users.id
        WHERE matches.round_id = ?
    """, (round_id,))
    predictions = cursor.fetchall()
    conn.close()
    return predictions