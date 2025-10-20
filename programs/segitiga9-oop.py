import math

class Triangle:
    jenis_segitiga = ['Siku-Siku', 'Sama Sisi', 'Sama Kaki', 'Sembarang', '']
    
    def __init__(self, jenis, nama, alas):
        self.jenis = jenis if jenis else 'Siku-Siku'
        self.nama = nama.upper().strip()
        self.alas = int(alas.strip())
        self._tinggi = None
        self._namasisi = None
        self._panjangsisi = None
        self._keliling = None
        self._luas = None
        
    def get_tinggi(self):
        if self._tinggi is not None:
            return self._tinggi
        
        if self.jenis == 'Sama Sisi':
            tinggi = self.get_height()
        elif self.jenis == 'Sembarang':
            s = 0.5 * (sum(self.get_panjangsisi()))
            kali = 1
            for i in range(len(self.get_namasisi())):
                kali *= s - self.get_panjangsisi()[i]
            try:
                luas = math.sqrt(s * kali)
            except ValueError:
                pass
            tinggi = 2 * luas / self.alas
        else:
            tinggi = int(input('Tinggi (cm)? ').strip())
        
        self._tinggi = tinggi
        return self._tinggi
        
    def get_namasisi(self):
        if self._namasisi is not None:
            return self._namasisi
        
        new = []
        nama = self.nama
        for i in range(len(nama)):
            new.append(''.join(sorted(nama[i] + nama[(i + 1) % len(nama)])))
        
        self._namasisi = new
        return self._namasisi
    
    def get_panjangsisi(self):
        if self._panjangsisi is not None:
            return self._panjangsisi
        
        panjangsisi = []
        if self.jenis == 'Siku-Siku':
            sisi1 = self.alas
            sisi2 = self.get_tinggi()
            sisi3 = self.get_tilt()
            
        elif self.jenis == 'Sama Sisi':
            sisi1 = self.alas
            sisi2 = self.alas
            sisi3 = self.alas
            
        elif self.jenis == 'Sembarang':
            print()
            sisi1 = self.alas
            sisi2 = self.prompt_distance(f'Panjang Sisi {self.get_namasisi()[1]}? ')
            sisi3 = self.prompt_distance(f'Panjang Sisi {self.get_namasisi()[2]}? ')
            
        elif self.jenis == 'Sama Kaki':
            sisi1 = self.alas
            sisi2 = self.get_tilt()
            sisi3 = sisi2
            
        panjangsisi = [sisi1, sisi2, sisi3]
        self._panjangsisi = panjangsisi
        return self._panjangsisi
        
    def get_keliling(self):
        if self._keliling is not None:
            return self._keliling
        
        keliling = sum(self.get_panjangsisi())
        self._keliling = keliling
        return self._keliling
        
    def get_luas(self):
        if self._luas is not None:
            return self._luas
        
        luas = 0.5 * self.alas * self.get_tinggi()
        self._luas = luas
        return self._luas
    
    def ceksisi(self):
        sisi1, sisi2, sisi3 = self.get_panjangsisi()
        if not((sisi1 + sisi3 > sisi2) and (sisi3 + sisi2 > sisi1) and (sisi1 + sisi2 > sisi3)):
            self.alas = 0
            self._tinggi = 0
            self._panjangsisi = [0, 0, 0]
    
    def get_tilt(self):
        return math.sqrt(self.alas**2 + (self.get_tinggi())**2)
    
    def get_height(self):
        return math.sqrt(self.alas**2 - (self.alas / 2)**2)
    
    def prompt_distance(self, prompt):
        while True:
            try:
                sisi = int(input(prompt))
                return sisi
            except ValueError:
                pass
    
    def __str__(self):
        sisi_str = []
        for i in range(len(self.get_namasisi())):
            sisi_str.append(f'    Sisi {self.get_namasisi()[i]}: {self.get_panjangsisi()[i]} cm')
        
        sisi_str = "\n".join(sisi_str)
        
        return f'''Jenis Segitiga    : {self.jenis}
Nama Segitiga    : {self.nama}
Panjang Alas    : {self.alas} cm
Tinggi        : {self.get_tinggi()} cm

Nama-Nama Sisi:
{sisi_str}

Keliling Segitiga = {self.get_keliling()} cm
Luas Segitiga = {self.get_luas()} cm² 
'''


def main():
    while True:
        jenis =  input('Jenis Segitiga (Enter: Siku-Siku)? ').strip().title()
        if jenis in Triangle.jenis_segitiga:
            break
        else:
            print(f'Masukkan jenis segitiga yang sesuai\nDiantaranya adalah : {", ".join(Triangle.jenis_segitiga)}\n')
        
    while True:
        nama = input('Nama Segitiga? ')
        if len(nama) == 3:
            break
        else:
            print('Jumlah huruf pada segitiga harus 3')
            
    alas = input('Panjang Alas (cm)? ')
    
    segitiga1 = Triangle(jenis, nama, alas)
    segitiga1.ceksisi()
    print(f'\n{segitiga1}')


if __name__ == '__main__':
    main()
