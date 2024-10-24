#Pengertian Operator Logika Python
#Operator logika adalah operator yang digunakan untuk membuat kesimpulan logis dari 
#2 kondisi boolean: true atau false. Dalam bahasa Python terdapat 3 operator logika:

# Operator	Penjelasan	Contoh	Hasil
# and	True jika kedua operand bernilai True	True and True	True
# or	True jika salah satu operand bernilai True	True or False	True
# not	True jika operand bernilai False	not False	True

#Dalam bentuk paling sederhana, operator logika hanya bisa diisi dengan operand 
#yang bernilai True atau False. Berikut percobaannya:

print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False  :', True and False)
print('Hasil dari False and True  :', False and True)
print('Hasil dari False and False :', False and False)
 
print('\n')
 
print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False  :', True or False)
print('Hasil dari False or True  :', False or True)
print('Hasil dari False or False :', False or False)
 
print('\n')
 
print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)

#Kita juga bisa menggabungkan lebih dari satu operasi seperti contoh berikut:

hasil = (4 > 5) and (6 <= 7)
print(hasil) 
hasil = ('duniaakhirat' == 'duniaakhirat') or (6 <= 7)
print(hasil)
hasil = not (8 < 8)
print(hasil)
hasil = ('duniailkom' == 'duniailkom') and (6 <= 7) or (9 != 9)
print(hasil)
