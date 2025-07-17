class Human:
    # 멤버 변수

    # 멤버 함수(메서드)
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def intro(self):
        print("나이: ",self.age)
        print("나이: ",self.name)

kim = Human(29, "김상형")
kim.intro()
# print("나이:",kim.age)
# print("이름:",kim.name)

lee = Human(45, "이승우")
lee.intro