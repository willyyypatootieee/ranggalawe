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

# ==========================================
# SCENE D02 - DUA DUNIA BERGERAK BERSAMAAN
# ==========================================
label scene_d02:
    scene bg 05 with fade
    # TODO: Gunakan aset BG asli: BG-02 & BG-05 (Split Screen)
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D02 (PARALLEL): Dua dunia bergerak bersamaan. Satu di balik meja dengan surat dan siasat. Satu lagi di jalan panjang dengan pedang dan tekad."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[LAYAR KIRI] Wiraraja menulis dua surat sekaligus. Satu untuk Raden Wijaya, satu untuk Jayakatwang."
    show arya khawatir at left with dissolve
    arya "Maafkan anakku, Jayakatwang. Ini bukan pengkhianatan. Ini... politik."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[LAYAR KANAN] Ken Kara melangkah di jalannya..."

    if siasat > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Bermain dua wajah terasa merendahkan harga diri ksatria. Tapi tanpa siasat, perlawanan terbuka berarti kematian sia-sia. Aku percaya ayahku."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Langkahku mantap menuju takdir yang belum selesai."

    return

# ==========================================
# SCENE D03 - NAMA BARU, TANGGUNG JAWAB BARU
# ==========================================
label scene_d03:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-05 / BG-06 (Kamp Hutan Tarik)

    if d01_choice == "A":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[CUTSCENE] Raden Wijaya memeluk Ken Kara. 'Kamu datang sendiri, tanpa diminta. Itulah keberanian yang Majapahit butuhkan.'"
    elif d01_choice == "B":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[CUTSCENE] Raden Wijaya meninjau 200 prajurit. 'Kamu tidak hanya membawa dirimu. Kamu membawa Madura.'"
    elif d01_choice == "C":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[CUTSCENE] Raden Wijaya berbisik. 'Wiraraja bilang kamu sudah tahu semuanya. Aku butuh orang seperti itu di dekatku.'"

    raden "Mulai hari ini, kamu kupanggil Ranggalawe - ia yang boleh memerintah anak buahku. Nama ini bukan hadiah. Ini tanggung jawab."

    menu:
        "Hamba berjanji akan mempertahankan nama ini dengan kehidupan hamba. (Konfrontasi)":
            $ konfrontasi += 1
            $ loyalitas += 20
            $ kehormatan += 15
            lembu "Nama yang berat. Tapi kamu kuat untuk membawanya."

        "Hamba bersedia. Tapi apa artinya Ranggalawe dalam situasi yang belum pasti ini? (Mediasi)":
            $ mediasi += 1
            $ kebijakan += 10
            $ kehormatan += 15
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Lembu Sora mengangguk pelan dari kejauhan, tidak berkata apa-apa."

        "Hamba bersedia. Dan izinkan hamba langsung menawarkan satu rencana. (Siasat)":
            $ siasat += 1
            $ keberanian += 10
            $ kebijakan += 15
            lembu "Hati-hati, keponakanku. Di sini orang dinilai dari cara ia diam, bukan berbicara."
            
    return

# ==========================================
# SCENE D04 - MALAM PERTAMA DI HUTAN TARIK
# ==========================================
label scene_d04:
    scene bg 07 with fade
    # TODO: Gunakan aset BG asli: BG-07 (Kamp Hutan Tarik - Malam)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Malam pertama di Hutan Tarik. Ada satu malam untuk berkenalan dengan orang-orang yang akan mewarnai perjalanannya."

    menu:
        "[[Duduk bersama Lembu Sora di api unggun] Paman punya cerita perang malam ini? (Mediasi)":
            $ mediasi += 1
            $ d04_choice = "A"
            $ kebijakan += 10
            $ loyalitas_sora += 15
            lembu "Kamu tahu kenapa aku masih hidup? Karena aku tahu kapan harus maju dan kapan harus diam."
            ranggalawe "Apakah ada saatnya diam adalah pengkhianatan, Paman?"
            lembu "Itu pertanyaan yang akan menjawab dirinya sendiri nanti."

        "[[Amati Nambi dari kejauhan] Kenapa ia selalu di sisi Raden Wijaya? (Siasat)":
            $ siasat += 1
            $ d04_choice = "B"
            $ kebijakan += 10
            $ kehormatan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengamati Nambi lekat-lekat dari bayangan, mencari kelemahannya."

        "[[Ajak Kebo Anabrang latihan fisik] Ayo, seberapa baik pendekar Majapahit bertarung. (Konfrontasi)":
            $ konfrontasi += 1
            $ d04_choice = "C"
            $ keberanian += 15
            $ kehormatan += 5
            kebo "Bagus. Di darat kamu tangguh. Tapi ingat - setiap orang punya tempat di mana ia paling lemah."
            ranggalawe "Termasuk kamu?"
            kebo "Tidak ada yang tidak bisa dipikirkan jawabannya. Termasuk pertanyaan itu."

        "Lewati malam dan istirahat.":
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih istirahat demi menyimpan tenaga."
            
    return

# ==========================================
# SCENE D05 - SIASAT MASUK KE KEDIRI
# ==========================================
label scene_d05:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-06 (Kamp Hutan Tarik - Siang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Rapat strategi. Wiraraja menguraikan rencana: berpura-pura tunduk kepada Jayakatwang dan masuk ke Kediri sebagai 'pengabdi'."
    
    menu:
        "Hamba siap. Hamba akan menjadi utusan pribadi Tuanku di Kediri. (Konfrontasi)":
            $ konfrontasi += 1
            $ kebijakan += 10
            $ keberanian += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengajukan diri sebagai garda terdepan utusan pura-pura ini."

        "Hamba minta jaminan keamanan Hutan Tarik selama hamba pergi. (Mediasi)":
            $ mediasi += 1
            $ kehormatan += 10
            $ kebijakan += 15
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menetapkan syarat rasional demi keselamatan pasukan."

        "Izinkan hamba ikut langsung ke Kediri mengantisipasi dari dalam. (Siasat)":
            $ siasat += 1
            $ loyalitas += 20
            $ keberanian += 10
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mencari posisi strategis di pusat intrik musuh."

    return

# ==========================================
# SCENE D06 - DI DALAM SARANG MUSUH
# ==========================================
label scene_d06:
    scene bg 08 with fade
    # TODO: Gunakan aset BG asli: BG-08 (Kediri - Alun-alun) / BG-09 (Kediri - Dalam Istana)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Berminggu-minggu bersandiwara di Kediri. Tunduk, menghormati, sambil menyiapkan kejatuhan musuh."
    
    if siasat > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[Batin] Aku mengamati mereka dengan kalkulasi... dan Nambi selalu dekat dengan kekuasaan tanpa harus berkeringat sepertiku."
    elif konfrontasi > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[Batin] Sandiwara ini membuatku muak. Aku tak sabar menarik pedang, apalagi saat melihat mereka percaya begitu saja pada Nambi yang tak teruji."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[Batin] Nambi mendapat kepercayaan luar biasa. Mungkinkah ada logika diplomasi darinya yang belum kupahami?"
        
    return

# ==========================================
# SCENE D07 - SUB-ARC MADURA (EKSKLUSIF HASIL D01)
# ==========================================
label scene_d07:
    if d01_choice == "A":
        scene bg 03 with fade
        # TODO: Gunakan aset BG asli: BG-03 (Jalur A) / BG-06 (Jalur B) / BG-02 (Jalur C)
        sembada "Anak Wiraraja? Nelayan-nelayan ini... mereka bukan sekadar nelayan. Mereka telinga Wiraraja di seluruh pesisir Jawa."
        $ kebijakan += 10
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "QUEST SELESAI: Info jaringan rahasia terbuka. (Modal Babak III)"
        
    elif d01_choice == "B":
        scene bg 06 with fade
        # TODO: Gunakan aset BG asli: BG-03 (Jalur A) / BG-06 (Jalur B) / BG-02 (Jalur C)
        komandan "Ranggalawe, pasukan mulai ragu akan kemenangan Raden Wijaya..."
        ranggalawe "Kumpulkan mereka. Malam ini aku bicara langsung."
        $ loyalitas_prajurit += 15
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "QUEST SELESAI: Loyalitas Pasukan Madura kuat."
        
    elif d01_choice == "C":
        scene bg 02 with fade
        # TODO: Gunakan aset BG asli: BG-03 (Jalur A) / BG-06 (Jalur B) / BG-02 (Jalur C)
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "[[Arsip Sumenep] Di antara gulungan tua, ada surat yang tak pernah disebut Wiraraja - ditujukan kepada pihak misterius."
        ranggalawe "Ayahku memainkan lebih banyak papan catur dari yang aku kira."
        $ kebijakan += 15
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "ITEM OBT: Surat Ketiga Wiraraja (Modal lawan Ra Galatik nanti)"

    return

# ==========================================
# BABAK II - RISING ACTION: Darah untuk Majapahit
# SCENE D08 - KEPUTUSAN BESAR: MANFAATKAN TARTAR
# ==========================================
label scene_d08:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-06 (Kamp Hutan Tarik - Siang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "20.000 prajurit Mongol mendarat menuntut balas pada Kertanegara."
    
    raden "Ini kesempatan. Kita sekutui mereka, gunakan untuk hancurkan Kediri, lalu usir setelah selesai."
    
    menu:
        "Tuanku, ini saat yang tak akan datang dua kali. Kita harus bergerak sekarang! (Konfrontasi)":
            $ konfrontasi += 1
            $ d08_choice = "A"
            $ keberanian += 15
            $ loyalitas += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kertarajasa melihatmu sebagai pahlawan berani, namun sulit dikontrol."

        "Setelah Kediri jatuh, kita harus sudah punya rencana mengusir mereka. (Mediasi)":
            $ mediasi += 1
            $ d08_choice = "B"
            $ kebijakan += 20
            $ kehormatan += 10
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kertarajasa mencatatmu sebagai pemikir strategis. Rencana usir Tartar terbuka."

        "Izinkan hamba memimpin garis depan, membangun relasi komandan mereka. (Siasat)":
            $ siasat += 1
            $ d08_choice = "C"
            $ keberanian += 20
            $ loyalitas += 15
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kertarajasa khawatir kamu terlalu dekat kekuatan asing. Namun relasi komandan terbuka."

    return

# ==========================================
# SCENE D09 - PERSIAPAN PERANG: DUA PERSPEKTIF
# ==========================================
label scene_d09:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-06 & BG-02 (Split Screen)

    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[LAYAR KIRI - KAMP] Ranggalawe melatih prajurit setiap pagi tanpa tidur dua hari."
    lembu "Kamu tahu cara perang yang baik bukan dari serangan pertama, tapi dari cara kamu pulang."
    ranggalawe "Aku tidak pernah memikirkan pulang."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[LAYAR KANAN - SUMENEP] Wiraraja duduk sendirian, menulis surat terakhir penuh kebohongan untuk Jayakatwang."
    show arya ambigu at right with dissolve
    arya "Jayakatwang yang terhormat... semoga kamu tidak pernah tahu berapa banyak kebohongan yang aku tulis atas namamu."
    
    return
