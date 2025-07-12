MUCH BETTER TO VIEW THE CODE THAN THE RENDERED VERSION

MODULAR STUDENT UTILITY SYSTEM (MSUS)
=====================================

The Modular Student Utility System (MSUS) is a Python-based application developed by Mohamed Aiman and Kefly Keflon for their DIT1014 Final Project. It showcases modular programming, data persistence, and error handling through a menu-driven terminal interface. MSUS includes fifteen built-in features organized across key areas such as student record management, mathematical operations, text processing, and file-based tasks. Each functionality is separated into dedicated modules, making the system structured and easy to maintain.

FEATURES
========

Mathematical Operations:
- Count even and odd numbers in integer lists
- Calculate sum of digits for any integer
- Compute averages of number lists
- Find minimum and maximum values with range calculation

Text Processing:
- Reverse word order in sentences
- Convert numeric grades (0-100) to letter grades (A-F)
- Count words in text strings
- Capitalize all words in text
- Count vowels and consonants in text

Student Database Management:
- Add new student records with name and age
- Remove existing students from database
- Lookup student information by name
- List all students with their details
- Generate database statistics (total count, average age, age range)

File Operations:
- Automatic JSON data persistence
- CSV import and export functionality
- Data validation and error recovery
- Merge and replace modes for data import
- Sample CSV file generation

Error Handling:
- Comprehensive input validation
- Graceful error recovery
- User-friendly error messages
- Data integrity protection

PROJECT STRUCTURE
=================

The project consists of four main Python files:

+------------------+--------------------------------------------------+
| File             | Description                                      |
+------------------+--------------------------------------------------+
| main.py          | Central controller with menu interface and       |
|                  | user interaction handling                        |
+------------------+--------------------------------------------------+
| math_utils.py    | Mathematical utility functions and calculations  |
+------------------+--------------------------------------------------+
| text_utils.py    | Text processing and string manipulation          |
|                  | functions                                        |
+------------------+--------------------------------------------------+
| student_utils.py | Student database management and file I/O         |
|                  | operations                                       |
+------------------+--------------------------------------------------+

Additional files created during runtime:

+------------------+--------------------------------------------------+
| File             | Description                                      |
+------------------+--------------------------------------------------+
| students.json    | Primary student database (auto-generated)        |
+------------------+--------------------------------------------------+
| students.csv     | CSV export/import file                           |
+------------------+--------------------------------------------------+

SYSTEM REQUIREMENTS
==================

- Python 3.8 or higher
- Standard Python libraries (json, csv, os, sys, math)
- No external dependencies required

INSTALLATION AND USAGE
======================

1. Download all four Python files to the same directory
2. Ensure Python 3.8+ is installed on your system
3. Open terminal/command prompt in the project directory
4. Run the application:

   python main.py

5. Follow the on-screen menu to navigate through available options

The application will automatically create a student database file (students.json) 
on first run with default sample data. All data is automatically saved when you 
exit the program.

MENU OPTIONS
============

The main menu provides 15 different operations:

+------+------------------------------------------+
| No.  | Operation                                |
+------+------------------------------------------+
| 1    | Count Even and Odd Numbers               |
| 2    | Calculate Sum of Digits                  |
| 3    | Get Letter Grade from Mark               |
| 4    | Reverse a Sentence                       |
| 5    | Lookup Student Age                       |
| 6    | Add New Student                          |
| 7    | Remove Student                           |
| 8    | List All Students                        |
| 9    | Student Database Statistics              |
| 10   | Export Students to CSV                   |
| 11   | Import Students from CSV                 |
| 12   | Math Operations (Average, Min/Max)       |
| 13   | Text Operations (Word Count, Capitalize) |
| 14   | Create Sample CSV File                   |
| 0    | Exit                                     |
+------+------------------------------------------+

DETAILED FUNCTION DOCUMENTATION
===============================

MATH_UTILS.PY FUNCTIONS
-----------------------

count_even_odd(numbers: list[int]) -> tuple[int, int]
    Counts even and odd numbers in a list of integers.
    
    Parameters:
        numbers: List of integers to analyze
    
    Returns:
        Tuple containing (even_count, odd_count)
    
    Raises:
        TypeError: If input is not a list or contains non-integers
        ValueError: If list is empty

sum_of_digits(n: int) -> int
    Calculates the sum of all digits in an integer.
    
    Parameters:
        n: Integer to process (negative values are converted to positive)
    
    Returns:
        Sum of all digits as integer
    
    Example:
        sum_of_digits(123) returns 6 (1+2+3)
        sum_of_digits(-456) returns 15 (4+5+6)

calculate_average(numbers: list[int]) -> float
    Computes the arithmetic mean of a list of integers.
    
    Parameters:
        numbers: List of integers
    
    Returns:
        Average as floating-point number

find_min_max(numbers: list[int]) -> tuple[int, int]
    Finds minimum and maximum values in a list.
    
    Parameters:
        numbers: List of integers
    
    Returns:
        Tuple containing (minimum, maximum)

TEXT_UTILS.PY FUNCTIONS
-----------------------

reverse_sentence(sentence: str) -> str
    Reverses the order of words in a sentence.
    
    Parameters:
        sentence: Input string to reverse
    
    Returns:
        String with words in reverse order
    
    Example:
        reverse_sentence("Hello world Python") returns "Python world Hello"

get_grade(mark: int) -> str
    Converts numeric grade to letter grade.
    
    Parameters:
        mark: Integer between 0 and 100
    
    Returns:
        Letter grade (A, B, C, D, or F)
    
    Grading Scale:
        A: 80-100
        B: 65-79
        C: 50-64
        D: 40-49
        F: 0-39

count_words(text: str) -> int
    Counts the number of words in a text string.
    
    Parameters:
        text: Input string
    
    Returns:
        Number of words as integer

capitalize_words(text: str) -> str
    Capitalizes the first letter of each word.
    
    Parameters:
        text: Input string
    
    Returns:
        String with each word capitalized

count_vowels_consonants(text: str) -> tuple[int, int]
    Counts vowels and consonants in text.
    
    Parameters:
        text: Input string
    
    Returns:
        Tuple containing (vowel_count, consonant_count)

STUDENT_UTILS.PY FUNCTIONS
--------------------------

lookup_student(name: str) -> str
    Searches for a student by name and returns their information.
    
    Parameters:
        name: Student name to search for
    
    Returns:
        String with student information or "Student not found"

add_student(name: str, age: int) -> str
    Adds a new student or updates existing student's age.
    
    Parameters:
        name: Student name
        age: Student age (must be 0-150)
    
    Returns:
        Success/failure message

remove_student(name: str) -> str
    Removes a student from the database.
    
    Parameters:
        name: Student name to remove
    
    Returns:
        Success/failure message

list_all_students() -> str
    Returns formatted list of all students in database.
    
    Returns:
        String containing all student records

get_student_stats() -> str
    Calculates and returns database statistics.
    
    Returns:
        String with total count, average age, and age range

export_to_csv() -> str
    Exports student database to CSV file.
    
    Returns:
        Success/failure message

import_from_csv(file_path: str) -> str
    Imports student data from CSV file.
    
    Parameters:
        file_path: Path to CSV file (optional, defaults to students.csv)
    
    Returns:
        Import status message

validate_csv_format(file_path: str) -> str
    Validates CSV file format before importing.
    
    Parameters:
        file_path: Path to CSV file to validate
    
    Returns:
        Validation report with issues found

DATA PERSISTENCE
================

The system uses two file formats for data storage:

JSON Format (students.json):
- Primary storage format
- Automatically loaded on startup
- Automatically saved on exit and after modifications
- Stores data as key-value pairs: {"name": age}

CSV Format (students.csv):
- Used for import/export operations
- Compatible with spreadsheet applications
- Format: Name,Age (with header row)
- Supports validation before import

Default Students:
If no existing data files are found, the system creates default entries:
- Alice: 20 years old
- Bob: 22 years old  
- Charlie: 19 years old

ERROR HANDLING
==============

The system implements good error handling:

Input Validation:
- Type checking for all function parameters
- Range validation for ages (0-150) and grades (0-100)
- Empty string and null value checking

File Operations:
- File existence verification
- Permission checking
- Encoding error handling
- Graceful fallback to default data

User Interface:
- Invalid menu choice handling
- Keyboard interrupt (Ctrl+C) support
- Automatic data saving on unexpected exit
- Clear error messages for user guidance

USAGE EXAMPLES
==============

Example 1: Adding Students
1. Run python main.py
2. Select option 6 (Add New Student)
3. Enter student name: "John Doe"
4. Enter age: 21
5. System confirms addition and saves data

Example 2: Mathematical Operations
1. Select option 1 (Count Even and Odd Numbers)
2. Enter numbers: 1 2 3 4 5 6
3. System displays: Even numbers: 3, Odd numbers: 3

Example 3: CSV Import
1. Create CSV file with format:
   Name,Age
   Student1,20
   Student2,21
2. Select option 11 (Import Students from CSV)
3. Choose import mode (replace or merge)
4. System validates and imports data

CONTRIBUTOR INFORMATION
=======================

This project was developed collaboratively by two team members:

Mohamed Aiman - Lead Developer:
- Developed main.py (menu system and user interface)
- Implemented text_utils.py (text processing functions)
- Created student_utils.py (database management and file I/O)
- Designed overall system architecture
- Made the README.md files and documented the system

Kefly Keflon - Co Developer:
- Developed math_utils.py (mathematical utility functions)
- Prepared the main Report
- Provided mathematical function testing and validation
- Implemented error handling and data validation

TECHNICAL SPECIFICATIONS
========================

Code Quality Features:
- Type hints for all function parameters and return values
- Comprehensive docstrings for all functions
- Consistent error handling patterns
- Input validation and sanitization
- Modular design with clear separation of concerns

Performance Considerations:
- Efficient file I/O operations
- Memory-conscious data structures
- Minimal external dependencies
- Fast startup and response times

Security Features:
- Input sanitization to prevent injection attacks
- File permission checking
- Safe file handling with proper exception management
- Data integrity validation


END OF DOCUMENTATION
====================
