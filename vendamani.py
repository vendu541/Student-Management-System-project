#Student Management  System
#Creating Data structure Lists ------>lists
#Initialize empty list
students=[]
print("===== Student Management System =====")
print("1.Add Student")
print("2.View Students")
print("3.Search Student")
print("4.Update Student")
print("5.Delete Student")
print("6.Save & Exit")

while True:
    choice=input("Enter your choice: ")
    if choice not in['1','2','3','4','5','6']:
        print("Invalid choice.Please try again.")
        break
    elif choice=='1':
        # Add Student
        row=[]
        id=input("Enter Student ID: ")
        name=input("Enter Student Name: ")
        age=input("Enter Student Age: ")
        course=input("Enter Student Course: ")
        marks=input("Enter Student Marks: ")

        row.append(id)
        row.append(name)
        row.append(age)
        row.append(course)
        row.append(marks)

        students.append(row)
        print("Student added succesfully!")
    elif choice=='2':
        #View Students
        print("ID\tName\tAge\tCourse\tMarks")

        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
            #studentr[0] -->ID
            #student[1] -->Name
            #student[2] -->Age
            #student[3] -->Course
            #student[4] -->Marks
    elif choice =='3':
        #Searching based on name
        search_name=input("Enter the name of the student to search:")
        searched_user=[]

        is_found=False
        for student in students:
            if student[1]==search_name:
                searched_user.append(student)
                is_found=True
        if not is_found:
            print("Student not found.")
        else:
            print("ID\tName\tAge\tCourse\tMarks")
            for student in searched_user:
              print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
    elif choice=='4':
            #Update Student
            update_det=input("Enter the column for which you want to update the details: ")#input of column name.
            #NAME -->name,name=name ,name -->name
            update_id=input("Enter Student ID to update the details: ")
            is_found=False
            for student in students:
                if student[0]==update_id:
                   is_found=True
                   if update_det.lower()=='name':
                       new_name=input("Enter new name: ")
                       student[1]=new_name
                   elif update_det.lower()=='age':
                       new_age=input("Enter new name: ")
                       student[2]=new_age
                   elif update_det.lower()=='course':
                       new_course=input("Enter new name: ")
                       student[3]=new_course
                   elif update_det.lower()=='marks':
                       new_marks=input("Enter new name: ")
                       student[4]=new_marks
                   else:
                       print("Invalid detail type.")
                       break
                   print("Student details updated successfully!")
                   break
            if not is_found:
                print("Invalid Student ID.")

    elif choice=='5':
       #Delete Student
       delete_id=input("Enter Student ID to delete: ")
       is_found=False
       for student in students:
           if student[0]==delete_id:
               students.remove(student)
               is_found=True
               print("Student deleted successfully!")
               break
       if not is_found:
           print(" invalid Student ID.")

    elif choice=='6':
           #Save & Exit
           print("Saving data and exiting...")
           break






Output:
"C:\Users\user\PycharmProjects\Student Management System\.venv\Scripts\python.exe" "C:\Users\user\PycharmProjects\Student Management System\vendu.py"
===== Student Management System =======
1.
Add
Student
2.
View
Students
3.
Search
Student
4.
Update
Student
5.
Delete
Student
6.
Save & Exit
Enter
your
choice: 1
Enter
Student
ID: 101
Enter
Student
Name: Govind
Raj
Enter
Student
Age: 25
Enter
Student
Course: B
tech
Enter
Student
Marks: 90
Student
added
succesfully!
Enter
your
choice: 2
ID
Name
Age
Course
Marks
101
Govind
Raj
25
B
tech
90

choice: 3
Enter
the
name
of
the
student
to
search: Govind
Raj
ID
Name
Age
Course
Marks
101
Govind
Raj
25
B
tech
90
Enter
your
choice: 4
Enter
the
column
for which you want to update the details: name
Enter
Student
ID
to
update
the
details: 101
Enter
new
name: rahul
Student
details
updated
successfully!
Enter
your
choice: 5
Enter
Student
ID
to
delete: 101
Student
deleted
successfully!
Enter
your
choice: 6
Saving
data and exiting...

Process
finished
with exit code 0
