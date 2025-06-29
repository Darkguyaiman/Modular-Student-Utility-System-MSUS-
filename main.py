import math_utils
import text_utils
import student_utils
import sys
import os

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
    print("\n--- Import Students from CSV ---")
    try:
        print("Warning: This will replace current student data with CSV data.")
        confirm = get_safe_input("Continue? (yes/no): ", "string")
        if confirm is None or confirm.lower() not in ['yes', 'y']:
            print("Import cancelled.")
            return
        
        result = student_utils.import_from_csv()
        print(f"\n{result}")
        
    except Exception as e:
        print(f"Error: {e}")

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
                choice = input("Enter your choice (0-13): ").strip()
                
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
                else:
                    print("\nInvalid choice. Please select a number from 0-13.")
                    
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
