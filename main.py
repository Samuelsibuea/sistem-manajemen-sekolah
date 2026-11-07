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


class InvalidGradeException(Exception):
    pass


class NILAI:
    def __init__(self):
        self.Data_Nilai = {}

    @staticmethod
    def Validasi_Angka(Nilai_Input: float, Komponen: str):
        if Nilai_Input < 0 or Nilai_Input > 100:
            raise InvalidGradeException(
                f"Nilai {Komponen} ({Nilai_Input}) tidak valid! Nilai wajib berada di rentang 0 sampai 100."
            )

    def INPUT_NILAI(
        self, NIS: str, Nama_Siswa: str, MP: str, Ulangan: float, UTS: float, UAS: float
    ):
        if not MP.strip():
            raise ValueError("Nama mata pelajaran tidak boleh kosong!")
        self.Validasi_Angka(Ulangan, "Ulangan")
        self.Validasi_Angka(UTS, "UTS")
        self.Validasi_Angka(UAS, "UAS")
        Nilai_Akhir = self.HITUNG_AKHIR(Ulangan, UTS, UAS)
        if NIS not in self.Data_Nilai:
            self.Data_Nilai[NIS] = {"Nama": Nama_Siswa, "MP": {}}
        self.Data_Nilai[NIS]["MP"][MP.strip()] = {
            "Ulangan": Ulangan,
            "UTS": UTS,
            "UAS": UAS,
            "Akhir": Nilai_Akhir,
        }

    @staticmethod
    def HITUNG_AKHIR(Ulangan: float, UTS: float, UAS: float) -> float:
        return (0.40 * Ulangan) + (0.30 * UTS) + (0.30 * UAS)

    def CETAK_RAPOR(self, NIS: str):
        if NIS not in self.Data_Nilai:
            print(f"\n[INFO] Belum ada data nilai untuk NIS {NIS}.")
            return
        Info = self.Data_Nilai[NIS]
        print("\n" + "=" * 64)
        print(f"TRANSKRIP & RAPOR SISWA : {Info['Nama']} (NIS: {NIS})")
        print("Bobot Penilaian         : 40% Ulangan | 30% UTS | 30% UAS")
        print("=" * 64)
        print(
            f"{'Mata Pelajaran':<20} | {'Ulangan':<8} | {'UTS':<8} | {'UAS':<8} | {'Nilai Akhir':<11}"
        )
        print("-" * 64)
        for Nama_MP, n in Info["MP"].items():
            print(
                f"{Nama_MP:<20} | {n['Ulangan']:<8.1f} | {n['UTS']:<8.1f} | "
                f"{n['UAS']:<8.1f} | {n['Akhir']:<11.2f}"
            )
        print("=" * 64)


class MANAJEMEN_SEKOLAH:
    def __init__(self):
        self.Daftar_Siswa = {}
        self.Daftar_Guru = {}
        self.Daftar_Kelas = {}
        self.Absensi_Mgr = ABSENSI()
        self.Nilai_Mgr = NILAI()
        self._Muat_Data_Awal()

    def _Muat_Data_Awal(self):
        g1 = GURU("19880101", "Mirza Ilhami", "Pemrograman OOP", "X-IPA-1")
        g2 = GURU("19900202", "Kelvin Pratama", "Struktur Data", "X-IPA-2")
        self.Daftar_Guru[g1.Nomor_Induk] = g1
        self.Daftar_Guru[g2.Nomor_Induk] = g2
        k1 = KELAS("X-IPA-1")
        k1.ASSIGN(g1)
        self.Daftar_Kelas[k1.Kelas] = k1
        Data_Awal_Siswa = [
            {
                "NIS": "251112460",
                "Nama": "Dian Felix Panjaitan",
                "Kelas": "X-IPA-1",
                "Wali": "Bapak Panjaitan",
            },
            {
                "NIS": "251110996",
                "Nama": "Jose Aldrian Brahmana",
                "Kelas": "X-IPA-1",
                "Wali": "Bapak Brahmana",
            },
            {
                "NIS": "251111743",
                "Nama": "Samuel Early Sibuea",
                "Kelas": "X-IPA-1",
                "Wali": "Bapak Sibuea",
            },
            {
                "NIS": "251111194",
                "Nama": "Samuel Ides Hutapea",
                "Kelas": "X-IPA-1",
                "Wali": "Bapak Hutapea",
            },
        ]
        for item in Data_Awal_Siswa:
            Obj_Siswa = SISWA.DICT(item)
            self.Daftar_Siswa[Obj_Siswa.Nomor_Induk] = Obj_Siswa
            k1.TAMBAH_SISWA(Obj_Siswa)
        k1.TAMBAH_JADWAL("Senin", "08:00 - 09:40", "Pemrograman OOP", g1.Nama)
        k1.TAMBAH_JADWAL("Kamis", "09:00 - 10:40", "Struktur Data", g2.Nama)
        self.Absensi_Mgr.CATAT("251112460", "Dian Felix Panjaitan", "01-11-2026", "HADIR")
        self.Absensi_Mgr.CATAT("251112460", "Dian Felix Panjaitan", "02-11-2026", "HADIR")
        self.Absensi_Mgr.CATAT("251112460", "Dian Felix Panjaitan", "03-11-2026", "IZIN")
        self.Nilai_Mgr.INPUT_NILAI(
            "251112460", "Dian Felix Panjaitan", "Pemrograman OOP", 90, 85, 95
        )
        self.Nilai_Mgr.INPUT_NILAI(
            "251110996", "Jose Aldrian Brahmana", "Pemrograman OOP", 88, 90, 92
        )

    def DEMO_UTS(self):
        print("\n" + "#" * 66)
        print(f"{'SIMULASI DEMO FITUR 1 - 10 SISTEM MANAJEMEN SEKOLAH':^66}")
        print("#" * 66)
        print("\n>>> [FITUR 1 & 2] DIREKTORI DATA INDUK SISWA & GURU :")
        Data_Induk = [self.Daftar_Siswa["251112460"], self.Daftar_Guru["19880101"]]
        for item in Data_Induk:
            item.PROFIL()
            print("-" * 56)
        print("\n>>> [FITUR 3, 4 & 5] INFO KELAS, WALI KELAS, URUT NIS & JADWAL:")
        Kelas_Demo = self.Daftar_Kelas["X-IPA-1"]
        Kelas_Demo.INFO_KELAS()
        Kelas_Demo.TAMPIL_JADWAL()
        print("\n>>> [FITUR 6 & 7] REKAP PRESENSI HARIAN & PERSENTASE KEHADIRAN :")
        self.Absensi_Mgr.CETAK_REKAP("251112460")
        print("\n>>> [FITUR 8 & 10] TRANSKRIP RAPOR & NILAI AKHIR :")
        self.Nilai_Mgr.CETAK_RAPOR("251112460")
        print("\n>>> [FITUR 9] UJI VALIDASI CUSTOM EXCEPTION :")
        try:
            print("Mencoba menginput nilai UTS = 125 (di luar batas 0-100)...")
            self.Nilai_Mgr.INPUT_NILAI(
                "251112460", "Dian Felix Panjaitan", "Matematika", 80, 125, 90
            )
        except InvalidGradeException as err:
            print(f"[BERHASIL DITANGKAP OLEH EXCEPTION] {err}")
        print("#" * 66 + "\n")


Sistem = MANAJEMEN_SEKOLAH()
while True:
    print("\n" + "=" * 58)
    print(f"{'SISTEM MANAJEMEN SEKOLAH':^58}")
    print("=" * 58)
    print(" 1. Pendaftaran Siswa Baru")
    print(" 2. Pendaftaran Guru Baru")
    print(" 3. Atur Kelas & Wali Kelas")
    print(" 4. Pembagian Kelas Siswa")
    print(" 5. Kelola Jadwal Pelajaran")
    print(" 6. Input Presensi Harian")
    print(" 7. Rekap Kehadiran Siswa")
    print(" 8. Penginputan Nilai Siswa")
    print(" 9. Lihat Transkrip / Rapor Siswa")
    print("10. Direktori Guru & Siswa")
    print("11. Jalankan Simulasi Demo")
    print(" 0. Keluar")
    print("=" * 58)
    Pilihan = input("Pilih menu (0-11): ").strip()

    if Pilihan == "1":
        print("\n" + "-" * 5 + " [Menu 1] Pendaftaran Siswa Baru " + "-" * 5)
        try:
            NIS = input(f"{'NIS (Angka)':<20}: ").strip()
            if NIS in Sistem.Daftar_Siswa:
                raise ValueError(f"Siswa dengan NIS {NIS} sudah terdaftar di sistem!")
            Nama = input(f"{'Nama Lengkap':<20}: ").strip()
            Kelas = input(f"{'Kelas (mis: X-IPA-1)':<20}: ").strip().upper()
            Wali = input(f"{'Nama Orang Tua/Wali':<20}: ").strip()
            Siswa_Baru = SISWA(NIS, Nama, Kelas, Wali)
            Sistem.Daftar_Siswa[NIS] = Siswa_Baru
            if Kelas in Sistem.Daftar_Kelas:
                Sistem.Daftar_Kelas[Kelas].TAMBAH_SISWA(Siswa_Baru)
            print("\n[SUKSES] Data siswa baru berhasil didaftarkan!")
        except ValueError as err:
            print(f"\n[VALIDASI GAGAL] {err}")

    elif Pilihan == "2":
        print("\n" + "-" * 5 + " [Menu 2] Pendaftaran Guru Baru " + "-" * 5)
        try:
            NIP = input(f"{'NIP (Angka)':<20}: ").strip()
            if NIP in Sistem.Daftar_Guru:
                raise ValueError(f"Guru dengan NIP {NIP} sudah terdaftar di sistem!")
            Nama = input(f"{'Nama Lengkap':<20}: ").strip()
            MP = input(f"{'Mata Pelajaran':<20}: ").strip()
            Kls_Wali = input(f"{'Wali Kelas (Opsional)':<20}: ").strip()
            Guru_Baru = GURU(NIP, Nama, MP, Kls_Wali)
            Sistem.Daftar_Guru[NIP] = Guru_Baru
            print("\n[SUKSES] Data guru baru berhasil didaftarkan!")
        except ValueError as err:
            print(f"\n[VALIDASI GAGAL] {err}")

    elif Pilihan == "3":
        print("\n" + "-" * 5 + " [Menu 3] Atur Kelas & Wali Kelas " + "-" * 5)
        try:
            Nama_Kls = input(f"{'Nama Ruang/Kelas':<20}: ").strip().upper()
            NIP_Wali = input(f"{'NIP Wali Kelas':<20}: ").strip()
            if NIP_Wali not in Sistem.Daftar_Guru:
                raise ValueError(f"Guru dengan NIP {NIP_Wali} tidak ditemukan!")
            if Nama_Kls not in Sistem.Daftar_Kelas:
                Sistem.Daftar_Kelas[Nama_Kls] = KELAS(Nama_Kls)
            Sistem.Daftar_Kelas[Nama_Kls].ASSIGN(Sistem.Daftar_Guru[NIP_Wali])
            print(
                f"\n[SUKSES] Kelas {Nama_Kls} berhasil ditetapkan dengan Wali Kelas: {Sistem.Daftar_Guru[NIP_Wali].Nama}!"
            )
        except ValueError as err:
            print(f"\n[VALIDASI GAGAL] {err}")

    elif Pilihan == "4":
        print("\n" + "-" * 5 + " [Menu 4] Pembagian Kelas Siswa " + "-" * 5)
        try:
            Nama_Kls = input(f"{'Kelas Tujuan':<20}: ").strip().upper()
            NIS_Siswa = input(f"{'NIS Siswa':<20}: ").strip()
            if Nama_Kls not in Sistem.Daftar_Kelas:
                raise ValueError(f"Kelas {Nama_Kls} belum dibuat/terdaftar!")
            if NIS_Siswa not in Sistem.Daftar_Siswa:
                raise ValueError(f"Siswa dengan NIS {NIS_Siswa} belum terdaftar!")
            Sistem.Daftar_Kelas[Nama_Kls].TAMBAH_SISWA(Sistem.Daftar_Siswa[NIS_Siswa])
            print(f"\n[SUKSES] Siswa berhasil ditempatkan ke kelas {Nama_Kls}!")
            Sistem.Daftar_Kelas[Nama_Kls].INFO_KELAS()
        except ValueError as err:
            print(f"\n[VALIDASI GAGAL] {err}")

    elif Pilihan == "5":
        print("\n" + "-" * 5 + " [Menu 5] Kelola Jadwal Pelajaran " + "-" * 5)
        Nama_Kls = input(f"{'Nama Kelas':<20}: ").strip().upper()
        if Nama_Kls not in Sistem.Daftar_Kelas:
            print(f"\n[PERINGATAN] Data kelas {Nama_Kls} tidak ditemukan!")
        else:
            Sub = input("Pilih aksi [1: Tambah Jadwal | 2: Tampilkan Jadwal]: ").strip()
            if Sub == "1":
                try:
                    Hari = input(f"{'Hari':<20}: ")
                    Jam = input(f"{'Jam (08:00 - 09:40)':<20}: ")
                    MP = input(f"{'Mata Pelajaran':<20}: ")
                    Guru_Pengampu = input(f"{'Guru Pengampu':<20}: ")
                    Sistem.Daftar_Kelas[Nama_Kls].TAMBAH_JADWAL(Hari, Jam, MP, Guru_Pengampu)
                    print("\n[SUKSES] Jadwal pelajaran berhasil ditambahkan!")
                except ValueError as err:
                    print(f"\n[VALIDASI GAGAL] {err}")
            Sistem.Daftar_Kelas[Nama_Kls].TAMPIL_JADWAL()

    elif Pilihan == "6":
        print("\n" + "-" * 5 + " [Menu 6] Input Presensi Harian " + "-" * 5)
        try:
            NIS = input(f"{'NIS Siswa':<20}: ").strip()
            if NIS not in Sistem.Daftar_Siswa:
                raise ValueError(f"Siswa dengan NIS {NIS} tidak ditemukan!")
            Tgl = input(f"{'Tanggal (DD-MM-YYYY)':<20}: ").strip()
            Status = input(f"{'Status (HADIR/IZIN/SAKIT/ALPHA)':<20}: ").strip()
            Nama_S = Sistem.Daftar_Siswa[NIS].Nama
            Sistem.Absensi_Mgr.CATAT(NIS, Nama_S, Tgl, Status)
            print(
                f"\n[SUKSES] Presensi atas nama {Nama_S} berhasil dicatat! (Total Entri: {Sistem.Absensi_Mgr.Total_Log})"
            )
        except ValueError as err:
            print(f"\n[VALIDASI GAGAL] {err}")

    elif Pilihan == "7":
        print("\n" + "-" * 5 + " [Menu 7] Rekap Kehadiran Siswa " + "-" * 5)
        NIS = input(f"{'Masukkan NIS Siswa':<20}: ").strip()
        Sistem.Absensi_Mgr.CETAK_REKAP(NIS)

    elif Pilihan == "8":
        print("\n" + "-" * 5 + " [Menu 8] Penginputan Nilai Siswa " + "-" * 5)
        try:
            NIS = input(f"{'NIS Siswa':<20}: ").strip()
            if NIS not in Sistem.Daftar_Siswa:
                raise ValueError(f"Siswa dengan NIS {NIS} tidak ditemukan!")
            MP = input(f"{'Mata Pelajaran':<20}: ").strip()
            Ulangan = float(input(f"{'Nilai Ulangan (40%)':<20}: "))
            UTS = float(input(f"{'Nilai UTS (30%)':<20}: "))
            UAS = float(input(f"{'Nilai UAS (30%)':<20}: "))

            Nama_S = Sistem.Daftar_Siswa[NIS].Nama
            Sistem.Nilai_Mgr.INPUT_NILAI(NIS, Nama_S, MP, Ulangan, UTS, UAS)
            print(f"\n[SUKSES] Penilaian untuk {Nama_S} berhasil disimpan!")
            Sistem.Nilai_Mgr.CETAK_RAPOR(NIS)
        except InvalidGradeException as err:
            print(f"\n[BATAS NILAI TIDAK VALID - InvalidGradeException] {err}")
        except ValueError as err:
            print(f"\n[FORMAT INPUT TIDAK VALID] Pastikan nilai berupa angka! Detail: {err}")

    elif Pilihan == "9":
        print("\n" + "-" * 5 + " [Menu 9] Transkrip & Rapor Siswa " + "-" * 5)
        NIS = input(f"{'Masukkan NIS Siswa':<20}: ").strip()
        Sistem.Nilai_Mgr.CETAK_RAPOR(NIS)

    elif Pilihan == "10":
        print("\n" + "=" * 56)
        print(f"{'DIREKTORI DATA INDUK GURU & SISWA':^56}")
        print("=" * 56)
        Data_Induk = list(Sistem.Daftar_Guru.values()) + list(Sistem.Daftar_Siswa.values())
        for item in Data_Induk:
            item.PROFIL()
            print("-" * 56)

    elif Pilihan == "11":
        Sistem.DEMO_UTS()

    elif Pilihan == "0":
        print("\nSesi Sistem Manajemen Sekolah telah selesai. Terima kasih!")
        break

    else:
        print("\nPilihan tidak dikenali! Silakan masukkan nomor menu (0-11).")
