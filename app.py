# app.py
from flask import Flask, render_template, request
import pg8000
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the level from the form
        level = request.form["level"]
        return render_template("timetable.html", level=level, data=[], message="Loading timetable...")
    
    return render_template("index.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')  # Get level from the query parameters
    if not level:
        return "Level not provided", 400

    conn = pg8000.connect(
        user=os.getenv("POSTGRES_USER"), 
        password=os.getenv("POSTGRES_PASSWORD"), 
        host=os.getenv("POSTGRES_HOST"), 
        port=int(os.getenv("POSTGRES_PORT")), 
        database=os.getenv("POSTGRES_DB")
    )

    cur = conn.cursor()
    if level == 'All':
        query = "SELECT * FROM timetable_abdulaziz.timetable;"  #table name can be diff
        cur.execute(query)
    else:
        query = "SELECT * FROM timetable_abdulaziz.timetable WHERE level = %s;"  #table name can be diff
        cur.execute(query, (level,))
    rows = cur.fetchall()

    # Pass data to the template
    if rows:
        return render_template("timetable.html", level=level, data=rows, message="")
    else:
        return render_template("timetable.html", level=level, data=[], message="No data found for this level.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
