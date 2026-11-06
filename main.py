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


class KELAS:
    def __init__(self, Kelas: str):
        if not Kelas.strip():
            raise ValueError("Nama ruang kelas tidak boleh kosong!")
        self.Kelas = Kelas.strip().upper()
        self.Wali = None
        self.Daftar_Siswa = []
        self.Jadwal = []

    def ASSIGN(self, Objek_Guru: GURU):
        self.Wali = Objek_Guru
        Objek_Guru.Kelas = self.Kelas

    def TAMBAH_SISWA(self, Objek_Siswa: SISWA):
        for s in self.Daftar_Siswa:
            if s.Nomor_Induk == Objek_Siswa.Nomor_Induk:
                raise ValueError(
                    f"Siswa dengan NIS {Objek_Siswa.Nomor_Induk} sudah terdaftar di kelas ini!"
                )
        Objek_Siswa.Kelas = self.Kelas
        self.Daftar_Siswa.append(Objek_Siswa)
        self.Daftar_Siswa = sorted(self.Daftar_Siswa, key=lambda item: item.Nomor_Induk)

    def TAMBAH_JADWAL(self, Hari: str, Jam: str, MP: str, Nama_Guru: str):
        if not Hari.strip() or not Jam.strip() or not MP.strip():
            raise ValueError("Hari, Jam, dan Mata Pelajaran wajib diisi lengkap!")
        Entri = {
            "Hari": Hari.strip().capitalize(),
            "Jam": Jam.strip(),
            "MP": MP.strip(),
            "Guru": Nama_Guru.strip(),
        }
        self.Jadwal.append(Entri)

    def INFO_KELAS(self):
        Nama_Wali = self.Wali.Nama if self.Wali else "Belum Ditentukan"
        print("\n" + "=" * 56)
        print(f"DATA ROMBEL KELAS : {self.Kelas}")
        print(f"Wali Kelas        : {Nama_Wali}")
        print(f"Jumlah Siswa      : {len(self.Daftar_Siswa)} Siswa (Terurut berdasarkan NIS)")
        print("-" * 56)
        if not self.Daftar_Siswa:
            print("Belum ada siswa terdaftar di kelas ini.")
        else:
            for idx in range(len(self.Daftar_Siswa)):
                s = self.Daftar_Siswa[idx]
                print(f"{idx + 1}. [{s.Nomor_Induk}] {s.Nama:<22} | Wali: {s.Wali}")
        print("=" * 56)

    def TAMPIL_JADWAL(self):
        print("\n" + "=" * 56)
        print(f"JADWAL PELAJARAN KELAS {self.Kelas}")
        print("=" * 56)
        if not self.Jadwal:
            print("Belum ada jadwal pelajaran pada kelas ini.")
        else:
            for idx in range(len(self.Jadwal)):
                j = self.Jadwal[idx]
                print(f"{idx + 1}. {j['Hari']:<8} | {j['Jam']:<13} | {j['MP']:<16} | {j['Guru']}")
        print("=" * 56)


class ABSENSI:
    STATUS_VALID = ("HADIR", "IZIN", "SAKIT", "ALPHA")

    def __init__(self):
        self.Riwayat = {}
        self.Total_Log = 0
        self._Coroutine = self._Hitung_Log()
        next(self._Coroutine)

    def _Hitung_Log(self):
        Akumulasi = 0
        while True:
            Tambahan = yield Akumulasi
            Akumulasi += Tambahan

    def CATAT(self, NIS: str, Nama_Siswa: str, Tanggal: str, Status: str):
        Status_Kapital = Status.strip().upper()
        if Status_Kapital not in self.STATUS_VALID:
            raise ValueError("Status presensi hanya boleh: HADIR, IZIN, SAKIT, atau ALPHA!")
        if not Tanggal.strip():
            raise ValueError("Tanggal presensi tidak boleh kosong!")
        if NIS not in self.Riwayat:
            self.Riwayat[NIS] = {"Nama": Nama_Siswa, "Log": []}
        self.Riwayat[NIS]["Log"].append({"Tanggal": Tanggal.strip(), "Status": Status_Kapital})
        self.Total_Log = self._Coroutine.send(1)

    def PERSENTASE(self, NIS: str) -> float:
        if NIS not in self.Riwayat:
            return 0.0
        Daftar_Log = self.Riwayat[NIS]["Log"]
        if not Daftar_Log:
            return 0.0
        Daftar_Hadir = [item for item in Daftar_Log if item["Status"] == "HADIR"]
        return (len(Daftar_Hadir) / len(Daftar_Log)) * 100.0

    def CETAK_REKAP(self, NIS: str):
        if NIS not in self.Riwayat:
            print(f"\n[INFO] Belum ada data presensi untuk NIS {NIS}.")
            return
        Data_Siswa = self.Riwayat[NIS]
        print("\n" + "=" * 56)
        print(f"REKAP KEHADIRAN SISWA : {Data_Siswa['Nama']} (NIS: {NIS})")
        print("=" * 56)
        Items = iter(Data_Siswa["Log"])
        Urutan = 1
        while True:
            try:
                Log_Item = next(Items)
                print(
                    f"Pertemuan ke-{Urutan:<2} | Tanggal: {Log_Item['Tanggal']:<12} | Status: {Log_Item['Status']}"
                )
                Urutan += 1
            except StopIteration:
                break
        Persen = self.PERSENTASE(NIS)
        print("-" * 56)
        print(f"Total Pertemuan      : {len(Data_Siswa['Log'])} Hari")
        print(f"Persentase Kehadiran : {Persen:.2f}%")
        print("=" * 56)


