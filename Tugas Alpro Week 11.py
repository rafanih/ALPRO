import math

# Fungsi untuk mencari panjang persegi panjang jika diketahui lebar, luas, atau keliling
def cari_panjang(lebar=None, luas=None, keliling=None):
    if luas is not None and lebar is not None:
        return luas / lebar
    elif keliling is not None and lebar is not None:
        return (keliling / 2) - lebar
    else:
        return None

# Fungsi untuk mencari lebar persegi panjang jika diketahui panjang, luas, atau keliling
def cari_lebar(panjang=None, luas=None, keliling=None):
    if luas is not None and panjang is not None:
        return luas / panjang
    elif keliling is not None and panjang is not None:
        return (keliling / 2) - panjang
    else:
        return None

# Fungsi untuk mencari sisi persegi jika diketahui luas atau keliling
def cari_sisi_persegi(luas=None, keliling=None):
    if luas is not None:
        return math.sqrt(luas)
    elif keliling is not None:
        return keliling / 4
    else:
        return None

# Fungsi untuk mencari radius lingkaran jika diketahui luas atau keliling
def cari_radius(luas=None, keliling=None):
    if luas is not None:
        return math.sqrt(luas / math.pi)
    elif keliling is not None:
        return keliling / (2 * math.pi)
    else:
        return None

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("\nPilih bentuk yang ingin dihitung:")
        print("1. Persegi Panjang")
        print("2. Persegi")
        print("3. Lingkaran")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        
        if pilihan == '1':
            print("Menghitung Persegi Panjang")
            lebar = input("Masukkan lebar (atau ketik 'None' untuk tidak ada): ")
            luas = input("Masukkan luas (atau ketik 'None' untuk tidak ada): ")
            keliling = input("Masukkan keliling (atau ketik 'None' untuk tidak ada): ")
            
            panjang = cari_panjang(
                lebar=float(lebar) if lebar != 'None' else None,
                luas=float(luas) if luas != 'None' else None,
                keliling=float(keliling) if keliling != 'None' else None
            )
            print(f"Panjang: {panjang}")
        
        elif pilihan == '2':
            print("Menghitung Persegi")
            luas = input("Masukkan luas (atau ketik 'None' untuk tidak ada): ")
            keliling = input("Masukkan keliling (atau ketik 'None' untuk tidak ada): ")
            
            sisi = cari_sisi_persegi(
                luas=float(luas) if luas != 'None' else None,
                keliling=float(keliling) if keliling != 'None' else None
            )
            print(f"Sisi Persegi: {sisi}")
        
        elif pilihan == '3':
            print("Menghitung Lingkaran")
            luas = input("Masukkan luas (atau ketik 'None' untuk tidak ada): ")
            keliling = input("Masukkan keliling (atau ketik 'None' untuk tidak ada): ")
            
            radius = cari_radius(
                luas=float(luas) if luas != 'None' else None,
                keliling=float(keliling) if keliling != 'None' else None
            )
            print(f"Radius Lingkaran: {radius}")
        
        elif pilihan == '4':
            print("Terima kasih! Program dihentikan.")
            break
        
        else:
            print("Pilihan tidak valid!")

# Memastikan main() hanya berjalan saat file ini dijalankan langsung
if __name__ == "__main__":
    main()
