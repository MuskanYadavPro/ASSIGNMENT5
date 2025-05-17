student_marks = {'Alice':85,'Mike':95,'Tom':80}
name = input("Enter the student's name: ")
if name in student_marks:
    print(name+"'s marks:",student_marks[name])
else:
    print("Student not found.")
