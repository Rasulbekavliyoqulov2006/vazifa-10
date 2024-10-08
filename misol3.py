class Shape:
    def draw(self):
        pass

class Chiziq(Shape):
    def draw(self):
        print("chiziq:")
        print("*" * 30)


class Uchburchak(Shape):
    def draw(self):
        print("uchburchak:")
        balandlik =int(input(" son kiriting: "))
        for i in range(balandlik):
            print(' ' * (balandlik - i - 1) + '*' * (2 * i + 1))

class Tortburchak(Shape):
    def draw(self):
        print("tortburchak:")
        kenglik =int(input(" kengliginini  kiriting: "))
        balandlik = int(input(" balandligini kiriting:"))
        print('*' * kenglik)
        for _ in range(balandlik - 2):
            print('*' + ' ' * (kenglik - 2) + '*')
        print('*' * kenglik)

class BoshShakl(Shape):
    def draw(self):
        print("bo'sh shakl")

shakl_nomi = input("chiziq\nuchburchak\ntortburchak\ntanlang:  ")

match shakl_nomi.lower():
    case "chiziq":
        shakl = Chiziq()
    case "uchburchak":
        shakl = Uchburchak()
    case "tortburchak":
        shakl = Tortburchak()
    case _:
        shakl = BoshShakl()

shakl.draw()
