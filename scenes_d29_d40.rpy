# ==========================================
# BABAK V - RESOLUSI / EPILOG
# ==========================================

label scene_d29:
    if not dokumen_hukum:
        return

    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D29 - Dokumen Sima: kemenangan setelah kematian. (Opsional)"

    menu:
        "Kirim dokumen Sima ke Kertarajasa.":
            $ d29_choice = "A"
            $ kehormatan += 20
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Tuban diakui sebagai Sima—tiga bulan kemudian."

        "Simpan untuk putra Ranggalawe.":
            $ d29_choice = "B"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Warisan jadi pegangan Kuda Anjampiani."

    return

label scene_d30:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-20 (Makam Ranggalawe)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D30 - Lembu Sora menghadapi diri sendiri."

    if d25_choice == "A":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora hidup dalam rasa bersalah. Kelak ia memberontak juga—korban sistem yang sama."
    elif d25_choice == "B":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora membawa beban tak terampuni sampai akhir."
    elif d25_choice == "C":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora menjaga makam—diam, sendirian, sampai akhir hayat."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora menatap makam tanpa jawaban."

    return

label scene_d31:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-16 (Trowulan Kediaman Mahapati)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D31 - Mahapati dan warisan intrik. (Opsional)"

    if mahapati_letter_given:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Surat gelap itu akhirnya dipakai. Mahapati menghilang dari istana."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Mahapati pun disingkirkan oleh intrik—seperti yang ia lakukan pada orang lain."

    return

label scene_d32:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-14 & BG-20 (Split Screen)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D32 - Sesudah Ranggalawe: dua versi sejarah. (Parallel)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Versi kerajaan: pemberontak. Versi Tuban: pahlawan. Keduanya benar sekaligus."
    return

label scene_d33:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: VN-UI-06 (Relationship Meter) / UI-10
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D33 - Status hubungan akhir (ringkasan)."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Raden Wijaya/Kertarajasa: sahabat menjadi raja yang takut bayangan." 
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Lembu Sora: berubah sesuai D25." 
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Arya Wiraraja: ayah yang mencintai dengan cara paling rumit." 
    if rakyat_loyal:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Rakyat Tuban: loyalitas tinggi—warisan paling tulus." 
    return

label scene_d34:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-10 (Pelabuhan Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D34 - Kuda Anjampiani: sang putra."

    menu:
        "Pergi ke Trowulan, pelajari hukum, ajukan klaim warisan. (Siasat)":
            $ d34_choice = "A"
            $ siasat += 1
            $ kehormatan += 15
            $ kebijakan += 20

        "Membangun Tuban agar pantas dicintai. (Mediasi)":
            $ d34_choice = "B"
            $ mediasi += 1
            $ kehormatan += 10
            $ loyalitas_rakyat += 25

        "Membawa nama Ranggalawe ke mana pun pergi. (Konfrontasi)":
            $ d34_choice = "C"
            $ konfrontasi += 1
            $ keberanian += 15
            $ kehormatan += 10

    return

label scene_d35:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-14 & BG-20 (Split Screen)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D35 - Dua tafsir yang abadi."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Ia pemberontak—atau ia pahlawan. Di antara keduanya, kisahnya hidup."

    # Routing ending by dominant tendency.
    $ ending = "A"
    if mediasi > konfrontasi and mediasi >= siasat:
        $ ending = "B"
    elif siasat > konfrontasi and siasat > mediasi:
        $ ending = "C"

    if ending == "A":
        call scene_d36
    elif ending == "B":
        call scene_d37
    else:
        call scene_d38

    if rakyat_loyal:
        call scene_d39

    call scene_d40

    return

label scene_d36:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-20 (Makam Ranggalawe)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D36 - ENDING A (Konfrontasi) - Tone: Pahit."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kata terakhir menyebut Mahapati. Nama itu berbisik lama di Tuban."
    if mahapati_letter_given:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Bertahun-tahun kemudian, surat gelap itu menyingkirkan Mahapati."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Bagi sebagian, ia pemberontak. Bagi Tuban... ia simbol keberanian melawan ketidakadilan."
    return

label scene_d37:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-20 (Makam Ranggalawe)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D37 - ENDING B (Mediasi) - Tone: Melankolik."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Nambi mendengar kabar kematianmu sendirian. Ada sesuatu yang berubah dalam matanya."
    if d26_pact:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[Variasi] Kebo Anabrang mengakui martabatmu sebelum ia gugur karena luka lain."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Ada keindahan yang menyakitkan dalam memaafkan orang yang tidak meminta maaf."
    return

label scene_d38:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-20 (Makam Ranggalawe)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D38 - ENDING C (Siasat/Mobilisasi) - Tone: Enigmatik."
    if d17_route == "C":
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Ra Galatik menghilang dari Majapahit. Di pasar, tangannya berhenti setiap kali namamu disebut."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Diam, kadang, adalah cara paling lantang untuk berkata bahwa kamu pernah ada."
    return

label scene_d39:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-10 / BG-12 (Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D39 - Rakyat Tuban bergerak. (Opsional; aktif jika D15-C)"

    menu:
        "Izinkan rakyat membangun monumen.":
            $ d39_choice = "A"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Tuban jadi pusat ziarah."

        "Larang—terlalu berbahaya secara politik.":
            $ d39_choice = "B"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kenangan hidup dalam lagu, lebih sulit dipadamkan."

        "Biarkan rakyat memutuskan sendiri.":
            $ d39_choice = "C"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Selalu ada yang membawa bunga ke tepi Tambak Beras."

    return

label scene_d40:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-20 (Makam Ranggalawe)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D40 - Epilog akhir: nilai yang tidak bisa diusir."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Seca Wecana — setia pada janji."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Sura ing Pati — berani demi kebenaran."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Lila ing Donya — ikhlas berkorban."

    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di antara dua tafsir itu, kisah Ranggalawe hidup—dalam abu-abu yang paling jujur."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Bagi sebagian, ia pemberontak. Bagi Tuban... ia simbol keberanian melawan ketidakadilan."

    return
