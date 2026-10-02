# Python File Handling & Automation
# Project: Automated File Manager

# Name of the text file
file_name = "sample.txt"

# Writing data into the text file
import os
import csv
import shutil
try:
    with open(file_name, "w") as file:
        file.write("Python File Handling Project\n")
        file.write("This is a sample text file.\n")
        file.write("File handling is useful for automation.")

    print("Data written successfully to", file_name)

except Exception as error:
    print("Error while writing file:", error)


# Reading data from the text file
try:
    with open(file_name, "r") as file:
        data = file.read()

    print("\nContents of the file:")
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

except Exception as error:
    print("Error while reading file:", error)
# ---------------------------------------------
# CSV FILE HANDLING
# ---------------------------------------------

import csv

csv_file = "students.csv"

# Creating and writing data to CSV
try:
    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        # Write column headings
        writer.writerow(["Name", "Age", "Department"])

        # Write student records
        writer.writerow(["Rahul", 20, "ECE"])
        writer.writerow(["Priya", 21, "CSE"])
        writer.writerow(["Arun", 20, "EEE"])

    print("\nCSV file created successfully.")

except Exception as error:
    print("Error while creating CSV:", error)


# Reading data from CSV
try:
    with open(csv_file, "r") as file:

        reader = csv.reader(file)

        print("\nStudent Details:")

        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: CSV file not found.")

except Exception as error:
    print("Error while reading CSV:", error)
# ---------------------------------------------
# CREATE FOLDERS
# ---------------------------------------------

# Folder where files will be stored
input_folder = "input_files"

# Folder where processed files will be stored
output_folder = "output_files"

try:
    # Create input folder if it does not already exist
    os.makedirs(input_folder, exist_ok=True)

    # Create output folder if it does not already exist
    os.makedirs(output_folder, exist_ok=True)

    print("\nFolders created successfully.")

except Exception as error:
    print("Error while creating folders:", error)
    
# ---------------------------------------------
# CREATE A FILE FOR AUTOMATION
# ---------------------------------------------

automation_file = os.path.join(input_folder, "automation_test.txt")

try:
    # Create a sample file inside input_files
    with open(automation_file, "w") as file:
        file.write("This file is created for automation testing.")

    print("Automation test file created successfully.")

except Exception as error:
    print("Error while creating automation file:", error)

# ---------------------------------------------
# RENAME FILE
# ---------------------------------------------

old_name = os.path.join(input_folder, "automation_test.txt")
new_name = os.path.join(input_folder, "renamed_file.txt")

try:
    # Check whether the original file exists
    if os.path.exists(old_name):

        # Rename the file
        os.rename(old_name, new_name)

        print("File renamed successfully.")
        print("New file name:", new_name)

    else:
        print("Error: File to rename does not exist.")

except Exception as error:
    print("Error while renaming file:", error)
    
# ---------------------------------------------
# MOVE FILE
# ---------------------------------------------

# Source location of the renamed file
source_file = os.path.join(input_folder, "renamed_file.txt")

# Destination location where the file will be moved
destination_file = os.path.join(output_folder, "renamed_file.txt")

try:
    # Check whether the file exists before moving
    if os.path.exists(source_file):

        # Move the file from input folder to output folder
        shutil.move(source_file, destination_file)

        print("File moved successfully.")
        print("Moved to:", destination_file)

    else:
        print("Error: File to move does not exist.")

except Exception as error:
    print("Error while moving file:", error)
    
# ---------------------------------------------
# DELETE FILE
# ---------------------------------------------

try:
    # Check whether the file exists before deleting
    if os.path.exists(destination_file):

        # Delete the file
        os.remove(destination_file)

        print("File deleted successfully.")

    else:
        print("Error: File to delete does not exist.")

except Exception as error:
    print("Error while deleting file:", error)

# ---------------------------------------------
# CREATE PROJECT FOLDERS
# ---------------------------------------------

input_folder = "input_files"
output_folder = "output_files"

# Create folders if they do not already exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------

# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------

# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------

while True:

    print("\n=========================================")
    print("       AUTOMATED FILE MANAGER")
    print("=========================================")

    print("1. Create TXT File")
    print("2. Read TXT File")
    print("3. Create CSV File")
    print("4. Read CSV File")
    print("5. Rename File")
    print("6. Move File")
    print("7. Delete File")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # -----------------------------------------
    # OPTION 1 - CREATE TXT FILE
    # -----------------------------------------

    if choice == "1":

        try:
            file_name = input("Enter TXT file name: ")

            file_path = os.path.join(
                input_folder,
                file_name + ".txt"
            )

            content = input("Enter the content to write: ")

            with open(file_path, "w") as file:
                file.write(content)

            print("\nTXT file created successfully.")
            print("File location:", file_path)

        except Exception as error:
            print("Error while creating TXT file:", error)


    # -----------------------------------------
    # OPTION 2 - READ TXT FILE
    # -----------------------------------------

    elif choice == "2":

        try:
            file_name = input("Enter TXT file name: ")

            file_path = os.path.join(
                input_folder,
                file_name + ".txt"
            )

            with open(file_path, "r") as file:
                content = file.read()

            print("\n----- FILE CONTENT -----")
            print(content)
            print("------------------------")

        except FileNotFoundError:
            print("Error: TXT file not found.")

        except Exception as error:
            print("Error while reading TXT file:", error)


    # -----------------------------------------
    # OPTION 3 - CREATE CSV FILE
    # -----------------------------------------

    elif choice == "3":

        try:
            csv_name = input("Enter CSV file name: ")

            csv_path = os.path.join(
                input_folder,
                csv_name + ".csv"
            )

            with open(csv_path, "w", newline="") as file:

                writer = csv.writer(file)

                # Write column headings
                writer.writerow(
                    ["Name", "Age", "Department"]
                )

                print("\nEnter student details.")

                name = input("Enter name: ")
                age = input("Enter age: ")
                department = input("Enter department: ")

                # Write student information
                writer.writerow(
                    [name, age, department]
                )

            print("\nCSV file created successfully.")
            print("File location:", csv_path)

        except Exception as error:
            print("Error while creating CSV file:", error)


    # -----------------------------------------
    # OPTION 4 - READ CSV FILE
    # -----------------------------------------

    elif choice == "4":

        try:
            csv_name = input("Enter CSV file name: ")

            csv_path = os.path.join(
                input_folder,
                csv_name + ".csv"
            )

            with open(csv_path, "r") as file:

                reader = csv.reader(file)

                print("\n----- CSV CONTENT -----")

                for row in reader:
                    print(" | ".join(row))

                print("-----------------------")

        except FileNotFoundError:
            print("Error: CSV file not found.")

        except Exception as error:
            print("Error while reading CSV file:", error)


    # -----------------------------------------
    # OPTION 5 - RENAME FILE
    # -----------------------------------------

    elif choice == "5":

        try:
            old_file = input("Enter current file name: ")
            new_file = input("Enter new file name: ")

            old_path = os.path.join(
                input_folder,
                old_file
            )

            new_path = os.path.join(
                input_folder,
                new_file
            )

            if os.path.exists(old_path):

                # Rename the file
                os.rename(old_path, new_path)

                print("\nFile renamed successfully.")
                print("New file name:", new_file)

            else:
                print("Error: File not found.")

        except FileExistsError:
            print("Error: A file with the new name already exists.")

        except Exception as error:
            print("Error while renaming file:", error)


    # -----------------------------------------
    # OPTION 6 - MOVE FILE
    # -----------------------------------------

    elif choice == "6":

        try:
            file_name = input("Enter file name to move: ")

            source_path = os.path.join(
                input_folder,
                file_name
            )

            destination_path = os.path.join(
                output_folder,
                file_name
            )

            if os.path.exists(source_path):

                # Move the file
                shutil.move(
                    source_path,
                    destination_path
                )

                print("\nFile moved successfully.")
                print("Moved to:", destination_path)

            else:
                print("Error: File not found.")

        except Exception as error:
            print("Error while moving file:", error)


    # -----------------------------------------
    # OPTION 7 - DELETE FILE
    # -----------------------------------------

    elif choice == "7":

        try:
            file_name = input("Enter file name to delete: ")

            # Check input folder first
            file_path = os.path.join(
                input_folder,
                file_name
            )

            # If the file is not in input_files,
            # check the output_files folder
            if not os.path.exists(file_path):

                file_path = os.path.join(
                    output_folder,
                    file_name
                )

            if os.path.exists(file_path):

                confirmation = input(
                    "Are you sure you want to delete this file? (y/n): "
                )

                if confirmation.lower() == "y":

                    # Delete the file
                    os.remove(file_path)

                    print("File deleted successfully.")

                else:
                    print("Delete operation cancelled.")

            else:
                print("Error: File not found.")

        except Exception as error:
            print("Error while deleting file:", error)


    # -----------------------------------------
    # OPTION 8 - EXIT
    # -----------------------------------------

    elif choice == "8":

        print("\nThank you for using Automated File Manager.")
        print("Exiting program...")

        break


    # -----------------------------------------
    # INVALID CHOICE
    # -----------------------------------------

    else:

        print(
            "\nInvalid choice. "
            "Please enter a number from 1 to 8."
        )