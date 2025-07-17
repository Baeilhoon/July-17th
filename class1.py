#class1.py

# class 클래스명:
#     멤버변수1 : 속성_값1
#     def 함수1(self, 매개변수):
#         동작_코드블록
#     def 함수2(self):
#         self.멤버변수2 : 속성_값2
#         return 반환값  
# 객체명 = 클래스명(인수)

class Singer:
    name = "아이유"
    name1 = "거북이"

    def sing(self):
        print("이 밤 그날의 반딧불을 당신의 창 가까이에 보낼게요~")

iu = Singer()

# 멤버변수 사용
print(iu.name)

# 멤버변수 사용
iu.sing()

print("---------------------------------")
class Cexm:
    varl = 10       # 클래스 멤버 변수 정의
    x = 20
    def fsam(self):
        print("멤버 함수(메소드)")
    def fsbm(self, pa):
        self.x = pa # 인스턴스 멤버 변수
        print("멤버 변수 x는", self.x)
ca = Cexm()
print(Cexm.x)       # 클래스 멤버 변수 사용
print(ca.x)         # 인스턴스 멤버 변수 사용
ca.fsam()
ca.fsbm(10)
print(ca.x)         # 인스턴스 멤버 변수 사용

# <네임스페이스와 변수 관계>
# 클래스 사용에서 메서드의 지역/전역 범위는 동작이 상이

# 메서드 안에서만 쓰이는 변수 => 지역변수
# 클래스 밖에서 정의된 변수 => 전역변수

# 클래스 블록에서 정의된 변수 => 클래스 변수
    # (모든 객체 공유 가능)
# 클래스 객체를 통해 메서드 안에서 정의된 변수 => 인스턴스 변수
    # (해당 객체 사용 가능)

na = 10
nb = int("10")
print(type(nb))
print(nb)