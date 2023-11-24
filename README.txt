Ayman Madani
101237658
COMP3005
Assignment 4

Setup Instructions for the database:
	Create a new login/group role:
		Name: Aymanm
		Password: password
		
		Turn on Privileges:
			Can login
			Superuser
			Create roles
			Create databases
	
	Create a new Database:
		Name: A4Q1
		User: Aymanm

Steps to compile and run your application:
Used Python 3.10.6 using visual studio code in demonstration.

	Step 1. You Need to install psycopg2 using this command: pip install psycopg2

	Step 2. Run the python code


Brief explanation of each function:

getAllStudents(): Gets all students from the table and prints them to the terminal
addStudent(first_name, last_name, email, enrollment_date): Adds a new student to the students table
updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
deleteStudent(student_id): Deletes the record of the student with the specified student_id.


Video Demonstration:
https://youtu.be/LukiE-xkSb8