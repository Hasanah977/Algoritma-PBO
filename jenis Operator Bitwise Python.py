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

g = 4
h = 2
 
print('g berisi angka',g ,'desimal atau',bin(g),'biner')
print('h berisi angka',h ,'desimal atau',bin(h),'biner')
 
print('\n')
 
print('x & y  :',g & h)
print('x | y  :',g | h)
print('x ^ y  :',g ^ h)
print('~x     :',~g)
print('x << 4:',g << 4)
print('x >> 4 :',g >> 4)