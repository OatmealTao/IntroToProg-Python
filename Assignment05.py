# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Bao Truong, 5/20/2024, Modified Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
# Holds the first name of a student entered by the user.
student_first_name: str = ""  

# Holds the last name of a student entered by the user.
student_last_name: str = ""  

# Holds the name of a course entered by the user.
course_name: str = "" 

# Holds combined string data seperated by a comma.
csv_data: str = ""

# Holds a reference to an opened file.
file_obj: object = None  

# Hold the choice made by the user.
menu_choice: str  

# Row of student data
student_data: dict = {} 

# table of student data (2D)
students: list[dict] = []


# Reading in existing CSV file for student_data
try:
    with open(FILE_NAME, "r") as file_obj:
        for each_row in file_obj.readlines():
            student = each_row.strip().split(",")
            student_data = {"first_name": student[0], "last_name": student[1], "course_name": student[2]}
            students.append(student_data)
except FileNotFoundError:
    print("ERROR: File not found!")

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  
        try:
            student_first_name = input("Enter the student's first name: ")
            if len(student_first_name) == 0:
                raise Exception ("First name can not be empty!")
            student_last_name = input("Enter the student's last name: ")
            if len(student_last_name) == 0:
                raise Exception ("Last name can not be empty!")
            course_name = input("Please enter the name of the course: ")
            if len(course_name) == 0: 
                raise Exception ("Course name can not be empty!")
            student_data = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
            students.append(student_data)
            continue
        except Exception as e:
            print(f"ERROR: {e}")
            
            
    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        for student in students:
            print(f"{student["first_name"]},{student["last_name"]},{student["course_name"]}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file_obj:
                for student in students:
                    csv_data += f"{student["first_name"]},{student["last_name"]},{student["course_name"]}\n"
                file_obj.write(csv_data)
            print(f"{csv_data}\nHas been saved to {FILE_NAME}")
            continue
        except FileNotFoundError:
            print("ERROR: File not found!")

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")