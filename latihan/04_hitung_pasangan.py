# Latihan 4 - Menghitung Pasangan
# Pertemuan 06 Algoritma dan Pemrograman

# Input nilai n
n = int(input("Masukkan n: "))

# Validasi n harus positif
while n <= 0:
    print("n harus berupa bilangan positif.")
    n = int(input("Masukkan n: "))

# Counter jumlah pasangan
count = 0

# Nested loop untuk memeriksa seluruh pasangan
for i in range(1, n + 1):
    for j in range(1, n + 1):

        # Kondisi pasangan yang dihitung
        if i + j <= n:
            print(f"Pasangan yang memenuhi: ({i}, {j})")
            count += 1

# Menampilkan hasil
print(f"\nBanyak pasangan = {count}")