def tambahkan_agenda(agenda, agenda_baru):
    agenda.append(agenda_baru)
    print("\nagenda berhasil di tambahkan!")

def lihat_agenda(agenda):
    print("\nDaftar agenda")
    for index, item in enumerate(agenda):
        print(f'{index+1}, {item}')

def main():
    agenda = []

    while True:
        
        print("\nSelamat datang di agenda")
        print("1. Tambahkan agenda")
        print("2. Lihat agenda")
        print("3. Keluar agenda")

        pilihan = input("Pilih 1, 2, 3 : ")

        if pilihan == '1':
            print("anda memilih 1")
            agenda_baru = input("Masukkan agenda anda: ")
            tambahkan_agenda(agenda, agenda_baru)

        elif pilihan == '2':
            print("Anda memilih 2")
            lihat_agenda(agenda)
        elif pilihan == '3':
            break
        else:
            print("\n")
            print("Pilihlah yang benar!!")

    print("Keluar dari agenda!")
main()

