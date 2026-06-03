# Genetic Algorithm: Word Matching Optimization 🧬

Repositori ini berisi implementasi **Algoritma Genetika (Genetic Algorithm)** untuk memecahkan kasus *Word Matching Problem*. Sistem dirancang untuk mencari dan merekonstruksi kata target tertentu (dalam studi kasus ini: `"GENETIKA"`) melalui proses evolusi komputasional yang meniru teori seleksi alam Darwin.

Proyek ini dikembangkan sebagai bagian dari eksplorasi optimasi heuristik dalam lingkup Sains Data Terapan di Politeknik Elektronika Negeri Surabaya (PENS).

## 🚀 Fitur dan Implementasi
Repositori ini menyediakan dua versi pendekatan penulisan kode:

1. **`genetic_algorithm_pure.py` (Zero-Dependency)**
   * Dibangun 100% menggunakan Python murni tanpa *library* eksternal.
   * Sangat cocok untuk tujuan edukasi karena memperlihatkan aliran logika Algoritma Genetika secara mendetail, mulai dari *looping* evaluasi *fitness*, seleksi mesin roullete, hingga manipulasi *array* pada saat *crossover* dan mutasi.

2. **`genetic_algorithm_numpy.py` (High-Performance Vectorization)**
   * Dioptimalkan menggunakan library `NumPy`.
   * Berfokus pada vektorisasi operasi matriks (skala besar). Menghilangkan perulangan (`for loop`) konvensional pada evaluasi populasi sehingga komputasi berjalan ratusan kali lebih cepat.

## ⚙️ Cara Kerja Sistem (Alur Evolusi)
Algoritma ini mengandalkan konsep dasar Simple Genetic Algorithm (SGA) dengan penerapan *Elitism*. 
1. **Inisialisasi & Representasi:** Target kata direpresentasikan ke dalam numerik (urutan alfabet A-Z = 1-26).
2. **Populasi Awal:** Komputer menebak 10 kata acak sebagai generasi pertama.
3. **Evaluasi Fitness:** Setiap kata dievaluasi seberapa dekat jarak antar hurufnya terhadap kata target.
4. **Seleksi (Mesin Roullete):** Individu dengan skor *fitness* terbaik memiliki probabilitas lebih tinggi untuk terpilih sebagai induk.
5. **Reproduksi (Crossover & Mutasi):** * **Crossover (80%):** Induk saling menukar sebagian kombinasi hurufnya.
   * **Mutasi (10%):** Beberapa huruf bergeser secara acak untuk mempertahankan diversitas populasi.
6. **Elitism:** Sistem mempertahankan tebakan terbaik dari generasi sebelumnya agar tidak rusak karena mutasi yang buruk.
7. Proses terus berulang hingga kata target terbentuk secara sempurna.

## 🛠️ Prasyarat & Cara Menjalankan
Pastikan Anda telah menginstal Python (minimal versi 3.x) di perangkat Anda. Khusus untuk versi NumPy, pastikan *library* sudah terpasang:

```bash
pip install numpy
