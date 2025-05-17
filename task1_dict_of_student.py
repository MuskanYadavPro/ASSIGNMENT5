dict = {'Alice':85,'Mike':95,'Tom':80}
name = input("Enter the student's name: ")
if name in dict:
    print(name+"'s marks:",dict[name])
else:
    print("Student not found.")
