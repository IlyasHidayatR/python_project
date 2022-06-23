class Buaya:

    # Dictionary of names of buaya
    jenis_buaya = {
        'B01' : 'Buaya kerdil, Osteolaemus tetraspis',
        'B02' : 'Crocodylus acutus, buaya Amerika',
        'B03' : 'Crocodylus cataphractus, Buaya moncong-ramping',
        'B04' : 'Crocodylus intermedius , buaya Orinoco',
        'B05' : 'Crocodylus johnsoni, buaya air-tawar Australia',
        'B06' : 'Crocodylus mindorensis, buaya Filipina',
        'B07' : 'Crocodylus moreletii , buaya Meksiko',
        'B08' : 'Tomistoma machikanense',
        'B09' : 'Tomistoma cairense',
        'B10' : 'Tomistoma schlegelii, buaya senyulong atau gavial Malaya',
        'B11' : 'Tomistoma lusitanica',
    }

    # Dictionary genus of buaya
    genus = {
        'F01' : 'Mekosuchinae',
        'F02' : 'Crocodylinae',
        'F03' : 'Tomistominae'
    }

    # Dictionary Species of buaya
    species = {
        'G01' : 'Euthecodon',
        'G02' : 'Rimasuchus',
        'G03' : 'Osteolaemus',
        'G04' : 'Crocodylus',
        'G05' : 'Kentisuchus',
        'G06' : 'Rhamphosuchus',
        'G07' : 'Gavialosuchus',
        'G08' : 'Thecachampsa',
        'G09' : 'Tomistoma',
        'G10' : 'Paratomistoma'
    }

    # Dictionary ciri-ciri buaya
    ciri_ciri = {
        'C01' : 'Memiliki rahang yang kuat, gigi taring yang tajam, dan moncong yang panjang untuk menangkap mangsa dan merobek daging.',
        'C02' : 'Memiliki moncong yang memanjang dan pada saat moncong tersebut menangkup, kedua deret gigi yaitu  yang berada di rahang atas dan rahang bawah terlihat berseling.',
        'C03' : 'Genus ini dapat dibedakan dengan kombinasi gigi ziphodont ini dan moncong yang lebar. Ia juga memiliki struktur alveolar (soket gigi) yang unik dan prosesus palatina anterior yang pendek (tulang mulut bagian atas).',
        'C04' : 'Osteolaemus memiliki moncong pendek yang tumpul, selagi lebar, mirip dengan caiman kerdil Cuvier, mungkin akibat menduduki yang serupa ceruk ekologi.',
        'C05' : 'Sisik punggung berlunas pendek, berjumlah 16 – 17 baris dari depan ke belakang, biasanya dalam 6 – 8 baris.  Umumnya sisik berlunas tidak mempunyai tulang yang tebal.',
        'C06' : 'Jari kakinya memiliki selaput, dan sisi kakinya berlunas.',
        'C07' : 'Ukuran tubuh 4-5 Meter',
        'C08' : 'Moncong yang memanjang dan warna cokelat pucat dengan marking coklat tua yang tersebar',
        'C09' : 'Sisik bundar dan kerikil menutupi sisi samping dan sisi luar kaki',
        'C010' : 'Tonjolan besar di ujung moncong',
        'C11' : 'Ditemukan di benua Amerika',
        'C12' : 'Ditemukan di benua Asia',
        'C13' : 'Ditemukan di benua Afrika',
        'C14' : 'Ditemukan di benua Australia',
        'C15' : 'Ditemukan di benua Eropa',

    }

    # Fungsi masukkan genus, family, species, ciri-ciri buaya
    def masukkan(self, genus, species, ciri_ciri):
        self.genus = genus
        self.species = species
        self.ciri_ciri = ciri_ciri

    # Fungsi masukkan nama buaya
    def masukkan_nama(self, jenis_buaya):
        
        self.jenis_buaya = jenis_buaya
        if self.jenis_buaya == 'B01':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G03'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C04'] + '\n' + self.ciri_ciri['C13'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B02':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C07'] + '\n' + self.ciri_ciri['C11'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B03':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C13'])

            for a in anu:
              print(a)  

        if self.jenis_buaya == 'B04':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C08'] + '\n' + self.ciri_ciri['C11'])

            for a in anu:
              print(a)   
        
        if self.jenis_buaya == 'B05':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C09'] + '\n' + self.ciri_ciri['C14'])

            for a in anu:
              print(a)
        
        if self.jenis_buaya == 'B06':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C12'])

            for a in anu:
              print(a)
  
        if self.jenis_buaya == 'B07':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F02'])
            anu.append('Nama species: ' + self.species['G04'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C01'] + '\n' + self.ciri_ciri['C05'] + '\n' + self.ciri_ciri['C11'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B08':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F03'])
            anu.append('Nama species: ' + self.species['G09'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C03'] + '\n' + self.ciri_ciri['C06'] + '\n' + self.ciri_ciri['C12'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B09':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F03'])
            anu.append('Nama species: ' + self.species['G09'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C03'] + '\n' + self.ciri_ciri['C06'] + '\n' + self.ciri_ciri['C13'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B10':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F03'])
            anu.append('Nama species: ' + self.species['G09'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C03'] + '\n' + self.ciri_ciri['C06'] + '\n' + self.ciri_ciri['C10'] + '\n' + self.ciri_ciri['C12'])

            for a in anu:
              print(a)

        if self.jenis_buaya == 'B11':
            # masukan family, genus, species, dan ciri-ciri buaya dalam array
            anu = []

            anu.append('Nama genus: ' + self.genus['F03'])
            anu.append('Nama species: ' + self.species['G09'])
            anu.append('Ciri_ciri: ' + '\n' + self.ciri_ciri['C03'] + '\n' + self.ciri_ciri['C06'] + '\n' + self.ciri_ciri['C15'])

            for a in anu:
              print(a)


    # Fungsi rule buaya dari family, genus, species, ciri-ciri
    def rule(self):
        if self.genus == 'F02':
          if self.species == 'G03':
            if 'C01' in self.ciri_ciri and 'C04' in self.ciri_ciri and 'C13' in self.ciri_ciri:
              return 'B01'
          elif self.species == 'G04':
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C07' in self.ciri_ciri and 'C11' in self.ciri_ciri:
                return 'B02'
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C13' in self.ciri_ciri:
                return 'B03'
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C08' in self.ciri_ciri and 'C11' in self.ciri_ciri:
                return 'B04'
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C09' in self.ciri_ciri and 'C14' in self.ciri_ciri:
                return 'B05'
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C12' in self.ciri_ciri:
                return 'B06'
            if 'C01' in self.ciri_ciri and 'C05' in self.ciri_ciri and 'C11' in self.ciri_ciri:
                return 'B07'
          elif self.species == 'G09':
            if 'C03' in self.ciri_ciri and 'C06' in self.ciri_ciri and 'C12' in self.ciri_ciri:
                return 'B08'
            if 'C03' in self.ciri_ciri and 'C06' in self.ciri_ciri and 'C13' in self.ciri_ciri:
                return 'B09'
            if 'C03' in self.ciri_ciri and 'C06' in self.ciri_ciri and 'C10' in self.ciri_ciri and 'C12' in self.ciri_ciri:
                return 'B10'
            if 'C03' in self.ciri_ciri and 'C06' in self.ciri_ciri and 'C15' in self.ciri_ciri:
                return 'B11'
                   
    # print rule buaya
    def print_rule(self):
        # nama buaya
        print('Nama buaya: ' + self.jenis_buaya[self.rule()])
  


# Inisialisasi buaya
buaya = Buaya()

# Main program
if __name__ == '__main__':
    # Pilih jenis masukkan
    pilih = ''
    print('Pilih jenis masukkan:')
    print('1. Masukkan nama buaya')
    print('2. Masukkan genus, species, ciri-ciri')
    pilih = input('Masukkan pilihan: ')
    # Pilih jenis masukkan
    if pilih == '1':
        # Masukkan nama buaya
        jenis_buaya = input('Masukkan nama buaya: ')
        # Masukkan nama buaya ke class buaya
        buaya.masukkan_nama(jenis_buaya)

    elif pilih == '2':
        # Masukkan genus, family, species, ciri-ciri
        genus = input('Masukkan genus: ')
        species = input('Masukkan species: ')
        ciri_ciri = input('Masukkan ciri-ciri: ')
        # Masukkan genus, family, species, ciri-ciri ke class buaya
        buaya.masukkan(genus, species, ciri_ciri)
        # Masukkan genus, family, species, ciri-ciri ke class buaya
        buaya.print_rule()
    else:
        print('Pilihan tidak ada')