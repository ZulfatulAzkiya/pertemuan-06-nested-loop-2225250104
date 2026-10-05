# Tugas 3 - Tabel Perkalian dan Statistik
# Pertemuan 06 Algoritma dan Pemrograman

print("======================================")
print("     TABEL PERKALIAN DAN STATISTIK")
print("======================================")

# Input nilai n
n = int(input("Masukkan n: "))

# Validasi agar n merupakan bilangan positif
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

# Akumulator untuk total seluruh hasil
total_semua = 0

# Counter untuk menghitung hasil perkalian yang genap
count_genap = 0

print("\nTabel Perkalian:")

# Loop luar untuk baris
for i in range(1, n + 1):

    # Akumulator jumlah setiap baris
    total_baris = 0

    # Loop dalam untuk kolom
    for j in range(1, n + 1):

        # Menghitung hasil perkalian
        hasil = i * j

        # Menampilkan hasil secara teratur
        print(f"{hasil:4}", end="")

        # Menambahkan hasil ke jumlah baris
        total_baris += hasil

        # Menambahkan hasil ke total keseluruhan
        total_semua += hasil

        # Mengecek apakah hasil perkalian genap
        if hasil % 2 == 0:
            count_genap += 1

    # Menampilkan jumlah setiap baris
    print(f" | jumlah baris = {total_baris}")

# Menampilkan hasil akhir
print("\n======================================")
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
print("======================================")