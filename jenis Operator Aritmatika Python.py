# Tabel berikut merangkum 7 operator aritmatika dalam bahasa pemrograman Python:

# Operator	Penjelasan	Contoh
# +	Penambahan	20 + 6, hasil: 26
# –	Pengurangan	20 – 6, hasil: 14
# *	Perkalian	20 * 6, hasil: 120
# /	Pembagian (real/pecahan)	20 / 6, hasil: 3.3333
# //	Pembagian (dibulatkan ke bawah)	20 // 6, hasil: 3
# %	Modulus (sisa hasil bagi)	20 % 6, hasil: 2
# **	Pemangkatan	20 ** 6, hasil: 64000000

#Dan berikut 2 jenis operator aritmatika unary (hanya butuh 1 operand):

#Operator	Penjelasan	Contoh
# +	Positif (plus)	+5
# –	Negatif (min)	-3

a = 20
b = 40
print('a + b =',a+b)
print('a - b =',a-b)
print('a * b =',a*b)
print('a / b =',a/b)
print('a // b =',a//b)
print('a % b =',a%b)
print('a ** b =',a**b)

#Prioritas Operator Aritmatika Python
#dalam matematika biasa, operator perkalian dan pembagian memiliki prioritas yang 
#lebih tinggi daripada operator penambahan dan pengurangan. Aturan ini juga berlaku di 
#operasi aritmatika Python. Berikut contohnya:

c = 12 + 6 * 4 - 8
print(c)