# ==============================================================================
# PROYEK UTS PERANCANGAN DAN PEMROGRAMAN BERORIENTASI OBJEK
# TOPIK   : [E2] SISTEM MANAJEMEN SEKOLAH
# KELOMPOK: KELOMPOK 2 (KELAS IF-A PAGI)
# DOSEN   : MIRZA ILHAMI, S.Kom., M.TI.
# ==============================================================================
# ANGGOTA KELOMPOK 2:
# 1. Dian Felix Panjaitan (251112460)
# 2. Jose Aldrian Brahmana (251110996)
# 3. Samuel Ides Edwart Hutapea (251111194)
# 4. Samuel Early Thimothy Sibuea (251111743)
# ==============================================================================
import abc


class SEKOLAH(abc.ABC):
    Jumlah = 0

    def __init__(self, Nomor_Induk: str, Nama: str, Peran: str):
        self.Validasi_Kode(Nomor_Induk, "Nomor Induk (NIS/NIP)")
        self.Validasi_Nama(Nama, "Nama Lengkap")
        self._Nomor_Induk = Nomor_Induk
        self._Nama = Nama
        self.Peran = Peran
        SEKOLAH.Jumlah += 1

    @property
    def Nomor_Induk(self) -> str:
        return self._Nomor_Induk

    @property
    def Nama(self) -> str:
        return self._Nama

    @Nama.setter
    def Nama(self, Nama_Baru: str):
        self.Validasi_Nama(Nama_Baru, "Nama Lengkap")
        self._Nama = Nama_Baru

    @staticmethod
    def Validasi_Kode(Kode: str, Label: str):
        if not Kode.isdigit():
            raise ValueError(f"{Label} wajib berupa angka murni!")
        if len(Kode) < 5 or len(Kode) > 12:
            raise ValueError(f"Panjang {Label} harus antara 5 sampai 12 digit angka!")

    @staticmethod
    def Validasi_Nama(Teks: str, Label: str):
        Clean = Teks.replace(" ", "").replace(".", "").replace(",", "")
        if not Clean:
            raise ValueError(f"{Label} tidak boleh kosong!")
        if not Clean.isalpha():
            raise ValueError(f"{Label} hanya boleh berisi huruf dan spasi!")

    @abc.abstractmethod
    def PROFIL(self):
        pass


class SISWA(SEKOLAH):
    def __init__(self, NIS: str, Nama: str, Kelas: str, Wali: str):
        super().__init__(NIS, Nama, "Siswa")
        self.Validasi_Nama(Wali, "Nama Wali Murid")
        if not Kelas.strip():
            raise ValueError("Nama kelas tidak boleh kosong!")
        self.Kelas = Kelas.strip().upper()
        self.Wali = Wali

    @classmethod
    def DICT(cls, Data: dict):
        return cls(Data["NIS"], Data["Nama"], Data["Kelas"], Data["Wali"])

    def PROFIL(self):
        print(f"{'Status Peran':<18}: {self.Peran}")
        print(f"{'NIS':<18}: {self.Nomor_Induk}")
        print(f"{'Nama Lengkap':<18}: {self.Nama}")
        print(f"{'Kelas':<18}: {self.Kelas}")
        print(f"{'Orang Tua / Wali':<18}: {self.Wali}")


class GURU(SEKOLAH):
    def __init__(self, NIP: str, Nama: str, MP: str, Kelas: str = "-"):
        super().__init__(NIP, Nama, "Guru")
        if not MP.strip():
            raise ValueError("Mata pelajaran tidak boleh kosong!")
        self.MP = MP.strip()
        self.Kelas = Kelas.strip().upper() if Kelas.strip() else "-"

    def PROFIL(self):
        print(f"{'Status Peran':<18}: {self.Peran}")
        print(f"{'NIP':<18}: {self.Nomor_Induk}")
        print(f"{'Nama Lengkap':<18}: {self.Nama}")
        print(f"{'Guru Pengampu':<18}: {self.MP}")
        print(f"{'Wali Kelas':<18}: {self.Kelas}")


