# manajemen kontak

kontak1 = {'nama': "Mail", 'HP':"123243432", 'Email':"mail@mail.com"}
kontak2 = {'nama': "Abdi", 'HP':"4323255435", 'Email':"abdi@mail.com"}
kontak = [kontak1,kontak2]


while True:
    print("\n Manajemen kontak")
    print("1. lihat kontak")
    print("2. Menambahkan kontak")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukkan pilihan anda (1,2,3 atau 4) : ")

    if pilihan == '1':
        if kontak:
            for num,item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["Email"]})')
        else:
            print("kontak kosong")
    elif pilihan == '2':
        # tambahkan kontak
        nama = input("Masukkan nama kontak: ")
        hp =input ("Masukkan Nomor HP kontak: ")
        email =input ("Masukkan Email kontak: ")
        kontak_baru = {'nama': nama, 'HP':hp, 'Email': email}
        kontak.append(kontak_baru)
        print('kontak berhasil di tambahkan')
    elif pilihan == '3':
        # menghapus kontak
        if kontak:
            for num,item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["Email"]})')
        else:
            print("kontak kosong")
            continue

        i = int(input("Masukkan nomor yang mau di hapus: "))
        del kontak[i-1]
    else:
        break

            