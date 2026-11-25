
def read_non_blank(question):
    while True:
        answer = input(question).strip()
        if answer:
            return answer
        print("Please enter a value.")

def read_percentage(question):
    while True:
        try:
            value = float(input(question))
        except ValueError:
            print("Please enter a number, such as 75 or 75.5.")
            continue

        if 0 <= value <= 100:
            return value

        print("The percentage must be between 0 and 100.")
        
#to store all records in a list of dictionaries
Students = []
#collecting data for three records
for number in range(1, 4):
    print(f"\nRecord {number}: of 3")
     
    Student_id = read_non_blank("What is the student's ID number? ")
    
    student_name = None

    for record in Students:
        if record["student_id"] == Student_id:
            student_name = record["name"]
            print(f"Found student {Student_id}: {student_name}")
            break

    if student_name is None:
        student_name = read_non_blank("What is the student's name? ")

    while True:
        subject = read_non_blank("Which subject is this mark for? ")

        duplicate_found = False
        for record in Students:
            if (
                record["student_id"] == Student_id
                and record["subject"].casefold() == subject.casefold()
            ):
                duplicate_found = True
                break

        if duplicate_found:
            print(f"{Student_id} already has a record for {subject}. Enter another subject.")
            continue

        break

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
            
            #Creating a Dictionary to store the student information
            if 0 <= grade <= 100 and 0 <= attendance <= 100:
                student = {
                    "student_id": Student_id,
                    "name": student_name,
                    "subject": subject,
                    "grade": grade,
                    "attendance": attendance,
                }
                Students.append(student) #Store the validated record.
                print(student)
                break
            else:
                print("Grade and Attendance must both be between 0 and 100. Please enter valid values.")
                
#display records
print(f"\nTotal records: {len(Students)}")
for student in Students:
    print(f"{student['student_id']} | {student['name']} | {student['subject']} | Mark: {student['grade']} | Attendance: {student['attendance']}%")




