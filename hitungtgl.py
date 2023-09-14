# Menghitung minggu ke berapa suatu tanggal pada tahun tertentu
# Input: tanggal, bulan, tahun
# Output: minggu ke berapa

import datetime

def hitungMinggu(tgl, bln, thn):
    tgl = int(tgl)
    bln = int(bln)
    thn = int(thn)
    hari = datetime.date(thn, bln, tgl)
    hari = hari.isocalendar()
    return hari[1]

def hitungTgl(minggu, tahun):
    minggu = int(minggu)
    tahun = int(tahun)
    # output: (tahun, bulan, tanggal) hingga (tahun, bulan, tanggal)
    tgl_awal = datetime.date(tahun, 1, 1)
    tgl_akhir = datetime.date(tahun, 12, 31)
    tgl_awal = tgl_awal.fromisocalendar(tahun, minggu, 1)
    tgl_akhir = tgl_akhir.fromisocalendar(tahun, minggu, 7)
    output = ('Minggu ke- ' + str(minggu) + ' tahun ' + str(tahun) + ': ' + str(tgl_awal) + ' hingga ' + str(tgl_akhir))
    return output

def main():
    print('Menghitung minggu ke berapa suatu tanggal pada tahun tertentu')
    print('1. Hitung minggu ke berapa')
    print('2. Hitung tanggal dari minggu ke berapa')
    pilih = int(input('Pilih: '))
    if pilih == 1:
        tgl = int(input('Tanggal: '))
        bln = int(input('Bulan: '))
        thn = int(input('Tahun: '))
        print(f'Minggu ke {hitungMinggu(tgl, bln, thn)}')
    elif pilih == 2:
        minggu = int(input('Minggu: '))
        tahun = int(input('Tahun: '))
        print(f'{hitungTgl(minggu, tahun)}')
    else:
        print('Pilihan salah')

if __name__ == '__main__':
    main()