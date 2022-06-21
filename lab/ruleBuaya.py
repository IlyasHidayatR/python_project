class Buaya:
    # Dictionary family of buaya
    family = {
        'L01': 'Crocodylus'
    }

    # Dictionary of names of buaya
    buaya = {
        'B01' : 'Buaya kerdil, Osteolaemus tetraspis',
        'B02' : 'Crocodylus acutus, buaya Amerika',
        'B03' : 'Crocodylus acutus, buaya Amerika',
        'B04' : 'Crocodylus cataphractus, Buaya moncong-ramping',
        'B05' : 'Crocodylus intermedius , buaya Orinoco',
        'B06' : 'Crocodylus johnsoni, buaya air-tawar Australia',
        'B07' : 'Crocodylus nigricans, buaya air-tawar Australia',
        'B08' : 'Crocodylus mindorensis, buaya Filipina',
        'B09' : 'Crocodylus moreletii , buaya Meksiko',
        'B10' : 'Tomistoma machikanense',
        'B11' : 'Tomistoma cairense',
        'B12' : 'Tomistoma schlegelii, buaya senyulong atau gavial Malaya',
        'B13' : 'Tomistoma lusitanica'
    }

    # Dictionary genus of buaya
    genus = {
        'F01' : 'Mekosuchinae',
        'F02' : 'Crocodyli',
        'F03' : 'Tomistominae'
    }

    # Dictionary Species of buaya
    species = {
        'S01' : 'Euthecodon',
        'S02' : 'Rimasuchus',
        'S03' : 'Osteolaemus',
        'S04' : 'Crocodylus',
        'S05' : 'Kentisuchus',
        'S06' : 'Rhamphosuchus',
        'S07' : 'Gavialosuchus',
        'S08' : 'Thecachampsa',
        'S09' : 'Tomistoma',
        'S10' : 'Paratomistoma'
    }

    # Dictionary ciri-ciri buaya
    ciri_ciri = {
        'C01' : 'Memiliki rahang yang kuat, gigi taring yang tajam, dan moncong yang panjang untuk menangkap mangsa dan merobek daging.',
        'C02' : 'Memiliki moncong yang memanjang dan pada saat moncong tersebut menangkup, kedua deret gigi yaitu  yang berada di rahang atas dan rahang bawah terlihat berseling.',
        'C03' : 'Genus ini dapat dibedakan dengan kombinasi gigi ziphodont ini dan moncong yang lebar. Ia juga memiliki struktur alveolar (soket gigi) yang unik dan prosesus palatina anterior yang pendek (tulang mulut bagian atas).',
        'C04' : 'Osteolaemus memiliki moncong pendek yang tumpul, selagi lebar, mirip dengan caiman kerdil Cuvier, mungkin akibat menduduki yang serupa ceruk ekologi.',
        'C05' : 'Sisik punggung berlunas pendek, berjumlah 16 – 17 baris dari depan ke belakang, biasanya dalam 6 – 8 baris.  Umumnya sisik berlunas tidak mempunyai tulang yang tebal.',
        'C06' : 'Jari kakinya memiliki selaput, dan sisi kakinya berlunas.'
    }

    # Fungsi masukkan genus, family, species, ciri-ciri buaya
    def masukkan(self, genus, family, species, ciri_ciri):
        self.genus = genus
        self.family = family
        self.species = species
        self.ciri_ciri = ciri_ciri

    # Fungsi masukkan nama buaya
    def masukkan_nama(self, nama):
        self.nama = nama

    # Fungsi rule buaya dari family, genus, species, ciri-ciri
    def rule(self):
        if self.family == 'L01':
            if self.genus == 'F01':
                if self.species == 'S03':
                    if self.ciri_ciri == 'C04':
                        return 'B01'
                elif self.species == 'S04':
                    if self.ciri_ciri == 'C05':
                        # print buaya kode B02 , B03, B04, dan B05
                        return 'B02'
    
    # Fungsi rule buaya dari nama buaya
    def rule_nama(self):
        # jika buaya kode B01 maka L01, F01, S03, C04
        if self.rule() == 'B01':
            return 'F01, L01, S03, C04'

                        
                        


    # print rule buaya
    def print_rule(self):
        # nama buaya
        print('Nama buaya: ' + self.buaya[self.rule()])
    
    # print rule buaya dari nama buaya
    def print_rule_nama(self):
        # nama buaya
        print('Nama buaya: ' + self.buaya[self.rule_nama()])
        # print species, genus, family, ciri-ciri
        print('Genus: ' + self.genus[self.genus[self.rule_nama()]])
        print('Family: ' + self.family[self.family[self.rule_nama()]])
        print('Species: ' + self.species[self.species[self.rule_nama()]])
        print('Ciri-ciri: ' + self.ciri_ciri[self.ciri_ciri[self.rule_nama()]])

    
# Main program
if __name__ == '__main__':
    # Pilih jenis masukkan
    print('Pilih jenis masukkan:')
    print('1. Masukkan nama buaya')
    print('2. Masukkan genus, family, species, ciri-ciri')
    pilih = input('Masukkan pilihan: ')
    # Pilih jenis masukkan
    if pilih == '1':
        # Masukkan nama buaya
        nama = input('Masukkan nama buaya: ')
        # Masukkan nama buaya ke class buaya
        buaya = Buaya()
        buaya.masukkan_nama(nama)
        # Masukkan nama buaya ke class buaya
        buaya.print_rule_nama()
    elif pilih == '2':
        # Masukkan genus, family, species, ciri-ciri
        genus = input('Masukkan genus: ')
        family = input('Masukkan family: ')
        species = input('Masukkan species: ')
        ciri_ciri = input('Masukkan ciri-ciri: ')
        # Masukkan genus, family, species, ciri-ciri ke class buaya
        buaya = Buaya()
        buaya.masukkan(genus, family, species, ciri_ciri)
        # Masukkan genus, family, species, ciri-ciri ke class buaya
        buaya.print_rule()


        



