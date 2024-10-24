#Operator Perbandingan Python
#Operator perbandingan dipakai untuk membandingkan 2 buah nilai, apakah nilai tersebut 
#sama besar, lebih kecil, lebih besar, dst. Hasil dari operator perbandingan ini adalah 
#boolean True atau False.

#Di dalam bahasa Python, terdapat 6 operator perbandingan:
# Operator	Penjelasan	Contoh	Hasil
# ==	Sama dengan	5 == 5	True
# !=	Tidak sama dengan	5 != 5	False
# >	Lebih besar	5 > 6	False
# <	Lebih kecil	5 < 6	True
# >=	Lebih besar atau sama dengan	5 >= 3	True
# <=	Lebih kecil atau sama dengan	5 <= 5	True

a = 7
b = 10
print('a =',a)
print('b =',b)
print('\n')
print('x == y hasilnya',a==b)
print('x != y hasilnya',a!=b)
print('x > y  hasilnya',a>b)
print('x < y  hasilnya',a<b)
print('x >= y hasilnya',a>=b)
print('x <= y hasilnya',a<=b)

#Operasi perbandingan tidak hanya untuk tipe data angka saja, tapi juga bisa 
#berbagai tiprint('Duniailkom' == 'Duniailkom')

print('Duniaakhirat' == 'duniaakhirat')
print('1234' == 1234)
print('1234' != 1234)

#Dalam prakteknya, operasi perbandingan baru berguna dalam percabangan kode 
#program seperti struktur if seperti contoh berikut:

c = 8
if (c % 2)==0:
  print('Variabel c berisi angka genap')
else:
  print('Variabel c berisi angka ganjil')
