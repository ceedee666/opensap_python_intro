# Create empty list
list_of_students = []

# Loop for creating tuples
for i in range(5):
    name = input("Bitte Namen eingeben: ")
    vorname = input("Bitte Vornamen eingeben: ")
    fach = input("Bitte Studienfach eingeben: ")
    matrikelnummer = int(input("Bitte Matrikelnummer (Integer) eingeben: "))
# Create a tuple out of single elements
    student = (name, vorname, fach, matrikelnummer)
# Append the tuple inside the list
    list_of_students.append(student)

print(list_of_students)