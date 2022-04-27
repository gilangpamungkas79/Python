class Mahasiswa:
    nama_univ = 'UNU Blitar'
    def __init__(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai
        self.nilai_tambahan = 0
    
    def remidi(self):
        self.nilai_tambahan += self.nilai_remidi
    def tambahan_tugas(self, nilai_remidi):
        self.nilai_tambahan += nilai_tugas
    def total_nilai(self):
        return (self.nilai + self.nilai_tambahan)/2

gilang = Mahasiswa('Gilang', 19, 5)
pamungkas = Mahasiswa('Pamungkas', 19, 5)

print(gilang.nama+', usia : '+str(gilang.usia)+", semester : "+str(gilang.semester))