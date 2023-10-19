"""
 code: python dasturlash tili
 muallif: Gulchiroy Tojaliyeva
 git hub: @chiroy07
 instagram: @kichkina_hacker
"""
# Mavzu: Pythonda ma'lumot turlari
# Ma'lumot turlar: int, float, str, bool, list, set
#O'zgaruvchi qabul qiymat turini type() funksiyasi orqali aniqlash mumkin

age = 16
print(type(age)) # int


name = "Gulchiroy"
print(type(name)) # str


number = 12.3
print(type(number)) # float


a = True
print(type(a)) # bool


array = ["apple"]
print(type(array)) # list


obyekt = {"cat"}
print(type(obyekt)) # set


# Misollar:
age = int(input("Enter your age>>>"))
print(age+1)


year = int(input("Nechinchi tug'ulgansiz..?"))
print(f"Siz {2023-year} yoshda ekansiz")


""" Futbol maydonida x ta o'yinchi bor, ulardan 5 tasi qizil olib o'yindan chiqdi
va yangi 7 ta o'yinchi o'yinga qo'shildi, o'yinchilar soni 24 ta bo'ldi. x = ?"""

y = 24
z = y - 7
x = z + 5
print(f"x = {x}")