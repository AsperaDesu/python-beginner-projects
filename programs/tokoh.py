def spaces(func):
    def wrapper(*args, **kwargs):
        print()
        func(*args, **kwargs)
        print()
        return 
    return wrapper

class Tokoh:
    def __init__(
        self,
        nama: str,
        tahunLahir: str,
        tahunWafat: str,
        kebangsaan: str,
        daftarJasa: list,
    ):
        self.nama = nama
        self.tahunLahir = tahunLahir
        self.tahunWafat = tahunWafat
        self.kebangsaan = kebangsaan
        self.daftarJasa = daftarJasa

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama):
        self._nama = nama.title()

    @property
    def tahunLahir(self):
        return self._tahunLahir

    @tahunLahir.setter
    def tahunLahir(self, tahunLahir):
        self._tahunLahir = tahunLahir

    @property
    def tahunWafat(self):
        return self._tahunWafat

    @tahunWafat.setter
    def tahunWafat(self, tahunWafat):
        self._tahunWafat = tahunWafat

    @property
    def kebangsaan(self):
        return self._kebangsaan

    @kebangsaan.setter
    def kebangsaan(self, kebangsaan):
        self._kebangsaan = kebangsaan.title()

    @property
    def daftarJasa(self):
        return self._daftarJasa

    @daftarJasa.setter
    def daftarJasa(self, daftarJasa):
        if not isinstance(daftarJasa, list):
            tempData = list()
            tempData.append(daftarJasa)
            daftarJasa = tempData
            
        formattedList = list()
        for jasa in daftarJasa:
            formattedList.extend([i.title() for i in jasa.split(';')])
            
        self._daftarJasa = formattedList

    def __str__(self):
        str_daftarJasa = ",\n            ".join(self.daftarJasa) + "."
        return f"""Nama Tokoh: {self.nama} ({self.tahunLahir} - {self.tahunWafat})
Kebangsaan: {self.kebangsaan}
Jasa      : {str_daftarJasa}"""


class DaftarTokoh:
    def __init__(self, daftartokoh=None):
        self.daftartokoh = daftartokoh

    @property
    def daftartokoh(self):
        return self._daftartokoh

    @daftartokoh.setter
    def daftartokoh(self, daftartokoh):
        self._daftartokoh = self.convertToClass(daftartokoh)

    def convertToClass(self, tokoh_list):
        if tokoh_list is None:
            return tokoh_list
        elif not isinstance(tokoh_list, list):
            tokoh_list = [tokoh_list]

        result = []
        for tokoh in tokoh_list:
            if not isinstance(tokoh, Tokoh):
                nama = tokoh.get("nama tokoh", "")
                tahun_lahir = tokoh.get("tahun lahir", 0)
                tahun_wafat = tokoh.get("tahun wafat", 0)
                kebangsaan = tokoh.get("kebangsaan", "")
                daftar_jasa = tokoh.get("daftar jasa", "").split(";")

                tokoh = Tokoh(nama, tahun_lahir, tahun_wafat,
                              kebangsaan, daftar_jasa)
                result.append(tokoh)
            else:
                result.append(tokoh)

        return result

    def tambah(self, tokoh):
        tokoh = self.convertToClass(tokoh)
        if isinstance(tokoh, list):
            self._daftartokoh += tokoh
        else:
            self._daftartokoh.append(tokoh)

    def input_tokoh(self):
        nama = input('Nama Tokoh    ? ')
        lahir = Menu.get_input(prompt = 'Tahun Lahir    ? ')
        wafat = Menu.get_input(prompt = 'Tahun Wafat    ? ')
        kebangsaan = input('Kebangsaan      ? ')
        jasa = input('Daftar Jasa   ? ')
        
        return (Tokoh(nama, lahir, wafat, kebangsaan, jasa))

    
    def cari(self, namaTokoh: str):
        namaTokoh = namaTokoh.title()
        scan_daftar = iter([i for i in range(len(self._daftartokoh)) 
                            if self._daftartokoh[i].nama == namaTokoh])
        posisi = next(scan_daftar, -1)
        
        return posisi

    def edit_tokoh(self, indexTokoh : int):
        new = self.input_tokoh()
        self._daftartokoh[indexTokoh] = new
        return new

    def __str__(self):
        return "\n\n".join(map(str, self.daftartokoh))


class Menu:
    def __init__(self):
        self.pilihan = None
        self.options = [
            "Tampilkan Semua Tokoh",
            "Tambahkan Tokoh",
            "Cari Tokoh",
            "Ubah Tokoh",
            "Hapus Tokoh",
        ]

        data = [
            Tokoh("Johannes Gutenberg", "1400", "1468",
                  "Jerman", ["Penemu mesin cetak"]),
            Tokoh("Tsai Lun", "50", "121", "Cina", ["Penemu kertas"]),
            Tokoh("Cristoforus Columbus", "1451", "1506",
                  "Italia", ["Penemu Benua Amerika"]),
            Tokoh("Albert Einstein", "1889", "1955", "Jerman", [
                  "Teori Relativitas Modern", "Teori Mekanika Quantum"]),
            Tokoh("Shi Huang Di", "259 SM", "210 SM", "Cina Kuno",
                  [
                      "Mendirikan Dinasti Qin",
                      "Mempersatukan Cina Kuno",
                      "Tulisan Cina",
                      "Pasukan",
                  ],
                  ),
        ]
        self.daftartokoh = DaftarTokoh(data)

    @property
    def pilihan(self):
        return self._pilihan

    @pilihan.setter
    def pilihan(self, pilihan):
        self._pilihan = pilihan

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        if not isinstance(options, list):
            options = list(options)
        options.append("Keluar")

        self._options = options
        self._exit = str(len(options))

    @property
    def daftartokoh(self):
        return self._daftartokoh

    @daftartokoh.setter
    def daftartokoh(self, daftartokoh):
        self._daftartokoh = daftartokoh

    def main_program(self):
        while self._pilihan != self._exit:
            self.display_menu()
            self.input_user()
            self.valuate_opt()

    def display_menu(self):
        print("<<< M E N U >>>")
        print("\n".join(
                [f"{num}. {opt}" for num, opt in enumerate(self.options, start=1)]
                )
            )

    def input_user(self):
        self._pilihan = self.get_input(
            prompt=f"Pilihan anda 1-{self._exit}? ", limit=[1, int(self._exit)]
        )

    @spaces
    def valuate_opt(self):
        match self._pilihan:
            case "1":
                print(self._daftartokoh)
                
            case '2':
                tambah_tokoh = self._daftartokoh.input_tokoh()
                self._daftartokoh.tambah(tambah_tokoh)
                print()
                print('Tokoh berhasil ditambahkan!!!')
                
            case '3':
                cari_tokoh = self.get_input(prompt = 'Nama Tokoh yang ditampilkan? ',
                                            data_type = str)
                find = self._daftartokoh.cari(cari_tokoh)
                
                print()
                if find == -1:
                    print(f'Tokoh dengan nama {cari_tokoh} tidak ditemukan!!!')
                else:
                    print(self._daftartokoh.daftartokoh[find])

            case '4':
                cari_tokoh = self.get_input(prompt = 'Nama tokoh yang ingin diedit? ', data_type = str)
                find = self._daftartokoh.cari(cari_tokoh)
                
                if find != -1:
                    print()
                    print(self._daftartokoh.daftartokoh[find])
                    self._daftartokoh.edit_tokoh(find)
                    print('\n' + f'Tokoh {cari_tokoh} sudah di-update!!!')
                else:
                    print(f'Tokoh {cari_tokoh} yang diedit tidak ditemukan!!!')
            
            case '5':
                cari_tokoh = self.get_input(prompt = 'Nama tokoh yang dihapus? ', 
                                            data_type = str)
                find = self._daftartokoh.cari(cari_tokoh)

                if find != -1:
                    print(self._daftartokoh.daftartokoh[find], '\n')
                
                    if self.yesOrNo():
                        self._daftartokoh.daftartokoh.pop(find)
                        print(f'Tokoh {cari_tokoh} sudah terhapus!!!')
                    else:
                        print(f'Penghapusan tokoh {cari_tokoh} dibatalkan')
                else:
                    print(f'Tokoh {cari_tokoh} yang dihapus tidak ditemukan!!!')

                         
                   
    @staticmethod
    def yesOrNo():
        answer = Menu.get_input(prompt = 'Benar mau dihapus [Y/N]? ', 
                                data_type = 'str',
                                limit = ['y', 'n'])
            
        return answer == 'y'
            
    @staticmethod
    def get_input(prompt, data_type=int, limit=None, return_type=str):
        while True:
            try:
                inputs = input(prompt)
                if not isinstance(data_type, str):
                    inputs = data_type(inputs)
                
                if limit is not None:    
                    if isinstance(data_type, int):    
                        if not limit[0] <= inputs <= limit[1]:
                            continue
                    elif isinstance(data_type, str):
                        if inputs.lower() not in limit and not inputs.isdigit():
                            continue
                
                return return_type(inputs)
                    
            except ValueError:
                continue


def main():
    menu = Menu()
    menu.main_program()


if __name__ == "__main__":
    main()