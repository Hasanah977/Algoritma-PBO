#Cara Pembuatan Tipe Data Tuple Python
#Untuk membuat tipe data Tuple, gunakan tanda kurung biasa, kemudian 
#setiap anggota list dipisah dengan tanda koma. Berikut contohnya:
a = ("hai", "aku?", "iyh", "kamu")
b = (1, 2, 3, 4)
c = ("baik", 10, 10.01, True)
print(a)
print(b)
print(c)

#Nyaris tidak berbeda dengan List. Namun tipe data Tuple dibuat menggunakan 
#tanda kurung bulat, bukan tanda kurung siku sebagaimana List. Berikut pembuktiannya:
d = ["kabar", "aku", "baik", "kamu?"]
print(type(d))
d = ("Baik", "juga", "sama", "kayakamu")
print(type(d))

#Cara Mengakses Tipe Data Tuple Python
#Cara mengakses tipe data Tuple tidak berbeda dengan tipe data List, 
#dimana kita menulis nomor urut index dalam tanda kurung siku:
e = ("generasi", 20, 45.20, True, 'emas', 45j)
  
print(e[0])
print(e[1])
print(e[2])
print(e[2:5])
print(e[:3])
print(e[3:])
print(e[:])