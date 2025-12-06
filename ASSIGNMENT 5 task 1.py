# Task 1: Create a Dictionary of Student Marks

dict  ={
    'sumit': 50,
     'ajay': 80,
     'virender': 90,

}

name = input("Enter the student name : ")

if name in dict:
    print(f"{name} marks is :",dict[name])

else:
    print(f"{name} not found")