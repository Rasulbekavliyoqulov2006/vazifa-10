import json

class Komanda:
    def __init__(self, nom, ishtirokchilar_son, trener, kapitan):
        self.nomi = nom
        self.ishtirokchilar_soni = ishtirokchilar_son
        self.trener = trener
        self.kapitani = kapitan
    def __str__(self):
        return f"komanda: {self.nomi}, ishtirokchilar soni: {self.ishtirokchilar_soni}, trener: {self.trener}, kapitani: {self.kapitani}"

    def to_dict(self):
        return {
            "nomi": self.nomi,
            "ishtirokchilar_soni": self.ishtirokchilar_soni,
            "trener": self.trener,
            "kapitani": self.kapitani
        }

class Liga:
    def __init__(self):
        self.komandalar = []

    def komanda_qoshish(self, komanda):
        self.komandalar.append(komanda)

    def komandalarni_chiqaring(self):
        komandalar = sorted(self.komandalar, key=lambda x: x.nomi)
        for komanda in komandalar:
            print(komanda)

    def komanda_qidirish(self, new_komanda):
        for komanda in self.komandalar:
            if komanda.nomi == new_komanda.lower():
                print(komanda)
                return
        print("bunday komanda yo'q.")

liga = Liga()

n = int(input("nechta komanda qo'shasiz: "))
for i in range(n):
    nomi = input(f"{i + 1}-komanda nomini kiriting: ")
    ishtirokchilar_soni = int(input(f"{i + 1}-komanda ishtirokchilar sonini kiriting: "))
    trener = input(f"{i + 1}-komanda trenerini kiriting: ")
    kapitani = input(f"{i + 1}-komanda kapitani nomini kiriting: ")
    komanda = Komanda(nomi, ishtirokchilar_soni, trener, kapitani)
    liga.komanda_qoshish(komanda)
    print()

print("\nsaralangan komandalar:")
liga.komandalarni_chiqaring()

new_komanda = input("\nkerak komanda nomini kiriting: ")
liga.komanda_qidirish(new_komanda)

with open("misol4.json", "a") as file:
    json.dump([komanda.to_dict() for komanda in liga.komandalar], file, indent=4)
