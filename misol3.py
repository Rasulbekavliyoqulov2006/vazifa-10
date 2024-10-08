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
        n = int(input("n = "))
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i == 1 or i == n or j == 1 or j == i:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()

class Tortburchak(Shape):
    def draw(self):
        print("tortburchak:")
        n = int(input("n = "))
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()

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
