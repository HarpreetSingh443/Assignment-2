
Student_id = input("what is the student's ID number? ")
student_name = input("what is the student's name? ")
print("Hello " + student_name + "!")

subject = input("which subject is this mark for? ")
grade = input("what is the student's mark (0-100)? ")
attendance = input("what is the student's attendance percentage (0-100)? ")

print(f"{Student_id} | {student_name} | {subject} | Mark: {grade} | Attendance: {attendance}%")

#Creating a Dictionary to store the student information

student = {
    "student_id": Student_id,
    "name": student_name,
    "subject": subject,
    "grade": grade,
    "attendance": attendance,
}
print(student)




