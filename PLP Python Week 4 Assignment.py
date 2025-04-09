# PLP Scholarship course exercise
# WEEK 4 Assignment and challenge: File and exception handling

# File Handling and Exception Handling Assignment

# Description

# 1. File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# 2. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

# solution to assignment
def read_write(filename):

    try:
        
        # read the file if it exist
        with open(filename, 'r') as file: print(file.read())
        print()
        print('file exists')
        print()
        file_read = open(filename, 'r')
        
        print()

        # write a modified content to a new file
        with open('modified.txt', 'w') as file: file.write(file_read.read() + '\nThis is a new content added here')
        modified = open('modified.txt' , 'r')
        print(modified.read())
    except FileNotFoundError:
        print('File not found')
        