# Sistem Manajemen Sekolah (School Management System CLI)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![OOP Paradigm](https://img.shields.io/badge/Paradigm-Object--Oriented%20Programming-brightgreen.svg)]()
[![Course](https://img.shields.io/badge/Mata%20Kuliah-PPBO%20(IF--A%20Pagi)-orange.svg)]()
[![Milestone](https://img.shields.io/badge/Milestone-UTS%20(100%25%20Completed)-success.svg)]()
[![Institution](https://img.shields.io/badge/Universitas-Mikroskil-red.svg)](https://mikroskil.ac.id/)

> **Tugas Besar Mata Kuliah Perancangan dan Pemrograman Berorientasi Objek (PPBO)**  
> **Topik:** `[E2] Sistem Manajemen Sekolah` — Tahap Evaluasi Tengah Semester (UTS)  
> **Dosen Pengampu:** Mirza Ilhami, S.Kom., M.TI.  
> **Kelompok 2 — Kelas IF-A Pagi (Semester 3)**

---

## 📖 Latar Belakang & Deskripsi Proyek

Aplikasi **Sistem Manajemen Sekolah** adalah platform administrasi akademik berbasis antarmuka baris perintah (*Command Line Interface / CLI*) yang dibangun dengan bahasa pemrograman **Python** murni. Proyek ini dirancang secara komprehensif untuk mengotomatisasi tata kelola data sekolah terpadu mulai dari registrasi data induk warga sekolah, penempatan kelas, penjadwalan mata pelajaran, sistem absensi presensi, hingga evaluasi rapor berbasis bobot nilai akademik.

Seluruh arsitektur kode mengimplementasikan prinsip-prinsip fundamental **Object-Oriented Programming (OOP)** secara ketat dan elegan sesuai standar kurikulum PPBO 2026.

---

## 📂 Struktur Repositori

Arsitektur kode dirancang modular dan terstruktur dalam satu file executable utama sehingga hierarki kelas dan dependensi objek dapat ditelaah secara kronologis dari atas ke bawah:

```text
sistem-manajemen-sekolah/
├── .gitignore          # Konfigurasi file pengabaian Git (Python, cache, venv)
├── README.md           # Dokumentasi komprehensif, roadmap, dan daftar kontributor
└── main.py             # Implementasi lengkap arsitektur OOP & antarmuka CLI interaktif
```

---

## 🎯 Fondasi Konsep OOP yang Diterapkan di Tahap UTS

Sistem ini merealisasikan 5 pilar utama dan pola pemrograman OOP tingkat lanjut:

### 1. Abstract Base Class (ABC) & Inheritance (Pewarisan)
* **Kelas Abstrak `SEKOLAH(abc.ABC)`**: Berfungsi sebagai cetak biru (*blueprint*) dasar bagi seluruh entitas civitas akademika sekolah.
* **Kelas Turunan `SISWA` dan `GURU`**: Mewarisi atribut dan perilaku umum dari `SEKOLAH` serta memanggil konstruktor induk melalui `super().__init__(Nomor_Induk, Nama, Peran)`.

### 2. Polymorphism (Polimorfisme) & Method Overriding
* Method abstrak `@abc.abstractmethod def PROFIL(self)` di dalam kelas `SEKOLAH` di-override dengan perilaku spesifik:
  * Pada kelas `SISWA`: Menampilkan data identitas NIS, Nama Lengkap, Ruang Kelas, dan Orang Tua / Wali.
  * Pada kelas `GURU`: Menampilkan NIP, Nama Lengkap, Mata Pelajaran yang diampu, serta status penugasan Wali Kelas.
* Memungkinkan pemrosesan koleksi heterogen (*polymorphic collection*) di Menu Direktori Data Induk dalam satu iterasi loop.

### 3. Encapsulation (Enkapsulasi) & Data Validation
* Proteksi integritas data menggunakan atribut internal `_Nomor_Induk` dan `_Nama`.
* Penggunaan decorator `@property` dan setter method `@Nama.setter` untuk menjamin keamanan mutasi state objek.
* Metode validasi statik (`@staticmethod`) untuk memastikan keabsahan format:
  * Nomor Induk (NIS/NIP) wajib berupa string numerik 5–12 digit.
  * Nama wajib berupa rangkaian alfabet dan spasi (anti karakter angka/simbol).

### 4. Custom Exception Handling
* Kelas eksepsi kustom turunan kelas bawaan Python:
  ```python
  class InvalidGradeException(Exception):
      """Dilempar saat nilai evaluasi siswa berada di luar rentang sah (0 - 100)."""
      pass
  ```
* Menjamin keandalan sistem saat terjadi anomali masukan nilai pada penginputan nilai harian, UTS, maupun UAS.

### 5. Advanced Python Patterns (Coroutine & Iterator)
* **Coroutine Generator**: Digunakan pada modul `ABSENSI` dengan mekanisme `yield` dan `.send(1)` untuk mencatat log presensi harian secara berkesinambungan dan mengupdate counter log secara real-time.
* **Iterator Pattern**: Menggunakan protokol `iter()` dan `next()` untuk melakukan traversal riwayat absensi siswa secara teratur saat mencetak rekapitulasi kehadiran.

---

## 📋 Checklist & Roadmap Fitur UTS (Fitur 1–10)

Berikut matriks verifikasi 10 fitur wajib tahap evaluasi tengah semester (UTS):

| No | Fitur UTS | Konsep OOP Terkait | Status Implementasi |
| :-: | :--- | :--- | :---: |
| 1 | **Registrasi Siswa Baru & Validasi NIS**<br>Validasi numerik (5–12 digit) & nama alfabet. | Encapsulation, Constructor (`__init__`), Property Setter, Staticmethod | ✅ Selesai (*Implemented*) |
| 2 | **Registrasi Guru Baru & Validasi NIP**<br>Pencatatan NIP, mata pelajaran, dan validasi data induk. | Inheritance (`SEKOLAH` → `GURU`), ABC | ✅ Selesai (*Implemented*) |
| 3 | **Atur Ruang Kelas & Wali Kelas**<br>Pengalokasian guru pendamping kelas melalui method `ASSIGN`. | Association / Aggregation, Object Reference | ✅ Selesai (*Implemented*) |
| 4 | **Pembagian Kelas & Enrolment Siswa**<br>Penempatan siswa ke kelas dengan validasi anti-duplikasi NIS dan auto-sort. | Encapsulation, List Management, Association | ✅ Selesai (*Implemented*) |
| 5 | **Pengelolaan Jadwal Pelajaran**<br>Penambahan jadwal pelajaran mingguan per ruang kelas (`TAMBAH_JADWAL`). | Composition, Nested Dictionary/List Collection | ✅ Selesai (*Implemented*) |
| 6 | **Input Presensi Harian Siswa**<br>Pencatatan status presensi (`HADIR`, `IZIN`, `SAKIT`, `ALPHA`). | Coroutine Generator (`yield`, `.send()`), State Tracking | ✅ Selesai (*Implemented*) |
| 7 | **Rekapitulasi Kehadiran & Persentase**<br>Perhitungan persentase kehadiran dan riwayat log siswa. | Iterator Pattern (`iter()`, `next()`), Algoritma Statistik | ✅ Selesai (*Implemented*) |
| 8 | **Penginputan Komponen Nilai Siswa**<br>Input nilai terpisah: Ulangan Harian (40%), UTS (30%), UAS (30%). | Encapsulation, Method Overloading Simulation | ✅ Selesai (*Implemented*) |
| 9 | **Validasi Rentang Nilai (0–100) & Exception**<br>Raise error `InvalidGradeException` saat nilai tidak valid. | Custom Exception Handling (`try...except InvalidGradeException`) | ✅ Selesai (*Implemented*) |
| 10 | **Transkrip Nilai Rapor & Nilai Akhir**<br>Kalkulasi nilai akhir terbobot dan pencetakan transkrip akademik. | Business Logic Calculation, String Formatting, Polymorphic Display | ✅ Selesai (*Implemented*) |

---

## 🚀 Panduan Menjalankan Program

### Prasyarat Sistem
* Python versi 3.10 atau versi yang lebih baru terinstal pada sistem operasi Anda.
* Git CLI.

### Langkah Eksekusi

1. **Clone Repositori:**
   ```bash
   git clone https://github.com/Samuelsibuea/sistem-manajemen-sekolah.git
   cd sistem-manajemen-sekolah
   ```

2. **Jalankan Aplikasi:**
   ```bash
   python main.py
   ```

3. **Menu Interaktif CLI:**
   Aplikasi menyediakan 12 menu navigasi terminal:
   ```text
   ==========================================================
                    SISTEM MANAJEMEN SEKOLAH
   ==========================================================
    1. Pendaftaran Siswa Baru
    2. Pendaftaran Guru Baru
    3. Atur Kelas & Wali Kelas
    4. Pembagian Kelas Siswa
    5. Kelola Jadwal Pelajaran
    6. Input Presensi Harian
    7. Rekap Kehadiran Siswa
    8. Penginputan Nilai Siswa
    9. Lihat Transkrip / Rapor Siswa
   10. Direktori Guru & Siswa
   11. Jalankan Simulasi Demo (Otomatis Fitur 1-10)
    0. Keluar
   ==========================================================
   ```
   > 💡 **Tips Pengujian Dosen / Reviewer:**  
   > Pilih menu **`11. Jalankan Simulasi Demo`** untuk melihat demonstrasi otomatis seluruh alur Fitur 1 hingga Fitur 10 secara komprehensif, termasuk simulasi penangkapan `InvalidGradeException`.

---

## 👥 Tim Pengembang (Kelompok 2 — IF-A Pagi)

Proyek ini dikembangkan dan diselesaikan secara kolaboratif oleh Kelompok 2:

| Foto Profil | Nama Anggota | NIM | Akun GitHub | Peran & Kontribusi Utama |
| :---: | :--- | :---: | :---: | :--- |
| <img src="https://github.com/Samuelsibuea.png?size=100" width="80" style="border-radius:50%;" alt="Samuel Sibuea"/> | **Samuel Early Thimothy Sibuea** | `251111743` | [@Samuelsibuea](https://github.com/Samuelsibuea) | **Project Lead**, Arsitektur Inti Sistem (`MANAJEMEN_SEKOLAH`), CLI Interactive Engine, & Git Setup |
| <img src="https://github.com/DianFelix.png?size=100" width="80" style="border-radius:50%;" alt="Dian Felix Panjaitan"/> | **Dian Felix Panjaitan** | `251112460` | [@DianFelix](https://github.com/DianFelix) | Desain Hirarki Kelas Abstrak (`SEKOLAH`, `SISWA`, `GURU`), Enkapsulasi, & Validasi Identitas |
| <img src="https://github.com/Hakau-venerable.png?size=100" width="80" style="border-radius:50%;" alt="Jose Aldrian Brahmana"/> | **Jose Aldrian Brahmana** | `251110996` | [@Hakau-venerable](https://github.com/Hakau-venerable) | Modul Presensi Harian (`ABSENSI`), Coroutine Generator Logger, & Iterator Pattern Rekapitulasi |
| <img src="https://github.com/Rhinos14.png?size=100" width="80" style="border-radius:50%;" alt="Samuel Ides Edwart Hutapea"/> | **Samuel Ides Edwart Hutapea** | `251111194` | [@Rhinos14](https://github.com/Rhinos14) | Modul Evaluasi Akademik (`NILAI`), Custom Exception (`InvalidGradeException`), & Rapor Generator |

---

## 🎓 Informasi Akademik

* **Program Studi:** S1 Teknik Informatika
* **Fakultas:** Fakultas Ilmu Komputer
* **Perguruan Tinggi:** Universitas Mikroskil, Medan
* **Tahun Ajaran:** 2026/2027 (Semester Ganjil)
* **Lisensi:** Proyek Terbuka Akademik untuk Keperluan Pendidikan & Penilaian UTS PPBO.