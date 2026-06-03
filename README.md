Ini versi **penjelasan paling sederhana, fokus ke “apa yang sebenarnya terjadi” tanpa tambahan teori yang ribet** 👇

---

# 🤖 Cara Kerja Program AI Ini (Sederhana Banget)

Program ini sebenarnya cuma melakukan 1 hal utama:

> **Mencari angka yang tepat supaya hasil perkalian cocok dengan data**

---

# 📊 Yang Diberikan ke AI

Kita kasih contoh:

```
0 → 0
1 → 2
2 → 4
3 → 6
4 → 8
```

Artinya AI disuruh menebak pola dari contoh itu.

---

# 🧠 Apa yang AI Punya?

AI cuma punya 1 angka:

```
pengetahuan_ai
```

Awalnya:

```
0.1
```

Artinya AI masih asal tebak:

```
angka × 0.1
```

---

# 🔄 Proses Belajar (Intinya)

AI melakukan ini berulang-ulang:

### 1. Lihat angka

Contoh:

```
3
```

---

### 2. Tebak jawaban

```
3 × pengetahuan_ai
```

---

### 3. Bandingkan dengan jawaban benar

Misalnya benar = 6

---

### 4. Hitung salahnya

```
selisih = jawaban_benar - tebakan
```

---

### 5. Perbaiki “pengetahuan”

AI sedikit mengubah angka `pengetahuan_ai` supaya lebih dekat ke jawaban benar.

---

# 🔁 Diulang Terus

Proses ini diulang ratusan sampai ribuan kali:

```
tebak → salah → perbaiki → tebak → salah → perbaiki
```

---

# 🎯 Hasil Akhir

Setelah cukup lama:

```
pengetahuan_ai → 2
```

Artinya AI menemukan pola:

```
hasil = angka × 2
```

---

# 🧠 Inti Sebenarnya

Program ini bukan “pintar” atau “cerdas”.

Tapi hanya:

> **mencari angka yang paling cocok dengan data**

---

# 💡 Analogi Paling Gampang

Bayangkan kamu lagi main tebak pola:

```
1 → 2
2 → 4
3 → 6
4 → ?
lalu jika 4 berapa => ? dst
```

Kamu coba:

* ×1 ❌
* ×1.5 ❌
* ×2 ✅

AI melakukan hal yang sama, tapi dengan matematika otomatis.

---

# ⚡ Kesimpulan Singkat

Program ini cuma:

* lihat contoh
* coba angka
* salah → perbaiki
* ulang terus
* akhirnya ketemu pola

---

Kalau disederhanakan lagi:

> 🧠 AI ini cuma “mesin pencari angka yang paling cocok”
