# Bag.py

class Bag:
    # 클래스 변수
    color = "black"     # 속성(명사)

    # 클래스 생성시 데이터 초기화 목적으로 사용
    def __init__(self):
        self.data=["우산"]

    # 가방에 넣다
    def add(self, x):   # 기능(동사)
        # 인스턴스 변수
        # self.data = []
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

handbag = Bag()
print(handbag.data)
# print(handbag.color)
handbag.add("핸드폰")
print(handbag.data)
handbag.addtwice("신용카드")
print(handbag.data)

print("---------------------")

backpack = Bag()
# print(handbag.color)
backpack.add("노트북")
print(backpack.data)
backpack.addtwice("헬멧")
print(backpack.data)