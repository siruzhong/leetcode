class Student:
    def __init__(self, id, sex, age, classes):
        self.id = id
        self.sex = sex
        self.age = age
        self.classes = classes

    def __str__(self):
        return f"Student{{id={self.id}, sex='{self.sex}', age={self.age}, classes='{self.classes}'}}"


class StudentHashTable:
    def __init__(self, size):
        self.size = size
        self.student_arr = [[] for _ in range(size)]

    def hash(self, id):
        return id % self.size

    def add(self, student):
        index = self.hash(student.id)
        self.student_arr[index].append(student)

    def list(self):
        for i, students in enumerate(self.student_arr):
            print(f"第{i}个链表中的学生为:")
            for student in students:
                print(student)

    def find_student_by_id(self, id):
        index = self.hash(id)
        for student in self.student_arr[index]:
            if student.id == id:
                return student
        return None

    def delete_student_by_id(self, id):
        index = self.hash(id)
        self.student_arr[index] = [student for student in self.student_arr[index] if student.id != id]


if __name__ == "__main__":
    hash_table = StudentHashTable(3)

    # 添加学生
    hash_table.add(Student(1, "Male", 20, "Compute Science"))
    hash_table.add(Student(2, "Male", 20, "Computer Science"))
    hash_table.add(Student(3, "Male", 20, "Computer Science"))
    hash_table.add(Student(4, "Male", 20, "Computer Science"))
    hash_table.add(Student(5, "Female", 19, "Computer Science"))
    hash_table.add(Student(6, "Female", 19, "Computer Science"))
    hash_table.add(Student(7, "Female", 19, "Computer Science"))
    hash_table.add(Student(8, "Female", 19, "Computer Science"))
    hash_table.add(Student(9, "Female", 19, "Computer Science"))

    # 查看所有学生
    hash_table.list()

    # 查找学号为3的学生
    student = hash_table.find_student_by_id(3)
    if student:
        print(f"找到学生: {student}")
    else:
        print("没有找到该学生")

    # 删除学号为6的学生
    hash_table.delete_student_by_id(6)

    # 查看所有学生
    hash_table.list()