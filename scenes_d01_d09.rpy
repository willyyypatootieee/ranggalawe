# ==========================================
# BABAK I - EKSPOSISI: Lahirnya Seorang Ksatria
# SCENE D01 - KABAR DATANG KE SUMENEP
# ==========================================
label scene_d01:
    # Aset placeholder
    scene bg 02 with fade
    # play music "placeholder_bgm_02.ogg" loop fadein 1.0
    # TODO: Ganti musik placeholder dengan aset BGM asli
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Singhasari, 1292 M. Prabu Kertanegara gugur di tangan Jayakatwang dari Kediri."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Raden Wijaya melarikan diri. Di Sumenep, Madura - seorang ayah menunggu putranya menyampaikan berita yang mengubah segala-galanya."

    show arya serius at center with dissolve
    arya "Anakku. Raden Wijaya dalam pelarian. Ia membutuhkan orang-orang yang ia percaya - sekarang, malam ini."
    arya "Ini bukan waktunya menangis. Ini waktunya memilih."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[Batin Ken Kara] Ayah tidak pernah berbicara seperti ini sebelumnya. Ada yang bergetar di dadaku - entah ketakutan, entah kegembiraan..."

    # Pilihan Pemain - Titik Percabangan Utama D01
    menu:
        "Katakan di mana Raden Wijaya. Aku akan pergi malam ini. (Konfrontasi)":
            $ konfrontasi += 1
            $ d01_choice = "A"
            $ keberanian += 15
            $ loyalitas += 10
            call d01_jalur_a
            
        "Satu hari, Ayah. Aku butuh mengumpulkan pria terbaik Madura. (Mediasi)":
            $ mediasi += 1
            $ d01_choice = "B"
            $ kebijakan += 15
            $ loyalitas += 5
            call d01_jalur_b
            
        "Aku tahu ada lebih dari sekadar 'pergi'. Apa yang Ayah rencanakan? (Siasat)":
            $ siasat += 1
            $ d01_choice = "C"
            $ kebijakan += 10
            $ kehormatan += 10
            call d01_jalur_c

    return

label d01_jalur_a:
    scene bg 01 with fade

    show arya bangga at center with dissolve
    arya "Pergi. Tapi ingat, anakku - yang pertama datang adalah yang paling dikenang."
    
    # Aset BG asli: BG-01 (Pendopo Sumenep Eksterior - Jalan Malam) sudah dipasang.
    scene expression Movie(play="video/berangkat.webm", size=(1920, 1080)) with fade
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Ken Kara berangkat sendiri, hanya membawa pedang dan bekal seadanya. Silhuetnya hilang dalam kegelapan."
    return

label d01_jalur_b:
    show arya bijak at center with dissolve
    arya "Kamu bijak. Kumpulkan 200 prajurit terbaik. Pasukan Madura adalah kekuatan nyata yang tidak bisa diabaikan."
    
    scene bg 01 with fade
    # Aset BG asli: BG-01 (Pendopo Sumenep Eksterior - Pagi) sudah dipasang.
    # TODO: Tambahkan aset cutscene
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[CUTSCENE] EXT. Halaman Pendopo - Pagi.\n200 prajurit berjejer. Ken Kara memimpin di depan. Terdengar irama genderang ringan."
    return

label d01_jalur_c:
    show arya ambigu at center with dissolve
    arya "(Tersenyum tipis) Kamu lebih cerdas dari yang kukira. Duduk. Dengarkan rencanaku yang sebenarnya."
    
    scene bg 02 with fade
    # TODO: Tambahkan aset cutscene
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[CUTSCENE] INT. Ruang Dalam Pendopo - Malam.\nPeta jaringan dan siasat ganda digelar di atas meja."
    return
