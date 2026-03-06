from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        hours REAL,
        date TEXT)
    """)
    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cur.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    hours = request.form["hours"]
    date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks(title,hours,date) VALUES(?,?,?)",
                (title, hours, date))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)