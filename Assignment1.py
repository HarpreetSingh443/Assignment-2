
Student_id = input("what is the student's ID number? ")
student_name = input("what is the student's name? ")
print("Hello " + student_name + "!")

subject = input("which subject is this mark for? ")
grade = input("what is the student's mark (0-100)? ")
attendance = input("what is the student's attendance percentage (0-100)? ")
grade = float(grade)
attendance = float(attendance)

print(f"{Student_id} | {student_name} | {subject} | Mark: {grade} | Attendance: {attendance}%")


#Creating a Dictionary to store the student information
if 0 <= grade <= 100 and 0 <= attendance <= 100:
    student = {
        "student_id": Student_id,
        "name": student_name,
        "subject": subject,
        "grade": grade,
        "attendance": attendance,
    }
    print(student)
else:
    print("Grade and Attendance must both be between 0 and 100. Please enter valid values.")




