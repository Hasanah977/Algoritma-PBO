#Cara Pembuatan Tipe Data Set Python
#Untuk membuat tipe data set, gunakan tanda kurung kurawal, kemudian setiap
#anggota set dipisah dengan tanda koma. Berikut contohnya:
a = {"indonesia", "generasi", "cemas", "gen z"}
b = {2000, 2006, 20, 45}
c = {"gen alpha", 2000, 20.13, True}
print(a)
print(b)
print(c)

#Menggunakan function type(), kita bisa melihat perbedaan cara penulisan 
#tipe data list, tuple dan set dalam bahasa Python:
e = ["generasi", "gen", "x", "indonesia"]
print(type(e))
f= ("generasi", "gen", "z", "indonesia")
print(type(f))
g = {"generasi", "gen", "alpha", "indonesia"}
print(type(g))

#Sifat Tipe Data Set Python
#Seperti yang dibahas pada bagian pengertian, sifat dari tipe data set adalah
#tidak ber-index dan hanya bisa menerima anggota dengan nilai yang 
#berbeda (unique value). Mari lihat dengan contoh kode program:
h = {"Belajar", "menjadi", "lebih", "baik", "lagi"}
i = {100, 200, 300, 400, 200, 300}
print(h)
print(i)

#Operasi Himpunan tipe data Set Python
#Tipe data set pada dasarnya adalah tipe data khusus yang dipakai untuk operasi
#himpunan, seperti operasi gabungan (union), operasi irisan (intersection), dst. 
#Lebih rinci tentang operasi himpunan ini akan kita bahas dalam tutorial
#khusus tenang operator di dalam bahasa Python.
#Namun sebagai gambaran, berikut contoh penggunaan tipe data set untuk operasi himpunan:
j = {1, 2, 3, 4, 5}
k = {3, 4, 5, 6, 7}
 
print (j | k) # union
print (j & k) # intersection