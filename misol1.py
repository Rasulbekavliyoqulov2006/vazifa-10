import json
import time

class Kitob:
    def __init__(self, nomi, muallifi, janri, narxi):
        self.nomi = nomi
        self.muallifi = muallifi
        self.janri = janri
        self.narxi = narxi



    def to_dict(self):
        return {
            "nomi": self.nomi,
            "muallifi": self.muallifi,
            "janri": self.janri,
            "narxi": self.narxi
        }
    



class Foydalanuvchi:
    def __init__(self, ism, login, parol):
        self.ism = ism
        self.login = login
        self.parol = parol



    def to_dict(self):
        return {
            "ism": self.ism,
            "login": self.login,
            "parol": self.parol
        }
    



class Kutubxona:
    def __init__(self):
        self.kitoblar = []
        self.foydalanuvchilar = []




    def kitob_qoshish(self, kitob):
        self.kitoblarni_yuklash() 
        self.kitoblar.append(kitob)
        self.kitoblarni_saqlash()  



    def kitoblarni_saqlash(self, fayl_nomi="misol1_kitob.json"):
        kitoblar_dict = [kitob.to_dict() for kitob in self.kitoblar]
        with open(fayl_nomi, 'w') as fayl:
            json.dump(kitoblar_dict, fayl, ensure_ascii=False, indent=4)





    def kitoblarni_yuklash(self, fayl_nomi="misol1.json"):
        try:
            with open(fayl_nomi, 'r') as fayl:
                kitoblar_dict = json.load(fayl)
                self.kitoblar = [Kitob(**kitob) for kitob in kitoblar_dict]
        except FileNotFoundError:
            print(f"{fayl_nomi} fayli topilmadi!")




    def kitobni_qidirish(self, kitob_nomi):
        self.kitoblarni_yuklash()  
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == kitob_nomi.lower():
                time.sleep(1)
                return f"Kitob topildi: {kitob.nomi}, Muallif: {kitob.muallifi}, Janr: {kitob.janri}, Narx: {kitob.narxi} so'm"
        return "Bunday kitob topilmadi."




    def foydalanuvchi_royxatdan_otish(self, foydalanuvchi):
        for foydalanuvchi_obj in self.foydalanuvchilar:
            if foydalanuvchi_obj.login == foydalanuvchi.login:
                return "Bunday login mavjud, boshqa login tanlang."
        self.foydalanuvchilar.append(foydalanuvchi)
        self.foydalanuvchilarni_saqlash()
        return f"Foydalanuvchi ro'yxatdan o'tdi: {foydalanuvchi.ism}"
    

    

    def foydalanuvchi_tizimga_kirish(self, login, parol):
        for foydalanuvchi in self.foydalanuvchilar:
            if foydalanuvchi.login == login and foydalanuvchi.parol == parol:
                return f"Xush kelibsiz, {foydalanuvchi.ism}!"
        return "Login yoki parol xato!"





    def foydalanuvchilarni_saqlash(self, fayl_nomi="misol1_foydalanuvchilar.json"):
        foydalanuvchilar_dict = [foydalanuvchi.to_dict() for foydalanuvchi in self.foydalanuvchilar]
        with open(fayl_nomi, 'w') as fayl:
            json.dump(foydalanuvchilar_dict, fayl, ensure_ascii=False, indent=4)




    def foydalanuvchilarni_yuklash(self, fayl_nomi="misol1_foydalanuvchilar.json"):
        try:
            with open(fayl_nomi, 'r') as fayl:
                foydalanuvchilar_dict = json.load(fayl)
                self.foydalanuvchilar = [Foydalanuvchi(**foydalanuvchi) for foydalanuvchi in foydalanuvchilar_dict]
        except FileNotFoundError:
            print(f"{fayl_nomi} fayli topilmadi!")





kutubxona = Kutubxona()
kutubxona.foydalanuvchilarni_yuklash("misol1_foydalanuvchilar.json")



tekshiruv = input("Ro'yxatdan o'tganmisiz?(ha/yo'q):  ").lower()

if tekshiruv == "ha":
    while True:
        login = input("Loginni kiriting: ")
        parol = input("Parolni kiriting: ")
        result = kutubxona.foydalanuvchi_tizimga_kirish(login, parol)
        print(result)
        if "Xush kelibsiz" in result:
            break  



elif tekshiruv == "yo'q":
    ism = input("Ismingizni kiriting: ")
    login = input("Loginni kiriting: ")
    parol = input("Parolni kiriting: ")
    yangi_foydalanuvchi = Foydalanuvchi(ism, login, parol)
    print(kutubxona.foydalanuvchi_royxatdan_otish(yangi_foydalanuvchi))



while True:
    print("\n1. Kitob qoshish")
    print("2. Kitob qidirish")
    print("3. Chiqish")
    
    kirish_nomi = input("Kirish nomini tanlang: ").capitalize()
    
    if kirish_nomi == "Kitob qoshish":
        nomi = input("Kitob nomini kiriting: ")
        muallifi = input("Muallifi kiriting: ")
        janri = input("Janr kiriting: ")
        narxi = float(input("Narxini kiriting: "))
        kutob = Kitob(nomi, muallifi, janri, narxi)
        kutubxona.kitob_qoshish(kutob)
        print("Kitob qo'shildi!")
    elif kirish_nomi == "Kitob qidirish":
        kitob_nomi = input("Kitob nomini kiriting: ")
        print(kutubxona.kitobni_qidirish(kitob_nomi))
    elif kirish_nomi == "Chiqish":
        break
