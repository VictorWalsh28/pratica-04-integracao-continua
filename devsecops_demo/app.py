from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect("devsecops_demo/mydb.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
def index():
    return """
    <h1>Flask SQL Injection Example</h1>
    <form action="/login" method="get">
      <input name="username" placeholder="Usuário">
      <input name="password" placeholder="Senha">
      <button type="submit">Submit</button>
    </form>
    """


@app.get("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")

    # VULNERÁVEL: concatenação direta de dados fornecidos pelo usuário.
    sql = (
        "SELECT id, username, password FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )

    conn = get_connection()
    rows = conn.execute(sql).fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])


if __name__ == "__main__":
    app.run()
