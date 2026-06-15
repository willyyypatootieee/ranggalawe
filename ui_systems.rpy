################################################################################
## ui_systems.rpy  –  Relationship Tracker, Kamus, Date Stamps, Timed Choice
################################################################################

# ── Chapter / Scene Progress Tracking ─────────────────────────────────────────
default current_chapter = 1
default current_chapter_name = "Lahirnya Seorang Ksatria"


################################################################################
## Relationship Tracker
################################################################################

screen relationship_tracker():
    tag menu
    modal True
    add Solid("#0a0f14")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22

        at float_in

        text "HUBUNGAN & LOYALITAS":
            size 44 bold True color "#f39c12" xalign 0.5
            outlines [(3, "#000000", 0, 0)]

        add Solid("#f39c12") xsize 680 ysize 2 xalign 0.5

        # ── Character relationships ────────────────────────────────────────
        frame:
            background Solid("#12161c")
            padding (30, 22)
            xsize 720
            xalign 0.5
            vbox:
                spacing 16

                text "Karakter Utama:" bold True color "#bdc3c7" size 17

                hbox:
                    spacing 14
                    xminimum 720
                    text "❤  Lembu Sora    " size 16 color "#e84393" yalign 0.5 xminimum 220
                    bar value loyalitas_sora range 100:
                        xsize 340 ysize 14
                        left_bar Solid("#e84393")
                        right_bar Solid("#1e1e2e")
                    text "[loyalitas_sora]" size 15 color "#e84393" yalign 0.5

                hbox:
                    spacing 14
                    xminimum 720
                    text "⚔  Pasukan Madura " size 16 color "#e74c3c" yalign 0.5 xminimum 220
                    bar value loyalitas_prajurit range 100:
                        xsize 340 ysize 14
                        left_bar Solid("#e74c3c")
                        right_bar Solid("#1e1e2e")
                    text "[loyalitas_prajurit]" size 15 color "#e74c3c" yalign 0.5

                hbox:
                    spacing 14
                    xminimum 720
                    text "🏘  Rakyat Tuban   " size 16 color "#2ecc71" yalign 0.5 xminimum 220
                    bar value loyalitas_rakyat range 100:
                        xsize 340 ysize 14
                        left_bar Solid("#2ecc71")
                        right_bar Solid("#1e1e2e")
                    text "[loyalitas_rakyat]" size 15 color "#2ecc71" yalign 0.5

                hbox:
                    spacing 14
                    xminimum 720
                    text "👑  Raden Wijaya   " size 16 color "#f1c40f" yalign 0.5 xminimum 220
                    bar value loyalitas range 100:
                        xsize 340 ysize 14
                        left_bar Solid("#f1c40f")
                        right_bar Solid("#1e1e2e")
                    text "[loyalitas]" size 15 color "#f1c40f" yalign 0.5

        # ── Style meter ────────────────────────────────────────────────────
        frame:
            background Solid("#0d1117")
            padding (30, 16)
            xsize 720
            xalign 0.5
            vbox:
                spacing 10
                text "Gaya Kepemimpinan:" bold True color "#bdc3c7" size 17
                hbox:
                    spacing 30 xalign 0.5
                    vbox:
                        text "⚔" size 28 xalign 0.5 color "#e74c3c"
                        text "Konfrontasi" size 13 color "#95a5a6" xalign 0.5
                        text "[konfrontasi]" size 32 bold True color "#e74c3c" xalign 0.5
                    vbox:
                        text "🤝" size 28 xalign 0.5 color "#3498db"
                        text "Mediasi" size 13 color "#95a5a6" xalign 0.5
                        text "[mediasi]"    size 32 bold True color "#3498db" xalign 0.5
                    vbox:
                        text "🔮" size 28 xalign 0.5 color "#9b59b6"
                        text "Siasat" size 13 color "#95a5a6" xalign 0.5
                        text "[siasat]"     size 32 bold True color "#9b59b6" xalign 0.5

        textbutton "Tutup":
            action Return()
            xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333")
            hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Kamus / Historical Glossary
################################################################################

init python:
    kamus_entries = [
        ("Adipati",          "Penguasa daerah setara gubernur, biasanya ditunjuk oleh raja."),
        ("Amangkubumi",      "Gelar Mahapatih / perdana menteri tertinggi kerajaan Majapahit."),
        ("Bhayangkara",      "Pasukan pengawal pribadi raja. Cikal-bakal konsep aparat negara."),
        ("Gajah Mada",       "Mahapatih legendaris Majapahit kelak setelah era Ranggalawe."),
        ("Jayakatwang",      "Raja Kediri yang menggulingkan Singhasari dan membunuh Kertanegara."),
        ("Kertanegara",      "Prabu Singhasari yang wafat diserang Jayakatwang, 1292 M."),
        ("Kertarajasa",      "Gelar resmi Raden Wijaya setelah dinobatkan sebagai Raja Majapahit."),
        ("Kidung",           "Karya sastra puisi tradisional Jawa, sering merekam sejarah."),
        ("Ksatria",          "Kasta prajurit / bangsawan. Wajib menjunjung kode etik kehormatan."),
        ("Majapahit",        "Kerajaan besar Jawa (1293–~1527 M), didirikan Raden Wijaya di Trowulan."),
        ("Pararaton",        "'Kitab Para Raja' — kronik historis utama tentang Singhasari & Majapahit."),
        ("Patih",            "Pejabat tinggi kerajaan, setara menteri. Di bawah Mahapatih."),
        ("Pendopo",          "Bangunan pertemuan terbuka, tanpa dinding, khas arsitektur Jawa."),
        ("Prasasti Sima",    "Piagam batu yang memberikan hak otonomi pajak pada suatu wilayah."),
        ("Rakryan",          "Gelar pejabat tinggi istana Majapahit, di bawah raja langsung."),
        ("Ranggalawe",       "Nama gelar Ken Kara; 'Rangga' (pejabat militer) + 'Lawe' (benang/pengikat)."),
        ("Singhasari",       "Kerajaan Jawa Timur sebelum Majapahit, berpusat di Malang."),
        ("Sira",             "Kata ganti orang kedua hormat dalam bahasa Jawa Kuno."),
        ("Tartar / Mongol",  "Pasukan Kubilai Khan yang mendarat di Jawa 1293 M untuk menghukum Kertanegara."),
        ("Trowulan",         "Ibukota Majapahit, kini situs arkeologi di Mojokerto, Jawa Timur."),
        ("Wiraraja",         "Arya Wiraraja — Adipati Sumenep, ayah Ranggalawe, ahli strategi politik."),
    ]

screen kamus():
    tag menu
    modal True
    add Solid("#0a0f14")

    default search = ""
    default scroll_pos = 0.0

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 0

        at float_in

        # Header
        frame:
            background Solid("#12161c")
            xsize 860
            xalign 0.5
            padding (28, 18)
            vbox:
                spacing 10
                text "📖 KAMUS SEJARAH":
                    size 38 bold True color "#f39c12" xalign 0.5
                text "Istilah Jawa Kuno & Historis":
                    size 18 italic True color "#7f8c8d" xalign 0.5

        # Entries
        frame:
            background Solid("#0d1117")
            xsize 860
            xalign 0.5
            ysize 460
            padding (0, 0)
            viewport:
                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                xsize 860
                vbox:
                    spacing 0
                    for term, meaning in kamus_entries:
                        frame:
                            background Solid("#12161c")
                            xfill True
                            padding (24, 14)
                            vbox:
                                spacing 4
                                text term:
                                    size 20 bold True color "#f39c12"
                                text meaning:
                                    size 16 color "#bdc3c7"
                        frame:
                            background Solid("#1e2530")
                            xfill True
                            ysize 1
                            padding (0, 0)

        # Footer
        frame:
            background Solid("#12161c")
            xsize 860
            xalign 0.5
            padding (20, 14)
            textbutton "Tutup":
                action Return()
                xalign 0.5
                text_size 20 text_bold True text_color "#fff"
                background Solid("#333")
                hover_background Solid("#555")
                padding (28, 10)


################################################################################
## Scene Date / Location Header Stamp
## Usage: show screen scene_header("1292 M", "Sumenep, Madura")
################################################################################

screen scene_header(date_text, location_text=""):
    zorder 200
    timer 2.8 action Hide("scene_header")

    frame:
        xalign 0.5
        yalign 0.0
        yoffset 8
        background Solid("#0a0f14cc")
        padding (22, 10)

        at _header_stamp_anim

        hbox:
            spacing 18
            text date_text:
                size 20 color "#f39c12" italic True yalign 0.5
            text "—":
                size 20 color "#444" yalign 0.5
            text location_text:
                size 20 color "#bdc3c7" yalign 0.5


################################################################################
## Chapter Activity Hub
## Use for preparation / council scenes before major decisions.
################################################################################

screen chapter_activity_hub(title, subtitle=""):
    modal True
    zorder 180
    add Solid("#081019e8")

    frame:
        align (0.5, 0.5)
        xysize (920, 520)
        background Solid("#111820")
        padding (32, 24)

        vbox:
            spacing 18
            xfill True

            text title:
                size 34 bold True color "#f39c12" xalign 0.5 outlines [(2, "#000000", 0, 0)]
            if subtitle:
                text subtitle:
                    size 16 italic True color "#95a5a6" xalign 0.5

            add Solid("#f39c12") xsize 760 ysize 2 xalign 0.5

            text "Gunakan fase ini untuk memeriksa peta, hubungan, catatan, dan istilah sebelum lanjut." size 17 color "#bdc3c7" xalign 0.5

            hbox:
                spacing 14
                xalign 0.5
                textbutton "Peta" action ShowMenu('peta') text_size 20 text_bold True background Solid("#1f4d6b") hover_background Solid("#2e6f9a") text_color "#fff" padding (24, 12)
                textbutton "Relasi" action ShowMenu('relationship_tracker') text_size 20 text_bold True background Solid("#4c2a6a") hover_background Solid("#6b3b94") text_color "#fff" padding (24, 12)
                textbutton "Jurnal" action ShowMenu('journal') text_size 20 text_bold True background Solid("#3f4a22") hover_background Solid("#5a6b31") text_color "#fff" padding (24, 12)
                textbutton "Kamus" action ShowMenu('kamus') text_size 20 text_bold True background Solid("#6b4a1a") hover_background Solid("#8c6424") text_color "#fff" padding (24, 12)

            textbutton "Lanjut":
                action Return()
                xalign 0.5
                text_size 22 text_bold True text_color "#fff"
                background Solid("#333")
                hover_background Solid("#555")
                padding (34, 12)


################################################################################
## Timed Choice Screen
## Presents choices with a visible countdown. Auto-picks default if time runs out.
## Usage: call screen timed_choice(items, timeout, default_idx)
##   items      = list of (caption, return_value) tuples
##   timeout    = seconds before auto-pick
##   default_idx= index in items to pick on timeout
################################################################################

screen timed_choice(items, timeout=8.0, default_idx=0):
    modal True
    default tl = timeout

    # Count down
    timer 0.05 repeat True action SetScreenVariable("tl", max(0.0, tl - 0.05))
    # Auto-pick on expiry
    timer timeout action Return(items[default_idx][1])

    vbox:
        style_prefix "choice"
        xalign 0.5
        ypos 380
        yanchor 0.5
        spacing 12

        for i, (caption, val) in enumerate(items):
            button:
                style "choice_button"
                action Return(val)
                at choice_slide_in(i * 0.08)
                hbox:
                    spacing 12
                    yalign 0.5
                    text "›" style "choice_button_text" color "#f39c12" size 28 yalign 0.5
                    text caption style "choice_button_text" yalign 0.5

    # Countdown bar + label
    frame:
        xalign 0.5
        yalign 0.88
        background Solid("#0a0f14bb")
        padding (20, 10)
        vbox:
            spacing 6
            text ("⏱ " + str(int(tl) + 1) + " detik"):
                size 18 color ("#e74c3c" if tl < 3.0 else "#f39c12") xalign 0.5 bold True
            bar value tl range timeout:
                xsize 600 ysize 10
                left_bar  Solid("#f39c12" if tl > 3.0 else "#e74c3c")
                right_bar Solid("#1e1e2e")
