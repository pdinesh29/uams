from flask import Flask, render_template, request, redirect
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Function to connect to the SQLite3 database
def get_db():
    conn = sqlite3.connect('example.db')  # SQLite database file is 'example.db'
    conn.row_factory = sqlite3.Row  # Make rows behave like dictionaries
    return conn

# Route to display all users
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Get all users from the database
    users = cursor.fetchall()  # Fetch all the rows
    conn.close()
    return render_template('index.html', users=users)  # Pass the users to the template

# Route to add a new user to the database
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')  # Get the user input from the form
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))  # Insert user into DB
    conn.commit()  # Commit the transaction
    conn.close()
    return redirect('/')  # Redirect back to the main page to show the updated list

# Function to create the database and 'users' table (if not already created)
def create_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT)''')  # Create table if it doesn't exist
    conn.commit()
    conn.close()

# Create the database and table on app startup (ensure they exist)
create_db()

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
