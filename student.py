# Quyidagi parametr va metodlardan foydalanib, Student nomli class yarating.  
# Dastur classdan tashqari to’g’ridan to’gri talabaning ismi, id raqami  va 
# bahosini bilishga yo’l o’ymasligi lozim. Faqat metodlar orqali talabaning 
# ismi, id raqami va bahosini ekranga chiqaruvchi dastur yarating. Dasturda 
# ball 0  va 100 orasida bo’lishi ta’minlansin.
# Student atributlari: name, id, grade (standart atribut)
# Student metodlari: get_grade(), set_grade()

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 < new_grade <= 100:
            self.grade = new_grade
        else:
            print("Noto'g'ri baho")

if __name__ == "__main__":
    student = Student("Surayyo", 123456, 5)
    print("Student Name:", student.name)
    print("Student ID:", student.student_id)
    print("Student Grade:", student.get_grade())

    student.set_grade(10)
    print("Student new_Grade:", student.get_grade())
