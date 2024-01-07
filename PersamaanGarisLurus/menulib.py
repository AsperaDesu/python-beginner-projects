class Menu:
    def __init__(self, mymenu : list, pilihan = 0):
        self.mymenu = mymenu
        self.pilihan = pilihan
        
    @property
    def mymenu(self):
        return self._mymenu
    
    @mymenu.setter
    def mymenu(self, mymenu):
        self._mymenu = mymenu
        self._menu_str = str(self)
        
    def display_menu(self):
        print('<<< M E N U >>>')    
        print(self._menu_str)
        print()
        self.pilihan = self.get_input(prompt = f'Pilihan anda 1-{len(self)}? ', limit= [1, len(self)], return_type = int)
    
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
    
    def __len__(self):
        return len(self.mymenu)
    
    def __getitem__(self, indeks : int):
        return self._mymenu[indeks]

    def __str__(self):
        menu_str = [f'{num}. {content}' for num, content in enumerate(self._mymenu, start = 1)]
        return '\n'.join(menu_str)
    
def main():
    menupil = Menu(['Membuat Persamaan Garis Lurus ', 'Membuat dengan Gradien dan Satu titik', 'Membuat dengan Dua Titik', 'Keluar'])        
    menupil.display_menu()
    print(menupil.pilihan)


if __name__ == '__main__':
    main()