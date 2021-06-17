class student:
    student_count = 0

    def __init__(self, name, grade, drink):
     self.name = name
     self.grade = grade
     self.drink = drink
     student.student_count += 1

    def info(self):
        print(f'이름 : {self.name}')
        print(f'학년 : {self.grade}')
        print(f'최애술집 : {self.drink}')
        print()

    def attack(self, drink_num):
        print(self.drink[drink_num])

student1 = student('권순성', 2, '사군자')
student2 = student('천우희', 2, ['라바라운지','청춘'])
student3 = student('강하늘', 3, ['말자싸롱','마요네즈'])



student1.info()
student2.info()
student3.info()

student2.attack(0)
student3.attack(0)

