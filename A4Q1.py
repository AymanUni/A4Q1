# Ayman Madani
# 101237659
# 2023 November 23
# COMP 3005 A

# need to install psycopg2 using this command:
# pip install psycopg2

import psycopg2
from psycopg2 import sql

# Establish a connection to the database
conn = psycopg2.connect(
    dbname='A4Q1',
    user='Aymanm',
    password='password',
    host='localhost'
)

# Create a cursor object
cur = conn.cursor()

# Create the students table
cur.execute("""
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    )
""")

# Insert initial data
cur.execute("""
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
""")

# save changes
conn.commit()

# Gets all students from the table and prints them to the terminal
def getAllStudents():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Adds a new student to the students table
def addStudent(first_name, last_name, email, enrollment_date):

        # Checks to make sure no email is the same
        cur.execute("SELECT email FROM students")
        emails = cur.fetchall()
        for emailList in emails:
            if emailList[0] == email:
               print("ERROR: A student with this email already exists.")
               return
        
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()

# Updates students email
def updateStudentEmail(student_id, new_email):
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id)
    )
    conn.commit()

#deletes a student
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id))
    conn.commit()


option = 0
# runs application infinitly until user decides to quit
while option != 5:
    print("APPLICATION MENU OPTIONS:")
    print("1. Get All Students.")
    print("2. Add a Student.")
    print("3. Update Student Email.")
    print("4. Delete Student.")
    print("5. Quit\n")
    
    #Makes sure user is inputing a proper option
    while option < 1 or option > 5:
        option = int(input("What would you like to do? (Enter Menu Option Number): "))
        if option < 1 or option > 5:
            print("Please Enter a Valid Option!")
    
    print()
    
    # cases for each option
    if option == 1:
        getAllStudents()
        print("\n")
        option = 0
    elif option == 2:
        print("You have chosen to Enroll a student.\nFollow the Instructions on Screen.\n")
        first_name = input("Enter Student First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Student Email: ")
        enrollment_date = input("Enter Enrollment Date: ")
        addStudent(first_name, last_name, email, enrollment_date)
        print("\n")
        option = 0
    elif option == 3:
        print("You have chosen to Update a Student Email.\nFollow the Instructions on Screen.\n")
        student_id = input("Enter Student ID: ")
        new_email = input("Enter New Student Email: ")
        updateStudentEmail(student_id, new_email)
        print("\n")
        option = 0
    elif option == 4:
        print("You have chosen to Delete a Student.\nFollow the Instructions on Screen.\n")
        student_id = input("Enter Student ID: ")
        deleteStudent(student_id)
        print("\n")
        option = 0
    elif option == 5:
        print("Goodbye!")
        cur.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        


# Close the cursor and connection
cur.close()
conn.close()