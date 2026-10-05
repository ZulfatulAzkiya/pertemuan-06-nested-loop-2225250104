# Latihan 2 - Pola Segitiga
# Pertemuan 06 Algoritma dan Pemrograman

# Input jumlah baris
n = int(input("Masukkan n: "))

# Validasi n harus positif
while n <= 0:
    print("n harus berupa bilangan positif.")
    n = int(input("Masukkan n: "))

# Membentuk pola segitiga
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()