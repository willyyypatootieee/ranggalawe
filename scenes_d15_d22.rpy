# ==========================================
# BABAK III - KLIMAKS
# ==========================================

label scene_d15:
    scene blackscreen with fade
    show screen scene_header("1295 M", "Kadipaten Tuban")
    call screen chapter_activity_hub("FASE PERSIAPAN", "Cek peta, relasi, jurnal, dan kamus sebelum kamu memilih langkah Tuban.")
    scene pasartuban:
        xysize(1920,1080)
    with fade
    narrator "Kehidupan sebagai Adipati Tuban."
    $ add_journal("D15", "Tuban menunggu pilihanmu: hukum, konfrontasi, atau musyawarah rakyat.")

    menu:
        "Siapkan argumen hukum Prasasti Sima. (Siasat)":
            $ siasat += 1
            $ d15_choice = "A"
            $ dokumen_hukum = True
            $ kebijakan += 15
            $ kehormatan += 10
            $ add_journal("D15", "Kamu menyiapkan dasar hukum Prasasti Sima sebagai perisai Tuban.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menyiapkan dasar hukum untuk hari buruk."

        "Tolak pembayaran; tunggu respons resmi Trowulan. (Konfrontasi)":
            $ konfrontasi += 1
            $ d15_choice = "B"
            $ kehormatan += 15
            $ keberanian += 10
            $ kebijakan -= 5
            $ add_journal("D15", "Kamu menolak tekanan dan menguji batas kekuasaan Trowulan.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menguji seberapa jauh mahkota berani menekan adipati."

        "Musyawarah rakyat Tuban. (Mediasi)":
            $ mediasi += 1
            $ d15_choice = "C"
            $ kehormatan += 20
            $ loyalitas_rakyat += 20
            $ rakyat_loyal = True
            $ add_journal("D15", "Rakyat Tuban dilibatkan langsung; loyalitas mulai terbentuk.")
            $ unlock_achievement("people_king")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Rakyat merasa dilibatkan. Mereka mengingatnya kelak."

        "Lewati tahun-tahun ini.":
            $ d15_choice = "SKIP"
            $ add_journal("D15", "Kamu membiarkan tahun-tahun Tuban berlalu dalam diam.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menjalani Tuban dalam diam."

    return

label scene_d16:
    scene surat:
        xysize(1920,1080)
    with fade
    show screen scene_header("1295 M", "Pelabuhan Tuban")
    # TODO: Gunakan aset BG asli: BG-10 (Pelabuhan Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D16 - Nambi diangkat sebagai Patih Amangkubumi. (Bottleneck/W-merge)"
    $ add_journal("D16", "Surat dari Trowulan tiba: Nambi diangkat menjadi Patih Amangkubumi.")
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di pelabuhan Tuban, surat itu tiba."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "'Dari Yang Mulia Kertarajasa: {a=call:show_ensik_nambi}Nambi{/a} diangkat sebagai Patih Amangkubumi.'"

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
    show screen scene_header("1295 M", "Kadipaten Tuban")
    call screen chapter_activity_hub("FASE RAPAT", "Keputusan sidang dikunci. Gunakan ini untuk memeriksa hubungan dan catatan dulu.")
    scene balai:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Api dalam dada: respons pertama."

    # Rollback dikunci — keputusan ini tidak bisa diubah
    $ renpy.block_rollback()
    $ add_journal("D17", "Keputusan untuk merespons Trowulan dikunci; jalur ini tidak bisa ditarik kembali.")
    menu:
        "Datang sendiri ke Trowulan dan konfrontasi. (Jalur A)":
            $ d17_route = "A"
            $ konfrontasi += 1
            $ kemarahan += 20
            $ kehormatan += 10
            call d17_a_exclusive from _call_d17_a_exclusive

        "Kirim Lembu Sora sebagai utusan; tunggu di Tuban. (Jalur B)":
            $ d17_route = "B"
            call d17_b_exclusive from _call_d17_b_exclusive

        "Mobilisasi diam-diam di pegunungan. (Jalur C)":
            $ d17_route = "C"
            call d17_c_exclusive from _call_d17_c_exclusive

    return

label d17_a_exclusive:
    call effect_rage from _call_effect_rage
    scene marah:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Balai sidang Trowulan. {a=call:show_ensik_mahapati}Mahapati{/a} tampak di latar."
    scene marah2:
        xysize(1920,1080)
    with fade
    ranggalawe "Mengapa Nambi? Ia tidak pernah menumpahkan darah untuk kerajaan ini."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kertarajasa menutup ruang debat. Tapi kamu melihat sesuatu: {a=call:show_ensik_mahapati}Mahapati{/a} bergerak."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Seorang pelayan menyelipkan gulungan hitam."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "ITEM OBT: Surat Gelap {a=call:show_ensik_mahapati}Mahapati{/a} (fitnah kudeta)."
    $ mahapati_letter = True
    $ unlock_achievement("letter_found")
    $ add_journal("D17", "Kamu menemukan Surat Gelap Mahapati. Bukti politik mulai terbuka.")
    call clear_effects from _call_clear_effects_3
    return

label d17_b_exclusive:
    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Pendopo Tuban. Malam. {a=call:show_ensik_nambi}Nambi{/a} datang tanpa pengawal."
    scene expression Movie(play="video/scene1_9.webm", mute=True, size=(1920, 1080))

    nambi "Aku tidak datang sebagai Patih. Aku terjebak juga. {a=call:show_ensik_mahapati}Mahapati{/a} yang mengusulkan namaku."

    menu:
        "Percaya Nambi. (Mediasi)":
            $ d17_b_choice = "B1"
            $ mediasi += 1
            $ kebijakan += 15
            $ kehormatan += 5
            $ nambi_delays_troops = True
            $ add_journal("D17", "Kamu mempercayai Nambi dan menciptakan jeda untuk pasukan lawan.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kesepakatan rahasia. Di perang nanti, satu kompi terlambat 2 jam."

        "Netral—tunggu bukti. (Siasat)":
            $ d17_b_choice = "B2"
            $ siasat += 1
            $ kehormatan += 10
            $ kebijakan -= 5
            $ add_journal("D17", "Kamu menahan diri dan memilih menunggu bukti.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu tidak membantu, tidak juga mengkhianati."

        "Gunakan Nambi—beri info posisi pasukan palsu. (Siasat)":
            $ d17_b_choice = "B3"
            $ siasat += 1
            $ kehormatan -= 15
            $ kebijakan += 20
            $ mahapati_misinformed = True
            $ add_journal("D17", "Kamu memakai Nambi untuk menyesatkan Mahapati.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Mahapati mendapat laporan kacau. Koordinasi musuh terganggu."

    return

label d17_c_exclusive:
    scene blackscreen with fade
    scene gunung:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-13 (Pegunungan Utara Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Pegunungan utara Tuban. Ada kebocoran. Ra Galatik mata-mata Mahapati."

    menu:
        "Tangkap Ra Galatik. (Konfrontasi)":
            $ d17_c_choice = "C1"
            $ konfrontasi += 1
            $ kehormatan += 10
            $ kebijakan += 5
            $ add_journal("D17", "Ra Galatik ditangkap; jalur intel Mahapati mulai retak.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Rantai intel Mahapati putus."

        "Biarkan, tapi beri info palsu lewat dia. (Siasat)":
            $ d17_c_choice = "C2"
            $ siasat += 1
            $ kebijakan += 20
            $ kehormatan -= 10
            $ mahapati_misinformed = True
            $ add_journal("D17", "Ra Galatik dibiarkan lewat dengan informasi palsu.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Mahapati salah baca strategi."

        "Ampuni dan tarik ke pihakmu. (Mediasi)":
            $ d17_c_choice = "C3"
            $ mediasi += 1
            $ kehormatan += 15
            $ kebijakan += 15
            $ galatik_turned = True
            $ add_journal("D17", "Ra Galatik berbalik dan membuka ruang baru untukmu.")
            $ unlock_achievement("spy_turned")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Ra Galatik berbalik. Intel rencana Mahapati terbuka."

    return

label scene_d18:
    scene blackscreen with fade
    show screen scene_header("1295 M", "Trowulan")
    scene split1:
        xysize(1920,1080)
    with fade
    narrator "Malam yang membelah."
    lembu "Masih ada jalan damai, keponakanku."
    ranggalawe "Kita sudah melewati batas itu, Paman. Yang tersisa hanya cara kita berdiri di hadapannya."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Di Trowulan, {a=call:show_ensik_mahapati}Mahapati{/a} menutup semua ruang damai dengan kata 'ancaman'."
    return

label scene_d19:
    scene blackscreen with fade
    show screen scene_header("1295 M", "Tuban")
    scene ultimatum:
        xysize(1920,1080)
    with fade
    narrator "SCENE D19 - Ultimatum dari Trowulan."
    $ add_journal("D19", "Ultimatum dari Trowulan tiba. Kamu harus memilih respons yang tepat.")

    call screen timed_choice([
        ("Buka surat dan balas sekarang.", "read"),
        ("Tahan dulu, kumpulkan orang dan bukti.", "hold"),
        ("Kirim mediator sebelum semua membara.", "delegate")
    ], timeout=7.0, default_idx=1)
    $ d19_pressure = _return

    if d19_pressure == "read":
        $ keberanian += 5
        $ kehormatan += 5
        narrator "Kamu memilih menatap ancaman itu langsung."
    elif d19_pressure == "hold":
        $ kebijakan += 5
        narrator "Kamu menunda sejenak agar Tuban punya napas."
    else:
        $ mediasi += 1
        $ kebijakan += 10
        narrator "Kamu masih memberi satu kesempatan pada kata-kata."

    menu:
        "Proklamasi otonomi Tuban dengan dasar Sima. (Konfrontasi)" if dokumen_hukum:
            $ d19_choice = "A"
            $ konfrontasi += 1
            $ kebijakan += 15
            $ kehormatan += 10
            $ add_journal("D19", "Kamu memakai Prasasti Sima sebagai tameng politik.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih jalur hukum—memberi sedikit waktu ekstra."

        "Kirim mediator terakhir. (Mediasi)":
            $ d19_choice = "B"
            $ mediasi += 1
            $ kehormatan += 10
            $ kebijakan += 5
            $ add_journal("D19", "Mediator terakhir dikirim untuk menahan perang sebentar lagi.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu masih memberi satu kesempatan."

        "Mobilisasi penuh—siapkan pertahanan Tuban. (Konfrontasi)":
            $ d19_choice = "C"
            $ konfrontasi += 1
            $ keberanian += 15
            $ kehormatan += 10
            $ add_journal("D19", "Tuban dimobilisasi penuh; perang menjadi tak terelakkan.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengunci pilihan: perang."

    return

label scene_d20:
    scene blackscreen with fade
    show screen scene_header("1295 M", "Pelabuhan Tuban")
    scene expression Movie(play="video/scene1_10.webm", mute=True, size=(1920, 1080))

    # TODO: Gunakan aset BG asli: BG-11 / BG-10 (Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Perang tidak bisa dihindari."

    lembu "Keponakanku... aku sudah coba semua jalan yang aku tahu."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        show ranggalawe determination
        ranggalawe "Aku tahu, Paman. Ini pilihan Mahapati—bukan pilihanmu."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        show ranggalawe sad
        ranggalawe "Masih ada satu jalan yang belum kita coba... atau sudah tidak ada?"
    elif siasat >= konfrontasi and siasat >= mediasi:
        show ranggalawe neutral
        ranggalawe "Aku sudah memperkirakan ini. Terima kasih sudah berusaha."
    else:
        show ranggalawe sad
        ranggalawe "...Ya. Aku tahu."

    scene keris:
        xysize(1920,1080)
    with fade
    narrator "Ra Jaran Waha menawarkan keris pusaka."

    menu:
        "Simpan keris untuk dirimu.":
            $ keris_state = "KEEP"
            $ has_keris = True
            $ add_journal("D20", "Kamu menyimpan keris pusaka untuk dirimu sendiri.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Keris itu terasa dingin di tanganmu."

        "Berikan keris pada Lembu Sora.":
            $ keris_state = "SORA"
            $ has_keris = True
            $ keris_given_sora = True
            $ add_journal("D20", "Keris pusaka kamu titipkan kepada Lembu Sora.")
            $ unlock_achievement("keris_given")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menitipkan keris pada paman—seolah menitipkan doa."

        "Tolak—biarkan tetap di gudang.":
            $ keris_state = "NONE"
            $ add_journal("D20", "Kamu menolak menjadikan keris sebagai simbol beban baru.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih tidak menambah beban simbol."

    return

# ==========================================
# SCENE D21 - STRATEGI PERTAHANAN TUBAN
# ==========================================

init python:
    class D21DefensePlanner:
        def __init__(self):
            # Unit types: "tombak" (Spearmen), "panah" (Archers), "kuda" (Cavalry)
            # Positions: "depan" (Frontline), "sayap" (Flanks), "belakang" (Rearguard)
            self.positions = {
                "depan": None,
                "sayap": None,
                "belakang": None
            }
            self.score = 0
            self.formation_status = ""
            self.hovered = None
            self.unit_desc = {
                "tombak": "Tombak — Infanteri berperisai, kuat untuk menahan serangan di garis depan.",
                "panah": "Panah — Pemanah jarak jauh; efektif dari belakang untuk dukungan tembakan.",
                "kuda": "Kuda — Kavaleri cepat; ideal untuk manuver di sayap dan flank."
            }

        def place_unit(self, pos, unit):
            # Jika unit sudah di posisi yang sama -> batal (toggle/deselect)
            if self.positions.get(pos) == unit:
                self.positions[pos] = None
                self.hovered = None
                return

            # Cek jika unit sudah dipakai, hapus dari posisi lama
            for p, u in list(self.positions.items()):
                if u == unit and p != pos:
                    self.positions[p] = None

            # Tempatkan unit di posisi baru
            self.positions[pos] = unit

            # Update hovered preview on touch/click so mobile users see info
            if unit is None:
                self.hovered = None
            else:
                self.hovered = unit

        def reset(self):
            # Reset semua posisi dan status
            for p in self.positions.keys():
                self.positions[p] = None
            self.score = 0
            self.formation_status = ""

        def set_hover(self, unit):
            # Set atau clear hovered unit for info panel
            self.hovered = unit

        def calculate_score(self):
            self.score = 0
            
            # --- Logika Sinergi Formasi ---
            # Garis Depan: Butuh penahan fisik (Tombak)
            if self.positions["depan"] == "tombak":
                self.score += 40
            elif self.positions["depan"] == "kuda":
                self.score += 15
            elif self.positions["depan"] == "panah":
                self.score -= 20 # Panah di depan hancur dibanting infanteri musuh

            # Sayap: Butuh mobilitas untuk flanking (Kuda)
            if self.positions["sayap"] == "kuda":
                self.score += 35
            elif self.positions["sayap"] == "tombak":
                self.score += 15
            elif self.positions["sayap"] == "panah":
                self.score -= 5

            # Garis Belakang: Butuh penyerang jarak jauh pelindung (Panah)
            if self.positions["belakang"] == "panah":
                self.score += 45
            elif self.positions["belakang"] == "tombak":
                self.score -= 10
            elif self.positions["belakang"] == "kuda":
                self.score -= 10

            # Status Evaluasi
            if self.score >= 100:
                self.formation_status = "perfect"
            elif self.score >= 50:
                self.formation_status = "good"
            else:
                self.formation_status = "bad"
                
            return self.score

        def is_ready(self):
            return all(u is not None for u in self.positions.values())

screen d21_minigame_formasi():
    modal True
    add "#1a1a1ae6" # Gelap transparan

    default planner = D21DefensePlanner()

    python:
        sw = getattr(renpy.config, 'screen_width', 800)
        sh = getattr(renpy.config, 'screen_height', 600)
        narrow = sw < 900
        button_pad = (14, 10) if narrow else (8, 6)
        button_xmax = 260 if narrow else 200
        title_sz = 28 if narrow else 34
        subtitle_sz = 16 if narrow else 18
        button_text_sz = 20 if narrow else 16
        info_xmax = 280 if narrow else 300

    frame:
        align (0.5, 0.5)
        padding (20, 20)
        xysize (950, 700)
        background Solid("#2c3e50")
        
        vbox:
            spacing 20
            align (0.5, 0.0)
            text "⚔️ PETA FORMASI PERTAHANAN TUBAN ⚔️" size title_sz bold True xalign 0.5 color "#ecf0f1"
            text "Tempatkan ketiga resimen pada posisi strategis untuk menyambut Gempuran Majapahit." size subtitle_sz xalign 0.5 color "#bdc3c7" xmaximum 820
            
            null height 10

            # Unit Selection & Placement Grid (revamped)
            if narrow:
                vbox:
                    spacing 12
                    # Stack each position for narrow screens
                    frame background Solid("#34495e") padding (12,12):
                        vbox:
                            text "Garis Depan (Front)" bold True color "#ecf0f1" xalign 0.5
                            null height 8
                            hbox:
                                spacing 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "depan", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "depan", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "depan", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                    frame background Solid("#34495e") padding (12,12):
                        vbox:
                            text "Sayap (Flanks)" bold True color "#ecf0f1" xalign 0.5
                            null height 8
                            hbox:
                                spacing 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "sayap", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "sayap", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "sayap", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                    frame background Solid("#34495e") padding (12,12):
                        vbox:
                            text "Garis Belakang (Rear)" bold True color "#ecf0f1" xalign 0.5
                            null height 8
                            hbox:
                                spacing 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "belakang", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "belakang", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "belakang", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                    # Info panel under stacked columns
                    frame background Solid("#2c3e50") padding (12,12) xmaximum 720:
                        vbox:
                            text "Informasi Unit" bold True color "#ecf0f1"
                            null height 8
                            if planner.hovered:
                                text planner.unit_desc.get(planner.hovered, "") color "#ecf0f1" xmaximum info_xmax
                            else:
                                text "Tap tombol unit untuk melihat deskripsi." color "#bdc3c7" xmaximum info_xmax
                            null height 10
                            text "Pilihan Saat Ini:" bold True color "#ecf0f1"
                            null height 6
                            hbox:
                                text "Depan:" color "#bdc3c7"
                                if planner.positions["depan"]:
                                    text planner.positions["depan"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            hbox:
                                text "Sayap:" color "#bdc3c7"
                                if planner.positions["sayap"]:
                                    text planner.positions["sayap"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            hbox:
                                text "Belakang:" color "#bdc3c7"
                                if planner.positions["belakang"]:
                                    text planner.positions["belakang"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            null height 10
                            text "Skor Perkiraan: [planner.calculate_score()]" color "#f1c40f"
                            null height 10
                            hbox:
                                spacing 8
                                if planner.is_ready():
                                    textbutton "SAHKAN" action [Function(planner.calculate_score), Return(planner)] background Solid("#27ae60") text_color "#ffffff" padding button_pad text_size button_text_sz
                                textbutton "Reset" action Function(planner.reset) background Solid("#7f8c8d") text_color "#ffffff" padding button_pad text_size button_text_sz
                                textbutton "Batal" action [Function(planner.set_hover, None), Return(None)] background Solid("#c0392b") text_color "#ffffff" padding button_pad text_size button_text_sz

            else:
                hbox:
                    spacing 24
                    xalign 0.5

                    # Left: three position columns
                    hbox:
                        spacing 14

                        # Front column
                        frame background Solid("#34495e") padding (10,10):
                            vbox:
                                text "Garis Depan (Front)" bold True color "#ecf0f1" xalign 0.5
                                null height 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "depan", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "depan", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "depan", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["depan"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["depan"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                        # Flank column
                        frame background Solid("#34495e") padding (10,10):
                            vbox:
                                text "Sayap (Flanks)" bold True color "#ecf0f1" xalign 0.5
                                null height 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "sayap", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "sayap", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "sayap", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["sayap"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["sayap"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                        # Rear column
                        frame background Solid("#34495e") padding (10,10):
                            vbox:
                                text "Garis Belakang (Rear)" bold True color "#ecf0f1" xalign 0.5
                                null height 8
                                textbutton "🛡️ Tombak" action [Function(planner.place_unit, "belakang", "tombak")] hovered Function(planner.set_hover, "tombak") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "tombak" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "tombak" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🏹 Panah" action [Function(planner.place_unit, "belakang", "panah")] hovered Function(planner.set_hover, "panah") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "panah" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "panah" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz
                                textbutton "🐎 Kuda" action [Function(planner.place_unit, "belakang", "kuda")] hovered Function(planner.set_hover, "kuda") unhovered Function(planner.set_hover, None) background (Solid("#27ae60") if planner.positions["belakang"] == "kuda" else Solid("#2c3e50")) text_color ("#ffffff" if planner.positions["belakang"] == "kuda" else "#ecf0f1") padding button_pad xmaximum button_xmax text_size button_text_sz

                    # Right: Info panel
                    frame background Solid("#2c3e50") padding (14,12) xmaximum 330:
                        vbox:
                            text "Informasi Unit" bold True color "#ecf0f1"
                            null height 8
                            if planner.hovered:
                                text planner.unit_desc.get(planner.hovered, "") color "#ecf0f1" xmaximum info_xmax
                            else:
                                text "Arahkan kursor/tap tombol unit untuk melihat deskripsi." color "#bdc3c7" xmaximum info_xmax
                            null height 10
                            text "Pilihan Saat Ini:" bold True color "#ecf0f1"
                            null height 6
                            hbox:
                                text "Depan:" color "#bdc3c7"
                                if planner.positions["depan"]:
                                    text planner.positions["depan"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            hbox:
                                text "Sayap:" color "#bdc3c7"
                                if planner.positions["sayap"]:
                                    text planner.positions["sayap"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            hbox:
                                text "Belakang:" color "#bdc3c7"
                                if planner.positions["belakang"]:
                                    text planner.positions["belakang"].upper() color "#ecf0f1"
                                else:
                                    text "KOSONG" color "#bdc3c7"
                            null height 10
                            text "Skor Perkiraan: [planner.calculate_score()]" color "#f1c40f"
                            null height 10
                            hbox:
                                spacing 8
                                if planner.is_ready():
                                    textbutton "SAHKAN" action [Function(planner.calculate_score), Return(planner)] background Solid("#27ae60") text_color "#ffffff" padding button_pad text_size button_text_sz
                                textbutton "Reset" action Function(planner.reset) background Solid("#7f8c8d") text_color "#ffffff" padding button_pad text_size button_text_sz
                                textbutton "Batal" action [Function(planner.set_hover, None), Return(None)] background Solid("#c0392b") text_color "#ffffff" padding button_pad text_size button_text_sz

            null height 30

            # --- Panel Rekap ---
            frame:
                background Solid("#34495e")
                padding (18, 18)
                xfill True
                vbox:
                    text "Visualisasi Peta Taktis:" bold True color "#ecf0f1"
                    null height 6
                    hbox:
                        text "Depan: " size 20 color "#ecf0f1"
                        if planner.positions["depan"]:
                            frame background Solid("#2c3e50") padding (6,4):
                                text planner.positions["depan"].upper() size 20 color "#ffffff"
                        else:
                            text "KOSONG" size 20 color "#bdc3c7"
                        text "  <-- Garis Musuh" size 18 color "#bdc3c7"

                    hbox:
                        text "Sayap: " size 20 color "#ecf0f1"
                        if planner.positions["sayap"]:
                            frame background Solid("#2c3e50") padding (6,4):
                                text planner.positions["sayap"].upper() size 20 color "#ffffff"
                        else:
                            text "KOSONG" size 20 color "#bdc3c7"

                    hbox:
                        text "Belakang: " size 20 color "#ecf0f1"
                        if planner.positions["belakang"]:
                            frame background Solid("#2c3e50") padding (6,4):
                                text planner.positions["belakang"].upper() size 20 color "#ffffff"
                        else:
                            text "KOSONG" size 20 color "#bdc3c7"
                        text "  <-- Ranggalawe" size 18 color "#bdc3c7"
            
            # --- Konfirmasi & Controls ---
            hbox:
                spacing 20
                xalign 0.5
                if planner.is_ready():
                    textbutton "SAHKAN FORMASI" action [Function(planner.calculate_score), Return(planner)] xalign 0.5 text_size 28 text_bold True background Solid("#27ae60") text_color "#ffffff" padding (12,8)
                textbutton "Reset" action Function(planner.reset) text_size button_text_sz background Solid("#7f8c8d") text_color "#ffffff" padding button_pad
                textbutton "Batal" action Return(None) text_size button_text_sz background Solid("#c0392b") text_color "#ffffff" padding button_pad

label scene_d21:
    scene blackscreen with fade
    show screen scene_header("1295 M", "Pertahanan Tuban")
    call screen chapter_activity_hub("FASE PERTAHANAN", "Atur formasi, cek relasi, lalu sahkan pertahanan Tuban.")
    scene expression Movie(play="video/scene1_11.webm", mute=True, size=(1920, 1080))

    # TODO: Gunakan aset BG asli: BG-11 (Kadipaten Tuban Pendopo)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Strategi pertahanan Tuban."
    
    narrator "Mata-mata melaporkan pasukan {a=call:show_ensik_kebo_anabrang}Kebo Anabrang{/a} sudah mendekati pesisir Tuban. Waktu untuk negosiasi sudah habis."
    ranggalawe "Gelar peta pertahanan. Aku harus menempatkan pasukan kita dengan cermat di batas kota."
    
    # Panggil Minigame Formasi D21
    call screen d21_minigame_formasi
    
    # Ambil hasil kalkulasi
    $ d21_defense_planner = _return
    $ d21_formation_status = d21_defense_planner.formation_status
    
    if d21_formation_status == "perfect":
        $ siasat += 2
        $ unlock_achievement("perfect_form")
        $ add_journal("D21", "Formasi pertahanan Tuban berhasil disusun dengan sempurna.")
        narrator "Formasi Sempurna. Tombak menahan serbuan di depan, kuda bersiap mengepung dari sayap, dan hujan panah melindungimu di belakang."
        ranggalawe "Biarkan mereka datang. Mereka akan terkoyak di gerbang kita."
    elif d21_formation_status == "good":
        $ add_journal("D21", "Formasi pertahanan cukup baik, walau belum optimal.")
        narrator "Formasi Cukup Baik. Meskipun tidak ideal, garis pertahanan ini masih bisa menahan gempuran awal."
    else:
        $ kebijakan -= 2
        $ add_journal("D21", "Formasi pertahananmu berisiko dan membuka celah fatal.")
        narrator "Formasi Berisiko! Penempatan pasukan yang tidak wajar membuka celah fatal di beberapa sisi pertahanan."
        ranggalawe "Sudah terlambat untuk memindahkan mereka sekarang. Kita bertarung dengan apa yang ada!"

    menu:
        "Pertahanan garis pantai, manfaatkan pasir. (Siasat)":
            $ d21_choice = "A"
            $ siasat += 1
            $ kebijakan += 15
            $ keberanian += 10
            $ add_journal("D21", "Kamu memilih pertahanan pantai dan memanfaatkan pasir.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kuda mereka melambat. Kamu menghemat nyawa."

        "Gerilya—serang cepat, mundur pegunungan. (Siasat)":
            $ d21_choice = "B"
            $ siasat += 1
            $ kebijakan += 20
            $ kehormatan -= 5
            $ add_journal("D21", "Kamu memilih gerilya untuk menekan musuh lalu menghilang.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Efektif, tapi meninggalkan noda kecil di kode ksatria."

        "Hadapi langsung di gerbang Tuban. (Konfrontasi)":
            $ d21_choice = "C"
            $ konfrontasi += 1
            $ keberanian += 25
            $ kehormatan += 20
            $ kebijakan -= 15
            $ add_journal("D21", "Kamu memilih menghadapi musuh langsung di gerbang Tuban.")
            if rakyat_loyal:
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Rakyat Tuban ikut berdiri bersamamu, tanpa diminta."
            else:
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kamu memilih kehormatan tertinggi."

    return

label scene_d22:
    call effect_battle from _call_effect_battle_2
    scene blackscreen with fade
    show screen scene_header("1295 M", "Tambak Beras")
    scene perang1:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Wajah yang dikenal di garis musuh."
    scene perang2:
        xysize(1920,1080)
    with fade
    narrator "Di depan musuh: {a=call:show_ensik_kebo_anabrang}Kebo Anabrang{/a}. Di belakang: {a=call:show_ensik_lembu_sora}Lembu Sora{/a}—di sisi berlawanan."

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        show screen impact_flash("#ff2200cc")
        $ add_journal("D22", "Kamu menatap Kebo Anabrang secara langsung di garis musuh.")
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap {a=call:show_ensik_kebo_anabrang}Kebo Anabrang{/a}. Matamu menyala."
    elif mediasi >= konfrontasi and mediasi >= siasat:
        $ add_journal("D22", "Pertempuran terasa seperti percakapan yang terlambat diselamatkan.")
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap {a=call:show_ensik_lembu_sora}Lembu Sora{/a}. Kamu hanya mengangguk: 'Aku tahu paman sudah berusaha.'"
    elif siasat >= konfrontasi and siasat >= mediasi:
        $ add_journal("D22", "Kamu menghitung jarak dan jumlah saat perang dimulai.")
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menghitung jumlah dan jarak. Kamu tidak memberi ruang pada perasaan."
    else:
        show screen impact_flash("#000000aa")
        $ add_journal("D22", "Kamu tidak bisa memilih salah satu dari dua arah yang memukulmu bersamaan.")
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Dua orang. Dua arah. Kamu tidak bisa memilih salah satunya."

    call clear_effects from _call_clear_effects_4
    return
