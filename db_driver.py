import sqlite3

class PersonalAssistantDB:
    def __init__(self, db_name="assistant_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                time TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_schedule(self, task, time):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO schedule (task, time) VALUES (?, ?)", (task, time))
        self.conn.commit()

    def get_all_schedules(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM schedule")
        return cursor.fetchall()

    def get_schedules_by_task(self, task):
        # Escape LIKE special characters so user-supplied task is treated literally
        escaped = task.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM schedule WHERE task LIKE ? ESCAPE '\\'",
            (f"%{escaped}%",),
        )
        return cursor.fetchall()
