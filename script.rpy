# The script of the game goes in this file.

# Safe placeholder visuals (so the project runs before assets exist).
image bg placeholder = Solid("#000")

# Declare characters used by this game.
define ranggalawe = Character("Ken Kara / Ranggalawe", color="#c8ffc8")
define arya = Character("Arya Wiraraja", color="#ffc8c8")
define raden = Character("Raden Wijaya", color="#ffffc8")
define lembu = Character("Lembu Sora", color="#c8c8ff")
define nambi = Character("Nambi", color="#ffc8ff")
define kebo = Character("Kebo Anabrang", color="#c8ffff")
define sembada = Character("Nyai Sembada", color="#ffd5c8")
define komandan = Character("Komandan Garda", color="#c8ffd5")
define narrator = Character(None, what_italic=True)

# Game Variables for Dynamic Branching
default konfrontasi = 0
default mediasi = 0
default siasat = 0

# Trackers for exclusive routes and choices
default d01_choice = ""
default d04_choice = ""
default d08_choice = ""
default d10_choice = ""
default d12_choice = ""
default d15_choice = ""
default d17_route = ""
default d17_b_choice = ""
default d17_c_choice = ""
default d19_choice = ""
default d21_choice = ""
default d23_choice = ""
default d25_choice = ""
default d27_choice = ""
default d29_choice = ""
default d34_choice = ""
default d39_choice = ""

# Game Flags and Stats
default keberanian = 0
default kebijakan = 0
default kehormatan = 0
default loyalitas = 0
default loyalitas_sora = 0
default loyalitas_prajurit = 0

# Extra state used by later scenes (D10-D40).
default kemarahan = 0
default loyalitas_rakyat = 0
default rakyat_loyal = False
default dokumen_hukum = False
default mahapati_letter = False
default mahapati_letter_given = False
default nambi_delays_troops = False
default mahapati_misinformed = False
default galatik_turned = False
default has_keris = False
default keris_given_sora = False
default keris_state = "NONE"  # NONE | KEEP | SORA
default d26_pact = False

# The game starts here.
label start:
    # Babak 1
    call scene_d01
    call scene_d02
    call scene_d03
    call scene_d04
    call scene_d05
    call scene_d06
    call scene_d07
    
    # Babak 2
    call scene_d08
    call scene_d09

    # Babak 2 (lanjutan) - Babak 5
    call scene_d10
    call scene_d11
    call scene_d12
    call scene_d13
    call scene_d14
    call scene_d15
    call scene_d16
    call scene_d17
    call scene_d18
    call scene_d19
    call scene_d20
    call scene_d21
    call scene_d22
    call scene_d23
    call scene_d24
    call scene_d25
    call scene_d26
    call scene_d27
    call scene_d28

    # Epilog
    call scene_d29
    call scene_d30
    call scene_d31
    call scene_d32
    call scene_d33
    call scene_d34
    call scene_d35
    
    return

# ==========================================
# BABAK I - EKSPOSISI: Lahirnya Seorang Ksatria
# SCENE D01 - KABAR DATANG KE SUMENEP
# ==========================================
label scene_d01:
    # Aset placeholder
    scene bg placeholder with fade
    # play music "placeholder_bgm_02.ogg" loop fadein 1.0
    
    narrator "Singhasari, 1292 M. Prabu Kertanegara gugur di tangan Jayakatwang dari Kediri."
    narrator "Raden Wijaya melarikan diri. Di Sumenep, Madura - seorang ayah menunggu putranya menyampaikan berita yang mengubah segala-galanya."

    arya "Anakku. Raden Wijaya dalam pelarian. Ia membutuhkan orang-orang yang ia percaya - sekarang, malam ini."
    arya "Ini bukan waktunya menangis. Ini waktunya memilih."
    
    narrator "[Batin Ken Kara] Ayah tidak pernah berbicara seperti ini sebelumnya. Ada yang bergetar di dadaku - entah ketakutan, entah kegembiraan..."

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
    arya "Pergi. Tapi ingat, anakku - yang pertama datang adalah yang paling dikenang."
    
    scene bg placeholder with fade
    narrator "[CUTSCENE] EXT. Jalan Sumenep - Malam.\nKen Kara berangkat sendiri, hanya membawa pedang dan bekal seadanya. Silhuetnya hilang dalam kegelapan."
    return

label d01_jalur_b:
    arya "Kamu bijak. Kumpulkan 200 prajurit terbaik. Pasukan Madura adalah kekuatan nyata yang tidak bisa diabaikan."
    
    scene bg placeholder with fade
    narrator "[CUTSCENE] EXT. Halaman Pendopo - Pagi.\n200 prajurit berjejer. Ken Kara memimpin di depan. Terdengar irama genderang ringan."
    return

label d01_jalur_c:
    arya "(Tersenyum tipis) Kamu lebih cerdas dari yang kukira. Duduk. Dengarkan rencanaku yang sebenarnya."
    
    scene bg placeholder with fade
    narrator "[CUTSCENE] INT. Ruang Dalam Pendopo - Malam.\nPeta jaringan dan siasat ganda digelar di atas meja."
    return

# ==========================================
# SCENE D02 - DUA DUNIA BERGERAK BERSAMAAN
# ==========================================
label scene_d02:
    scene bg placeholder with fade
    
    narrator "SCENE D02 (PARALLEL): Dua dunia bergerak bersamaan. Satu di balik meja dengan surat dan siasat. Satu lagi di jalan panjang dengan pedang dan tekad."
    
    narrator "[LAYAR KIRI] Wiraraja menulis dua surat sekaligus. Satu untuk Raden Wijaya, satu untuk Jayakatwang."
    arya "Maafkan anakku, Jayakatwang. Ini bukan pengkhianatan. Ini... politik."
    
    narrator "[LAYAR KANAN] Ken Kara melangkah di jalannya..."

    if siasat > 0:
        narrator "Bermain dua wajah terasa merendahkan harga diri ksatria. Tapi tanpa siasat, perlawanan terbuka berarti kematian sia-sia. Aku percaya ayahku."
    else:
        narrator "Langkahku mantap menuju takdir yang belum selesai."

    return

# ==========================================
# SCENE D03 - NAMA BARU, TANGGUNG JAWAB BARU
# ==========================================
label scene_d03:
    scene bg placeholder with fade

    if d01_choice == "A":
        narrator "[CUTSCENE] Raden Wijaya memeluk Ken Kara. 'Kamu datang sendiri, tanpa diminta. Itulah keberanian yang Majapahit butuhkan.'"
    elif d01_choice == "B":
        narrator "[CUTSCENE] Raden Wijaya meninjau 200 prajurit. 'Kamu tidak hanya membawa dirimu. Kamu membawa Madura.'"
    elif d01_choice == "C":
        narrator "[CUTSCENE] Raden Wijaya berbisik. 'Wiraraja bilang kamu sudah tahu semuanya. Aku butuh orang seperti itu di dekatku.'"

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
    scene bg placeholder with fade
    narrator "Malam pertama di Hutan Tarik. Ada satu malam untuk berkenalan dengan orang-orang yang akan mewarnai perjalanannya."

    menu:
        "[Duduk bersama Lembu Sora di api unggun] Paman punya cerita perang malam ini? (Mediasi)":
            $ mediasi += 1
            $ d04_choice = "A"
            $ kebijakan += 10
            $ loyalitas_sora += 15
            lembu "Kamu tahu kenapa aku masih hidup? Karena aku tahu kapan harus maju dan kapan harus diam."
            ranggalawe "Apakah ada saatnya diam adalah pengkhianatan, Paman?"
            lembu "Itu pertanyaan yang akan menjawab dirinya sendiri nanti."

        "[Amati Nambi dari kejauhan] Kenapa ia selalu di sisi Raden Wijaya? (Siasat)":
            $ siasat += 1
            $ d04_choice = "B"
            $ kebijakan += 10
            $ kehormatan -= 5
            narrator "Kamu mengamati Nambi lekat-lekat dari bayangan, mencari kelemahannya."

        "[Ajak Kebo Anabrang latihan fisik] Ayo, seberapa baik pendekar Majapahit bertarung. (Konfrontasi)":
            $ konfrontasi += 1
            $ d04_choice = "C"
            $ keberanian += 15
            $ kehormatan += 5
            kebo "Bagus. Di darat kamu tangguh. Tapi ingat - setiap orang punya tempat di mana ia paling lemah."
            ranggalawe "Termasuk kamu?"
            kebo "Tidak ada yang tidak bisa dipikirkan jawabannya. Termasuk pertanyaan itu."

        "Lewati malam dan istirahat.":
            narrator "Kamu memilih istirahat demi menyimpan tenaga."
            
    return

# ==========================================
# SCENE D05 - SIASAT MASUK KE KEDIRI
# ==========================================
label scene_d05:
    scene bg placeholder with fade
    narrator "Rapat strategi. Wiraraja menguraikan rencana: berpura-pura tunduk kepada Jayakatwang dan masuk ke Kediri sebagai 'pengabdi'."
    
    menu:
        "Hamba siap. Hamba akan menjadi utusan pribadi Tuanku di Kediri. (Konfrontasi)":
            $ konfrontasi += 1
            $ kebijakan += 10
            $ keberanian += 5
            narrator "Kamu mengajukan diri sebagai garda terdepan utusan pura-pura ini."

        "Hamba minta jaminan keamanan Hutan Tarik selama hamba pergi. (Mediasi)":
            $ mediasi += 1
            $ kehormatan += 10
            $ kebijakan += 15
            narrator "Kamu menetapkan syarat rasional demi keselamatan pasukan."

        "Izinkan hamba ikut langsung ke Kediri mengantisipasi dari dalam. (Siasat)":
            $ siasat += 1
            $ loyalitas += 20
            $ keberanian += 10
            $ kebijakan -= 5
            narrator "Kamu mencari posisi strategis di pusat intrik musuh."

    return

# ==========================================
# SCENE D06 - DI DALAM SARANG MUSUH
# ==========================================
label scene_d06:
    scene bg placeholder with fade
    narrator "Berminggu-minggu bersandiwara di Kediri. Tunduk, menghormati, sambil menyiapkan kejatuhan musuh."
    
    if siasat > 0:
        narrator "[Batin] Aku mengamati mereka dengan kalkulasi... dan Nambi selalu dekat dengan kekuasaan tanpa harus berkeringat sepertiku."
    elif konfrontasi > 0:
        narrator "[Batin] Sandiwara ini membuatku muak. Aku tak sabar menarik pedang, apalagi saat melihat mereka percaya begitu saja pada Nambi yang tak teruji."
    else:
        narrator "[Batin] Nambi mendapat kepercayaan luar biasa. Mungkinkah ada logika diplomasi darinya yang belum kupahami?"
        
    return

# ==========================================
# SCENE D07 - SUB-ARC MADURA (EKSKLUSIF HASIL D01)
# ==========================================
label scene_d07:
    if d01_choice == "A":
        scene bg placeholder with fade
        sembada "Anak Wiraraja? Nelayan-nelayan ini... mereka bukan sekadar nelayan. Mereka telinga Wiraraja di seluruh pesisir Jawa."
        $ kebijakan += 10
        narrator "QUEST SELESAI: Info jaringan rahasia terbuka. (Modal Babak III)"
        
    elif d01_choice == "B":
        scene bg placeholder with fade
        komandan "Ranggalawe, pasukan mulai ragu akan kemenangan Raden Wijaya..."
        ranggalawe "Kumpulkan mereka. Malam ini aku bicara langsung."
        $ loyalitas_prajurit += 15
        narrator "QUEST SELESAI: Loyalitas Pasukan Madura kuat."
        
    elif d01_choice == "C":
        scene bg placeholder with fade
        narrator "[Arsip Sumenep] Di antara gulungan tua, ada surat yang tak pernah disebut Wiraraja - ditujukan kepada pihak misterius."
        ranggalawe "Ayahku memainkan lebih banyak papan catur dari yang aku kira."
        $ kebijakan += 15
        narrator "ITEM OBT: Surat Ketiga Wiraraja (Modal lawan Ra Galatik nanti)"

    return

# ==========================================
# BABAK II - RISING ACTION: Darah untuk Majapahit
# SCENE D08 - KEPUTUSAN BESAR: MANFAATKAN TARTAR
# ==========================================
label scene_d08:
    scene bg placeholder with fade
    narrator "20.000 prajurit Mongol mendarat menuntut balas pada Kertanegara."
    
    raden "Ini kesempatan. Kita sekutui mereka, gunakan untuk hancurkan Kediri, lalu usir setelah selesai."
    
    menu:
        "Tuanku, ini saat yang tak akan datang dua kali. Kita harus bergerak sekarang! (Konfrontasi)":
            $ konfrontasi += 1
            $ d08_choice = "A"
            $ keberanian += 15
            $ loyalitas += 10
            narrator "Kertarajasa melihatmu sebagai pahlawan berani, namun sulit dikontrol."

        "Setelah Kediri jatuh, kita harus sudah punya rencana mengusir mereka. (Mediasi)":
            $ mediasi += 1
            $ d08_choice = "B"
            $ kebijakan += 20
            $ kehormatan += 10
            narrator "Kertarajasa mencatatmu sebagai pemikir strategis. Rencana usir Tartar terbuka."

        "Izinkan hamba memimpin garis depan, membangun relasi komandan mereka. (Siasat)":
            $ siasat += 1
            $ d08_choice = "C"
            $ keberanian += 20
            $ loyalitas += 15
            $ kebijakan -= 5
            narrator "Kertarajasa khawatir kamu terlalu dekat kekuatan asing. Namun relasi komandan terbuka."

    return

# ==========================================
# SCENE D09 - PERSIAPAN PERANG: DUA PERSPEKTIF
# ==========================================
label scene_d09:
    scene bg placeholder with fade

    narrator "[LAYAR KIRI - KAMP] Ranggalawe melatih prajurit setiap pagi tanpa tidur dua hari."
    lembu "Kamu tahu cara perang yang baik bukan dari serangan pertama, tapi dari cara kamu pulang."
    ranggalawe "Aku tidak pernah memikirkan pulang."
    
    narrator "[LAYAR KANAN - SUMENEP] Wiraraja duduk sendirian, menulis surat terakhir penuh kebohongan untuk Jayakatwang."
    arya "Jayakatwang yang terhormat... semoga kamu tidak pernah tahu berapa banyak kebohongan yang aku tulis atas namamu."
    
    return


    
