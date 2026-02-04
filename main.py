from collections import defaultdict

catatan = []

def tambah_catatan():
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = int(input("Masukkan durasi belajar (dalam menit): "))
    
    # Simpan data ke dalam dictionary dan tambahkan ke list catatan
    data_catatan = {
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    }
    catatan.append(data_catatan)
    print("Catatan berhasil ditambahkan!")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
    else:
        print("Daftar Catatan Belajar:")
        for i, item in enumerate(catatan, 1):
            print(f"{i}. Mapel: {item['mapel']}")
            print(f"   Topik: {item['topik']}")
            print(f"   Durasi: {item['durasi']} menit")
            print("---")

def total_waktu():
    total = sum(item['durasi'] for item in catatan)
    print(f"Total waktu belajar: {total} menit")

def mapel_favorit():
    if not catatan:
        print("Belum ada catatan belajar.")
        return
    
    durasi_per_mapel = defaultdict(int)
    for item in catatan:
        durasi_per_mapel[item['mapel']] += item['durasi']
    
    favorit = max(durasi_per_mapel, key=durasi_per_mapel.get)
    print(f"Mapel favorit: {favorit} dengan total durasi {durasi_per_mapel[favorit]} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Lihat mapel favorit")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        mapel_favorit()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")
