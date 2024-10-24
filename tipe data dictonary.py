#Cara Pembuatan Tipe Data Dictionary Python
#Dalam pembuatan dictionary, kita menggunakan tanda kurung kurawal { dan } . 
#selain itu setiap element merupakan pasangan dari key dan value.
#Antar satu element dengan element lain dipisah dengan tanda koma seperti contoh berikut:
a = { 1: "kita", 2: "itu", 3: "gen z" }
b = { "mengapa": "kita", "kuat": "itu", "sukses": "gen z" }
c = { 1: "kita", "apa?": "kita", "sukses": "gen z" }
print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)

#Nilai atau value dari setiap element dictionary bisa terdiri dari berbagai tipe data:
biodata = { 1: "gen z", 
        2: ["khazana", "prezekc", "zekc"],
        "website": "prezekcc",
        "menyerah" : False,
        "target": 2030,
        "riwayat_sekolah": {
          "SD": "SDN china",
          "SMP": "SMP mesir",
          "SMA": "SMA US"}
      }
print(biodata)

#Cara Mengakses Element Dictionary Python
#Untuk menampilkan satu element yang ada di dalam dictionary, tulis key atau 
#index yang ingin diakses dalam kurung siku:
d = { "kegiatan": "nontong",
        "judul": "upin ipin",
        "apakah seru?": "ya seru" }
print(d["kegiatan"])

#Cara Mengubah Element Dictionary Python
#Setelah di deklarasikan, kita bisa mengubah nilai dari sebuah element dictionary.
#Caranya mirip seperti tipe data list, yakni mengisi nilai ke dalam key atau index 
#dictionary:
e = { "kegiatan": "main game",
        "nama game": "ml",
        "rank": "legend" }
e["kegiatan"] = "belajar!"
print(e)

#Cara Menambah Element Dictionary Python
#Untuk menambah element baru ke dalam dictionary, bisa dilakukan dengan 
#cara mengisi nilai ke sebuah key baru:
f= { "nama": "siregar",
        "umur": "10thn",
        "cita-cita": "kapal laut" }
f["target tercapai"] = 2045
print(f)

#Cara Menghapus Element Dictionary Python
#Untuk menghapus element dari sebuah dictionary, bsia menggunakan perintah del. 
#Berikut contohnya:
g = { "nama": "siregar",
        "umur": "10thn",
        "cita-cita": "kapal laut" }
del g["umur"]
print(g)

#Pembuatan Dictionary dengan constructor dict()
#Selain menggunakan tanda kurung kurawal, proses pembuatan dictionary di dalam 
#bahasa Python juga bisa dilakukan menggunakan "constructor" dict():
h = siregar ( pendidikan = "sekolah",
             asal = "jawa",
             gen = "alpha" )       
print(h)
#Dengan menggunakan perintah dict(), kita tidak lagi memakai tanda kurung kurawal, 
#tapi cukup tanda kurung biasa. Selain itu key element juga tidak perlu menggunakan 
#tanda kutip, dan tanda sama dengan '='  dipakai untuk menginput nilai ke dalam element 
#dictionary.
