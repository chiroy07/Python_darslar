"""
 code: python dasturlash tili
 muallif: Gulchiroy Tojaliyeva
 git hub: @chiroy07
 instagram: @kichkina_hacker
"""
# Mavzu: Pythonda satrlar bilan ishlash
# Satrlar - qo'shtirnoq ichiga olingan unicode kodidagi belgilar ketma-ketligi.

name = "Gulchiroy"
print(type(name))


season = "Bahor!"
print(len(season)) #len - satr uzunligini aniqlash uchun funksiya


a = "Good morning, "
b = "Welcome!"
c = a + "Dear pupil " + b #Satrlarni birlashtirish uchun " + " amali qo'llaniladi
print(c)


# Pythonda bitta so'zni ekranga bir necha amrotaba chiqarish uchun " * " amali bajariladi
abc = "Hello!"
print(abc*10)


area = "UZBEKISTAN"
print(area[4]) # 4-indexdagi belgini chiqaradi
print(area[3:6]) # 3-indexdan 6-indexgacha belgini chiqaradi
print(area[:6]) # 0-indexdan 6-indexgacha belgini chiqaradi
print(area[6:]) # 6-indexdan oxirigacha bo'lgan belgilarni chiqaradi
print(area[3:10:3]) # 3-indexdan 10-indexgacha bo'lgan belgilarni 3 qadam bilan chiqaradi


print("Good morning. \nWelcome!") # \n yangi satrga o'tish
print("Good morning. \tWelcome!") # \t tabulyatsiya belgisi


# Buyruqlarni ketma-ket berish orqli oddiy shakllarni yasash mumkin:
print('*' * 14)
print('*' * 5 + ' ' * 4 + '*' * 5)
print('*' * 2 + ' ' * 10 + '*' * 2)
print('*' * 5 + ' ' * 4 + '*' * 5)
print('*' * 14)

print(" "*2+"~")
print(" "*1+"---")
print("(o o)")
print("/ ^ /")
print("/(_)/")
print("^^ ^^")

print('+++++++')
print('+++++++')
print('+++++++')
print('+++++++')

print('*' * 10)
print(' ' + '*' * 8)
print(' ' * 2 + '*' * 6)
print(' ' * 3 + '*' * 4)
print(' ' * 4 + '*' * 2)