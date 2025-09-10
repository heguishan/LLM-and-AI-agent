class CuteCat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def speak(self, content):
        print("喵" * self.age)
        print(f"小猫在说\"{content}\"")

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grade = {"Chinese":0, "Math":0, "English":0}
    def set_score(self, course, score):
        if course in self.grade:
            self.grade[course] = score
    def get_score(self):
        print(f"{self.name}的成绩为")
        for course in self.grade:
            print(f"{course}: {self.grade[course]}")


cat1 = CuteCat("Jack", "blue", 3)
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
cat1.speak("我是狗")

Qi = Student("Qi", 2120230367)
Qi.set_score("Chinese", 100)
Qi.get_score()
