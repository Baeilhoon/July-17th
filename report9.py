# class Phone:
#     def __init__(self, company, year, color):
#         print('휴대폰 생성')
#         self.company = company
#         self.year = year
#         self.color = color
#         print('제조사:',self.company)
#         print('출고년도:',self.year)
#         print('색상:',self.color)

# my_phone = Phone('rokey',2025,'black')

# print("----------------------")

# class Phone:
#     def __init__(self):
#         print('휴대폰 생성')
    
#     def info(self,company,year,color):
#         self.company = company
#         self.year = year
#         self.color = color
#         print('제조사:',self.company)
#         print('출고년도:',self.year)
#         print('색상:',self.color)

# my_phone = Phone()
# my_phone.info('rokey',2025,'black')

print("----------------------")

class Phone:
    def __init__(self):
        print('휴대폰 생성')

    def setInfo(self):
          company = input("제조사를 입력하세요:")
          year = input("출고년도를 입력하세요:")
          color = input("색상을 입력하세요:")
          self.company = company
          self.year = year
          self.color = color

    def info(self):
        print('제조사:',self.company)
        print('출고년도:',self.year)
        print('색상:',self.color)

my_phone = Phone()
my_phone.setInfo()
my_phone.info()

# example.py


### 10차시 예습
def foo():
    print("foo() 호출")

if __name__ == "__main__":
    # 이 블록은 example.py를
    # 직접 실행할 때만 동작
    foo()

print("---------------------")

class Animal:
    def sound(self):
        print("소리를 낸다")

class Dog(Animal):
    def sound(self):
        print("멍멍")   # 부모의 sound를 ‘멍멍’으로 바꿈

class Cat(Animal):
    def sound(self):
        print("야옹")

animal = Animal()
animal.sound()
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()