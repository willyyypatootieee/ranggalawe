# Game Assets
image blackscreen = Solid("#000")
image arya = Transform("arya ambigu", zoom=0.55, yalign=1.0) # default if 'arya' is used without tags
image arya ambigu = Transform("images/arya/arya ambigu.png", zoom=0.55, yalign=1.0)
image arya bangga = Transform("images/arya/arya bangga.png", zoom=0.55, yalign=1.0)
image arya bijak = Transform("images/arya/arya bijak.png", zoom=0.55, yalign=1.0)
image arya khawatir = Transform("images/arya/arya khawatir.png", zoom=0.55, yalign=1.0)
image arya serius = Transform("images/arya/arya serius.png", zoom=0.55, yalign=1.0)

image raden_k berathati = Transform("images/raden_k/raden_k berathati.png", zoom=0.55, yalign=1.0)
image raden_k berwibawa = Transform("images/raden_k/raden_k berwibawa.png", zoom=0.55, yalign=1.0)
image raden_k ragu = Transform("images/raden_k/raden_k ragu.png", zoom=0.55, yalign=1.0)
image raden_k tegas = Transform("images/raden_k/raden_k tegas.png", zoom=0.55, yalign=1.0)

image raden_p berwibawa = Transform("images/raden_p/raden_p berwibawa.png", zoom=0.55, yalign=1.0)
image raden_p lelah = Transform("images/raden_p/raden_p lelah.png", zoom=0.55, yalign=1.0)
image raden_p tulus = Transform("images/raden_p/raden_p tulus.png", zoom=0.55, yalign=1.0)
image raden_p waspada = Transform("images/raden_p/raden_p waspada.png", zoom=0.55, yalign=1.0)

image ranggalawe angry = Transform("images/ranggalawe/ranggalawe angry.png", zoom=0.55, yalign=1.0)
image ranggalawe determination = Transform("images/ranggalawe/ranggalawe determination.png", zoom=0.55, yalign=1.0)
image ranggalawe happy = Transform("images/ranggalawe/ranggalawe happy.png", zoom=0.55, yalign=1.0)
image ranggalawe neutral = Transform("images/ranggalawe/ranggalawe neutral.png", zoom=0.55, yalign=1.0)
image ranggalawe sad = Transform("images/ranggalawe/ranggalawe sad.png", zoom=0.55, yalign=1.0)
image ranggalawe shock = Transform("images/ranggalawe/ranggalawe shock.png", zoom=0.55, yalign=1.0)
image ranggalawe terluka = Transform("images/ranggalawe/ranggalawe terluka.png", zoom=0.55, yalign=1.0)
image ranggalawe = Transform("ranggalawe neutral", zoom=0.55, yalign=1.0)

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

