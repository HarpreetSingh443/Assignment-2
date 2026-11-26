
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
         
def add_record(records):
    
    Student_id = read_non_blank("What is the student's ID number? ")
    
    student_name = None

    for record in records:
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
    records.append(student)  # Store the validated record.
    print(student)
    
def find_records(records, student_id):
    matches = []

    for record in records:
        if record["student_id"] == student_id:
            matches.append(record)

    return matches

def rename_student(records, student_id, new_name):
    matches = find_records(records, student_id)

    for record in matches:
        record["name"] = new_name

    return len(matches)
    
Students = []

while True:
    print("\n1. Add record")
    print("2. View all records")
    print("3. Search by student ID")
    print("4. Rename student")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_record(Students)
    elif choice == "2":
        display_records(Students)
    elif choice == "3":
        student_id = read_non_blank("Enter the student ID to search for: ")
        matches = find_records(Students, student_id)

        if matches:
            display_records(matches)
        else:
            print("No records found for that student ID.")
    elif choice == "4":
        student_id = read_non_blank("Enter the student ID to rename: ")
        matches = find_records(Students, student_id)

        if not matches:
            print("Student not found.")
        else:
            display_records(matches)
            new_name = read_non_blank("Enter the new name: ")
            updated = rename_student(Students, student_id, new_name)
            print(f"Records updated: {updated}")

    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

     
