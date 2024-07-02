# Student Registry

## Description

This Python script simplifies the process of collecting and storing student ID numbers for an exam registration. It does the following:

1. **Asks:** Prompts the user to input the number of students registering.
2. **Collects:** Gathers the ID number of each student using a loop.
3. **Stores:** Saves the ID numbers in a text file named `reg_form.txt`.

This script is a helpful learning tool for:

* **File Handling:** It demonstrates how to open, write to, and close files in Python.
* **Loops:** It uses a `for` loop to efficiently handle a variable number of student inputs.
* **Lists:** It temporarily stores the ID numbers in a list before writing them to the file.
* **Basic Input/Output:** It interacts with the user through the console.

## Installation

This script requires no additional installation steps. It is designed to run on a standard Python environment.

## Usage

1. **Run the Script:** Execute the Python script from your terminal or IDE.
2. **Enter Number of Students:** You'll be asked to input the total number of students registering.
3. **Enter IDs:** For each student, you'll be prompted to enter their ID number.
4. **Check Output:** The script will create or overwrite a file named `reg_form.txt` in the same directory, containing the student ID numbers.

## File Output

The `reg_form.txt` file will look like this:

```
ID_Number1...................
ID_Number2...................
ID_Number3................... 
... 
```
![image](https://github.com/BabaJD/Student-Registry/assets/96452821/cdffc1f9-11a3-4451-9eca-628749fcd730)


## Credits

* **Author:** Babajide Abraham Alamu

## Potential Improvements

* **Error Handling:** Add input validation to ensure the user enters a valid number of students and valid ID numbers.
* **Data Format:** Allow the user to choose a different delimiter (e.g., comma, tab) for the output file.
* **Append to File:** Provide the option to append new ID numbers to an existing file instead of overwriting it.
* **Data Validation:** Check if entered IDs are unique, preventing duplicates.
