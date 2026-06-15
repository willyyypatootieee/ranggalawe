################################################################################
## effects.rpy
## Cinematic ATL Transforms, Visual Effects, Custom Screens
## All reusable across the entire game.
################################################################################


################################################################################
## ATL Transforms – Character animations
################################################################################

## Shake side-to-side (anger, impact, shock)
transform shake:
    xoffset 0
    linear 0.05 xoffset -12
    linear 0.05 xoffset 12
    linear 0.05 xoffset -9
    linear 0.05 xoffset 9
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0

## Bounce up from below when entering (happy, triumphant)
transform bounce_in:
    yoffset 70 alpha 0.0
    easein 0.4 yoffset 0 alpha 1.0

## Slide in from the right edge (villain reveal, dramatic entrance)
transform slide_in_right:
    xalign 1.6 alpha 0.0
    ease 0.45 xalign 1.0 alpha 1.0

## Slide in from the left edge
transform slide_in_left:
    xalign -0.6 alpha 0.0
    ease 0.45 xalign 0.0 alpha 1.0

## Fade + slight rise (narrator thoughts, ghost memory)
transform float_in:
    yoffset 20 alpha 0.0
    ease 0.6 yoffset 0 alpha 1.0

## Subtle breathing idle (long contemplation scenes)
transform breathe:
    zoom 1.00
    ease 3.5 zoom 1.025
    ease 3.5 zoom 1.00
    repeat

## Entrance for ensiklopedia popup panel
transform enc_slide_in:
    yoffset 45 alpha 0.0
    ease 0.3 yoffset 0 alpha 1.0

## Staggered slide-in for choice buttons (takes a delay parameter)
transform choice_slide_in(delay=0.0):
    alpha 0.0 xoffset 28
    pause delay
    ease 0.22 alpha 1.0 xoffset 0

## Dialogue window slides up on first appear
transform say_window_anim:
    on show:
        yoffset 20 alpha 0.0
        ease 0.2 yoffset 0 alpha 1.0
    on hide:
        ease 0.15 alpha 0.0

## Stat gain popup – floats up then fades
transform _stat_popup_anim:
    yoffset -18 alpha 0.0
    ease 0.28 yoffset 0 alpha 1.0
    pause 1.0
    ease 0.52 yoffset -18 alpha 0.0

## Achievement popup – slides in from right then out
transform _ach_popup_anim:
    xoffset 380 alpha 0.0
    ease 0.4 xoffset 0 alpha 1.0
    pause 2.5
    ease 0.6 xoffset 380 alpha 0.0

## Choice hover hint – quick fade in
transform _hint_fade_in:
    alpha 0.0
    ease 0.15 alpha 1.0

## Flash screens – fade out from alpha
transform _flash_impact:
    alpha 0.75
    ease 0.45 alpha 0.0

transform _flash_victory:
    alpha 0.55
    ease 0.9 alpha 0.0

transform _flash_white:
    alpha 0.9
    ease 0.35 alpha 0.0

## Scene header date stamp – fade in, hold, fade out
transform _header_stamp_anim:
    alpha 0.0
    ease 0.4 alpha 1.0
    pause 1.6
    ease 0.8 alpha 0.0


################################################################################
## Custom Transition Defines
################################################################################

## Ink-wipe style (use for time skips / flashbacks once you have the image)
# define t_ink = ImageDissolve("gui/transition_ink.png", 1.2)

## Wipe transitions for battle / dramatic scene changes
define t_wipe_left   = CropMove(0.5, "wipeleft")
define t_wipe_right  = CropMove(0.5, "wiperight")
define t_dissolve_slow = Dissolve(1.2)


################################################################################
## Choice Hover Hint Helper
################################################################################

init python:
    def _choice_hint(caption):
        """Auto-detect stat impact from choice caption keywords."""
        c = caption.lower()
        parts = []
        if "konfrontasi" in c:
            parts.append("⚔2️ Keberanian ↑  🏆 Kehormatan ↑")
        if "mediasi" in c:
            parts.append("🧠 Kebijakan ↑  ❤ Loyalitas ↑")
        if "siasat" in c:
            parts.append("🔮 Siasat ↑  🧠 Kebijakan ↑")
        return "   ".join(parts)


################################################################################
## Inner-Thought Narrator – Custom Say Screen
## Use narrator_batin "..." for inner monologue / batin thoughts.
## Renders via batin_say screen instead of the standard say window.
################################################################################

transform batin_panel_appear:
    alpha 0.0 yoffset -10
    ease 0.38 alpha 1.0 yoffset 0

style batin_clear_window is default:
    background None
    padding (0, 0)
    xfill False
    yminimum 0

define narrator_batin = Character(None,
    screen       = "batin_say",
    window_style = "batin_clear_window",
    what_prefix  = "\u201c ",
    what_suffix  = " \u201d")

screen batin_say(who, what):
    frame:
        id "window"
        xalign    0.5
        yalign    0.42
        xmaximum  840
        background None
        padding   (0, 0)
        at batin_panel_appear

        text what:
            id "what"
            italic True
            color "#c4e5f8"
            size 30
            text_align 0.5
            xalign 0.5
            line_leading 6
            outlines [(2, "#000000dd", 0, 0), (1, "#000000", 1, 1)]


################################################################################
## Stats HUD – Persistent overlay (toggled via quick menu)
################################################################################

default persistent.show_hud = False

screen stats_hud():
    zorder 90
    if persistent.show_hud:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -12
            yoffset 78
            background Frame(Solid("#0d1117ee"), 6, 6)
            padding (14, 10)
            vbox:
                spacing 5
                text "📊 STATUS" size 13 bold True color "#f39c12" xalign 0.5
                null height 1
                null height 3
                text "[current_chapter_name]" size 11 italic True color "#7f8c8d" xalign 0.5
                null height 2
                hbox:
                    spacing 6
                    text "⚔" size 13 color "#e74c3c"
                    text "Keberanian " size 12 color "#95a5a6" xminimum 85
                    text "[keberanian]" size 12 bold True color "#e74c3c"
                hbox:
                    spacing 6
                    text "🧠" size 13 color "#3498db"
                    text "Kebijakan  " size 12 color "#95a5a6" xminimum 85
                    text "[kebijakan]"  size 12 bold True color "#3498db"
                hbox:
                    spacing 6
                    text "🏆" size 13 color "#2ecc71"
                    text "Kehormatan " size 12 color "#95a5a6" xminimum 85
                    text "[kehormatan]" size 12 bold True color "#2ecc71"
                hbox:
                    spacing 6
                    text "❤" size 13 color "#e84393"
                    text "Loyalitas  " size 12 color "#95a5a6" xminimum 85
                    text "[loyalitas]"  size 12 bold True color "#e84393"

init python:
    config.overlay_screens.append("stats_hud")


################################################################################
## Stat Gain Popup – Brief floating notification after a choice
################################################################################

screen stat_gain_popup(stat_name, value, color="#f1c40f"):
    zorder 200
    timer 1.8 action Hide("stat_gain_popup")
    frame:
        xalign 0.5
        yalign 0.09
        background Solid("#00000000")
        at _stat_popup_anim
        text "+ [value]  [stat_name]":
            size 27 bold True color color
            outlines [(2, "#000000bb", 1, 1)]


################################################################################
## Chapter Title Card – Cinematic act breaks
## Usage:  call screen chapter_title_card("BABAK I", "Lahirnya Seorang Ksatria")
################################################################################

init python:
    _chapter_quotes = {
        "BABAK I":   "\"Yang pertama datang adalah yang paling dikenang.\"",
        "BABAK II":  "\"Darah yang tumpah tidak pernah bisa disebut sia-sia.\"",
        "BABAK III": "\"Ada api yang tidak bisa dipadamkan dengan kata-kata.\"",
        "EPILOG":    "\"Nama bertahan. Tubuh tidak.\"",
    }

screen chapter_title_card(title, subtitle="", duration=3.2):
    modal True
    zorder 300
    timer duration action Return()

    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16

        at float_in

        text title:
            size 70 bold True color "#f1c40f" xalign 0.5
            outlines [(3, "#000000", 0, 0)]

        if subtitle != "":
            add Solid("#f39c1299") xsize 520 ysize 2 xalign 0.5
            text subtitle:
                size 30 italic True color "#bdc3c7" xalign 0.5

        if title in _chapter_quotes:
            null height 12
            text _chapter_quotes[title]:
                size 20 italic True color "#7f8c8d" xalign 0.5


################################################################################
## Epilog Recap Screen – Show before the final ending
## Usage:  call screen epilog_recap
################################################################################

screen epilog_recap():
    modal True
    zorder 300

    add Solid("#0a0f14")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 28

        at float_in

        text "PERJALANAN RANGGALAWE":
            size 50 bold True color "#f1c40f" xalign 0.5
            outlines [(3, "#000000", 0, 0)]

        add Solid("#f39c12") xsize 720 ysize 2 xalign 0.5

        null height 5

        hbox:
            spacing 35
            xalign 0.5

            frame:
                background Solid("#1a0a0a")
                padding (22, 18)
                vbox:
                    spacing 6
                    text "⚔ KEBERANIAN" size 16 bold True color "#e74c3c" xalign 0.5
                    text "[keberanian]"  size 52 bold True color "#ffffff" xalign 0.5

            frame:
                background Solid("#0a0f1a")
                padding (22, 18)
                vbox:
                    spacing 6
                    text "🧠 KEBIJAKAN" size 16 bold True color "#3498db" xalign 0.5
                    text "[kebijakan]"  size 52 bold True color "#ffffff" xalign 0.5

            frame:
                background Solid("#0a1a0a")
                padding (22, 18)
                vbox:
                    spacing 6
                    text "🏆 KEHORMATAN" size 16 bold True color "#2ecc71" xalign 0.5
                    text "[kehormatan]"  size 52 bold True color "#ffffff" xalign 0.5

            frame:
                background Solid("#1a0a12")
                padding (22, 18)
                vbox:
                    spacing 6
                    text "❤ LOYALITAS" size 16 bold True color "#e84393" xalign 0.5
                    text "[loyalitas]"  size 52 bold True color "#ffffff" xalign 0.5

        frame:
            background Solid("#12161c")
            padding (28, 16)
            xsize 860
            xalign 0.5
            vbox:
                spacing 6
                text "Gaya Kepemimpinan:" bold True color "#bdc3c7" size 17 xalign 0.5
                hbox:
                    spacing 24
                    xalign 0.5
                    text "Konfrontasi [konfrontasi]" size 15 color "#e74c3c"
                    text "•" size 15 color "#444444"
                    text "Mediasi [mediasi]"         size 15 color "#3498db"
                    text "•" size 15 color "#444444"
                    text "Siasat [siasat]"            size 15 color "#9b59b6"

        null height 5

        textbutton "Teruskan ke Epilog →":
            action Return()
            xalign 0.5
            text_size 22 text_bold True text_color "#ffffff"
            background Solid("#922b21")
            hover_background Solid("#e74c3c")
            padding (30, 12)
