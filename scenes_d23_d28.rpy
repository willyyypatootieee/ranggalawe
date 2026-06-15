# ==========================================
# BABAK IV - FALLING ACTION
# ==========================================

init python:
    class D23TempoPlanner:
        def __init__(self):
            self.tempo = None
            self.intent = ""

        def choose(self, tempo):
            self.tempo = tempo
            if tempo == "cepat":
                self.intent = "Dorong musuh sebelum mereka sempat mengatur ulang."
            elif tempo == "stabil":
                self.intent = "Jaga garis dan paksa mereka masuk ke posisi buruk."
            else:
                self.intent = "Pancing mereka bergerak lalu serang dari sudut yang lebih aman."

        def is_ready(self):
            return self.tempo is not None


screen d23_tempo_choice():
    modal True
    add "#000000dd"

    default planner = D23TempoPlanner()

    frame:
        align (0.5, 0.5)
        xysize (860, 420)
        background Solid("#16202bcc")
        padding (28, 24)

        vbox:
            spacing 14
            text "FASE TEMPO" size 30 bold True color "#f39c12" xalign 0.5
            text "Sebelum perang pecah penuh, pilih ritme awal agar pasukan tidak bergerak buta." size 16 color "#c7d0d9" xalign 0.5
            add Solid("#f39c12") xsize 700 ysize 2 xalign 0.5

            hbox:
                spacing 12
                xalign 0.5
                textbutton "Cepat" action Function(planner.choose, "cepat") text_size 18 text_bold True text_color "#fff" background Solid("#8e4b16") hover_background Solid("#b1601f") padding (18, 10)
                textbutton "Stabil" action Function(planner.choose, "stabil") text_size 18 text_bold True text_color "#fff" background Solid("#23405d") hover_background Solid("#335b83") padding (18, 10)
                textbutton "Umpan" action Function(planner.choose, "umpan") text_size 18 text_bold True text_color "#fff" background Solid("#3f4a22") hover_background Solid("#5a6b31") padding (18, 10)

            frame:
                background Solid("#0c1218cc")
                xfill True
                padding (18, 14)
                vbox:
                    spacing 6
                    text "Pilihanmu akan mengubah pembacaan awal pertempuran." size 15 color "#95a5a6"
                    if planner.tempo:
                        text planner.intent size 16 color "#ecf0f1"

            if planner.is_ready():
                textbutton "KUNCI TEMPO":
                    action Return(planner)
                    xalign 0.5
                    text_size 22 text_bold True text_color "#fff"
                    background Solid("#27ae60")
                    hover_background Solid("#2ecc71")
                    padding (24, 12)

init python:
    class D29LegacyCouncil:
        def __init__(self):
            self.focus = None
            self.summary = ""

        def choose(self, focus):
            self.focus = focus
            if focus == "law":
                self.summary = "Kamu menekankan hukum sebagai benteng ingatan."
            elif focus == "people":
                self.summary = "Kamu menaruh rakyat sebagai pewaris utama cerita."
            else:
                self.summary = "Kamu menyerahkan nama untuk bertahan di mulut zaman."

        def is_ready(self):
            return self.focus is not None


screen d29_legacy_council():
    modal True
    add "#000000dd"

    default council = D29LegacyCouncil()

    frame:
        align (0.5, 0.5)
        xysize (900, 440)
        background Solid("#121a22dd")
        padding (28, 24)

        vbox:
            spacing 14
            text "MAJELIS WARISAN" size 30 bold True color "#f39c12" xalign 0.5
            text "Pilih cara warisan ini akan diingat: lewat hukum, rakyat, atau nama." size 16 color "#c7d0d9" xalign 0.5
            add Solid("#f39c12") xsize 720 ysize 2 xalign 0.5

            hbox:
                spacing 12
                xalign 0.5
                textbutton "Hukum" action Function(council.choose, "law") text_size 18 text_bold True text_color "#fff" background Solid("#23405d") hover_background Solid("#335b83") padding (18, 10)
                textbutton "Rakyat" action Function(council.choose, "people") text_size 18 text_bold True text_color "#fff" background Solid("#3f4a22") hover_background Solid("#5a6b31") padding (18, 10)
                textbutton "Nama" action Function(council.choose, "name") text_size 18 text_bold True text_color "#fff" background Solid("#6b4a1a") hover_background Solid("#8c6424") padding (18, 10)

            frame:
                background Solid("#0c1218cc")
                xfill True
                padding (18, 14)
                vbox:
                    spacing 6
                    text "Pilihan ini akan menentukan penekanan epilog." size 15 color "#95a5a6"
                    if council.focus:
                        text council.summary size 16 color "#ecf0f1"

            if council.is_ready():
                textbutton "KUNCI WARISAN":
                    action Return(council)
                    xalign 0.5
                    text_size 22 text_bold True text_color "#fff"
                    background Solid("#27ae60")
                    hover_background Solid("#2ecc71")
                    padding (24, 12)

label scene_d23:
    show screen scene_header("1295 M", "Medan Perang Tuban")
    call screen chapter_activity_hub("FASE GARDA", "Cek peta, hubungan, dan jurnal sebelum garis depan pecah.")
    call screen d23_tempo_choice
    $ d23_tempo = _return.tempo
    scene blackscreen with fade
    scene expression Movie(play="video/scene1_6.webm", mute=True, size=(1920, 1080)) with fade 
    narrator "Pertempuran pecah: gelombang pertama."
    $ add_journal("D23", "Kamu memilih tempo awal pertempuran: [d23_tempo].")

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
            $ add_journal("D23", "Kamu memilih serangan balik langsung begitu gelombang pertama pecah.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Momentum awal berpihak padamu—risiko tetap tinggi."

        "Tahan di ketinggian, pilih medan. (Mediasi)":
            $ d23_choice = "B"
            $ mediasi += 1
            $ kebijakan += 20
            $ keberanian += 5
            $ add_journal("D23", "Kamu menahan medan tinggi untuk memaksa musuh masuk lebih dalam.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu membuat mereka masuk lebih dalam dari yang aman."

        "Kirim utusan negosiasi terakhir. (Mediasi)":
            $ d23_choice = "C"
            $ mediasi += 1
            $ kehormatan += 15
            $ kebijakan += 5
            $ keberanian -= 5
            $ add_journal("D23", "Kamu mengirim utusan terakhir sebagai penutup peluang damai.")
            if d04_choice == "C":
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kebo Anabrang memberi jeda satu jam—penghormatan sesama pendekar."

    return

label scene_d24:
    show screen scene_header("1295 M", "Trowulan & Tuban")
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-17 & BG-16 (Split Screen)
    # TODO: Tambahkan Voice Over (VO) narrator
    scene expression Movie(play="video/scene1_7.webm", mute=True, size=(1920, 1080)) with fade

    narrator "Di dua front sekaligus."
    $ add_journal("D24", "Pertempuran membelah fokusmu: Trowulan dan Tuban bergerak bersamaan.")
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[Medan perang] Gelombang demi gelombang datang seperti laut."
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "[[Trowulan] {a=call:show_ensik_mahapati}Mahapati{/a} menunggu laporan di ruang nyaman: 'Ranggalawe harus tidak ada lagi setelah ini.'"
    return

label scene_d25:
    show screen scene_header("1295 M", "Medan Perang Tuban")
    scene expression Movie(play="video/scene1_8.webm", mute=True, size=(1920, 1080)) with fade

    
    # TODO: Gunakan aset BG asli: BG-17 (Medan Perang Tuban)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Bertemu {a=call:show_ensik_lembu_sora}Lembu Sora{/a} di tengah pertempuran."
    $ add_journal("D25", "Kamu berhadapan dengan Lembu Sora di tengah pertempuran dan pilihanmu mulai menyempit.")

    if keris_given_sora:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Lembu Sora mengeluarkan keris titipanmu."
        lembu "Kamu mau aku kembalikan ini?"
        ranggalawe "Simpan. Sebagai pengingat."
        $ kehormatan += 5
    scene expression Movie(play="video/scene1_12.webm", mute=True, size=(1920, 1080))

    lembu "Keponakanku. Masih belum terlambat."

    menu:
        "Paman tahu aku benar. Tapi Paman tetap berdiri di sana. (Konfrontasi)":
            $ d25_choice = "A"
            $ konfrontasi += 1
            $ kehormatan += 15
            $ loyalitas_sora -= 10
            $ add_journal("D25", "Kamu menekan Lembu Sora dengan kebenaran yang menyakitkan.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kebenaranmu jujur—dan menyakiti."

        "Jika Paman bisa pastikan ini berakhir tanpa lebih banyak darah... (Mediasi)":
            $ d25_choice = "B"
            $ mediasi += 1
            $ kebijakan += 10
            $ kehormatan += 5
            $ loyalitas += 5
            $ add_journal("D25", "Kamu meminta Lembu Sora mencari jalan keluar tanpa lebih banyak darah.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Ada janji yang bahkan pamanmu tak mampu tepati."

        "Pergilah, Paman. Jangan paksa aku berhadapan denganmu. (Siasat)":
            $ d25_choice = "C"
            $ siasat += 1
            $ kehormatan += 20
            $ keberanian += 10
            $ add_journal("D25", "Kamu melindungi Lembu Sora dengan memintanya mundur."
)
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Kamu melindungi pamanmu... dengan memecahkan hatimu sendiri."

    return

label scene_d26:
    show screen scene_header("1295 M", "Sungai Tambak Beras")
    scene blackscreen with fade
    scene beridir:
        xysize(1920,1080)
    with fade
    narrator "Di tepi Sungai Tambak Beras."
    $ add_journal("D26", "Di tepi Tambak Beras, duel dan martabat menjadi satu keputusan.")
    kebo "{a=call:show_ensik_ranggalawe}Ranggalawe{/a}! Masuk ke air. Selesaikan ini seperti ksatria."

    if d04_choice == "C" and kehormatan >= 7:
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Perjanjian Diam Kebo Anabrang."
        menu:
            "Terima Perjanjian Diam (Node tersembunyi)":
                $ d26_pact = True
                $ kehormatan += 25
                $ add_journal("D26", "Kamu menerima perjanjian diam Kebo Anabrang. Duel itu menjadi lebih sunyi.")
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kebo mengusir prajurit dari tepi sungai. Duel tanpa penonton."
            "Tolak—biarkan semuanya melihat":
                $ d26_pact = False
                $ add_journal("D26", "Kamu menolak perjanjian diam dan membiarkan duel dilihat semua orang.")
                # TODO: Tambahkan Voice Over (VO) narrator
                narrator "Kamu memilih duel di mata banyak orang."
    else:
        $ d26_pact = False

    return

label scene_d27:
    show screen scene_header("1295 M", "Sungai Tambak Beras")
    scene blackscreen with fade
    # TODO: Gunakan aset BG asli: BG-19 (Sungai Tambak Beras - Senja Merah)
    # TODO: Tambahkan Voice Over (VO) narrator
    scene beridir:
        xysize(1920,1080)
    with fade
    narrator "Keputusan terakhir seorang ksatria."
    $ add_journal("D27", "Keputusan terakhir di Tambak Beras dipilih saat semua arah menutup.")

    if konfrontasi >= mediasi and konfrontasi >= siasat:
        scene teriak:
            xysize(1920,1080)
        with fade
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu berteriak: '{a=call:show_ensik_mahapati}MAHAPATI{/a}! Sejarah akan mengingatmu!'"
    elif mediasi >= konfrontasi and mediasi >= siasat:
        scene menatap:
            xysize(1920,1080)
        with fade
        # TODO: Tambahkan Voice Over (VO) narrator
        narrator "Kamu menatap Lembu Sora dari kejauhan—mengangguk tanpa kata."
    elif siasat >= konfrontasi and siasat >= mediasi:
        scene senyum:
            xysize(1920,1080)
        with fade
        narrator "Kamu tersenyum tipis—ironi yang hanya kamu pahami."
    else:
        scene beridir:
            xysize(1920,1080)
        with fade
        narrator "Kamu menatap langit. Tak ada kata yang cukup."

    menu:
        "Masuk ke air tanpa ragu. (Konfrontasi)":
            $ d27_choice = "A"
            $ konfrontasi += 1
            $ keberanian += 25
            $ kehormatan += 25
            $ add_journal("D27", "Kamu masuk ke air tanpa ragu dan memutus jalan mundur.")

        "Mundur strategis... tapi tidak ada jalan. (Mediasi)":
            $ d27_choice = "B"
            $ mediasi += 1
            $ kebijakan += 5
            $ kehormatan += 5
            $ add_journal("D27", "Kamu mencoba mundur strategis, meski ruang sudah tertutup."
)

        "Berdiri dan berseru tentang ketidakadilan, lalu melompat. (Konfrontasi)":
            $ d27_choice = "C"
            $ konfrontasi += 1
            $ kehormatan += 30
            $ keberanian += 20
            $ add_journal("D27", "Kamu berseru tentang ketidakadilan sebelum melompat ke sungai.")

        "Serahkan Surat Gelap Mahapati pada Lembu Sora. (EKSKLUSIF)" if mahapati_letter:
            $ d27_choice = "D"
            $ mahapati_letter_given = True
            $ kehormatan += 30
            $ keberanian += 20
            $ add_journal("D27", "Kamu menyerahkan Surat Gelap Mahapati kepada Lembu Sora di ambang sungai.")
            # TODO: Tambahkan Voice Over (VO) narrator
            narrator "Warisan kebenaran ikut turun ke sungai—tapi tidak ikut tenggelam."

    return

label scene_d28:
    show screen scene_header("1295 M", "Tambak Beras")
    scene mati:
        xysize(1920,1080)
    with fade
    # TODO: Gunakan aset BG asli: BG-19 (Sungai Tambak Beras - Senja Merah)
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "SCENE D28 - {a=call:show_ensik_ranggalawe}Ranggalawe{/a} gugur di Tambak Beras (1295 M). (Bottleneck final)"
    $ add_journal("D28", "Ranggalawe gugur di Tambak Beras, dan babak perang mencapai titik paling sunyi.")
    # TODO: Tambahkan Voice Over (VO) narrator
    narrator "Dua ksatria. Satu sungai. Satu nasib."
    return
