# class Mobil:
#     jenis = "yamaha"

#     def info(self):
#         print("ini adalah mobil")


# mobil1 = Mobil()
# mobil2 = Mobil()
# mobil1.info()


# class Pohon:
#     def info(self):
#         print("ini adalah pohon info ")

# pohon1 = Pohon()

# pohon1.info()

# class Pohon:
#     def __init__(self):
#         print("ini adalalah pohon init ")

# pohon1 = Pohon()


# class Manusia:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur
#     def info(self):
#         print(f"ini adalah {self.nama} dan umur {self.umur}")

# human = Manusia("budi", 20)
# print(human.nama)
# print(human.umur)
# human.info()



# class Hewan:
#     def __init__(self, nama, umur, suara):
#         self.nama = nama
#         self.umur = umur
#         self.suara = suara
#         # self.bersuara = bersuar
#     def info(self):
#         print(f"ini adalah {self.nama} dan umur {self.umur}")
#     def bersuara(self, num):
#         print(f"{self.suara}"* num)

# hewan1 = Hewan("Kucing", "3 tahun","meow") 
# hewan1.info()
# hewan1.bersuara()


class bank:
    def __init__(self, nama, saldo, rekening,):
        self.nama = nama
        self._saldo = saldo
        self.rekening = rekening
        self.__pin = "123"
    
    def info(self):
        print(f"nama {self.nama} saldo {self._saldo} rekening {self.rekening}")
    def tambah_saldo(self, saldo):
        self._saldo += saldo
        print(f"Saldo berhasil di tambahkan sebesar Rp. {saldo} ")
        print(f"Saldo anda sekarang Rp. {self._saldo}")
    def tarik_saldo(self, saldo, pin):
        if pin == self.__pin:
            if saldo <= self._saldo:
                self._saldo -= saldo
                print(f"Saldo berhasil di tarik sebesar Rp. {saldo}")
                print(f'Saldo anda sekarang {self._saldo}')
            else:
                print("Saldo anda tidak cukup")
        else:
            print("Pin anda salah")
    def ganti_pin(self, pin_lama, pin_baru):
        if pin_lama == self.__pin:
            self.__pin = pin_baru
            print("Pin berhasil di ganti")
        else:
            print("Pin lama salah")


akun1 = bank(  "budi", 10000, "1234567890")
akun1.info()
akun1.tambah_saldo(20000)
akun1.info()
akun1.tarik_saldo(10000, "123")
akun1.ganti_pin("123", "2345")
akun1.tarik_saldo(10000, "2345")
