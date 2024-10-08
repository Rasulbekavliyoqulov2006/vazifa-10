import json

class Register:
    def __init__(self, fullname, email, username, password):
        self.fullname = fullname.strip()  
        self.email = email.strip()        
        self.username = username.strip()  
        self.password = password.strip()  

        self.check_name(self.fullname)    
        self.check_email(self.email)      
        self.check_username(self.username)
        self.check_password(self.password)
        
        self.save_to_file()

    def save_to_file(self):
        data = {
            "fullname": self.fullname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
        }

        try:
            with open("misol2_register.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        
        for user in users:
            if user["username"] == self.username or user["email"] == self.email:
                print("bu foydalanuvchi nomi yoki email avvaldan ro'yxatdan o'tgan!!!")
                return

        users.append(data)

        with open("misol2_register.json", "w") as file:
            json.dump(users, file, indent=4)

        print("hisob ro'yxatdan o'tkazildi.")

    def check_name(self, new_name):
        parts = new_name.split()
        if len(parts) < 3 or len(parts) > 4:
            raise Exception("iltimos, to'liq ism va familiya kiriting (masalan, Rasulbek Avliyoqulov Abdullayevich yoki Abdulla o'g'li)!!!")
        
        for part in parts:
            if part[0].islower():
                raise Exception("to'liq ismdagi har bir qismning birinchi harfi katta bo'lishi kerak!!!")

        if not (new_name.endswith("vich") or new_name.endswith("vna") or new_name.endswith("o'g'li") or new_name.endswith("qizi")):
            raise Exception("to'liq ism tegishli qo'shimchalar bilan tugashi kerak (vich, vna, o'g'li, qizi)!!!")

    def check_email(self, new_email):
        if "@" not in new_email:
            raise Exception("emailda '@' belgisini bo'lishi shart!!!")
        if len(new_email[:new_email.find("@")]) < 5:
            raise Exception("emailning '@' dan oldingi qismi 5 ta belgidan ko'p bo'lishi kerak!!!")
        if not (new_email.endswith("@gmail.com") or new_email.endswith("@gmail.ru")):
            raise Exception("email @gmail.com yoki @gmail.ru bilan tugashi kerak.")

    def check_username(self, new_username):
        if len(new_username) < 5:
            raise Exception("foydalanuvchi nomi kamida 5 ta belgidan iborat bo'lishi kerak!!!")
        if not new_username.isalnum():
            raise Exception("foydalanuvchi nomi faqat harflar va raqamlardan iborat bo'lishi kerak!!!")
        if new_username.lower() in ["admin", "root", "user", "guest"]:
            raise Exception("foydalanuvchi nomi 'admin', 'root', 'user' yoki 'guest' bo'lishi mumkin emas!!!")

    def check_password(self, new_password):
        if len(new_password) < 8:
            raise Exception("parol kamida 8 ta belgidan iborat bo'lishi kerak!!!")
        if not any(char.isdigit() for char in new_password):
            raise Exception("parolda kamida bitta raqam bo'lishi kerak!!!")
        if not any(char.isupper() for char in new_password):
            raise Exception("parolda kamida bitta katta harf bo'lishi kerak!!!")
        if not any(char.islower() for char in new_password):
            raise Exception("parolda kamida bitta kichik harf bo'lishi kerak!!!")
        if new_password.lower() == self.username.lower():
            raise Exception("parol foydalanuvchi nomi bilan bir xil bo'lmasligi kerak!!!")
        if new_password.lower() == self.email.lower():
            raise Exception("parol email bilan bir xil bo'lmasligi kerak!!!")

register = Register(
    input("F.I.SH kiriting: "), 
    input("email kiriting: "), 
    input("foydalanuvchi nomi kiriting: "), 
    input("parol kiriting: ")
)
