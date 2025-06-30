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

def import_from_csv(file_path: str = None) -> str:
    """
    Import student data from a specified CSV file.
    
    Args:
        file_path: Path to the CSV file to import from
        
    Returns:
        Status message
    """
    try:
        if file_path is None:
            file_path = CSV_FILE
        
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' not found."
        
        # Check if file is readable
        if not os.access(file_path, os.R_OK):
            return f"Error: Cannot read file '{file_path}'. Check permissions."
        
        old_count = len(students)
        imported_students = {}
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Try to detect if first row is header
            first_row = next(reader, None)
            if first_row is None:
                return f"Error: File '{file_path}' is empty."
            
            # Check if first row looks like a header
            is_header = False
            if len(first_row) >= 2:
                try:
                    # If second column can't be converted to int, it's likely a header
                    int(first_row[1])
                except ValueError:
                    is_header = True
            
            # If not header, process first row as data
            if not is_header and len(first_row) >= 2:
                try:
                    name = first_row[0].strip()
                    age = int(first_row[1].strip())
                    if name and 0 <= age <= 150:
                        imported_students[name] = age
                except ValueError:
                    pass
            
            # Process remaining rows
            row_number = 2 if is_header else 1
            for row in reader:
                row_number += 1
                if len(row) >= 2:
                    try:
                        name = row[0].strip()
                        age = int(row[1].strip())
                        if name and 0 <= age <= 150:
                            imported_students[name] = age
                        elif name:
                            print(f"Warning: Skipped invalid age for {name} on row {row_number}")
                    except ValueError:
                        print(f"Warning: Skipped invalid data on row {row_number}: {row}")
                        continue
        
        if not imported_students:
            return f"Error: No valid student data found in '{file_path}'. Expected format: Name, Age"
        
        # Replace current students with imported data
        students.clear()
        students.update(imported_students)
        
        # Save to JSON file
        if save_students_to_json():
            return f"Successfully imported {len(students)} students from '{file_path}' (was {old_count}). Data saved to {JSON_FILE}."
        else:
            return f"Imported {len(students)} students from '{file_path}' but failed to save to {JSON_FILE}."
            
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except PermissionError:
        return f"Error: Permission denied accessing '{file_path}'."
    except UnicodeDecodeError:
        return f"Error: Cannot read '{file_path}'. File may not be a valid text file."
    except Exception as e:
        return f"Error importing from CSV: {e}"


def import_and_merge_csv(file_path: str) -> str:
    """
    Import student data from CSV and merge with existing data.
    
    Args:
        file_path: Path to the CSV file to import from
        
    Returns:
        Status message
    """
    try:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' not found."
        
        old_count = len(students)
        imported_count = 0
        updated_count = 0
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Skip header if present
            first_row = next(reader, None)
            if first_row and len(first_row) >= 2:
                try:
                    int(first_row[1])
                    # First row is data, process it
                    name = first_row[0].strip()
                    age = int(first_row[1].strip())
                    if name and 0 <= age <= 150:
                        if name in students:
                            students[name] = age
                            updated_count += 1
                        else:
                            students[name] = age
                            imported_count += 1
                except ValueError:
                    # First row is header, skip it
                    pass
            
            # Process remaining rows
            for row in reader:
                if len(row) >= 2:
                    try:
                        name = row[0].strip()
                        age = int(row[1].strip())
                        if name and 0 <= age <= 150:
                            if name in students:
                                students[name] = age
                                updated_count += 1
                            else:
                                students[name] = age
                                imported_count += 1
                    except ValueError:
                        continue
        
        if imported_count == 0 and updated_count == 0:
            return f"No valid student data found in '{file_path}'."
        
        # Save to JSON file
        if save_students_to_json():
            result = f"Successfully processed '{file_path}': "
            if imported_count > 0:
                result += f"{imported_count} new students added"
            if updated_count > 0:
                if imported_count > 0:
                    result += f", {updated_count} students updated"
                else:
                    result += f"{updated_count} students updated"
            result += f". Total students: {len(students)}. Data saved to {JSON_FILE}."
            return result
        else:
            return f"Processed data but failed to save to {JSON_FILE}."
            
    except Exception as e:
        return f"Error importing and merging CSV: {e}"


def validate_csv_format(file_path: str) -> str:
    """
    Validate CSV file format before importing.
    
    Args:
        file_path: Path to the CSV file to validate
        
    Returns:
        Validation result message
    """
    try:
        if not os.path.exists(file_path):
            return f"File '{file_path}' not found."
        
        valid_rows = 0
        total_rows = 0
        issues = []
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            for row_num, row in enumerate(reader, 1):
                total_rows += 1
                if len(row) < 2:
                    issues.append(f"Row {row_num}: Not enough columns")
                    continue
                
                name = row[0].strip()
                try:
                    age = int(row[1].strip())
                    if not name:
                        issues.append(f"Row {row_num}: Empty name")
                    elif not (0 <= age <= 150):
                        issues.append(f"Row {row_num}: Invalid age {age}")
                    else:
                        valid_rows += 1
                except ValueError:
                    if row_num == 1 and row[1].lower() in ['age', 'years', 'old']:
                        # Likely header row
                        continue
                    issues.append(f"Row {row_num}: Invalid age '{row[1]}'")
        
        result = f"CSV Validation Results for '{file_path}':\n"
        result += f"Total rows: {total_rows}\n"
        result += f"Valid student records: {valid_rows}\n"
        
        if issues:
            result += f"Issues found ({len(issues)}):\n"
            for issue in issues[:5]:  # Show first 5 issues
                result += f"  - {issue}\n"
            if len(issues) > 5:
                result += f"  ... and {len(issues) - 5} more issues\n"
        
        if valid_rows > 0:
            result += f"\nFile is ready for import ({valid_rows} valid records)."
        else:
            result += f"\nFile cannot be imported (no valid records found)."
        
        return result
        
    except Exception as e:
        return f"Error validating CSV: {e}"

def get_student_stats() -> str:
    try:
        if not students:
            return "No students in database."
        
        ages = list(students.values())
        total_students = len(students)
        avg_age = sum(ages) / total_students
        min_age = min(ages)
        max_age = max(ages)
        
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
