def get_student_data():
    name = input("Enter student's name: ")
    firstname = input("Enter student's firstname: ")
    student_ID = input("Enter student's ID: ")
    return (name, firstname, student_ID)

new_student = get_student_data()

print(new_student)