# pertemuan-06-nested-loop-2225250104
## Identitas

**Nama:** Zulfatul Azkiya
**NIM:** 2225250104
**Kelas:** 3A

---

## Deskripsi

Pertemuan 06 membahas penggunaan **nested loop** atau perulangan bersarang dalam Python. Nested loop digunakan ketika sebuah perulangan berada di dalam perulangan lainnya.

Pada pertemuan ini, nested loop digunakan untuk membuat pasangan indeks, membentuk pola, melakukan akumulasi nilai per baris maupun keseluruhan, serta melakukan pencacahan berdasarkan kondisi tertentu.

Program dibuat dan diuji menggunakan Python melalui Visual Studio Code.

---

## Tujuan

Tujuan dari kegiatan Pertemuan 06 adalah:

1. Memahami konsep nested loop.
2. Menjelaskan hubungan antara loop luar dan loop dalam.
3. Membentuk pola baris dan kolom menggunakan nested loop.
4. Menggunakan akumulator untuk menghitung jumlah nilai.
5. Menggunakan counter untuk menghitung banyak kejadian yang memenuhi kondisi.
6. Melakukan tracing terhadap perubahan nilai `i` dan `j`.
7. Menguji program menggunakan beberapa test case.
8. Mengelola hasil program menggunakan Git dan GitHub.

---

## Struktur Folder

```text
pertemuan-06-nested-loop-2225250104/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
│
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

---

# Latihan

## 1. Pasangan Indeks

File:

```text
latihan/01_pasangan_indeks.py
```

Program menggunakan nested loop untuk menampilkan seluruh pasangan nilai `i` dan `j`.

Loop luar menggunakan:

```python
for i in range(1, 4):
```

sedangkan loop dalam menggunakan:

```python
for j in range(1, 5):
```

Jumlah pasangan yang dihasilkan adalah:

```text
3 × 4 = 12 pasangan
```

Program juga menggunakan variabel `count` sebagai counter untuk menghitung jumlah pasangan.

### Hasil yang diharapkan

```text
Banyak pasangan = 12
```

---

## 2. Pola Segitiga

File:

```text
latihan/02_pola_segitiga.py
```

Program menerima nilai `n` dari pengguna dan membentuk pola bintang berbentuk segitiga.

Loop luar menentukan jumlah baris, sedangkan loop dalam menentukan jumlah bintang pada setiap baris.

Contoh untuk:

```text
n = 5
```

hasilnya:

```text
* 
* * 
* * * 
* * * * 
* * * * *
```

Program juga melakukan validasi agar nilai `n` harus lebih besar dari 0.

---

## 3. Jumlah Per Baris

File:

```text
latihan/03_jumlah_per_baris.py
```

Program menghitung hasil perkalian `i * j` untuk:

```text
i = 1 sampai 4
j = 1 sampai 3
```

Pada setiap pergantian nilai `i`, variabel `total_baris` direset menjadi 0.

Hal tersebut dilakukan karena program ingin mendapatkan jumlah untuk setiap baris secara terpisah.

### Hasil

```text
Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
Jumlah baris 4 = 24
```

---

## 4. Menghitung Pasangan

File:

```text
latihan/04_hitung_pasangan.py
```

Program menerima nilai `n`, kemudian memeriksa seluruh pasangan `i` dan `j` dari 1 sampai `n`.

Pasangan dihitung apabila memenuhi kondisi:

```python
i + j <= n
```

Variabel `count` digunakan sebagai counter untuk menghitung jumlah pasangan yang memenuhi kondisi.

### Test Case

Program diuji menggunakan:

```text
n = 2
n = 3
n = 5
```

---

# Tugas 3 - Tabel Perkalian dan Statistik

File:

```text
tugas/tabel_perkalian_dan_statistik.py
```

Program Tugas 3 membuat tabel perkalian dari 1 sampai `n`.

Program memiliki beberapa proses utama, yaitu:

1. Membaca nilai `n`.
2. Memvalidasi agar `n` merupakan bilangan positif.
3. Membentuk tabel perkalian menggunakan nested loop.
4. Menghitung jumlah setiap baris.
5. Menghitung total seluruh hasil perkalian.
6. Menghitung banyak hasil perkalian yang genap.

---

## Algoritma Tugas 3

1. Meminta pengguna memasukkan nilai `n`.
2. Jika `n <= 0`, program meminta input kembali.
3. Membuat `total_semua = 0`.
4. Membuat `count_genap = 0`.
5. Loop luar digunakan untuk nilai `i` dari 1 sampai `n`.
6. Pada setiap baris, `total_baris` diatur kembali menjadi 0.
7. Loop dalam digunakan untuk nilai `j` dari 1 sampai `n`.
8. Menghitung `hasil = i * j`.
9. Menambahkan `hasil` ke `total_baris`.
10. Menambahkan `hasil` ke `total_semua`.
11. Jika `hasil` genap, `count_genap` ditambah 1.
12. Setelah loop dalam selesai, jumlah baris ditampilkan.
13. Setelah seluruh loop selesai, total keseluruhan dan jumlah hasil genap ditampilkan.

---

## Peran Variabel

| Variabel      | Fungsi                                       |
| ------------- | -------------------------------------------- |
| `n`           | Menentukan ukuran tabel perkalian            |
| `i`           | Mengatur baris                               |
| `j`           | Mengatur kolom                               |
| `hasil`       | Menyimpan hasil perkalian `i * j`            |
| `total_baris` | Menghitung jumlah hasil pada setiap baris    |
| `total_semua` | Menghitung jumlah seluruh hasil perkalian    |
| `count_genap` | Menghitung banyak hasil perkalian yang genap |

---

# Cara Menjalankan Program

Pastikan Python sudah terpasang dan interpreter Python sudah dipilih di VS Code.

### Latihan 1

```bash
python latihan/01_pasangan_indeks.py
```

### Latihan 2

```bash
python latihan/02_pola_segitiga.py
```

### Latihan 3

```bash
python latihan/03_jumlah_per_baris.py
```

### Latihan 4

```bash
python latihan/04_hitung_pasangan.py
```

### Tugas 3

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

Pada macOS atau Linux, perintah `python3` dapat digunakan jika `python` tidak tersedia.

---

# Hasil Pengujian Tugas 3

| Input n | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status   |
| ------: | --------------: | ----------: | -----------------: | -------- |
|       1 |               1 |           1 |                  0 | Berhasil |
|       2 |               4 |           9 |                  3 | Berhasil |
|       3 |               9 |          36 |                  5 | Berhasil |

Jumlah pasangan untuk setiap input dihitung dengan rumus:

```text
n × n
```

Sehingga:

```text
n = 1 → 1 × 1 = 1
n = 2 → 2 × 2 = 4
n = 3 → 3 × 3 = 9
```

---

# Analisis Efisiensi

Pada Tugas 3, loop luar berjalan sebanyak `n` kali dan loop dalam juga berjalan sebanyak `n` kali untuk setiap iterasi loop luar.

Dengan demikian, badan loop dalam dijalankan sebanyak:

```text
n × n = n²
```

kali.

Contohnya:

```text
n = 1 → 1 iterasi
n = 2 → 4 iterasi
n = 3 → 9 iterasi
n = 10 → 100 iterasi
```

Semakin besar nilai `n`, semakin banyak proses yang dilakukan oleh program.

---

# Konsep Akumulasi

Akumulasi digunakan untuk menjumlahkan nilai.

Pada program ini terdapat dua jenis akumulasi.

### 1. Akumulasi per baris

```python
total_baris = 0
```

Diletakkan di dalam loop luar karena nilainya harus kembali ke 0 setiap kali masuk ke baris baru.

### 2. Akumulasi keseluruhan

```python
total_semua = 0
```

Diletakkan sebelum nested loop karena nilainya harus terus bertambah sampai seluruh tabel selesai diproses.

---

# Konsep Pencacahan

Pencacahan digunakan untuk menghitung banyak kejadian yang memenuhi kondisi tertentu.

Pada Tugas 3 digunakan:

```python
if hasil % 2 == 0:
    count_genap += 1
```

Artinya, `count_genap` hanya bertambah ketika hasil perkalian merupakan bilangan genap.

---

# Kesalahan yang Perlu Dihindari

Beberapa kesalahan yang perlu diperhatikan dalam nested loop adalah:

1. Kesalahan indentasi.
2. Batas `range()` tidak sesuai.
3. `total_baris` tidak direset pada setiap baris.
4. `total_semua` direset di dalam loop sehingga hasil keseluruhan menjadi salah.
5. `count_genap` ditambah tanpa kondisi yang benar.
6. `print()` untuk pindah baris diletakkan pada posisi yang salah.

---

# Refleksi

Setelah mengerjakan Pertemuan 06, saya memahami bahwa nested loop digunakan untuk memproses data yang memiliki lebih dari satu tingkat perulangan. Loop luar dapat digunakan untuk menentukan baris atau kelompok, sedangkan loop dalam digunakan untuk memproses elemen pada setiap baris tersebut.

Saya juga memahami bahwa posisi inisialisasi variabel sangat berpengaruh terhadap hasil program. `total_baris` harus direset pada setiap iterasi loop luar karena digunakan untuk menghitung jumlah pada masing-masing baris. Sementara itu, `total_semua` harus dibuat sebelum kedua loop agar dapat menghitung seluruh hasil perkalian.

Kesalahan yang perlu diperhatikan dalam nested loop adalah indentasi, batas perulangan, dan posisi akumulator atau counter. Dengan melakukan tracing terhadap nilai `i` dan `j`, kesalahan logika dapat lebih mudah ditemukan dan diperbaiki.
