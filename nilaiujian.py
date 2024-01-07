class mymenu:
    def __init__(self, grup = []):
        self.pilihan = [
            "tampilkan semua siswa",
            "tampilkan satu siswa",
            "input siswa",
            "edit siswa",
            "edit nilai",
            "hapus siswa",
        ]
        self.choose = None
        self.grup = GrupSiswa(grup)

    @property
    def pilihan(self):
        return self._pilihan

    @pilihan.setter
    def pilihan(self, pilihan):
        if 'keluar' not in pilihan:
            pilihan = pilihan + ['keluar']
            
        self._pilihan = pilihan
        self._display = "\n".join(
            [
                f"{num}. {content.title()}"
                for num, content in enumerate(self._pilihan, start=1)
            ]
        )

    def spaces(func):
        def wrapper(*args, **kwargs):
            print()
            result = func(*args, **kwargs)
            print()
            return result
        return wrapper
    
    def display_menu(self):
        print(
            f"""<<< M E N U >>>
{str(self)}
""")
        self.choose = self.get_input(f"Pilihan anda 1-{len(self._pilihan)}? ", limit = [1, len(self)])
        self.evaluateChoice()
    
    @spaces
    def evaluateChoice(self):
        match self.choose:
            case '1':
                print('TAMPILKAN SEMUA SISWA')
                print(self.grup.cetak_semua_siswa())
            
            case '2':
                print('TAMPILKAN SATU SISWA SAJA')
                again = True
                while again:
                    nama = self.get_input(prompt = 'Nama siswa? ', data_type = str)
                    print(self.grup.cetak_satu_siswa(nama))
                    
                    again = self.askContinue()
            
            case '3':
                print('TAMBAH SISWA')
                print('Siswa Baru:')
                again = True
                while again: 
                    nama = self.get_input(prompt = 'Nama? ', data_type=str)
                    kelas = self.get_input(prompt = 'Kelas? ', return_type= int)
                    siswa = Siswa(nama, kelas)
                    
                    self.grup.tambahsiswa(siswa)
                    again = self.askContinue()
                    
            case '4':
                print('EDIT SISWA')
                again = True
                while again:
                    nama = self.get_input(prompt = 'Nama Siswa? ', data_type = str)
                    self.grup.editsiswa(nama, displayTxt= False)
                    again = self.askContinue()
            
            case '5':
                print('EDIT NILAI SISWA')
                again = True
                
                while again:
                    nama = self.get_input(prompt = 'Nama Siswa? ', data_type = str)
                    cari = self.grup.cari_siswa(nama)
                    self.grup.editnilaisiswa(cari)
                    
                    again = self.askContinue()
                    
            case '6':
                print('HAPUS SISWA')
                again = True
                
                while again:
                    nama = self.get_input(prompt = 'Nama Siswa? ', data_type = str)
                    cari = self.grup.cari_siswa(nama, displayTxt = False)
                    
                    del self.grup[cari]
                    print('Data sudah dihapus...')
                    again = self.askContinue()
                    
    @staticmethod
    def get_input(prompt: str, data_type=int, limit=None, return_type=str):
        valid = True
        while True:
            try:
                inputs = input(prompt).strip()
                if isinstance(data_type, str) is False:
                    inputs = data_type(inputs)

                if isinstance(data_type, int):
                    if (limit[0] <= inputs <= limit[1]) is False:
                        valid = False

                if valid:
                    return return_type(inputs)
            except ValueError:
                pass

    @staticmethod
    @spaces
    def askContinue(prompt = 'Lagi [Y/T]?: Enter lagi berarti "Y"? '):
        answer = 'ENTERANSWERHERE'
        while answer != 'y' and answer != 't' and answer != '':
            answer = input(prompt).strip().lower()
        
        if answer == 'y' or answer == '':
            return True
        else:
            return False
    
    def __len__(self):
        return len(self._pilihan)

    def __str__(self):
        return self._display


class GrupSiswa:
    def __init__(self, grupsiswa : list = []):
        self.grupsiswa = grupsiswa
        
    @property
    def grupsiswa(self):
        return self._grupsiswa
    
    @grupsiswa.setter
    def grupsiswa(self, grupsiswa):
        self._grupsiswa = grupsiswa

    def cari_siswa(self, cari, displayTxt = True, displayNilai = True):
        def display(result, cari):
            if result != -1:
                print(f'Siswa dengan nama {cari} ditemukan pada posisi indeks {result}')
            else:
                print(f'Siswa dengan nama {cari} tidak ditemukan!')
            
        cari = cari.title()
        result = -1
        for num, siswa in enumerate(self._grupsiswa):
            if cari in siswa.nama_siswa:
                result = num
                break
        
        if displayTxt:
            display(result, cari)
            
        if displayNilai and result != -1:
            print(repr(siswa))
            
        return result
    
    def cetak_satu_siswa(self, nama : str):
        posisiSiswa = self.cari_siswa(nama, displayTxt = False)
        if posisiSiswa != -1:
            return repr(self[posisiSiswa])
        else:
            return (f'Siswa {nama} tidak ditemukan!')
            
    def cetak_semua_siswa(self):
        result = []
        for siswa in self._grupsiswa:
            result.append(repr(siswa))
        
        return '\n'.join(result)
    
    def tambahsiswa(self, listSiswa):
        if isinstance(listSiswa, list) is False:
            listSiswa = [listSiswa]
                       
        for siswa in listSiswa:
            print(f'{siswa.nama_siswa} sudah ditambahkan...')
        
        self._grupsiswa.extend(listSiswa)
    
    def editsiswa(self, siswa, displayTxt = True): 
        siswa = siswa.title()
        
        if (indeks := self.cari_siswa(siswa, displayTxt= displayTxt)) != -1:
            nama = mymenu.get_input('Nama Baru? ', data_type = str)
            kelas = mymenu.get_input('Kelas Baru? ')            

            self._grupsiswa.pop(indeks)
            self._grupsiswa.insert(indeks, Siswa(nama, kelas))

            print('Data sudah diedit..\n')
            
        else:
            print('Edit tidak bisa dilakukan!')
        
        return
    
    def editnilaisiswa(self, indeks : int):
        if indeks == -1:
            print('Edit nilai tidak bisa dilakukan!')
            return
        
        siswa = self[indeks]
        for mapel, nilai in siswa.nilai.items():
            print(f'>>>Nilai {mapel.upper()} sekarang:')
            while True:
                try:
                    editNilai = input(f'{nilai} menjadi [Enter berarti sama!]? ')
                    if editNilai == '':
                        editNilai = nilai
                        break
                    else:
                        editNilai = int(editNilai)
                    break
                except ValueError:
                    continue
            siswa[mapel] = editNilai
        
        self[indeks] = siswa
        print('Data nilai sudah diedit...')        
        return self[indeks].nama_siswa
        
    def __setitem__(self, index, value):
        self._grupsiswa.pop(index)
        self._grupsiswa.insert(index, value)
        return self._grupsiswa
    
    def __getitem__(self, indeks : int):
        return self._grupsiswa[indeks]
    
    def __delitem__(self, indeks : int):
        del self._grupsiswa[indeks]
        return self._grupsiswa        
    def __str__(self):
        grup_str = [f'{siswa.nama_siswa}, {siswa.kelas}' for siswa in self._grupsiswa]
        return '\n'.join(grup_str)


class Siswa:
    def __init__(
        self,
        nama_siswa: str,
        kelas: int,
        nilai={
            "agama": -1,
            "pkn": -1,
            "ipa": -1,
            "ips": -1,
            "mtk": -1,
            "bindo": -1,
            "bing": -1,
            "penjas": -1,
        },
    ):
        self.nama_siswa = nama_siswa
        self.kelas = kelas
        self.nilai = nilai

    @property
    def nama_siswa(self):
        return self._nama_siswa

    @nama_siswa.setter
    def nama_siswa(self, nama_siswa):
        self._nama_siswa = nama_siswa.title()

    @property
    def kelas(self):
        return self._kelas

    @kelas.setter
    def kelas(self, kelas):
        self._kelas = kelas

    def __str__(self):
        str_siswa = (
            f'{"Nama":<5} : {self._nama_siswa}\n' + f'{"Kelas":<5} : {self._kelas}'
        )
        return str_siswa

    def __repr__(self) -> str:
        str_nilai = "\n".join(
            [f"{key.upper():<15} {value:^10}" for key, value in self.nilai.items()]
            )
        
        str_siswa2 = f"""{str(self)}
{'-' * 25}
{'Mata Pelajaran':<15} {'Nilai':^10}
{'=' * 25}
{str_nilai}
{'-' * 25}
"""
        return str_siswa2

    def __iter__(self):
        for nilai in [
            f"{key.upper():<15} {value:^10}" for key, value in self.nilai.items()
        ]:
            yield nilai

    def __setitem__(self, key, value):
        self.nilai[key] = value
    
    def __getitem__(self, key):
        return self.nilai[key]
    
    def __eq__(self, other):
        if type(self) is type(other):
            return other._nama_siswa == self._nama_siswa
        else:
            return other == self._nama_siswa
        
def main():
    aku = Siswa('Hendri Tay', 168)
    kamu = Siswa('Ferdinand', 178)
    kembaran = Siswa('hendro', 168)
    menu = mymenu([aku, kamu, kembaran])
    
    while menu.choose != str(len(menu)):
        menu.display_menu()
    
    
        
if __name__ == "__main__":
    main()
