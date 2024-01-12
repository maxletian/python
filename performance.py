def enter_marks():
    students = []
    
    num_students = int(input("Enter the number of students: "))
    num_subjects = 5
    
    for i in range(num_students):
        student_name = input(f"Enter the name of student {i + 1}: ")
        marks = []
        
        for j in range(num_subjects):
            subject_mark = float(input(f"Enter marks for subject {j + 1} for {student_name}: "))
            marks.append(subject_mark)
        
        students.append({'name': student_name, 'marks': marks, 'total': sum(marks)})
    
    return students

def sort_students(students):
    return sorted(students, key=lambda x: x['total'], reverse=True)

def display_students(students):
    print("\nSorted Students based on Total Marks:")
    print("{:<15} {:<10}".format("Student Name", "Total Marks"))
    
    for student in students:
        print("{:<15} {:<10}".format(student['name'], student['total']))

if __name__ == "__main__":
    students_data = enter_marks()
    sorted_students = sort_students(students_data)
    display_students(sorted_students)
