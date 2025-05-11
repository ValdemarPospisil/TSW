from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    if request.method == "POST":
        comment = request.form["comment"]
        c.execute(
            f"INSERT INTO comments (text) VALUES ('{comment}')"
        )  # XSS NEZABEZPEČENÉ
        conn.commit()

    c.execute("SELECT text FROM comments")
    comments = c.fetchall()
    conn.close()
    return render_template("index.html", comments=comments)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'" 
        print(f"DEBUG: {query}")
        c.execute(query)
        result = c.fetchall()
        conn.close()
        if result:
            return f"<h2>Welcome {username}</h2><pre>{result}</pre>"
        else:
            error = "Invalid login"

    return f"""
        <h2>Login</h2>
        {'<p style="color:red;">' + error + '</p>' if error else ''}
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
