# Latihan 1 - Pasangan Indeks
# Pertemuan 06 Algoritma dan Pemrograman

# Loop luar untuk nilai i
# Loop dalam untuk nilai j
# Counter digunakan untuk menghitung jumlah pasangan

count = 0

for i in range(1, 4):
    for j in range(1, 5):
        print(f"Pasangan: ({i}, {j})")
        count += 1

print(f"\nBanyak pasangan = {count}")