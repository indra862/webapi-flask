# import sqlite3
# conn = sqlite3.connect('st_data.sqlite3')
# cursor = conn.cursor()
# conn.commit

# # Function to create data
# def create_table():
#     cursor.execute("""CREATE TABLE IF NOT EXISTS ss(
#                    s_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    s_name TEXT NOT NULL,
#                    s_roll INTEGER NOT NULL,
#                    s_address TEXT NOT NULL)""")
#     conn.commit
#     print("Table Created Successfully!!")

# # Function to insert data
# def insert_data(s_name,s_roll,s_address):
#     cursor.execute("""INSERT INTO ss(s_name,s_roll,s_address)VALUES(?,?,?)"""
#                    ,(s_name,s_roll,s_address))
#     conn.commit
#     print("Data added successfully!")

# # Function to update data
# def update_data(s_name,s_roll,s_address,s_id):
#     cursor.execute("""UPDATE ss SET s_name=?,s_roll=?,s_address=? WHERE s_id=?"""
#                    ,(s_name,s_roll,s_address,s_id))
#     conn.commit
#     print('Data updated successfully!')

# # Function to show the table !
# def show_table():
#     cursor.execute("SELECT * FROM ss")
#     data = cursor.fetchall()
#     print(data)

# print("Please choose the option below: ")
# try:
#     print("1. Insert Data\n2. Update Data\n3. Show Data")
#     user_input = int(input("Please select the option: "))
#     if user_input == 1:
#         s_name = input("Name: ")
#         s_roll = int(input("S_roll: "))
#         s_address = input("Address: ")
#         insert_data(s_name,s_roll,s_address)
    
#     elif user_input == 2:
#         s_id = int(input("s_id: "))
#         s_name = input("Name: ")
#         s_roll = int(input("S_roll: "))
#         s_address = input("Address: ")
#         update_data(s_name,s_roll,s_address,s_id)

#     elif user_input ==3:
#         show_table()

#     else:
#         print("Invalid Option Selected!")

# except ValueError:
#     print("Invalid!!!")
# finally:
#     conn.close()

import sqlite3
conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
cursor = conn.cursor()
# Function to create the table
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS ss(
                   s_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   s_name TEXT NOT NULL,
                   s_roll INTEGER NOT NULL,
                   s_address TEXT NOT NULL)""")
    conn.commit()
    conn.close()
    print("Table Created Successfully!!")

# Function to create student's marks table!
def student_marks():
    cursor.execute("""CREATE TABLE IF NOT EXISTS mm(
                   s_id INTEGER PRIMERY KEY,
                   computer INTEGER NOT NULL,
                   science INTEGER NOT NULL,
                   math INTEGER NOT NULL,
                   nepali INTEGER NOT NULL,
                   english INTEGER NOT NULL)""")
    conn.commit
student_marks()
# Function to insert data
def insert_data(s_name, s_roll, s_address):
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("""INSERT INTO ss(s_name, s_roll, s_address) VALUES (?, ?, ?)""", (s_name, s_roll, s_address))
    conn.commit()
    conn.close()
    print("Data added successfully into student's info!")

# Function to insert data into marks table
def insert_data_m(s_id,computer,science,math,nepali,english):
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("""INSERT INTO mm(s_id,computer,science,math,nepali,english) VALUES (?, ?, ?,?,?,?)""", (s_id,computer,science,math,nepali,english))
    conn.commit()
    conn.close()
    print("Data added successfully into marks table!")

# Function to update data
def update_data(s_name, s_roll, s_address, s_id):
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("""UPDATE ss SET s_name = ?, s_roll = ?, s_address = ? WHERE s_id = ?"""
                   , (s_name, s_roll, s_address, s_id))
    conn.commit()
    conn.close()
    print('Data updated successfully!')

# Function to update data into marks table
def update_data_m(computer,science,math,nepali,english,s_id):
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("""UPDATE ss SET computer = ?, science = ?, math = ?, nepali = ?, english =? WHERE s_id = ?"""
                   , (computer,science,math,nepali,english,s_id))
    conn.commit()
    conn.close()
    print('Data updated successfully!')

# Function to show the mm table
def show_table_m():
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("SELECT * FROM mm")
    data = cursor.fetchall()
    conn.close()
    if data:
        print("Data in the table:")
        for row in data:
            print(f"s_id: {row[0]}, computer: {row[1]}, science: {row[2]}, math: {row[3]},nepali: {row[4]},english: {row[5]}")
    else:
        print("The table is empty.")

# Function to show the ss table
def show_table_s():
    # conn = sqlite3.connect('st_data.sqlite3')  # Define connection inside the function
    # cursor = conn.cursor()
    cursor.execute("SELECT * FROM ss")
    data = cursor.fetchall()
    conn.close()
    if data:
        print("Data in the table:")
        for row in data:
            print(f"s_id: {row[0]}, s_name: {row[1]}, s_roll: {row[2]}, s_address: {row[3]}")
    else:
        print("The table is empty.")

# Main logic
print('Select the option below:\n1. Insert Data into student info table\n2. Update Data in student info table\n3. Show Data from student info\n4. Insert data into student marks table\n5. Updata into student mark\n6. Show student marks table')
try:
    user_opt = int(input("Please select the option above: "))
    if user_opt == 1:
        s_name = input("Name: ")
        s_roll = int(input("Roll: "))
        s_address = input("Address: ")
        insert_data(s_name, s_roll, s_address)
    elif user_opt == 2:
        s_id = int(input("Student ID: "))
        s_name = input("Name: ")
        s_roll = int(input("Roll: "))
        s_address = input("Address: ")
        update_data(s_name, s_roll, s_address, s_id)
    elif user_opt == 3:
        show_table_s()
    elif user_opt ==4:
        s_id = int(input("Student ID: "))
        computer = int(input("Computer: "))
        science = int(input("Science: "))
        math = int(input("Math: "))
        nepali = int(input("Nepali: "))
        english = int(input("English: "))
        insert_data_m(s_id,computer,science,math,nepali,english)
    elif user_opt ==5:
        s_id = int(input("Student ID: "))
        computer = int(input("Computer: "))
        science = int(input("Science: "))
        math = int(input("Math: "))
        nepali = int(input("Nepali: "))
        english = int(input("English: "))
        update_data_m(computer,science,math,nepali,english,s_id)
    elif  user_opt ==6:
        show_table_m()
    else:
        print("Invalid option!")
except ValueError:
    print("Invalid input. Please enter a valid number.")





