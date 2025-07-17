#class1.py

# class 클래스:
#     멤버변수1 : 속성_값1
#     def 함수1(self):
#         동작_코드블록
#     def 함수2(self):
#         self.멤버변수2 : 속성_값2

class Singer:
    name = "아이유"
    def sing(self):
        print("이 밤 그날의 반딧불을 당신의 창 가까이에 보낼게요~")

iu = Singer()
print(iu.name)
iu.sing()