
Student_id = input("what is the student's ID number? ")
student_name = input("what is the student's name? ")
print("Hello " + student_name + "!")

subject = input("which subject is this mark for? ")
grade = input("what is the student's mark (0-100)? ")
attendance = input("what is the student's attendance percentage (0-100)? ")


#to store all records in a list of dictionaries
Students = []
#collecting data for three records
for number in range(1, 4):
    print(f"\nStudent {number}: of 3")
        
    while True:
        
        Student_id = input("what is the student's ID number? ").strip()
        if Student_id:
            break
        print("Student ID cannot be blank. Please enter a valid ID number.")
    
    while True:
        student_name = input("what is the student's name? ").strip()
        if student_name:
            break
        print("Student name cannot be blank. Please enter a valid name.")
        
     while True:
        subject = input("which subject is this mark for? ").strip()
        if not subject:
            print("Subject cannot be blank. Please enter a valid subject.")
            continue
        
        duplicate_found = False
        for record in Students:
            if (
                record["student_id"] == Student_id and
                record["subject"].casefold() == subject.casefold()
            ):
                duplicate_found = True
                break

        if duplicate_found:
            print(f"{Student_id} already has a record for the subject {subject}. Enter another subject.")
            continue

    #final error message with loop to ensure valid input for grade and attendance
    while True:
        grade = input("what is the student's mark (0-100)? ")
        attendance = input("what is the student's attendance percentage (0-100)? ")
            
        #Error handling for invalid input
        try:
            grade = float(grade)
            attendance = float(attendance)
        except ValueError:
            print("Please enter a number for the grade and attendance.")
        else:
            if 0 <= grade <= 100 and 0 <= attendance <= 100:
                student = {
                    "student_id": Student_id,
                    "name": student_name,
                    "subject": subject,
                    "grade": grade,
                    "attendance": attendance,
                }
                Students.append(student) #Accepts the student record and adds it to the list of students
                print(student)
                break
            else:
                print("Grade and Attendance must both be between 0 and 100. Please enter valid values.")
                
#display records
print(f"\nTotal records: {len(Students)}")
for student in Students:
    print(f"{student['student_id']} | {student['name']} | {student['subject']} | Mark: {student['grade']} | Attendance: {student['attendance']}%")




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




