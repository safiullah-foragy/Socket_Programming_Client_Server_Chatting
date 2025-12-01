import sqlite3
from contextlib import contextmanager

DATABASE_NAME = 'results.db'

@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def init_database():
    """Initialize the database with results table"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                result TEXT NOT NULL,
                college TEXT NOT NULL,
                board TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("Database initialized successfully!")

def insert_result(name, result, college, board):
    """Insert a new result into the database"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO results (name, result, college, board)
            VALUES (?, ?, ?, ?)
        ''', (name, result, college, board))
        return cursor.lastrowid

def get_result_by_id(result_id):
    """Retrieve a result by ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE id = ?', (result_id,))
        return cursor.fetchone()

def get_result_by_name(name):
    """Retrieve results by name"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results WHERE name LIKE ?', (f'%{name}%',))
        return cursor.fetchall()

def get_all_results():
    """Retrieve all results"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results ORDER BY id DESC')
        return cursor.fetchall()

def delete_result(result_id):
    """Delete a result by ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM results WHERE id = ?', (result_id,))
        return cursor.rowcount > 0
