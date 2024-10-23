#Cara Penggunaan Tipe Data Boolean Python
a = True
b = False
print(a)
print(b)

#Selain diinput manual, tipe data boolean lebih sering di dapat sebagai hasil
#  dari operasi perbandingan, seperti apakah suatu angka lebih besar dari angka
#  lainnya, apakah lebih kecil, atau sama dengan. Berikut contoh penggunaan operasi
#  perbandingan ini:
c = 20 < 10
print(c)
d = 50 > 20
print(d)
hasil = "c" == "c"
print(hasil)

#Hasil boolean dari operasi perbandingan ini juga bisa didapat tanpa harus
#menyimpannya ke dalam variabel, seperti contoh berikut:
print(6 < 9)
print(3 > 6)
print("d" == "D")

#Lebih jauh lagi, metode perbandingan seperti ini sangat sering dipakai 
#dalam struktur logika IF seperti contoh berikut:
e = 25
f = 20
if (e < f):
  print("Isi variabel a lebih kecil daripada variabel b")
elif (e > f):
  print("Isi variabel a lebih besar daripada variabel b")
else:
  print("Isi variabel a sama dengan variabel b")