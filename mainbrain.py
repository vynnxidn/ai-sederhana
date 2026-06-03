from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# =====================================================
# DATA LATIHAN
# =====================================================

data_latihan = [
    (0, 0),
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8)
]

pengetahuan_ai = 0.1
kecepatan_belajar = 0.1

# =====================================================
# HEADER AI
# =====================================================

console.print(
    Panel.fit(
        "[bold magenta]AI INITIALIZED[/bold magenta]\n"
        "[purple]Sistem belajar pola angka dimulai...[/purple]",
        title="[bold white]TRAINING CORE[/bold white]",
        border_style="magenta"
    )
)

# =====================================================
# TRAINING LOOP
# =====================================================

for putaran_belajar in range(1000):

    total_kesalahan_putaran_ini = 0

    console.print(
        Panel.fit(
            f"[bold magenta]PUTARAN {putaran_belajar}[/bold magenta]\n"
            f"[purple]pengetahuan_ai awal = {pengetahuan_ai}[/purple]",
            title="[bold]TRAINING SESSION[/bold]",
            border_style="magenta"
        )
    )

    for angka_yang_dilihat_ai, jawaban_benar in data_latihan:

        tebakan_ai = pengetahuan_ai * angka_yang_dilihat_ai

        selisih_dengan_jawaban_benar = jawaban_benar - tebakan_ai

        perubahan = (
            kecepatan_belajar
            * selisih_dengan_jawaban_benar
            * angka_yang_dilihat_ai
        )

        pengetahuan_ai_baru = pengetahuan_ai + perubahan

        total_kesalahan_putaran_ini += abs(selisih_dengan_jawaban_benar)

        # =================================================
        # PANEL STEP (UNGU)
        # =================================================

        console.print(
            Panel(
                f"[bold magenta]INPUT[/bold magenta] : {angka_yang_dilihat_ai} → {jawaban_benar}\n"
                f"[purple]TEBAKAN[/purple] : {tebakan_ai}\n"
                f"[purple]ERROR[/purple] : {selisih_dengan_jawaban_benar}\n"
                f"[purple]UPDATE[/purple] : {pengetahuan_ai} → {pengetahuan_ai_baru}\n"
                f"[purple]TOTAL ERROR[/purple] : {total_kesalahan_putaran_ini}",
                border_style="magenta"
            )
        )

        pengetahuan_ai = pengetahuan_ai_baru

    # =====================================================
    # END PUTARAN
    # =====================================================

    console.print(
        Panel.fit(
            f"[bold magenta]AKHIR PUTARAN {putaran_belajar}[/bold magenta]\n"
            f"[purple]TOTAL ERROR = {total_kesalahan_putaran_ini}[/purple]\n"
            f"[purple]PENGETAHUAN AI = {pengetahuan_ai}[/purple]",
            border_style="magenta"
        )
    )

# =====================================================
# HASIL AKHIR
# =====================================================

console.print(
    Panel.fit(
        f"[bold magenta]FINAL RESULT[/bold magenta]\n\n"
        f"[purple]Pengetahuan AI = {pengetahuan_ai}[/purple]\n"
        f"[purple]Prediksi angka 10 = {pengetahuan_ai * 10}[/purple]",
        title="[bold magenta]AI TRAINING COMPLETE[/bold magenta]",
        border_style="magenta"
    )
)
