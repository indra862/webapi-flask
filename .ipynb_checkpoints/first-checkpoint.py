# from flask import Flask
# import sqlite3

# app = Flask(__name__)

# @app.route('/')
# def pr():
#     return "Hellooooo"

# @app.route('/students')
# def studentss():
#     # Connect to the database
#     conn = sqlite3.connect('st_data.sqlite3')
#     cursor = conn.cursor()
    
#     # Fetch data from the `ss` table
#     cursor.execute("SELECT * FROM ss")
#     rows = cursor.fetchall()
#     conn.close()

# if __name__ == "__first__":
#     app.run(debug=True)

from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def pr():
    return "Hellooooo"

@app.route('/students')
def studentss():
    # Connect to the database
    conn = sqlite3.connect('st_data.sqlite3')
    cursor = conn.cursor()
    
    # Fetch data from the `ss` table
    cursor.execute("SELECT * FROM ss")
    rows = cursor.fetchall()
    conn.close()

    # Format the data as HTML or plain text
    if rows:
        result = "<h1>Student List</h1><ul>"
        for row in rows:
            result += f"<li>s_id: {row[0]}, s_name: {row[1]}, s_roll: {row[2]}, s_address: {row[3]}</li>"
        result += "</ul>"
    else:
        result = "No students found in the database."
    
    return result

if __name__ == "__main__":
    app.run(debug=True)


