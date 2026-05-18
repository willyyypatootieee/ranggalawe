# ==========================================
# BABAK IV - FALLING ACTION
# ==========================================

label scene_d23:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 / BG-18 (Pantai Tuban - Pertahanan)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D23 - Pertempuran pecah: gelombang pertama."

    if nambi_delays_troops:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Efek: Nambi menunda satu kompi 2 jam—celah terbuka."
    if mahapati_misinformed:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Efek: koordinasi musuh kacau karena laporan palsu."
    if d17_c_choice == "C1":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Efek: pasukan musuh lebih kecil dari perkiraan."

    menu:
        "Serangan balik langsung. (Konfrontasi)":
            $ d23_choice = "A"
            $ konfrontasi += 1
            $ keberanian += 20
            $ kebijakan += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Momentum awal berpihak padamu—risiko tetap tinggi."

        "Tahan di ketinggian, pilih medan. (Mediasi)":
            $ d23_choice = "B"
            $ mediasi += 1
            $ kebijakan += 20
            $ keberanian += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu membuat mereka masuk lebih dalam dari yang aman."

        "Kirim utusan negosiasi terakhir. (Mediasi)":
            $ d23_choice = "C"
            $ mediasi += 1
            $ kehormatan += 15
            $ kebijakan += 5
            $ keberanian -= 5
            if d04_choice == "C":
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kebo Anabrang memberi jeda satu jam—penghormatan sesama pendekar."

    return

label scene_d24:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 & BG-16 (Split Screen)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D24 - Di dua front sekaligus. (Parallel)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[Medan perang] Gelombang demi gelombang datang seperti laut."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[Trowulan] Mahapati menunggu laporan di ruang nyaman: 'Ranggalawe harus tidak ada lagi setelah ini.'"
    return

label scene_d25:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D25 - Bertemu Lembu Sora di tengah pertempuran."

    if keris_given_sora:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora mengeluarkan keris titipanmu."
        lembu "Kamu mau aku kembalikan ini?"
        ranggalawe "Simpan. Sebagai pengingat."
        $ kehormatan += 5

    show lembu lelah
    lembu "Keponakanku. Masih belum terlambat."

    menu:
        "Paman tahu aku benar. Tapi Paman tetap berdiri di sana. (Konfrontasi)":
            $ d25_choice = "A"
            $ konfrontasi += 1
            $ kehormatan += 15
            $ loyalitas_sora -= 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kebenaranmu jujur—dan menyakiti."

        "Jika Paman bisa pastikan ini berakhir tanpa lebih banyak darah... (Mediasi)":
            $ d25_choice = "B"
            $ mediasi += 1
            $ kebijakan += 10
            $ kehormatan += 5
            $ loyalitas += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Ada janji yang bahkan pamanmu tak mampu tepati."

        "Pergilah, Paman. Jangan paksa aku berhadapan denganmu. (Siasat)":
            $ d25_choice = "C"
            $ siasat += 1
            $ kehormatan += 20
            $ keberanian += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu melindungi pamanmu... dengan memecahkan hatimu sendiri."

    return

label scene_d26:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-19 (Sungai Tambak Beras - Senja Merah)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D26 - Di tepi Sungai Tambak Beras."
    show kebo tegas
    kebo "Ranggalawe! Masuk ke air. Selesaikan ini seperti ksatria."

    if d04_choice == "C" and kehormatan >= 7:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[STAT GATE TERBUKA] Perjanjian Diam Kebo Anabrang."
        menu:
            "Terima Perjanjian Diam (Node tersembunyi)":
                $ d26_pact = True
                $ kehormatan += 25
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kebo mengusir prajurit dari tepi sungai. Duel tanpa penonton."
            "Tolak—biarkan semuanya melihat":
                $ d26_pact = False
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kamu memilih duel di mata banyak orang."
    else:
        $ d26_pact = False

    return

label scene_d27:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-19 (Sungai Tambak Beras - Senja Merah)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D27 - Keputusan terakhir seorang ksatria."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu berteriak: 'MAHAPATI! Sejarah akan mengingatmu!'"
    elif mediasi >= konfrontasi and mediasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap Lembu Sora dari kejauhan—mengangguk tanpa kata."
    elif siasat >= konfrontasi and siasat >= mediasi:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu tersenyum tipis—ironi yang hanya kamu pahami."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap langit. Tak ada kata yang cukup."

    menu:
        "Masuk ke air tanpa ragu. (Konfrontasi)":
            $ d27_choice = "A"
            $ konfrontasi += 1
            $ keberanian += 25
            $ kehormatan += 25

        "Mundur strategis... tapi tidak ada jalan. (Mediasi)":
            $ d27_choice = "B"
            $ mediasi += 1
            $ kebijakan += 5
            $ kehormatan += 5

        "Berdiri dan berseru tentang ketidakadilan, lalu melompat. (Konfrontasi)":
            $ d27_choice = "C"
            $ konfrontasi += 1
            $ kehormatan += 30
            $ keberanian += 20

        "Serahkan Surat Gelap Mahapati pada Lembu Sora. (EKSKLUSIF)" if mahapati_letter:
            $ d27_choice = "D"
            $ mahapati_letter_given = True
            $ kehormatan += 30
            $ keberanian += 20
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Warisan kebenaran ikut turun ke sungai—tapi tidak ikut tenggelam."

    return

label scene_d28:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-19 (Sungai Tambak Beras - Senja Merah)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D28 - Ranggalawe gugur di Tambak Beras (1295 M). (Bottleneck final)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Dua ksatria. Satu sungai. Satu nasib."
    return
