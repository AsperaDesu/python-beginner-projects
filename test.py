class Tokoh:
    def __init__(self, nama: str, tahunLahir: str, tahunWafat: str, kebangsaan: str, daftarJasa: list):
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
        if type(daftarJasa) != list:
            daftarJasa = daftarJasa.split(';')
            daftarJasa = [jasa.strip() for jasa in daftarJasa]

        self._daftarJasa = daftarJasa

    def __str__(self):
        str_daftarJasa = ',\n	    '.join(self.daftarJasa) + '.'
        return f'''Nama Tokoh: {self.nama} ({self.tahunLahir} - {self.tahunWafat})
Kebangsaan: {self.kebangsaan}
Jasa      : {str_daftarJasa}'''



class DaftarTokoh:
    def __init__(self, daftartokoh = None):    
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
                nama = tokoh.get('nama tokoh', '')
                tahun_lahir = tokoh.get('tahun lahir', 0)
                tahun_wafat = tokoh.get('tahun wafat', 0)
                kebangsaan = tokoh.get('kebangsaan', '')
                daftar_jasa = tokoh.get('daftar jasa', '').split(';')

                tokoh = Tokoh(nama, tahun_lahir, tahun_wafat, kebangsaan, daftar_jasa)
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

    def cari(self, namaTokoh : str):
        namaTokoh = namaTokoh.title()
        posisi = next(iter([i for i, tokoh in enumerate(self._daftartokoh) if tokoh.nama == namaTokoh]), None)
        if posisi is None:
            posisi = -1
            
        return posisi
        
    
    def __str__(self):
        return '\n\n'.join(map(str, self.daftartokoh))

new = {'nama tokoh' : 'Isaac Newton', 'tahun lahir' : 1643,
       'tahun wafat': 1727, 'kebangsaan' : 'Inggris',
       'daftar jasa' : 'Kekekalan momentum;Teleskop	pemantul;Teori warna'}

daftar = DaftarTokoh([Tokoh("Isaac Newton", "1643", "1727", "Inggris", ["Kekekalan momentum", "Teleskop", "Teori warna"])] + [new])

print(*new)