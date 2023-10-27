"""
 code: python dasturlash tili
 muallif: Gulchiroy Tojaliyeva
 git hub: @chiroy07
 instagram: @kichkina_hacker
"""
# Mavzu: Pythonda arifmetik amallarni bajarish
x = 7
y = 2
print(x + y) # '+' qo'shish

print(x - y) # '-' ayirish

print(x * y) # '*' ko'paytirish

print(x / y) # '/' bo'lish

print(x // y) # '//' butun qismini olish

print(x % y) # '%' qoldig'ini olish

print(x ** y) # '**' darajaga ko'tarish

# Masalalar:

"""5738 sononing birinchi va oxirgi xonasi ko'paytmasini toping"""
son = 5738
a = son // 1000 # 5
b = son % 10 # 8
c = a * b # 5 * 8
print(c) # javob: 40


""" a = 12325458 mm
Arqonning uzunligi millimetrda berilgan, 
shu uzunlikni kilometr, metr va santimetrda ifodalang"""
a = 12325458
b = a//1000000 # necha km
a = a%1000000 #qolgan qismi
c = a//1000 # necha m
a = a%1000 #qolgan qismi
d = a//10  # necha cm
a = a%10 #qolgan qismi
print(f"123456789 mm = {b} km {c} m {d} cm {a} mm")


"""Botir bir son o'yladi, unga 3ni qo'shib 15ni ayirdi keyin 6ga ko'paytirdi 
va 3ga bo'ldi 20 hosil bo'ldi. Botir qanday son o'ylagan."""
y = 20
z = y*3
q = z/6
m = q+15
x = m-3
print(x)