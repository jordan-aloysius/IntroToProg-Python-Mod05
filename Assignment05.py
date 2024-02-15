# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jordan Sellers,2/11/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
json_data: str = ''
file = None
menu_choice: str
student_data: dict = []
students: list = []

# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("The file could not be found; please check if it exists.\n")
    print("-- Error Details --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("An error was found!\n")
    print("-- Error Details --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name cannot contain numbers!")  # What if there's an apostrophe?
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name cannot contain numbers!")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print("-- Error Details --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("An error was found!\n")
            print("-- Error Details --")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved:")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except TypeError as e:
            print("Please check that data is in a valid JSON format.\n")
            print("-- Error details --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("An error was found!")
            print("-- Error Details --")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please choose option 1, 2, 3, or 4.")

print("Program Ended")