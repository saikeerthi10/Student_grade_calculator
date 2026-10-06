def get_letter_grade(percentage):
    """Determines the letter grade based on the calculated percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=========================================")
    print("       STUDENT GRADE CALCULATOR          ")
    print("=========================================")
   
    # 1. Take Student Information
    student_name = input("Enter student name: ").strip()
   
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("❌ Number of subjects must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a whole number.")
        return

    # 2. Collect Subject Marks with Validation
    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("⚠️ Invalid marks! Score must be between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid numerical score.")

    # 3. Perform Calculations
    total_marks = sum(marks)
    max_possible_marks = num_subjects * 100
    average_percentage = (total_marks / max_possible_marks) * 100
    final_grade = get_letter_grade(average_percentage)

    # 4. Display the Performance Summary
    print("\n=========================================")
    print("           PERFORMANCE REPORT            ")
    print("=========================================")
    print(f"Student Name:      {student_name}")
    print(f"Total Marks:       {total_marks:.2f} / {max_possible_marks}")
    print(f"Average percentage: {average_percentage:.2f}%")
    print(f"Final Grade:       {final_grade}")
    print("=========================================")

if __name__ == "__main__":
    main()
def get_letter_grade(percentage):
    """Determines the letter grade based on the calculated percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=========================================")
    print("       STUDENT GRADE CALCULATOR          ")
    print("=========================================")
   
    # 1. Take Student Information
    student_name = input("Enter student name: ").strip()
   
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("❌ Number of subjects must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a whole number.")
        return

    # 2. Collect Subject Marks with Validation
    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("⚠️ Invalid marks! Score must be between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid numerical score.")

    # 3. Perform Calculations
    total_marks = sum(marks)
    max_possible_marks = num_subjects * 100
    average_percentage = (total_marks / max_possible_marks) * 100
    final_grade = get_letter_grade(average_percentage)

    # 4. Display the Performance Summary
    print("\n=========================================")
    print("           PERFORMANCE REPORT            ")
    print("=========================================")
    print(f"Student Name:      {student_name}")
    print(f"Total Marks:       {total_marks:.2f} / {max_possible_marks}")
    print(f"Average percentage: {average_percentage:.2f}%")
    print(f"Final Grade:       {final_grade}")
    print("=========================================")

if __name__ == "__main__":
    main()
def get_letter_grade(percentage):
    """Determines the letter grade based on the calculated percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=========================================")
    print("       STUDENT GRADE CALCULATOR          ")
    print("=========================================")
   
    # 1. Take Student Information
    student_name = input("Enter student name: ").strip()
   
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("❌ Number of subjects must be greater than zero.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a whole number.")
        return

    # 2. Collect Subject Marks with Validation
    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("⚠️ Invalid marks! Score must be between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid numerical score.")

    # 3. Perform Calculations
    total_marks = sum(marks)
    max_possible_marks = num_subjects * 100
    average_percentage = (total_marks / max_possible_marks) * 100
    final_grade = get_letter_grade(average_percentage)

    # 4. Display the Performance Summary
    print("\n=========================================")
    print("           PERFORMANCE REPORT            ")
    print("=========================================")
    print(f"Student Name:      {student_name}")
    print(f"Total Marks:       {total_marks:.2f} / {max_possible_marks}")
    print(f"Average percentage: {average_percentage:.2f}%")
    print(f"Final Grade:       {final_grade}")
    print("=========================================")

if __name__ == "__main__":
    main()
