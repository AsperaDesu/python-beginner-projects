import sys
    
class Suhu():
    def __init__(self, converse, nilai):
        self.converse = converse
        self.nilai = nilai

    @classmethod
    def bagi(cls, converse):
        if converse == '-':
          sys.exit()  

        converse = converse.replace(' ' , '')
        nilai = ''.join([i for i in converse if i.isdigit()])
        converse = converse[converse.index(nilai[-1]) + 1:]
        
        cls.converse = converse
        cls.nilai = nilai

        return nilai, converse

    
    @classmethod
    def cel2fah(cls, nilai):
        return 9/5 * nilai + 32

        
    @classmethod
    def fah2cel(cls, nilai):
        return 5/9 * (nilai - 32)

        
    @classmethod
    def cel2rea(cls, nilai):
        return 4/5 * nilai
    

    @classmethod 
    def rea2cel(cls, nilai):
        return 5/4 * nilai


    @classmethod 
    def cel2kel(cls, nilai):
        return nilai + 273.15


    @classmethod
    def kel2cel(cls, nilai):
        return nilai - 273.15


    
def main():
    while True:
        print('Konversi Suhu, format:')
        konvers = input('     ')
        suhu, perintah = Suhu.bagi(konvers)


        print(f'Artinya mengkonversi {suhu}')


        derajat = cari(suhu, perintah)

        print(derajat)



def cari(nilai, perintah):
    nilai = int(nilai)
    derajat = True
    match perintah:
        case 'c-f':
            converts =  Suhu.cel2fah(nilai), derajat
        case 'f-c':
            converts = Suhu.fah2cel(nilai), derajat
        case 'c-r':
            converts = Suhu.cel2rea(nilai), derajat
        case 'r-c':
            converts = Suhu.rea2cel(nilai), derajat
        case 'c-k':
            derajat = False
            converts = Suhu.cel2kel(nilai), derajat
        case 'k-c':
            converts = Suhu.kel2cel(nilai), derajat
    
    huruf = perintah[-1]

    if huruf == 'c':
        satuan = 'Celcius'
    elif huruf == 'k':
        satuan = 'Kelvin'
    elif  huruf == 'r':
        satuan = 'Reaumur'
    elif huruf == 'f':
        satuan = 'Fahrenheit'


    return 

if __name__ == '__main__':
    main()

