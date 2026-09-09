import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("mydb.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cur.executemany(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    [
        ("teste@teste.com", "1234"),
        ("teste2@teste.com", "1234"),
        ("teste3@teste.com", "supersenha"),
        ("teste4@teste.com", "souhacker"),
    ],
)

conn.commit()
conn.close()
print(f"Banco criado em: {db_path}")
