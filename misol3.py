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
        n =int(input(" n = "))
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i == 1 or i == n or j == 1 or j == i:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()  # Yangi qator

class Tortburchak(Shape):
    def draw(self):
        print("tortburchak:")
        kenglik = int(input("Kengliginini kiriting: "))
        balandlik = int(input("Balandligini kiriting: "))
        print('*' * kenglik)
        for _ in range(balandlik - 2):
            print('*' + ' ' * (kenglik - 2) + '*')
        print('*' * kenglik)

class BoshShakl(Shape):
    def draw(self):
        print("bo'sh shakl")

shakl_nomi = input("chiziq\nuchburchak\ntortburchak\nTanlang: ")

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
