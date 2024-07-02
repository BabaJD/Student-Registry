# Ask the user for the number of students
num_students = int(input("How many students are registering for this exam?: "))
# Create an empty list to store the students' ID number
student_ID = []
# Use a for loop to ask for each student's ID number
for i in range(num_students):
    id_number = input(f"\nEnter {i+1} student's ID number: ")
    student_ID.append(id_number)
# Open the file in write mode
with open('reg_form.txt', 'w') as file:
 # Write each student's ID number to the file
    for id_number in student_ID:
        file.write(id_number + "..................." + "\n")
