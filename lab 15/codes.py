import sqlite3

conn = sqlite3.connect('student_record.db') 
cursor = conn.cursor() 
# Create student table if it doesn't exist 
cursor.execute('''CREATE TABLE IF NOT EXISTS students ( 
Enrollment INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL 
)''') 
# Create subject records table to store multiple subjects and marks for each student 
cursor.execute('''CREATE TABLE IF NOT EXISTS student_subjects ( 
Enrollment INTEGER NOT NULL, 
Subject TEXT NOT NULL, 
Mark INTEGER NOT NULL, 
FOREIGN KEY (Enrollment) REFERENCES students (Enrollment) 
)''') 
conn.commit() 
# Insert students 
students = [ 
(92301733016, 'ASHUTOSH KUMAR SINGH'),
(92301733017, 'HARSH VISHALBHAI TRIVEDI'), 
(92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA'), 
(92301733046, 'SHIVAM ATULKUMAR BHATT'), 
(92301733058, 'DEVENDRASINH DOLATSINH JADEJA') 
] 
cursor.executemany('INSERT INTO students (Enrollment, name) VALUES (?, ?)', students) 
# Insert subjects and marks for each student 
student_subjects = [ 
(92301733016, 'PWP', 95), 
(92301733016, 'Math', 89), 
(92301733017, 'PWP', 85), 
(92301733027, 'PWP', 90), 
(92301733046, 'PWP', 93), 
(92301733058, 'PWP', 75), 
(92301733058, 'Physics', 80) 
] 
cursor.executemany('INSERT INTO student_subjects (Enrollment, Subject, Mark) VALUES (?, ?, ?)', student_subjects) 
conn.commit() 
# Fetch and print all student records with their subjects
cursor.execute('''SELECT students.Enrollment, students.name, student_subjects.Subject, student_subjects.Mark 
FROM students 
JOIN student_subjects ON students.Enrollment = student_subjects.Enrollment''') 
rows = cursor.fetchall() 
print("All Student Records with Subjects:") 
for row in rows: 
    print(row) 
# Fetch and print students with marks greater than 90 
cursor.execute('''SELECT students.name, student_subjects.Subject, student_subjects.Mark 
FROM students 
JOIN student_subjects ON students.Enrollment = student_subjects.Enrollment 
WHERE student_subjects.Mark > 90''') 
high_marks = cursor.fetchall() 
print("\nStudents with Marks greater than 90:") 
for student in high_marks: 
    print(student) 
# Update marks for a specific student and subject 
cursor.execute('''UPDATE student_subjects SET Mark = 98 
WHERE Enrollment = 92301733016 AND Subject = 'PWP' ''')
conn.commit() 
# Fetch and print updated marks for the student 
cursor.execute('''SELECT students.name, student_subjects.Mark 
FROM students 
JOIN student_subjects ON students.Enrollment = student_subjects.Enrollment 
WHERE students.name = "ASHUTOSH KUMAR SINGH" AND student_subjects.Subject = 'PWP' ''') 
updated_mark = cursor.fetchone() 
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}") 
# Delete a specific student's subject record 
cursor.execute('''DELETE FROM student_subjects WHERE Enrollment = 92301733058 AND Subject = 'PWP' ''') 
conn.commit() 
# Confirm deletion 
cursor.execute('''SELECT * FROM student_subjects WHERE Enrollment = 92301733058 AND Subject = 'PWP' ''') 
deleted_name = cursor.fetchone() 
if deleted_name is None: 
    print("\nRecord for 'PWP' subject of DEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")
# Calculate and print the average mark across all subjects 
cursor.execute('''SELECT AVG(Mark) FROM student_subjects''') 
avg_mark = cursor.fetchone()[0] 
print(f"\nThe average mark of all subjects is: {avg_mark:.2f}") 
# Close the database connection 
conn.close()