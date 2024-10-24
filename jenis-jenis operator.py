#Tabel berikut merangkum 7 operator aritmatika dalam bahasa pemrograman Python:
# Operator	Penjelasan	Contoh
# +	Penambahan	20 + 6, hasil: 26
# –	Pengurangan	20 – 6, hasil: 14
# *	Perkalian	20 * 6, hasil: 120
# /	Pembagian (real/pecahan)	20 / 6, hasil: 3.3333
# //	Pembagian (dibulatkan ke bawah)	20 // 6, hasil: 3
# %	Modulus (sisa hasil bagi)	20 % 6, hasil: 2
# **	Pemangkatan	20 ** 6, hasil: 64000000

a = 10
b = 30
hasil = a + b
print(hasil)
a = 10
b = 30
hasil = a - b
print(hasil)
a = 10
b = 30
hasil = a * b
print(hasil)
a = 10
b = 30
hasil = a / b
print(hasil)
a = 10
b = 30
hasil = a // b
print(hasil)
a = 10
b = 30
hasil = a % b
print(hasil)
a = 10
b = 30
hasil = a ** b
print(hasil)

#Operator Perbandingan / Relasional
#Operator perbandingan dipakai untuk membandingkan 2 buah nilai, apakah nilai 
#tersebut sama besar, lebih kecil, lebih besar, dll. Hasil dari operator perbandingan 
#ini adalah tipe data boolean True atau False.

# Operator	Penjelasan	Contoh	Hasil
# ==	Sama dengan	5 == 5	True
# !=	Tidak sama dengan	5 != 5	False
# >	Lebih besar	5 > 6	False
# <	Lebih kecil	5 < 6	True
# >=	Lebih besar atau sama dengan	5 >= 3	True
# <=	Lebih kecil atau sama dengan	5 <= 5	True

c = 2 == 2
d = 2 != 2
print(c)
print(d)
c = 2 > 3
d = 2 < 3
print(c)
print(d)
c = 2 >= 3
d = 2 <= 3
print(c)
print(d)

#Operator Logika
#Operator logika adalah operator yang dipakai untuk membuat kesimpulan logis dari 
#2 kondisi boolean: true atau false. Dalam bahasa Python terdapat 3 operator logika:\
# Operator	Penjelasan	Contoh	Hasil
# and	True jika kedua operand bernilai True	True and True	True
# or	True jika salah satu operand bernilai True	True or False	True
# not	True jika operand bernilai False	not False	True

e = (1 > 2) and (4 <= 3)
print(e)
f = ('sisfo' == 'sisfo') or (4 <= 3)
print(f) 
e = not (1 < 1)
print(e)
f = ('sisfo' == 'sisfo') and (4 <= 3) or (1 != 1)
print(f)

#Operator Bitwise
#Bitwise adalah operator khusus untuk menangani operasi logika bilangan biner dalam 
#bentuk bit.

#Bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri dari 2 jenis angka, 
#yakni 0 dan 1. Jika nilai asal yang dipakai bukan bilangan biner, akan dikonversi 
#secara otomatis oleh bahasa Python menjadi bilangan biner. Misalnya 7 desimal = 0111 
#dalam bilangan biner.

#Bahasa Python mendukung 6 jenis operator bitwise. Daftar lengkapnya dapat dilihat pada tabel berikut:

#Operator	Nama	Contoh	Biner	Hasil (biner)	Hasil (decimal)
#&	And	10 & 12	1010 & 1100	1000	8
#|	Or	10 | 12	1010 | 1100	1110	14
#^	Xor	10 ^ 12	1010 ^ 1100	0110	6
#~	Not	~ 10	~1010	0101	-11 (two complement)
#<<	Left shift	10 << 1	1010 << 1	10100	20
#>>	Right shift	10 >> 1	1010 >> 1	101	5

#Contoh Kode Program Operator Bitwise Python
#Berikut contoh kode program dari penggunaan operator bitwise dalam bahasa pemrograman 
#Python:

g = 1
h = 2
 
print('g berisi angka',g ,'desimal atau',bin(g),'biner')
print('h berisi angka',h ,'desimal atau',bin(h),'biner')
 
print('\n')
 
print('x & y  :',g & h)
print('x | y  :',g | h)
print('x ^ y  :',g ^ h)
print('~x     :',~g)
print('x << 1 :',g << 1)
print('x >> 1 :',g >> 1)

#Operator Assignment
#Operator assignment juga memiliki variasi penulisan yang disebut sebagai operator 
#assignment gabungan (compound assignment).  Operator assignment gabungan adalah cara 
#penulisan singkat operator assignment yang digabung dengan dengan operator lain. Dalam 
#bahasa Python, operator assignment gabungan ini terdiri dari operator assignment dengan 
#operator lain seperti operator aritmatika dan bitwise.

#Tabel berikut merangkum semua operator assignment dalam bahasa Python:
# Operator	Contoh	Penjelasan
# +=	a += b	a = a + b
# -=	a -= b	a = a – b
# *=	a *= b	a = a * b
# /=	a /= b	a = a / b
# &=	a &= b	a = a & b
# |=	a |= b	a = a | b
# ^=	a ^= b	a = a ^ b
# <<=	a <<= b	a = a << b
# >>=	a >>= b	a = a >> b

#Contoh Kode Program Operator Assignment Python
#Dalam prakteknya, operator assignment juga bisa dipakai "bertingkat" seperti contoh 
#berikut:

i = 2
j = 4
j = j + 1
k = i + j
l = k + k + i
m = (k + l)* i
print('Isi variabel i:',i)
print('Isi variabel j:',j)
print('Isi variabel k:',k)
print('Isi variabel l:',l)
print('Isi variabel m:',m)

#Tabel berikut merangkum semua operator assignment dalam bahasa Python:
# Operator	Contoh	Penjelasan
# +=	a += b	a = a + b
# -=	a -= b	a = a – b
# *=	a *= b	a = a * b
# /=	a /= b	a = a / b
# %=	a %= b	a = a % b
# &=	a &= b	a = a & b
# |=	a |= b	a = a | b
# ^=	a ^= b	a = a ^ b
# <<=	a <<= b	a = a << b
# >>=	a >>= b	a = a >> b

n = 10
n += 5
print('n += 5  :',n) 
n = 10
n /= 5
print('n /= 5  :',n)  
n = 10
n **= 5
print('n *= 5 :',n)
n = 10
n <<= 2
print('n <<= 2 :',n)

#Operator identitas adalah operator yang bisa dipakai untuk memeriksa apakah nilai 
#sebuah variabel ada di tempat yang sama (di memory) atau tidak. Operator ini dikenal 
#juga sebagai identity operators.

#Operator ini terdiri dari 2 jenis:
# Operator	Penjelasan
# is	Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai 
#       yang sama.
# is not Bernilai True jika kedua operand merujuk ke object yang tidak sama

o = 5
p = 5
q = 6
print('o is p :', o is p)
print('o is q :', o is q)
print('o is not q:', o is not q)
print('\n')
  
r = 'Duniailkom'
s = 'Duniailkom'
print('r is s :', r is s)
print('r is not s :', r is not s)
print('\n');

t = ['a','b','c']
v = ['a','b','c']
print('t is v :', t is v)
print('t is not v :', t is not v)

#Pengertian dan Contoh Operator Keanggotaan Python
#Operator keanggotaan adalah operator yang dipakai untuk memeriksa apakah suatu nilai 
#ada di dalam sebuah himpunan atau tidak. Himpunan yang dimaksud terdiri dari tipe data 
#"berbentuk array" seperti string, list, tuple, set dan dictionary. Operator ini dikenal 
#juga sebagai membership operators.

#Operator ini terdiri dari 2 jenis:
#Operator	Penjelasan
# in	Bernilai True jika nilai yang dicari ada di dalam himpunan
# not in	Bernilai True jika nilai yang dicari tidak ada dalam himpunan

w = 'Duniailkom'
print('w :',w)
print('\'i\' in w    :', 'i' in w)
print('\'k\' not in w :', 'k' not in w)
print('\'d\' not in w :', 'd' not in w)
print('\n')
 
 
x = ['a','b','c']
print('x :',x)
print('\'a\' in x    :', 'a' in x)
print('\'a\' not in x :', 'a' not in x)
print('\'d\' not in x :', 'd' not in x)
print('\n')
 
y = (12,43,102,55)
print('y :',y)
print('102 in y    :', 102 in y)
print('102 not in y :', 102 not in y)
print('35 not in y  :', 35 in y)


