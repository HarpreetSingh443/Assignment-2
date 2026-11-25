
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


def display_records(records):
    if not records:
        print("No student records to display.")
        return

    print(f"\nTotal records: {len(records)}")
    for student in records:
        print(
            f"{student['student_id']} | {student['name']} | {student['subject']} | "f"Mark: {student['grade']} | Attendance: {student['attendance']}%"
        )
          
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

    #Read and validate each percentage separately.
    grade = read_percentage("What is the student's mark (0-100)? ")
    attendance = read_percentage("What is the student's attendance percentage (0-100)? ")

    student = {
        "student_id": Student_id,
        "name": student_name,
        "subject": subject,
        "grade": grade,
        "attendance": attendance,
    }
    Students.append(student)  # Store the validated record.
    print(student)
    
               
#display records
def add_record(records):
    Students = []

for number in range(1, 4):
    print(f"\nRecord {number} of 3")
    add_record(Students)

display_records(Students)



