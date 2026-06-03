# Data latihan

data_latihan = [
    (0, 0),
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8)
]

pengetahuan_ai = 0.1
kecepatan_belajar = 0.1

for putaran_belajar in range(1000):

    total_kesalahan_putaran_ini = 0

    print("\n" + "="*60)
    print(f"PUTARAN {putaran_belajar}")
    print("="*60)
    print(f"pengetahuan_ai awal putaran = {pengetahuan_ai}")

    for angka_yang_dilihat_ai, jawaban_benar in data_latihan:

        print("\n------------------------------")
        print(f"INPUT DIBACA: {angka_yang_dilihat_ai} -> {jawaban_benar}")

        print(f"pengetahuan_ai saat ini = {pengetahuan_ai}")

        tebakan_ai = (
            pengetahuan_ai
            * angka_yang_dilihat_ai
        )

        print(f"tebakan_ai = {pengetahuan_ai} * {angka_yang_dilihat_ai} = {tebakan_ai}")

        selisih_dengan_jawaban_benar = (
            jawaban_benar
            - tebakan_ai
        )

        print(f"selisih = {jawaban_benar} - {tebakan_ai} = {selisih_dengan_jawaban_benar}")

        perubahan = (
            kecepatan_belajar
            *
            selisih_dengan_jawaban_benar
            *
            angka_yang_dilihat_ai
        )

        print(
            f"perubahan = {kecepatan_belajar} * "
            f"{selisih_dengan_jawaban_benar} * "
            f"{angka_yang_dilihat_ai} = {perubahan}"
        )

        pengetahuan_ai_baru = (
            pengetahuan_ai
            +
            perubahan
        )

        print(f"pengetahuan_ai update: {pengetahuan_ai} + {perubahan} = {pengetahuan_ai_baru}")

        pengetahuan_ai = pengetahuan_ai_baru

        total_kesalahan_putaran_ini += abs(
            selisih_dengan_jawaban_benar
        )

        print(f"total_kesalahan_sementara = {total_kesalahan_putaran_ini}")

    print("\n==============================")
    print(f"AKHIR PUTARAN {putaran_belajar}")
    print(f"TOTAL KESALAHAN = {total_kesalahan_putaran_ini}")
    print(f"PENGETAHUAN AKHIR PUTARAN = {pengetahuan_ai}")
    print("="*60)

print("\nPengetahuan akhir AI:", pengetahuan_ai)

print(
    "Prediksi untuk angka 10 =",
    pengetahuan_ai * 10
)
