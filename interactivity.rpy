################################################################################
## interactivity.rpy  –  Achievements, Journal, Timeline, Gallery, Map
################################################################################

################################################################################
## Achievement System
################################################################################

default achievements_earned = []

init python:
    _ach_defs = {
        "solo_warrior":   ("⚔ Ksatria Sendiri",      "Berangkat ke medan perang sendirian tanpa pasukan."),
        "army_builder":   ("🪖 Pemimpin Pasukan",      "Mengumpulkan 200 prajurit Madura sebelum bergerak."),
        "strategist":     ("🔮 Dalang Perang",         "Mendapat skor sempurna di Peta Strategi Infiltrasi."),
        "victory_first":  ("🏆 Penakluk Kediri",       "Menyaksikan jatuhnya Kediri dan lahirnya Majapahit."),
        "loyal_uncle":    ("❤ Paman Setia",            "Loyalitas Lembu Sora mencapai 50."),
        "people_king":    ("🏘 Suara Rakyat",           "Rakyat Tuban berdiri bersamamu tanpa diminta."),
        "perfect_form":   ("⚔ Formasi Sempurna",       "Memenangkan pertahanan Tuban dengan formasi optimal."),
        "letter_found":   ("📜 Bukti Terungkap",        "Mendapatkan Surat Gelap Mahapati di sidang Trowulan."),
        "keris_given":    ("🗡 Keris untuk Sora",       "Menitipkan keris pusaka kepada Lembu Sora."),
        "spy_turned":     ("🔄 Mata-Mata Berbalik",     "Mengampuni dan menarik Ra Galatik ke pihakmu."),
    }

    def unlock_achievement(key):
        if key not in store.achievements_earned:
            store.achievements_earned.append(key)
            if key in _ach_defs:
                name, desc = _ach_defs[key]
                renpy.show_screen("achievement_popup", name=name, desc=desc)

screen achievement_popup(name, desc):
    zorder 500
    timer 3.5 action Hide("achievement_popup")
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -12
        yoffset 12
        background Solid("#0d1117ee")
        padding (16, 12)
        at _ach_popup_anim
        vbox:
            spacing 4
            text "🏅 PRESTASI TERBUKA!" size 13 bold True color "#f39c12"
            text name size 16 bold True color "#ffffff"
            text desc size 13 color "#95a5a6"

screen kodeks():
    tag menu
    modal True
    add Solid("#0a0f14")
    vbox:
        xalign 0.5 yalign 0.5 spacing 20
        at float_in
        text "🏅 KODEKS PRESTASI":
            size 44 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 600 ysize 2 xalign 0.5
        frame:
            background Solid("#12161c")
            xsize 780 xalign 0.5 padding (24,18)
            viewport:
                yinitial 0.0 scrollbars "vertical" mousewheel True xsize 740 ysize 400
                vbox:
                    spacing 8
                    for key, (name, desc) in _ach_defs.items():
                        $ earned = key in achievements_earned
                        frame:
                            background (Solid("#1a2530") if earned else Solid("#0d1117"))
                            xfill True padding (14, 10)
                            hbox:
                                spacing 14
                                text ("🏅" if earned else "🔒"):
                                    size 24 yalign 0.5
                                vbox:
                                    text name:
                                        size 18 bold True
                                        color ("#f39c12" if earned else "#444")
                                    text (desc if earned else "???"):
                                        size 14
                                        color ("#bdc3c7" if earned else "#333")
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Journal System
################################################################################

default journal_entries = []

init python:
    def add_journal(scene_label, text):
        store.journal_entries.append((scene_label, text))

screen journal():
    tag menu
    modal True
    add Solid("#0a0f14")
    vbox:
        xalign 0.5 yalign 0.5 spacing 20
        at float_in
        text "📖 JURNAL RANGGALAWE":
            size 42 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 600 ysize 2 xalign 0.5
        frame:
            background Solid("#12161c") xsize 780 xalign 0.5 padding (24, 18)
            if not journal_entries:
                text "Belum ada catatan." size 18 color "#7f8c8d" xalign 0.5 yalign 0.5
            else:
                viewport:
                    yinitial 1.0 scrollbars "vertical" mousewheel True xsize 740 ysize 400
                    vbox:
                        spacing 14
                        for scene_lbl, entry in journal_entries:
                            frame:
                                background Solid("#0d1117") xfill True padding (14, 12)
                                vbox:
                                    spacing 4
                                    text scene_lbl:
                                        size 13 italic True color "#7f8c8d"
                                    text entry:
                                        size 16 color "#bdc3c7"
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Timeline Screen  (uses renpy.seen_label – no tracking needed)
################################################################################

init python:
    _timeline_scenes = [
        ("D01","Kabar ke Sumenep"),    ("D02","Dua Dunia"),
        ("D03","Nama Baru"),           ("D04","Malam di Tarik"),
        ("D05","Siasat Masuk Kediri"), ("D06","Sarang Musuh"),
        ("D07","Sub-Arc Madura"),      ("D08","Manfaatkan Tartar"),
        ("D09","Persiapan Perang"),    ("D10","Jongbiru"),
        ("D11","Kediri Jatuh"),        ("D12","Usir Tartar"),
        ("D13","Majapahit Merdeka"),   ("D14","Konsekuensi"),
        ("D15","Adipati Tuban"),       ("D16","Nambi Diangkat"),
        ("D17","Api dalam Dada"),      ("D18","Malam Membelah"),
        ("D19","Ultimatum"),           ("D20","Tak Bisa Dihindari"),
        ("D21","Strategi Tuban"),      ("D22","Wajah di Garis Musuh"),
        ("D23","D23"),                 ("D24","D24"),
        ("D25","D25"),                 ("D26","D26"),
        ("D27","D27"),                 ("D28","D28"),
        ("D29","D29"),                 ("D30","D30"),
        ("D31","D31"),                 ("D32","D32"),
        ("D33","D33"),                 ("D34","D34"),
        ("D35","D35"),
    ]

screen timeline():
    tag menu
    modal True
    add Solid("#0a0f14")
    vbox:
        xalign 0.5 yalign 0.5 spacing 20
        at float_in
        text "📅 PERJALANAN WAKTU":
            size 42 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 600 ysize 2 xalign 0.5
        frame:
            background Solid("#12161c") xsize 900 xalign 0.5 padding (20, 16)
            viewport:
                xsize 860 ysize 420
                scrollbars "vertical" mousewheel True draggable True
                grid 5 7:
                    spacing 8
                    for sid, stitle in _timeline_scenes:
                        $ lbl = "scene_" + sid.lower()
                        $ seen = renpy.seen_label(lbl)
                        frame:
                            background (Solid("#1a3a50") if seen else Solid("#111"))
                            xysize (156, 54) padding (8, 6)
                            vbox:
                                spacing 2
                                text sid:
                                    size 13 bold True
                                    color ("#f39c12" if seen else "#333")
                                text (stitle if seen else "???"):
                                    size 11
                                    color ("#bdc3c7" if seen else "#222")
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Gallery  (scenes seen, using renpy.seen_label)
################################################################################

screen gallery():
    tag menu
    modal True
    add Solid("#0a0f14")
    vbox:
        xalign 0.5 yalign 0.5 spacing 20
        at float_in
        text "🎬 GALERI ADEGAN":
            size 42 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 600 ysize 2 xalign 0.5
        $ total   = len(_timeline_scenes)
        $ seen_ct = sum(1 for sid, _ in _timeline_scenes if renpy.seen_label("scene_" + sid.lower()))
        text ("[seen_ct] / [total] adegan terbuka"):
            size 18 color "#7f8c8d" xalign 0.5
        frame:
            background Solid("#12161c") xsize 780 xalign 0.5 padding (18, 14)
            bar value seen_ct range total:
                xsize 700 ysize 12 xalign 0.5
                left_bar Solid("#f39c12") right_bar Solid("#1e1e2e")
        frame:
            background Solid("#12161c") xsize 780 xalign 0.5 padding (18, 14)
            viewport:
                xsize 740 ysize 360 scrollbars "vertical" mousewheel True
                vbox:
                    spacing 6
                    for sid, stitle in _timeline_scenes:
                        $ lbl = "scene_" + sid.lower()
                        $ s = renpy.seen_label(lbl)
                        frame:
                            background (Solid("#1a2530") if s else Solid("#0d1117"))
                            xfill True padding (12, 8)
                            hbox:
                                spacing 14
                                text ("✅" if s else "🔒") size 20 yalign 0.5
                                text ("%s — %s" % (sid, stitle)):
                                    size 16 yalign 0.5
                                    color ("#ecf0f1" if s else "#333")
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Interactive Map of Java
################################################################################

init python:
    import pygame as _pg
    import math as _math

    class JavaMap(_pg.Surface if False else renpy.Displayable):
        _java = [
            (30,175),(75,135),(130,105),(195,90),(265,82),(340,76),
            (415,72),(490,68),(555,65),(615,62),(660,60),(700,65),
            (735,82),(760,108),(768,138),(758,165),(738,183),(705,198),
            (668,208),(625,214),(575,218),(515,220),(450,221),(385,218),
            (315,214),(245,208),(175,203),(110,200),(58,196),(25,190),
        ]
        _madura = [
            (625,52),(650,40),(685,38),(715,44),(735,58),
            (725,72),(698,78),(668,72),(640,60),
        ]
        _locs = [
            (695,48,"Sumenep","#f1c40f","sumenep"),
            (415,62,"Tuban","#3498db","tuban"),
            (310,140,"Kediri","#e74c3c","kediri"),
            (490,118,"Trowulan","#f39c12","trowulan"),
            (505,112,"Hutan Tarik","#2ecc71","hutan_tarik"),
        ]
        _chapter_highlights = {
            1: {"sumenep","hutan_tarik"},
            2: {"kediri","hutan_tarik"},
            3: {"trowulan","tuban","kediri"},
        }

        def __init__(self, chapter=1):
            super(JavaMap, self).__init__()
            self.chapter = chapter

        def render(self, width, height, st, at):
            W, H = 800, 280
            r    = renpy.Render(width, height)
            canvas = r.canvas()

            # Offsets for centering
            ox = (width - W) // 2
            oy = (height - H) // 2

            # Ocean
            canvas.rect((10, 22, 50, 255), (ox, oy, W, H))

            # Java land (offset points)
            java_pts = [(x + ox, y + oy) for x, y in self._java]
            canvas.polygon((28, 55, 35), java_pts)
            canvas.polygon((46, 90, 55), java_pts, 2)
            
            # Madura (offset points)
            madura_pts = [(x + ox, y + oy) for x, y in self._madura]
            canvas.polygon((28, 55, 35), madura_pts)
            canvas.polygon((46, 90, 55), madura_pts, 2)

            highlighted = self._chapter_highlights.get(self.chapter, set())

            import renpy.text.text as rt
            for lx, ly, name, color, key in self._locs:
                active = key in highlighted
                c = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
                alpha = 255 if active else 100
                radius = 9 if active else 5
                
                screen_x = lx + ox
                screen_y = ly + oy

                # Glow
                if active:
                    # simplified glow via multiple circles
                    canvas.circle(c + (40,), (screen_x, screen_y), radius*2)
                    canvas.circle(c + (60,), (screen_x, screen_y), int(radius*1.5))
                
                canvas.circle(c + (alpha,), (screen_x, screen_y), radius)
                canvas.circle((255, 255, 255, 180), (screen_x, screen_y), radius, 1)

                # Label
                text_color = color if active else "#969696"
                text_d = rt.Text(name, size=14, color=text_color)
                tr = renpy.render(text_d, width, height, st, at)
                r.subpixel_blit(tr, (screen_x + radius + 3, screen_y - 8))

            return r

        def visit(self):
            return []

screen peta():
    tag menu
    modal True
    add Solid("#080f1e")
    vbox:
        xalign 0.5 yalign 0.5 spacing 20
        at float_in
        text "🗺️ PETA JAWA — 1292–1295 M":
            size 40 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 600 ysize 2 xalign 0.5
        frame:
            background Solid("#0a1628") xysize (820, 300) xalign 0.5
            add JavaMap(chapter=current_chapter)
        frame:
            background Solid("#12161c") xsize 820 xalign 0.5 padding (18, 12)
            hbox:
                spacing 28 xalign 0.5
                text "🟡 Sumenep" size 15 color "#f1c40f"
                text "🔵 Tuban" size 15 color "#3498db"
                text "🔴 Kediri" size 15 color "#e74c3c"
                text "🟠 Trowulan" size 15 color "#f39c12"
                text "🟢 Hutan Tarik" size 15 color "#2ecc71"
                text "● = Lokasi aktif babak ini" size 13 italic True color "#7f8c8d"
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)
