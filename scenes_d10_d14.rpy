# ==========================================
# BABAK II (lanjutan)
# ==========================================

label scene_d10:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban, Jongbiru)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D10 - Pertempuran di Jongbiru. (Placeholder: BG-17, BGM-07)"
    # TODO: Ganti musik placeholder dengan aset BGM-07

    menu:
        "Serangan frontal. Ikut aku. (Konfrontasi)":
            $ konfrontasi += 1
            $ d10_choice = "A"
            $ keberanian += 20
            $ kehormatan += 10
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menerobos langsung. Barisan musuh retak, tapi namamu jadi terlalu menyala."

        "Kepung sayap kanan, putus jalur mundur. (Mediasi)":
            $ mediasi += 1
            $ d10_choice = "B"
            $ kebijakan += 20
            $ keberanian += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih medan dan tempo. Menang tanpa banyak gaya."

        "Serangan simultan dengan komandan Tartar. (Siasat)":
            $ siasat += 1
            $ d10_choice = "C"
            $ kebijakan += 15
            $ loyalitas += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengunci koordinasi dua arah. Relasi Tartar menguat."

    return

label scene_d11:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-08 / BG-09 (Kediri)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D11 - Kediri jatuh. (Bottleneck sejarah)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Jayakatwang menyerah. Majapahit lahir dari abu kemenangan ini."

    lembu "Kita menang, keponakanku."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        ranggalawe "Ya. Kita menang." 
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Nada suaramu bangga—dengan duri frustrasi kecil."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        ranggalawe "Ya. Kita menang."
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Ada pertanyaan yang tak sempat kamu ucapkan."
    else:
        ranggalawe "Ya. Kita menang."
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu sudah memikirkan langkah berikutnya bahkan sebelum sorak berhenti."

    return

label scene_d12:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D12 - Siasat mengusir Tartar. (Placeholder: BG-15, BGM-06)"
    # TODO: Ganti musik placeholder dengan aset BGM-06

    menu:
        "Adakan pesta, lengahkan mereka, lalu sergap. (Siasat)":
            $ siasat += 1
            $ d12_choice = "A"
            $ kehormatan -= 10
            $ kebijakan += 20
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Efektif—tapi meninggalkan rasa pahit."

        "Biarkan Lembu Sora memimpin tipu daya; aku siaga di luar. (Mediasi)":
            $ mediasi += 1
            $ d12_choice = "B"
            $ kehormatan += 10
            $ loyalitas_sora += 15
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kepercayaanmu pada paman jadi cerita yang tak semua orang pahami."

        "Tantang komandan Tartar duel terbuka. (Konfrontasi)":
            $ konfrontasi += 1
            $ d12_choice = "C"
            $ keberanian += 25
            $ kehormatan += 20
            $ kebijakan -= 15
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Nama kamu melegenda—dan itu membuat istana gelisah."

    return

label scene_d13:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-14 (Trowulan - Istana Majapahit)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D13 - Tartar terusir. Majapahit merdeka. (Bottleneck sejarah)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kertarajasa dinobatkan. Di sisi raja: Nambi. Kamu menyaksikan dari barisan belakang."
    ranggalawe "Aku membantu mendirikan ini... tapi ruang di sisi raja terasa bukan untukku."
    return

label scene_d14:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D14 - Konsekuensi cara mengusir Tartar. (Informatif)"

    if d12_choice == "A":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Pesan istana: kreativitas strategimu dihargai... tapi caramu dianggap terlalu tak terduga."
    elif d12_choice == "B":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Pesan istana: kerendahan hatimu dihargai... tapi keputusan besar butuh sosok yang berdiri di garis depan."
    elif d12_choice == "C":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Tidak ada kritik langsung. Tapi kamu melihat Nambi berdiri jauh di belakang raja—menatap tanpa bisa kamu baca."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Istana memberi pesan singkat yang terasa dingin."

    return
