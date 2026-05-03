# ==========================================
# BABAK III - KLIMAKS
# ==========================================

label scene_d15:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo) / BG-12 (Pasar Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D15 - Kehidupan sebagai Adipati Tuban. (Opsional; bisa skip)"

    menu:
        "Siapkan argumen hukum Prasasti Sima. (Siasat)":
            $ siasat += 1
            $ d15_choice = "A"
            $ dokumen_hukum = True
            $ kebijakan += 15
            $ kehormatan += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menyiapkan dasar hukum untuk hari buruk."

        "Tolak pembayaran; tunggu respons resmi Trowulan. (Konfrontasi)":
            $ konfrontasi += 1
            $ d15_choice = "B"
            $ kehormatan += 15
            $ keberanian += 10
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menguji seberapa jauh mahkota berani menekan adipati."

        "Musyawarah rakyat Tuban. (Mediasi)":
            $ mediasi += 1
            $ d15_choice = "C"
            $ kehormatan += 20
            $ loyalitas_rakyat += 20
            $ rakyat_loyal = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Rakyat merasa dilibatkan. Mereka mengingatnya kelak."

        "Lewati tahun-tahun ini.":
            $ d15_choice = "SKIP"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menjalani Tuban dalam diam."

    return

label scene_d16:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-10 (Pelabuhan Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D16 - Nambi diangkat sebagai Patih Amangkubumi. (Bottleneck/W-merge)"
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di pelabuhan Tuban, surat itu tiba."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "'Dari Yang Mulia Kertarajasa: Nambi diangkat sebagai Patih Amangkubumi.'"

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Darahmu naik cepat. Kamu ingin bergerak."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu diam lama, mencoba memahami."
    elif siasat >= konfrontasi and siasat >= mediasi:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu dingin. Kamu mulai menghitung langkah."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu tidak tahu harus merasa apa—dan itu yang paling menyakitkan."

    return

label scene_d17:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D17 - Api dalam dada: respons pertama. (W-shape split)"

    menu:
        "Datang sendiri ke Trowulan dan konfrontasi. (Jalur A)":
            $ d17_route = "A"
            $ konfrontasi += 1
            $ kemarahan += 20
            $ kehormatan += 10
            call d17_a_exclusive

        "Kirim Lembu Sora sebagai utusan; tunggu di Tuban. (Jalur B)":
            $ d17_route = "B"
            call d17_b_exclusive

        "Mobilisasi diam-diam di pegunungan. (Jalur C)":
            $ d17_route = "C"
            call d17_c_exclusive

    return

label d17_a_exclusive:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[EKSKLUSIF A] Balai sidang Trowulan. Mahapati tampak di latar."
    ranggalawe "Mengapa Nambi? Ia tidak pernah menumpahkan darah untuk kerajaan ini."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kertarajasa menutup ruang debat. Tapi kamu melihat sesuatu: Mahapati bergerak."

    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Seorang pelayan menyelipkan gulungan hitam."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "ITEM OBT: Surat Gelap Mahapati (fitnah kudeta)."
    $ mahapati_letter = True

    return

label d17_b_exclusive:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[EKSKLUSIF B] Pendopo Tuban. Malam. Nambi datang tanpa pengawal."
    nambi "Aku tidak datang sebagai Patih. Aku terjebak juga. Mahapati yang mengusulkan namaku."

    menu:
        "Percaya Nambi. (Mediasi)":
            $ d17_b_choice = "B1"
            $ mediasi += 1
            $ kebijakan += 15
            $ kehormatan += 5
            $ nambi_delays_troops = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kesepakatan rahasia. Di perang nanti, satu kompi terlambat 2 jam."

        "Netral—tunggu bukti. (Siasat)":
            $ d17_b_choice = "B2"
            $ siasat += 1
            $ kehormatan += 10
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu tidak membantu, tidak juga mengkhianati."

        "Gunakan Nambi—beri info posisi pasukan palsu. (Siasat)":
            $ d17_b_choice = "B3"
            $ siasat += 1
            $ kehormatan -= 15
            $ kebijakan += 20
            $ mahapati_misinformed = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Mahapati mendapat laporan kacau. Koordinasi musuh terganggu."

    return

label d17_c_exclusive:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-13 (Pegunungan Utara Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[EKSKLUSIF C] Pegunungan utara Tuban. Ada kebocoran. Ra Galatik mata-mata Mahapati."

    menu:
        "Tangkap Ra Galatik. (Konfrontasi)":
            $ d17_c_choice = "C1"
            $ konfrontasi += 1
            $ kehormatan += 10
            $ kebijakan += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Rantai intel Mahapati putus."

        "Biarkan, tapi beri info palsu lewat dia. (Siasat)":
            $ d17_c_choice = "C2"
            $ siasat += 1
            $ kebijakan += 20
            $ kehormatan -= 10
            $ mahapati_misinformed = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Mahapati salah baca strategi."

        "Ampuni dan tarik ke pihakmu. (Mediasi)":
            $ d17_c_choice = "C3"
            $ mediasi += 1
            $ kehormatan += 15
            $ kebijakan += 15
            $ galatik_turned = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Ra Galatik berbalik. Intel rencana Mahapati terbuka."

    return

label scene_d18:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 & BG-15 (Split Screen)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D18 - Malam yang membelah. (Parallel)"
    lembu "Masih ada jalan damai, keponakanku."
    ranggalawe "Kita sudah melewati batas itu, Paman. Yang tersisa hanya cara kita berdiri di hadapannya."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di Trowulan, Mahapati menutup semua ruang damai dengan kata 'ancaman'."
    return

label scene_d19:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D19 - Ultimatum dari Trowulan."

    menu:
        "Proklamasi otonomi Tuban dengan dasar Sima. (Konfrontasi)" if dokumen_hukum:
            $ d19_choice = "A"
            $ konfrontasi += 1
            $ kebijakan += 15
            $ kehormatan += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih jalur hukum—memberi sedikit waktu ekstra."

        "Kirim mediator terakhir. (Mediasi)":
            $ d19_choice = "B"
            $ mediasi += 1
            $ kehormatan += 10
            $ kebijakan += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu masih memberi satu kesempatan."

        "Mobilisasi penuh—siapkan pertahanan Tuban. (Konfrontasi)":
            $ d19_choice = "C"
            $ konfrontasi += 1
            $ keberanian += 15
            $ kehormatan += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengunci pilihan: perang."

    return

label scene_d20:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 / BG-10 (Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D20 - Perang tidak bisa dihindari."

    lembu "Keponakanku... aku sudah coba semua jalan yang aku tahu."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        ranggalawe "Aku tahu, Paman. Ini pilihan Mahapati—bukan pilihanmu."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        ranggalawe "Masih ada satu jalan yang belum kita coba... atau sudah tidak ada?"
    elif siasat >= konfrontasi and siasat >= mediasi:
        ranggalawe "Aku sudah memperkirakan ini. Terima kasih sudah berusaha."
    else:
        ranggalawe "...Ya. Aku tahu."

    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Quest opsional: Ra Jaran Waha menawarkan keris pusaka."

    menu:
        "Simpan keris untuk dirimu.":
            $ keris_state = "KEEP"
            $ has_keris = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Keris itu terasa dingin di tanganmu."

        "Berikan keris pada Lembu Sora.":
            $ keris_state = "SORA"
            $ has_keris = True
            $ keris_given_sora = True
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menitipkan keris pada paman—seolah menitipkan doa."

        "Tolak—biarkan tetap di gudang.":
            $ keris_state = "NONE"
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih tidak menambah beban simbol."

    return

label scene_d21:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D21 - Strategi pertahanan Tuban."

    menu:
        "Pertahanan garis pantai, manfaatkan pasir. (Siasat)":
            $ d21_choice = "A"
            $ siasat += 1
            $ kebijakan += 15
            $ keberanian += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kuda mereka melambat. Kamu menghemat nyawa."

        "Gerilya—serang cepat, mundur pegunungan. (Siasat)":
            $ d21_choice = "B"
            $ siasat += 1
            $ kebijakan += 20
            $ kehormatan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Efektif, tapi meninggalkan noda kecil di kode ksatria."

        "Hadapi langsung di gerbang Tuban. (Konfrontasi)":
            $ d21_choice = "C"
            $ konfrontasi += 1
            $ keberanian += 25
            $ kehormatan += 20
            $ kebijakan -= 15
            if rakyat_loyal:
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Rakyat Tuban ikut berdiri bersamamu, tanpa diminta."
            else:
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kamu memilih kehormatan tertinggi."

    return

label scene_d22:
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D22 - Wajah yang dikenal di garis musuh."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di depan musuh: Kebo Anabrang. Di belakang: Lembu Sora—di sisi berlawanan."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap Kebo Anabrang. Matamu menyala."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap Lembu Sora. Kamu hanya mengangguk: 'Aku tahu paman sudah berusaha.'"
    elif siasat >= konfrontasi and siasat >= mediasi:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menghitung jumlah dan jarak. Kamu tidak memberi ruang pada perasaan."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Dua orang. Dua arah. Kamu tidak bisa memilih salah satunya."

    return
