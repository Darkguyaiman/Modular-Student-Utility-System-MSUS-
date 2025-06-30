import math_utils
import text_utils
import student_utils
import sys
import os
import csv

def display_menu():
    print("\n" + "="*50)
    print("     Modular Student Utility System (MSUS)")
    print("="*50)
    print("1.  Count Even and Odd Numbers")
    print("2.  Calculate Sum of Digits")
    print("3.  Get Letter Grade from Mark")
    print("4.  Reverse a Sentence")
    print("5.  Lookup Student Age")
    print("6.  Add New Student")
    print("7.  Remove Student")
    print("8.  List All Students")
    print("9.  Student Database Statistics")
    print("10. Export Students to CSV")
    print("11. Import Students from CSV")
    print("12. Math Operations (Average, Min/Max)")
    print("13. Text Operations (Word Count, Capitalize)")
    print("14. Create Sample CSV File")
    print("0.  Exit")
    print("-"*50)

def get_safe_input(prompt: str, input_type: str = "string") -> any:
    while True:
        try:
            user_input = input(prompt).strip()
            
            if input_type == "int":
                return int(user_input)
            elif input_type == "float":
                return float(user_input)
            elif input_type == "string":
                if not user_input:
                    print("Input cannot be empty. Please try again.")
                    continue
                return user_input
            else:
                return user_input
                
        except ValueError as e:
            print(f"Invalid input. Please enter a valid {input_type}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

def get_integer_list() -> list[int]:
    while True:
        try:
            numbers_str = input("Enter numbers separated by spaces: ").strip()
            if not numbers_str:
                print("Please enter at least one number.")
                continue
                
            numbers = []
            for num_str in numbers_str.split():
                try:
                    numbers.append(int(num_str))
                except ValueError:
                    print(f"'{num_str}' is not a valid integer. Please try again.")
                    raise ValueError("Invalid number in list")
            
            if not numbers:
                print("Please enter at least one number.")
                continue
                
            return numbers
            
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

def handle_count_even_odd():
    print("\n--- Count Even and Odd Numbers ---")
    try:
        numbers = get_integer_list()
        if numbers is None:
            return
            
        even_count, odd_count = math_utils.count_even_odd(numbers)
        
        print(f"\nResults for {numbers}:")
        print(f"Even numbers: {even_count}")
        print(f"Odd numbers: {odd_count}")
        print(f"Total numbers: {len(numbers)}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_sum_of_digits():
    print("\n--- Calculate Sum of Digits ---")
    try:
        number = get_safe_input("Enter a number: ", "int")
        if number is None:
            return
            
        digit_sum = math_utils.sum_of_digits(number)
        print(f"\nSum of digits in {number}: {digit_sum}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_get_grade():
    print("\n--- Get Letter Grade from Mark ---")
    try:
        while True:
            mark = get_safe_input("Enter mark (0-100): ", "int")
            if mark is None:
                return
            if 0 <= mark <= 100:
                break
            print("Mark must be between 0 and 100.")
        
        grade = text_utils.get_grade(mark)
        print(f"\nMark: {mark} → Grade: {grade}")
        
        print("\nGrade Scale:")
        print("A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_reverse_sentence():
    print("\n--- Reverse a Sentence ---")
    try:
        sentence = get_safe_input("Enter a sentence: ", "string")
        if sentence is None:
            return
        
        reversed_sentence = text_utils.reverse_sentence(sentence)
        print(f"\nOriginal: {sentence}")
        print(f"Reversed: {reversed_sentence}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_lookup_student():
    print("\n--- Lookup Student Age ---")
    try:
        name = get_safe_input("Enter student name: ", "string")
        if name is None:
            return
        
        result = student_utils.lookup_student(name)
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_add_student():
    print("\n--- Add New Student ---")
    try:
        name = get_safe_input("Enter student name: ", "string")
        if name is None:
            return
        
        while True:
            age = get_safe_input("Enter student age (0-150): ", "int")
            if age is None:
                return
            if 0 <= age <= 150:
                break
            print("Age must be between 0 and 150.")
        
        result = student_utils.add_student(name, age)
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_remove_student():
    print("\n--- Remove Student ---")
    try:
        print("Current students:")
        print(student_utils.list_all_students())
        print()
        
        name = get_safe_input("Enter student name to remove: ", "string")
        if name is None:
            return
        
        confirm = get_safe_input(f"Are you sure you want to remove {name}? (yes/no): ", "string")
        if confirm is None or confirm.lower() not in ['yes', 'y']:
            print("Removal cancelled.")
            return
        
        result = student_utils.remove_student(name)
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_list_students():
    print("\n--- All Students ---")
    try:
        result = student_utils.list_all_students()
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_student_stats():
    print("\n--- Student Database Statistics ---")
    try:
        result = student_utils.get_student_stats()
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_export_csv():
    print("\n--- Export Students to CSV ---")
    try:
        result = student_utils.export_to_csv()
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_import_csv():
    """Handle importing students from a custom CSV file with error handling."""
    print("\n--- Import Students from CSV ---")
    try:
        print("Choose import option:")
        print("1. Use default CSV file (students.csv)")
        print("2. Specify custom CSV file path")
        print("3. Validate CSV file format first")
        
        choice = get_safe_input("Enter choice (1-3): ", "string")
        if choice is None:
            return
        
        if choice == "1":
            # Use default CSV file
            file_path = "students.csv"
            if not os.path.exists(file_path):
                print(f"Default file '{file_path}' not found.")
                return
        
        elif choice == "2":
            # Get custom file path
            print("\nEnter the full path to your CSV file:")
            print("Examples:")
            print("  Windows: C:\\Users\\YourName\\Documents\\students.csv")
            print("  Mac/Linux: /home/username/documents/students.csv")
            print("  Relative: ./data/students.csv")
            
            file_path = get_safe_input("File path: ", "string")
            if file_path is None:
                return
            
            # Remove quotes if user added them
            file_path = file_path.strip('"\'')
            
        elif choice == "3":
            # Validate file first
            print("\nEnter the path to the CSV file you want to validate:")
            file_path = get_safe_input("File path: ", "string")
            if file_path is None:
                return
            
            file_path = file_path.strip('"\'')
            validation_result = student_utils.validate_csv_format(file_path)
            print(f"\n{validation_result}")
            
            if "ready for import" in validation_result.lower():
                proceed = get_safe_input("\nProceed with import? (yes/no): ", "string")
                if proceed is None or proceed.lower() not in ['yes', 'y']:
                    print("Import cancelled.")
                    return
            else:
                print("Please fix the issues in your CSV file before importing.")
                return
        
        else:
            print("Invalid choice.")
            return
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            print("Please check the path and try again.")
            return
        
        # Show current data warning
        if len(student_utils.students) > 0:
            print(f"\nWarning: This will replace current student data ({len(student_utils.students)} students).")
            print("Choose import mode:")
            print("1. Replace all data (current data will be lost)")
            print("2. Merge with existing data (update existing, add new)")
            
            mode_choice = get_safe_input("Enter choice (1-2): ", "string")
            if mode_choice is None:
                return
            
            if mode_choice == "1":
                confirm = get_safe_input("Are you sure you want to replace all data? (yes/no): ", "string")
                if confirm is None or confirm.lower() not in ['yes', 'y']:
                    print("Import cancelled.")
                    return
                result = student_utils.import_from_csv(file_path)
            elif mode_choice == "2":
                result = student_utils.import_and_merge_csv(file_path)
            else:
                print("Invalid choice. Import cancelled.")
                return
        else:
            # No existing data, just import
            result = student_utils.import_from_csv(file_path)
        
        print(f"\n{result}")
        
        # Show sample of imported data
        if "Successfully" in result:
            print("\nSample of imported data:")
            sample_students = list(student_utils.students.items())[:5]
            for name, age in sample_students:
                print(f"  - {name}: {age} years old")
            if len(student_utils.students) > 5:
                print(f"  ... and {len(student_utils.students) - 5} more students")
        
    except Exception as e:
        print(f"Error: {e}")


def handle_create_sample_csv():
    """Create a sample CSV file for users to understand the format."""
    print("\n--- Create Sample CSV File ---")
    try:
        file_path = get_safe_input("Enter path for sample CSV file (e.g., sample_students.csv): ", "string")
        if file_path is None:
            return
        
        file_path = file_path.strip('"\'')
        
        # Create sample data
        sample_data = [
            ["Name", "Age"],
            ["John Smith", "20"],
            ["Emma Johnson", "19"],
            ["Michael Brown", "21"],
            ["Sarah Davis", "22"],
            ["David Wilson", "20"]
        ]
        
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)
        
        print(f"\nSample CSV file created: {file_path}")
        print("The file contains:")
        print("- Header row: Name, Age")
        print("- 5 sample student records")
        print("- Proper CSV formatting")
        print("\nYou can edit this file and import it using option 11.")
        
    except Exception as e:
        print(f"Error creating sample CSV: {e}")

def handle_math_operations():
    print("\n--- Math Operations ---")
    try:
        numbers = get_integer_list()
        if numbers is None:
            return
        
        average = math_utils.calculate_average(numbers)
        print(f"\nNumbers: {numbers}")
        print(f"Average: {average:.2f}")
        
        min_val, max_val = math_utils.find_min_max(numbers)
        print(f"Minimum: {min_val}")
        print(f"Maximum: {max_val}")
        print(f"Range: {max_val - min_val}")
        
    except Exception as e:
        print(f"Error: {e}")

def handle_text_operations():
    print("\n--- Text Operations ---")
    try:
        text = get_safe_input("Enter text: ", "string")
        if text is None:
            return
        
        word_count = text_utils.count_words(text)
        print(f"\nOriginal text: {text}")
        print(f"Word count: {word_count}")
        
        capitalized = text_utils.capitalize_words(text)
        print(f"Capitalized: {capitalized}")
        
        vowels, consonants = text_utils.count_vowels_consonants(text)
        print(f"Vowels: {vowels}, Consonants: {consonants}")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    try:
        print("Welcome to the Enhanced Modular Student Utility System!")
        print("Features: File I/O, Data Persistence, Error Handling")
        
        if os.path.exists("students.json"):
            print("Found existing student database")
        else:
            print("Will create new student database")
        
        while True:
            try:
                display_menu()
                choice = input("Enter your choice (0-14): ").strip()
                
                if choice == '0':
                    print("\nSaving data and exiting...")
                    if student_utils.save_students_to_json():
                        print("Data saved successfully!")
                    else:
                        print("Warning: Could not save data to file")
                    print("Thank you for using MSUS! Goodbye!")
                    break
                    
                elif choice == '1':
                    handle_count_even_odd()
                elif choice == '2':
                    handle_sum_of_digits()
                elif choice == '3':
                    handle_get_grade()
                elif choice == '4':
                    handle_reverse_sentence()
                elif choice == '5':
                    handle_lookup_student()
                elif choice == '6':
                    handle_add_student()
                elif choice == '7':
                    handle_remove_student()
                elif choice == '8':
                    handle_list_students()
                elif choice == '9':
                    handle_student_stats()
                elif choice == '10':
                    handle_export_csv()
                elif choice == '11':
                    handle_import_csv()
                elif choice == '12':
                    handle_math_operations()
                elif choice == '13':
                    handle_text_operations()
                elif choice == '14':
                    handle_create_sample_csv()
                else:
                    print("\nInvalid choice. Please select a number from 0-14.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                save_choice = input("Save data before exiting? (yes/no): ").strip().lower()
                if save_choice in ['yes', 'y']:
                    if student_utils.save_students_to_json():
                        print("Data saved successfully!")
                    else:
                        print("Warning: Could not save data")
                print("Goodbye!")
                break
            except Exception as e:
                print(f"\nUnexpected error in main menu: {e}")
                print("Please try again or contact support if the problem persists.")
            
            try:
                input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                continue
                
    except Exception as e:
        print(f"\nCritical error in main program: {e}")
        print("Program will now exit.")
        sys.exit(1)

if __name__ == "__main__":
    main()
