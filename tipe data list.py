#Cara Pembuatan Tipe Data List Python
#Untuk membuat tipe data List, gunakan tanda kurung siku, kemudian setiap anggota
#ist dipisah dengan tanda koma. Berikut contohnya:
a = ["Belajar", "Python", "di", "Duniailkom"]
b = [11, 12, 13, 14]
c = ["Python", 20, 7.99, True]
print(a)
print(b)
print(c)

#Menggunakan function type(), kita bisa memastikan bahwa ini adalah 
#tipe data list Python:
d = ["Belajar", "Python", "di", "Duniailkom"]
e = [11, 12, 13, 14]
f = ["Python", 20, 7.99, True] 
print(type(d))
print(type(e))
print(type(f))

#Cara Mengakses Tipe Data List Python
#Untuk mengakses nilai individu dari tipe data list, gunakan penomoran index.
#Data pertama bernomor index 0, data kedua bernomor index 1, dst. 
#Nomor index ini ditulis di dalam tanda kurung siku:
g = ["hasanah", 25, 20.06, 4j, 'anak ke_2', True]
print(g[0])
print(g[1])
print(g[2])
print(g[3])
print(g[4])
print(g[5])

#Cara Mengganti Nilai Tipe Data List Python
#Nilai yang ada di dalam List bisa diganti atau diupdate. Caranya, isikan
#data baru ke dalam nomor index seperti contoh berikut:
h = ["husna", 25, 20.06, 4j, 'anak ke_2', True]
print(h)
h[0] = 'hasanah'
h[3] = False
print(h)

#Menampilkan Sebagian Anggota List
#Sebelumnya kita telah bahas cara menampilkan isi anggota atau member dari List, 
#caranya dengan menulis nomor index dalam tanda kurung siku.
i = ["husna", 25, 20.06, 4j, 'anak ke_2', True]
print(i[3:4])
print(i[:4])
print(i[2:])
print(i[:])
