################################################################################
## visual_polish.rpy  –  Radar Chart, Parallax, Loading Tips, Dynamic Endings
################################################################################

################################################################################
## Stat Radar / Spider Chart
################################################################################

init python:
    import pygame as _pg_vp
    import math   as _math_vp

    class RadarChart(renpy.Displayable):
        def __init__(self, stats, colors, size=280):
            super(RadarChart, self).__init__()
            self.stats  = stats   # list of (label, value, max)
            self.colors = colors  # list of hex color strings matching stats
            self.size   = size

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            canvas = r.canvas()

            cx = width // 2
            cy = height // 2
            n  = len(self.stats)
            R  = self.size // 2 - 36

            def polar(angle, radius):
                a = _math_vp.pi / 2 - 2 * _math_vp.pi * angle / n
                return (cx + radius * _math_vp.cos(a),
                        cy - radius * _math_vp.sin(a))

            # Grid rings
            for lvl in [0.25, 0.5, 0.75, 1.0]:
                pts = [polar(i, R * lvl) for i in range(n)]
                canvas.polygon((255,255,255,18), pts, 1)

            # Axes
            for i in range(n):
                canvas.line((255,255,255,35), (cx, cy), polar(i, R), 1)

            # Data polygon
            data_pts = []
            for i, (_, val, mx) in enumerate(self.stats):
                frac = min(val, mx) / mx if mx else 0
                data_pts.append(polar(i, R * frac))

            if len(data_pts) >= 3:
                canvas.polygon((241,196,15,55), data_pts)
                canvas.polygon((241,196,15,200), data_pts, 2)

            # Dots + labels
            import renpy.text.text as rt
            for i, (lbl, val, mx) in enumerate(self.stats):
                frac = min(val, mx) / mx if mx else 0
                px, py = polar(i, R * frac)
                canvas.circle((241,196,15,255), (px, py), 5)
                # Axis label
                lx, ly = polar(i, R + 22)
                
                text_d = rt.Text(lbl, size=14, color="#b4b4b4")
                tr = renpy.render(text_d, width, height, st, at)
                tw, th = tr.get_size()
                r.subpixel_blit(tr, (lx - tw/2.0, ly - th/2.0))

            return r

        def visit(self):
            return []

screen radar_chart():
    tag menu
    modal True
    add Solid("#0a0f14")
    vbox:
        xalign 0.5 yalign 0.5 spacing 22
        at float_in
        text "📊 KOMPAS KSATRIA":
            size 42 bold True color "#f39c12" xalign 0.5
        add Solid("#f39c12") xsize 500 ysize 2 xalign 0.5
        frame:
            background Solid("#12161c")
            xysize (340, 340) xalign 0.5
            add RadarChart(
                stats=[
                    ("Keberanian", keberanian,  80),
                    ("Kebijakan",  kebijakan,   80),
                    ("Kehormatan", kehormatan,  80),
                    ("Loyalitas",  loyalitas,   80),
                    ("Kemarahan",  kemarahan,   80),
                ],
                colors=["#e74c3c","#3498db","#2ecc71","#e84393","#f39c12"]
            )
        textbutton "Tutup":
            action Return() xalign 0.5
            text_size 20 text_bold True text_color "#fff"
            background Solid("#333") hover_background Solid("#555")
            padding (28, 10)


################################################################################
## Main Menu Parallax Transform
################################################################################

init python:
    def _parallax_func(tr, st, at):
        try:
            mx, my = renpy.get_mouse_pos()
            sw = renpy.config.screen_width
            sh = renpy.config.screen_height
            nx = (mx / sw - 0.5)
            ny = (my / sh - 0.5)
            tr.zoom    = 1.06
            tr.xoffset = -nx * 18
            tr.yoffset = -ny * 10
        except Exception:
            pass
        return tr, 0.033

transform main_menu_parallax:
    function _parallax_func


################################################################################
## Historical Loading Tips
################################################################################

init python:
    _loading_tips = [
        "Ranggalawe adalah nama gelar; nama aslinya adalah Ken Kara, putra Arya Wiraraja.",
        "Majapahit didirikan tahun 1293 M di tepi Sungai Brantas, Trowulan.",
        "Pararaton ('Kitab Para Raja') adalah sumber utama kisah Ranggalawe.",
        "Lembu Sora adalah paman Ranggalawe dan salah satu prajurit paling setia Raden Wijaya.",
        "Pasukan Mongol Kubilai Khan mendarat di Jawa 1293 M — justru dimanfaatkan Raden Wijaya.",
        "Nambi kelak menjadi Rakryan Patih Amangkubumi pertama Majapahit.",
        "Arya Wiraraja mengirim dua surat sekaligus — kepada Raden Wijaya dan kepada Jayakatwang.",
        "Mahapati (Halayudha) tercatat dalam Pararaton sebagai dalang fitnah di balik pemberontakan.",
        "Kebo Anabrang adalah panglima Majapahit yang kelak memimpin tentara menekan Ranggalawe.",
        "Kata 'Lawe' dalam Ranggalawe berarti benang — ia yang merajut dan mengikat pasukan.",
        "Kidung Ranggalawe & Kidung Sorandaka adalah karya sastra yang mengabadikan kisah ini.",
        "Tuban adalah kadipaten pesisir utara Jawa — pusat perdagangan dan kekuatan Ranggalawe.",
    ]
    import random as _rnd

screen loading_tip():
    zorder 300
    modal True
    timer 3.0 action Return()

    add Solid("#000000")
    vbox:
        xalign 0.5 yalign 0.5 spacing 24
        at float_in
        text "📜":
            size 48 xalign 0.5
        add Solid("#f39c1244") xsize 400 ysize 1 xalign 0.5
        text _rnd.choice(_loading_tips):
            size 22 italic True color "#bdc3c7"
            xalign 0.5 text_align 0.5 xmaximum 700
        add Solid("#f39c1244") xsize 400 ysize 1 xalign 0.5
        text "— Fakta Sejarah —":
            size 15 color "#7f8c8d" xalign 0.5 italic True


################################################################################
## Dynamic Ending System
################################################################################

init python:
    _ending_defs = {
        "ksatria_jatuh": (
            "AKHIR: KSATRIA YANG JATUH BERDIRI",
            "Ranggalawe memilih kehormatan di atas segalanya. Ia gugur, tapi namanya tidak.",
            "#e74c3c",
        ),
        "diplomat_kesepian": (
            "AKHIR: JURU DAMAI YANG KESEPIAN",
            "Kamu mencoba menjembatani semuanya. Tapi ada kalanya jembatan itu hanya bisa dilewati sendirian.",
            "#3498db",
        ),
        "dalang_tersembunyi": (
            "AKHIR: DALANG DI BALIK LAYAR",
            "Mahapati mengira ia menang. Kamu tahu sebaliknya — dan sejarah juga.",
            "#9b59b6",
        ),
        "korban_intrik": (
            "AKHIR: KORBAN INTRIK ISTANA",
            "Kerajaan yang kamu bantu dirikan adalah kerajaan yang menghancurkanmu.",
            "#7f8c8d",
        ),
        "prajurit_setia": (
            "AKHIR: PRAJURIT HINGGA HEMBUSAN TERAKHIR",
            "Kamu berjuang. Kamu tidak menyesal. Itu cukup.",
            "#f39c12",
        ),
        "rakyat_dikenang": (
            "AKHIR: DIKENANG RAKYAT",
            "Raja tidak mengingatmu. Tapi rakyat Tuban menyebut namamu dalam doa.",
            "#2ecc71",
        ),
    }

    def get_ending_key():
        if store.konfrontasi >= store.mediasi and store.konfrontasi >= store.siasat:
            return "ksatria_jatuh" if store.kehormatan >= 40 else "prajurit_setia"
        elif store.mediasi >= store.konfrontasi and store.mediasi >= store.siasat:
            return "rakyat_dikenang" if store.rakyat_loyal else "diplomat_kesepian"
        else:
            return "dalang_tersembunyi" if store.mahapati_misinformed else "korban_intrik"

screen dynamic_ending():
    modal True
    zorder 350

    $ ekey   = get_ending_key()
    $ etitle, edesc, ecolor = _ending_defs.get(ekey, _ending_defs["korban_intrik"])

    add Solid("#000000")
    vbox:
        xalign 0.5 yalign 0.5 spacing 24
        at float_in

        text etitle:
            size 46 bold True color ecolor xalign 0.5
            outlines [(3, "#000000", 0, 0)]
        add Solid(ecolor) xsize 600 ysize 2 xalign 0.5

        text edesc:
            size 26 italic True color "#bdc3c7"
            xalign 0.5 text_align 0.5 xmaximum 800

        null height 20
        textbutton "Teruskan →":
            action Return() xalign 0.5
            text_size 22 text_bold True text_color "#fff"
            background Solid("#1a1a1a")
            hover_background Solid(ecolor)
            padding (30, 12)
