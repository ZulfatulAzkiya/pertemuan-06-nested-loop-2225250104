# Latihan 3 - Jumlah Per Baris
# Pertemuan 06 Algoritma dan Pemrograman

# Loop luar menentukan baris
for i in range(1, 5):

    # Reset total untuk setiap baris
    total_baris = 0

    # Loop dalam menghitung nilai pada setiap kolom
    for j in range(1, 4):
        nilai = i * j
        total_baris += nilai

    # Menampilkan jumlah setiap baris
    print(f"Jumlah baris {i} = {total_baris}")