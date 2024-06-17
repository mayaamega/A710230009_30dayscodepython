class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("List of Students:")
        for student in self.students:
            print(student)

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def remove_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"{name} has been removed.")
                return
        print(f"Student with name {name} not found.")

# Contoh penggunaan program:
if __name__ == "__main__":
    # Membuat objek manager siswa
    manager = StudentManager()

    # Menambahkan data siswa
    student1 = Student("Kim Seokjin", 31, "Senior")
    student2 = Student("Park Sung-hoon", 21, "Junior")

    manager.add_student(student1)
    manager.add_student(student2)

    # Menampilkan daftar siswa
    manager.display_students()

    # Mencari siswa berdasarkan nama
    search_name = "Kim Seokjin"
    found_student = manager.search_student(search_name)
    if found_student:
        print(f"\nFound student: {found_student}\n")
    else:
        print(f"\nStudent with name '{search_name}' not found.\n")

    # Menghapus siswa
    remove_name = "Park Sung-hoon"
    manager.remove_student(remove_name)

    # Menampilkan daftar siswa setelah penghapusan
    manager.display_students()
