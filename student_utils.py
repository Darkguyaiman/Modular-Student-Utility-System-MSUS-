import json
import csv
import os
from typing import Dict, Any

DEFAULT_STUDENTS = {"Alice": 20, "Bob": 22, "Charlie": 19}
JSON_FILE = "students.json"
CSV_FILE = "students.csv"
students = {}

def load_students_from_json() -> bool:
    global students
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r') as file:
                students = json.load(file)
            print(f"Loaded {len(students)} students from {JSON_FILE}")
            return True
        else:
            students = DEFAULT_STUDENTS.copy()
            save_students_to_json()
            print(f"Created new student database with {len(students)} default students")
            return True
    except (json.JSONDecodeError, IOError, PermissionError) as e:
        print(f"Error loading from JSON: {e}")
        students = DEFAULT_STUDENTS.copy()
        return False

def save_students_to_json() -> bool:
    try:
        with open(JSON_FILE, 'w') as file:
            json.dump(students, file, indent=2)
        return True
    except (IOError, PermissionError) as e:
        print(f"Error saving to JSON: {e}")
        return False

def load_students_from_csv() -> bool:
    global students
    try:
        if os.path.exists(CSV_FILE):
            students = {}
            with open(CSV_FILE, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header and header != ['Name', 'Age']:
                    try:
                        students[header[0]] = int(header[1])
                    except (ValueError, IndexError):
                        pass
                
                for row in reader:
                    if len(row) >= 2:
                        try:
                            name = row[0].strip()
                            age = int(row[1].strip())
                            if name and age >= 0:
                                students[name] = age
                        except ValueError:
                            continue
            
            if not students:
                students = DEFAULT_STUDENTS.copy()
            
            print(f"Loaded {len(students)} students from {CSV_FILE}")
            return True
        else:
            students = DEFAULT_STUDENTS.copy()
            save_students_to_csv()
            print(f"Created new CSV file with {len(students)} default students")
            return True
    except (IOError, PermissionError) as e:
        print(f"Error loading from CSV: {e}")
        students = DEFAULT_STUDENTS.copy()
        return False

def save_students_to_csv() -> bool:
    try:
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age'])
            for name, age in sorted(students.items()):
                writer.writerow([name, age])
        return True
    except (IOError, PermissionError) as e:
        print(f"Error saving to CSV: {e}")
        return False

def lookup_student(name: str) -> str:
    try:
        if not name or not name.strip():
            return "Please enter a valid student name."
        
        name = name.strip()
        if name in students:
            return f"{name} is {students[name]} years old."
        else:
            return "Student not found."
    except Exception as e:
        return f"Error looking up student: {e}"

def add_student(name: str, age: int) -> str:
    try:
        if not name or not name.strip():
            return "Error: Student name cannot be empty."
        
        if age < 0 or age > 150:
            return "Error: Age must be between 0 and 150."
        
        name = name.strip()
        
        if name in students:
            old_age = students[name]
            students[name] = age
            if save_students_to_json():
                return f"Updated {name}'s age from {old_age} to {age}."
            else:
                return f"Updated {name}'s age but failed to save to file."
        else:
            students[name] = age
            if save_students_to_json():
                return f"Student {name} (age {age}) has been added successfully."
            else:
                return f"Added {name} but failed to save to file."
                
    except Exception as e:
        return f"Error adding student: {e}"

def remove_student(name: str) -> str:
    try:
        if not name or not name.strip():
            return "Please enter a valid student name."
        
        name = name.strip()
        if name in students:
            age = students.pop(name)
            if save_students_to_json():
                return f"Student {name} (age {age}) has been removed successfully."
            else:
                return f"Removed {name} but failed to save to file."
        else:
            return "Student not found."
    except Exception as e:
        return f"Error removing student: {e}"

def list_all_students() -> str:
    try:
        if not students:
            return "No students in the database."
        
        result = f"Current students ({len(students)} total):\n"
        for name, age in sorted(students.items()):
            result += f"  - {name}: {age} years old\n"
        
        return result.strip()
    except Exception as e:
        return f"Error listing students: {e}"

def export_to_csv() -> str:
    try:
        if save_students_to_csv():
            return f"Successfully exported {len(students)} students to {CSV_FILE}"
        else:
            return "Failed to export to CSV file."
    except Exception as e:
        return f"Error exporting to CSV: {e}"

def import_from_csv() -> str:
    try:
        old_count = len(students)
        if load_students_from_csv():
            new_count = len(students)
            return f"Successfully imported {new_count} students from {CSV_FILE} (was {old_count})"
        else:
            return "Failed to import from CSV file."
    except Exception as e:
        return f"Error importing from CSV: {e}"

def get_student_stats() -> str:
    try:
        if not students:
            return "No students in database."
        
        ages = list(students.values())
        total_students = len(students)
        avg_age = sum(ages) / total_students
        min_age = min(ages)
        max_age = max(ages)  # Corrected this line
        
        result = f"Student Database Statistics:\n"
        result += f"  Total Students: {total_students}\n"
        result += f"  Average Age: {avg_age:.1f} years\n"
        result += f"  Age Range: {min_age} - {max_age} years\n"
        
        return result
    except Exception as e:
        return f"Error calculating statistics: {e}"

try:
    load_students_from_json()
except Exception as e:
    print(f"Warning: Could not initialize student data: {e}")
    students = DEFAULT_STUDENTS.copy()
