class Animal:
    def __init__(self, name,sound):
        self.name = name
        self.sound = sound

    def s(self):
        print(self.sound)

cat=Animal('고양이','야옹')
print(cat.name)
cat.s()