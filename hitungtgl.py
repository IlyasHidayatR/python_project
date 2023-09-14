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

tgl = input("Masukkan tanggal: ")
bln = input("Masukkan bulan: ")
thn = input("Masukkan tahun: ")
print("Minggu ke-", hitungMinggu(tgl, bln, thn))