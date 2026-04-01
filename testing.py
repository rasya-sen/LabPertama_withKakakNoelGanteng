class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

mahasiswa = Mahasiswa()
mahasiswa.nama = "Arya"
mahasiswa.perkenalan()
