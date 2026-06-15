# ==========================================
# BABAK II (lanjutan)
# ==========================================

label scene_d10:
    call effect_battle from _call_effect_battle_1
    show screen scene_header("1293 M", "Pertempuran Jongbiru")
    call screen chapter_activity_hub("FASE INVASI", "Cek relasi, jurnal, dan kamus sebelum benturan pertama di Jongbiru.")
    scene expression Movie(play="video/scene1_5.webm", mute=True, size=(1920, 1080)) with fade
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban, Jongbiru)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Pertempuran di Jongbiru."
    # TODO: Ganti musik placeholder dengan aset BGM-07
    $ add_journal("D10", "Pertempuran Jongbiru dimulai; kamu memilih cara menekan musuh pertama kali.")

    menu:
        "Serangan frontal. Ikut aku. (Konfrontasi)":
            $ konfrontasi += 1
            $ d10_choice = "A"
            $ keberanian += 20
            $ kehormatan += 10
            $ kebijakan -= 5
            $ add_journal("D10", "Kamu menerobos garis musuh dengan serangan frontal yang berisiko tinggi.")
            show screen impact_flash("#ff2200cc")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu menerobos langsung. Barisan musuh retak, tapi namamu jadi terlalu menyala."

        "Kepung sayap kanan, putus jalur mundur. (Mediasi)":
            $ mediasi += 1
            $ d10_choice = "B"
            $ kebijakan += 20
            $ keberanian += 10
            $ add_journal("D10", "Kamu memilih kepungan terukur untuk memutus jalur mundur musuh.")
            show screen impact_flash("#ff550088")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu memilih medan dan tempo. Menang tanpa banyak gaya."

        "Serangan simultan dengan komandan Tartar. (Siasat)":
            $ siasat += 1
            $ d10_choice = "C"
            $ kebijakan += 15
            $ loyalitas += 10
            $ add_journal("D10", "Kamu menautkan serangan dengan komandan Tartar dan menguatkan relasi taktis.")
            show screen impact_flash("#ff330099")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu mengunci koordinasi dua arah. Relasi Tartar menguat."

    call clear_effects from _call_clear_effects_1
    return

label scene_d11:
    call effect_aftermath from _call_effect_aftermath
    scene kediri:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-08 / BG-09 (Kediri)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kediri jatuh."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "{a=call:show_ensik_raden_wijaya}Raden Wijaya{/a} menang. Majapahit lahir dari abu kemenangan ini."
    $ add_journal("D11", "Kediri jatuh dan Majapahit lahir dari kemenangan yang mahal.")
    $ unlock_achievement("victory_first")

    call effect_triumph from _call_effect_triumph

    scene expression Movie(play="video/scene1_13.webm", mute=True, size=(1920, 1080))
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

    $ add_journal("D11", "Kemenangan datang, tetapi ruang di sisi raja mulai terasa sempit.")

    call clear_effects from _call_clear_effects_2
    return

# ==========================================
# SCENE D12 - SIASAT MENGUSIR TARTAR
# ==========================================

init python:
    class D12WargamePlanner:
        def __init__(self):
            self.taktik = None
            self.target = None
            
            self.honor = 0
            self.effectiveness = 0
            self.risk = 0
            self.choice_id = "A"

        def set_taktik(self, val):
            self.taktik = val
            self._update_stats()

        def set_target(self, val):
            self.target = val
            self._update_stats()

        def _update_stats(self):
            h = 50; e = 50; r = 50 # Base stats
            
            if self.taktik == "pesta":
                h -= 30; e += 40; r -= 20
                self.choice_id = "A"
            elif self.taktik == "kepung":
                h += 10; e += 20; r += 10
                self.choice_id = "B"
            elif self.taktik == "duel":
                h += 40; e -= 10; r += 40
                self.choice_id = "C"

            if self.target == "kamp":
                h += 10; e += 10; r += 20
            elif self.target == "kapal":
                h -= 10; e += 30; r -= 10
            elif self.target == "komandan":
                h += 20; e += 15; r += 30
                if self.taktik == "kepung":
                    self.choice_id = "C" # Override
            
            # Normalize
            self.honor = min(100, max(0, h))
            self.effectiveness = min(100, max(0, e))
            self.risk = min(100, max(0, r))

        def is_ready(self):
            return self.taktik is not None and self.target is not None

screen d12_minigame_wargame():
    modal True
    add "#000000e6" # Very dark overlay

    default planner = D12WargamePlanner()

    frame:
        align (0.5, 0.45) # Geser sedikit ke atas agar tidak menabrak quick menu
        padding (30, 30)
        xysize (1050, 680)
        background Solid("#1e272e") # Clean dark slate
        
        vbox:
            spacing 20
            align (0.5, 0.0)
            
            # --- Header ---
            vbox:
                spacing 5
                xalign 0.5
                text "♟️ DEWAN PERANG: PENGUSIRAN TARTAR" size 34 bold True xalign 0.5 color "#f39c12"
                text "Tentukan manuver taktis pasukan Majapahit. Analisis efektivitas, kehormatan, dan risiko." size 16 xalign 0.5 color "#7f8c8d"

            add Solid("#34495e") xsize 950 ysize 2 xalign 0.5

            hbox:
                spacing 40
                xalign 0.5

                # --- Kolom Pilihan ---
                vbox:
                    spacing 15
                    xsize 450
                    
                    text "1. Metode Pengusiran:" bold True size 20 color "#ecf0f1"
                    vbox:
                        spacing 8
                        textbutton "🍶 Gelar Pesta Palsu (Lengahkan)" action Function(planner.set_taktik, "pesta") text_size 18 text_color ("#ffffff" if planner.taktik == "pesta" else "#bdc3c7") background (Solid("#d35400") if planner.taktik == "pesta" else Solid("#2c3e50")) hover_background Solid("#e67e22") padding (12, 8) xfill True
                        textbutton "🛡️ Pengepungan Malam (Terkoordinasi)" action Function(planner.set_taktik, "kepung") text_size 18 text_color ("#ffffff" if planner.taktik == "kepung" else "#bdc3c7") background (Solid("#d35400") if planner.taktik == "kepung" else Solid("#2c3e50")) hover_background Solid("#e67e22") padding (12, 8) xfill True
                        textbutton "⚔️ Serangan Frontal & Duel" action Function(planner.set_taktik, "duel") text_size 18 text_color ("#ffffff" if planner.taktik == "duel" else "#bdc3c7") background (Solid("#d35400") if planner.taktik == "duel" else Solid("#2c3e50")) hover_background Solid("#e67e22") padding (12, 8) xfill True

                    null height 5

                    text "2. Target Operasi Utama:" bold True size 20 color "#ecf0f1"
                    vbox:
                        spacing 8
                        textbutton "⛺ Kamp Pasukan Tartar" action Function(planner.set_target, "kamp") text_size 18 text_color ("#ffffff" if planner.target == "kamp" else "#bdc3c7") background (Solid("#2980b9") if planner.target == "kamp" else Solid("#2c3e50")) hover_background Solid("#3498db") padding (12, 8) xfill True
                        textbutton "⚓ Armada Jung (Putus Akses)" action Function(planner.set_target, "kapal") text_size 18 text_color ("#ffffff" if planner.target == "kapal" else "#bdc3c7") background (Solid("#2980b9") if planner.target == "kapal" else Solid("#2c3e50")) hover_background Solid("#3498db") padding (12, 8) xfill True
                        textbutton "👑 Tenda Komandan Ike Mese" action Function(planner.set_target, "komandan") text_size 18 text_color ("#ffffff" if planner.target == "komandan" else "#bdc3c7") background (Solid("#2980b9") if planner.target == "komandan" else Solid("#2c3e50")) hover_background Solid("#3498db") padding (12, 8) xfill True

                # --- Kolom Parameter ---
                vbox:
                    spacing 15
                    xsize 450
                    
                    frame:
                        background Solid("#2f3640")
                        padding (25, 25)
                        xfill True
                        ysize 320
                        
                        vbox:
                            spacing 15
                            text "📊 PROYEKSI TAKTIS" size 22 bold True color "#e1b12c" xalign 0.5
                            
                            if planner.taktik or planner.target:
                                vbox:
                                    spacing 5
                                    text "Efektivitas Serangan:" color "#ecf0f1" size 16
                                    bar value planner.effectiveness range 100 left_bar Solid("#2ecc71") right_bar Solid("#1e272e") ysize 12 xfill True
                                    
                                vbox:
                                    spacing 5
                                    text "Tingkat Kehormatan:" color "#ecf0f1" size 16
                                    bar value planner.honor range 100 left_bar Solid("#3498db") right_bar Solid("#1e272e") ysize 12 xfill True
                                    
                                vbox:
                                    spacing 5
                                    text "Risiko Pasukan:" color "#ecf0f1" size 16
                                    bar value planner.risk range 100 left_bar Solid("#e74c3c") right_bar Solid("#1e272e") ysize 12 xfill True
                                
                                null height 10
                                text ("Dampak Politis: " + ("Siasat Licin" if planner.choice_id == "A" else "Mediasi Terukur" if planner.choice_id == "B" else "Konfrontasi Keras")) size 18 italic True color "#95a5a6" xalign 0.5
                            else:
                                text "Pilih metode pengusiran dan target operasi untuk melihat proyeksi taktis." size 16 color "#7f8c8d" xalign 0.5 text_align 0.5 yalign 0.5
                                
            # --- Konfirmasi Action ---
            if planner.is_ready():
                textbutton "✓ KUNCI STRATEGI & SERANG":
                    action [Return(planner)]
                    xalign 0.5
                    text_size 24
                    text_bold True
                    background Solid("#27ae60")
                    hover_background Solid("#2ecc71")
                    text_color "#ffffff"
                    padding (25, 12)

label scene_d12:
    scene blackscreen with fade
    scene tartar:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator " Siasat mengusir Tartar."
    # TODO: Ganti musik placeholder dengan aset BGM-06
    scene tartar1:
        xysize(1920,1080)
    with fade

    $ add_journal("D12", "Rapat malam di Trowulan membuka fase baru: mengusir Tartar dengan cara yang dipilih sendiri.")

    narrator "Rapat malam di Trowulan. Pasukan Tartar sedang merayakan jatuhnya Kediri. Sekarang adalah waktu yang tepat untuk mengusir mereka sebelum mereka menyadari niat kita."
    
    call screen d12_minigame_wargame
    
    $ d12_wargame_result = _return
    $ d12_choice = d12_wargame_result.choice_id
    
    if d12_wargame_result.choice_id == "A":
        $ siasat += 1
        $ kehormatan -= 10
        $ kebijakan += 20
        $ add_journal("D12", "Kamu memilih jamuan palsu dan melengahkan lawan dengan tipu daya.")
        narrator "Kamu menggunakan jamuan palsu untuk melengahkan mereka. Sangat efektif—tapi meninggalkan rasa pahit dan noda pada kehormatan ksatria."
    elif d12_wargame_result.choice_id == "B":
        $ mediasi += 1
        $ kehormatan += 10
        $ loyalitas_sora += 15
        $ add_journal("D12", "Kamu mendelegasikan pengepungan dan mempercayai sistem komando.")
        narrator "Kamu mendelegasikan pengepungan dengan rapi, mengatur ritme tempur. Kepercayaanmu pada Lembu Sora dan sistem komando terbukti."
    elif d12_wargame_result.choice_id == "C":
        $ konfrontasi += 1
        $ keberanian += 25
        $ kehormatan += 20
        $ kebijakan -= 15
        $ add_journal("D12", "Kamu menyerbu langsung dan menjadikan namamu legenda di garis depan.")
        narrator "Kamu menyerbu dengan gagah berani. Namamu melegenda menerjang pertahanan musuh—meski risiko pasukannya sangat tinggi."

    return

label scene_d13:
    scene blackscreen with fade
    scene kerajaan:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-14 (Trowulan - Istana Majapahit)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Tartar terusir. Majapahit merdeka."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Kertarajasa dinobatkan. Di sisi raja: Nambi. Kamu menyaksikan dari barisan belakang."
    $ add_journal("D13", "Majapahit dinobatkan, tetapi kamu berdiri di barisan belakang saat nama-nama baru naik ke dekat raja.")
    scene sedih:
        xysize(1920,1080)
    with fade
    ranggalawe "Aku membantu mendirikan ini... tapi ruang di sisi raja terasa bukan untukku."
    return

label scene_d14:
    scene blackscreen with fade
    scene kerajaan1:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-15 (Trowulan - Balai Sidang)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Konsekuensi cara mengusir Tartar."
    $ add_journal("D14", "Istana memberi penilaian atas caramu mengusir Tartar, dan penilaian itu tidak sepenuhnya hangat.")

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

    $ add_journal("D14", "Kemenangan di lapangan tidak menghapus jarak politik yang mulai terbuka di istana.")

    return
