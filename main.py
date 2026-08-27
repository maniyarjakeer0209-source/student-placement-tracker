class StudentProfile:
    platform = "KodNest"
    total_students = 0

    def __init__(self, student_id, name, branch, score):
        self.student_id = student_id
        self.name = StudentProfile.normalize_name(name)
        self.branch = branch
        self.__score = 0
        self.score = score
        StudentProfile.total_students += 1

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if StudentProfile.is_valid_score(value):
            self.__score = value
        else:
            print("Invalid score. Score must be between 0 and 100.")

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @staticmethod
    def normalize_name(name):
        return name.strip().title()

    def get_placement_status(self):
        if 80 <= self.score <= 100:
            return "Placement Ready"
        elif 60 <= self.score <= 79:
            return "Needs More Practice"
        else:
            return "Not Ready"

    def display_profile(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Mock Score: {self.score}")
        print(f"Placement Status: {self.get_placement_status()}")
        print(f"Platform: {self.platform}")

    @classmethod
    def from_string(cls, student_data):
        student_id, name, branch, score = student_data.split(",")
        name = cls.normalize_name(name)
        score = int(score)
        return cls(student_id, name, branch, score)

    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

    @classmethod
    def show_total_students(cls):
        print(f"Total Students: {cls.total_students}")


students = []

while True:
    print("\n===== Student Placement Tracker =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Score")
    print("4. Change Platform")
    print("5. Show Total Students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        student_data = input("Enter student details: ").strip()
        student_id = student_data.split(",")[0].strip()

        if any(student.student_id == student_id for student in students):
            print("Student ID already exists.")
        else:
            student = StudentProfile.from_string(student_data)
            students.append(student)
            print("Student added successfully.")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for student in students:
                student.display_profile()

    elif choice == "3":
        student_id = input("Enter Student ID: ").strip()
        student = None

        for current_student in students:
            if current_student.student_id == student_id:
                student = current_student
                break

        if student is None:
            print("Student not found.")
        else:
            new_score = int(input("Enter New Score: "))

            if StudentProfile.is_valid_score(new_score):
                student.score = new_score
                print("Score updated successfully.")
                print(f"Updated Score: {student.score}")
                print(f"Updated Status: {student.get_placement_status()}")
            else:
                print("Invalid score. Score was not updated.")

    elif choice == "4":
        new_platform = input("Enter the new platform name: ").strip()
        StudentProfile.change_platform(new_platform)
        print("Platform changed successfully.")

    elif choice == "5":
        StudentProfile.show_total_students()

    elif choice == "6":
        print("Thank you for using the Student Placement Tracker.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 6.")