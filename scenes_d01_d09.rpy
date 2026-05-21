# ==========================================
# BABAK I - EKSPOSISI: Lahirnya Seorang Ksatria
# SCENE D01 - KABAR DATANG KE SUMENEP
# ==========================================
label scene_d01:
    # Aset placeholder
    scene expression Movie(play="video/scene1_1.webm", mute=True, size=(1920, 1080)) with fade

    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene1_2.mp3" 
    narrator "Singhasari, 1292 M. Prabu Kertanegara gugur di tangan Jayakatwang dari Kediri."
    
    # TODO: Tambahkan Voice Over (VO) narrator

    voice "audio/scene1_3.mp3" 
    scene standing:
        xysize (1920, 1080)
    with fade

    narrator "{a=call:show_ensik_raden_wijaya}Raden Wijaya{/a} melarikan diri. Di Sumenep, Madura - seorang ayah menunggu putranya menyampaikan berita yang mengubah segala-galanya."

    scene joglo:
        xysize(1920, 1080)
    with fade
    show arya serius at center with dissolve
    arya "Anakku. {a=call:show_ensik_raden_wijaya}Raden Wijaya{/a} dalam pelarian. Ia membutuhkan orang-orang yang ia percaya - sekarang, malam ini."
    arya "Ini bukan waktunya menangis. Ini waktunya memilih."
    
    # TODO: Tambahkan Voice Over (VO) narrator

    voice "audio/scene1_4.mp3"
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
    scene bg 01:
        xysize (1920, 1080)
    with fade

    show arya bangga at center with dissolve
    arya "Pergi. Tapi ingat, anakku - yang pertama datang adalah yang paling dikenang."
    
    # Aset BG asli: BG-01 (Pendopo Sumenep Eksterior - Jalan Malam) sudah dipasang.
    scene expression Movie(play="video/berangkat.webm", size=(1920, 1080)) with fade
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene1a.mp3"
    narrator "Ken Kara berangkat sendiri, hanya membawa pedang dan bekal seadanya. Silhuetnya hilang dalam kegelapan."
    return

label d01_jalur_b:
    show arya bijak at center with dissolve
    arya "Kamu bijak. Kumpulkan 200 prajurit terbaik. Pasukan Madura adalah kekuatan nyata yang tidak bisa diabaikan."
    
    scene bg 01:
        xysize (1920, 1080)
    with fade

    # Aset BG asli: BG-01 (Pendopo Sumenep Eksterior - Pagi) sudah dipasang.
    # TODO: Tambahkan aset cutscene
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene2a.mp3"
    narrator "200 prajurit berjejer. Ken Kara memimpin di depan. Terdengar irama genderang ringan."
    return

label d01_jalur_c:
    show arya ambigu at center with dissolve
    arya "(Tersenyum tipis) Kamu lebih cerdas dari yang kukira. Duduk. Dengarkan rencanaku yang sebenarnya."
    
    scene bg 02 with fade
    # TODO: Tambahkan aset cutscene
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene3a.mp3"
    narrator "[[CUTSCENE] INT. Ruang Dalam Pendopo - Malam.\nPeta jaringan dan siasat ganda terbentang di atas meja. Garis-garis strategi saling bersilangan — menandakan permainan yang jauh lebih berbahaya daripada perang biasa."
    return

# ==========================================
# SCENE D02 - DUA DUNIA BERGERAK BERSAMAAN
# ==========================================
label scene_d02:
    # TODO: Gunakan aset BG asli: BG-02 & BG-05 (Split Screen)
    
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene5.mp3"
    scene split:
        xysize (1920, 1080)
    with fade
    narrator "Dua dunia bergerak bersamaan. Satu di balik meja dengan surat dan siasat. Satu lagi di jalan panjang dengan pedang dan tekad."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene6.mp3"
    scene write:
        xysize(1920,1080)
    with fade
    narrator "{a=call:show_ensik_arya_wiraraja}Wiraraja{/a} menulis dua surat sekaligus. Satu untuk {a=call:show_ensik_raden_wijaya}Raden Wijaya{/a}, satu untuk Jayakatwang."
    arya "Maafkan anakku, Jayakatwang. Ini bukan pengkhianatan. Ini... politik."
    
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene7.mp3"
    scene writing:
        xysize(1920,1080)
    with fade
    narrator "Ken Kara melangkah di jalannya..."

    if siasat > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene8.mp3"
        narrator "Bermain dua wajah terasa merendahkan harga diri ksatria. Tapi tanpa siasat, perlawanan terbuka berarti kematian sia-sia. Aku percaya ayahku."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene9.mp3"
        narrator "Langkahku mantap menuju takdir yang belum selesai."

    return

# ==========================================
# SCENE D03 - NAMA BARU, TANGGUNG JAWAB BARU
# ==========================================

init python:
    def parse_hyperlink(link):
        if link.startswith("show_ensik_"):
            target_char = link.replace("show_ensik_", "")
            renpy.show_screen("ensiklopedia_karakter", char_id=target_char)
            renpy.restart_interaction()
            return True
        return False
    config.hyperlink_handlers["call"] = parse_hyperlink

    # Define encyclopedia data globally
    ensik_data = {
        "ranggalawe": {
            "title": "ENSIKLOPEDIA: RANGGALAWE",
            "arti": ("Etimologi Jawa Kuno:", "Kata {b}'Rangga'{/b} berarti pejabat atau punggawa kerajaan tingkat menengah atas, yang berhak memerintah pasukan. Dan {b}'Lawe'{/b} merujuk pada benang (terutama benang sutra atau tenun), yang secara kiasan mengartikan tugas untuk merajut, mengikat, atau menertibkan jajaran pasukan yang berceceran."),
            "asal_usul": ("Konteks Historis:", "Berasal dari nama asli {b}Ken Kara{/b}. Menurut catatan, Pangeran Wijaya memberinya nama Ranggalawe berdasarkan Kitab Pararaton & Kidung Ranggalawe saat awal mula mendirikan pedukuhan di Hutan Tarik, sebagai penghargaan turun tangan Madura ke medan perang dalam membela yang berhak."),
            "nilai": ("Foreshadowing: Tiga Nilai Agung", "Kode etik utama kelak disandangnya:\n1. {b}Seca Wecana{/b} (ucapan yang bisa dipegang).\n2. {b}Sura ing Pati{/b} (berani berkalang tanah demi kehormatan).\n3. {b}Lila ing Donya{/b} (rela melepas jerat duniawi dan takhta demi nilai yang luhur).")
        },
        "raden_wijaya": {
            "title": "ENSIKLOPEDIA: RADEN WIJAYA",
            "arti": ("Etimologi Jawa Kuno:", "Kata {b}'Raden'{/b} bermakna 'yang mulia' atau terhormat (gelar kebangsawanan), sementara {b}'Wijaya'{/b} berarti kemenangan atau kejayaan agung dari bahasa Sanskerta."),
            "asal_usul": ("Konteks Historis:", "Menantu dari Prabu Kertanegara (Singhasari). Kelak menjadi pendiri dan raja pertama dari Kerajaan Majapahit dengan gelar {b}Kertarajasa Jayawardhana{/b} pada 1293 M."),
            "nilai": ("Visi Ksatria dan Politik", "Menggabungkan kharisma ksatria pelindung dengan visi politik tajam, menjalin aliansi (seperti dengan pasukan Tartar dan Arya Wiraraja) demi merebut kembali tahta dan kehormatan tanah Jawa.")
        },
        "lembu_sora": {
            "title": "ENSIKLOPEDIA: LEMBU SORA",
            "arti": ("Etimologi Jawa Kuno:", "Kata {b}'Lembu'{/b} sering digunakan sebagai gelar bagi satria tangguh dan gagah, mewakili ketahanan. {b}'Sora'{/b} berarti suara (keras/lantang), menggambarkan ketegasan dan nama besar seorang ksatria sakti."),
            "asal_usul": ("Konteks Historis:", "Merupakan paman dari Ranggalawe dan salah satu panglima paling dihormati. Ia terkenal sangat setia kepada Raden Wijaya sejak di masa pelarian, namun hatinya sering robek oleh pertarungan intrik dan dilema kehormatan (Kidung Sorandaka)."),
            "nilai": ("Keteladanan dan Dilema", "{b}Kesetiaan Tanpa Syarat{/b}: Simbol prajurit tua yang berpegang teguh pada hirarki yang sah walau terkadang berbenturan dengan nilai kekeluargaan dan persahabatan.")
        },
        "arya_wiraraja": {
            "title": "ENSIKLOPEDIA: ARYA WIRARAJA",
            "arti": ("Etimologi Jawa Kuno:", "Kata {b}'Arya'{/b} merupakan gelar untuk orang bangsawan/berilmu luhur. {b}'Wira'{/b} berarti pahlawan atau pejuang, dan {b}'Raja'{/b} adalah pemimpin. Secara harafiah: Pemimpin Pahlawan yang Terhormat."),
            "asal_usul": ("Konteks Historis:", "Adipati Madura (Sumenep). Seorang master negosiator, bapak dari Ranggalawe. Memberikan penampungan aman bagi Raden Wijaya, mendalangi tipu muslihat dengan surat tunduk palsu untuk membangun Majapahit."),
            "nilai": ("Otak di Balik Layar", "Perwujudan rasionalitas tanpa ampun dan {b}Siasat Tajam{/b}: Seseorang yang tahu kapan harus mundur agar bisa meloncat maju. Ahli merangkai intrik politik yang melampaui kemampuan musuhnya.")
        },
        "nambi": {
            "title": "ENSIKLOPEDIA: NAMBI",
            "arti": ("Makna Nama:", "Nambi adalah nama orang biasa yang tidak bergelar bawaan seperti 'Lembu' atau 'Gajah'. Namun, posisinya dan tindakannya kelak akan merepresentasikan kekuatan besar di balik gelar Mahapatih dalam hirarki."),
            "asal_usul": ("Konteks Historis:", "Tokoh berpengaruh besar; salah satu pemuda pengikut setia Raden Wijaya sejak runtuhnya Singhasari. Akan memicu intrik saat Kertarajasa mengangkatnya sebagai {b}Rakryan Patih Amangkubumi{/b}—posisi yang merasa lebih layak dipercayakan ke Ranggalawe atau Lembu Sora."),
            "nilai": ("Bayang-bayang Kekuasaan:", "Digambarkan sebagai figur tenang, dekat dengan inti kekuasaan tanpa harus terlalu menonjol di medan fisik, menjadikannya kanvas sempurna bagi fitnah politis.")
        }
    }

screen ensiklopedia_karakter(char_id):
    zorder 100
    modal True
    add "#000000cc" 
    
    default active_tab = "arti"
    $ data = ensik_data.get(char_id, ensik_data["ranggalawe"])

    frame:
        align (0.5, 0.5)
        xysize (900, 520)
        background Solid("#121a22")
        
        # Border Frame
        frame:
            align (0.5, 0.5)
            xysize (896, 516)
            background Solid("#1c2833")
            padding (40, 20)

            vbox:
                spacing 15
                align (0.5, 0.0)
                yoffset 25
                xfill True

                # Header
                text data["title"] size 34 bold True xalign 0.5 color "#f1c40f" outlines [(1, "#000", 0, 0)]
                add Solid("#f39c12") xsize 820 ysize 2 xalign 0.5 alpha 0.5
                null height 10

                # Tabs
                hbox:
                    spacing 10
                    xalign 0.5
                    
                    textbutton "Arti Nama":
                        action SetScreenVariable("active_tab", "arti")
                        text_size 20 
                        text_color ("#fff" if active_tab == "arti" else "#7f8c8d")
                        background (Solid("#d35400") if active_tab == "arti" else Solid("#2c3e50"))
                        hover_background Solid("#e67e22")
                        padding (20, 10)
                        
                    textbutton "Asal-usul":
                        action SetScreenVariable("active_tab", "asal_usul")
                        text_size 20 
                        text_color ("#fff" if active_tab == "asal_usul" else "#7f8c8d")
                        background (Solid("#2980b9") if active_tab == "asal_usul" else Solid("#2c3e50"))
                        hover_background Solid("#3498db")
                        padding (20, 10)
                        
                    textbutton "Nilai Taktis/Ksatria":
                        action SetScreenVariable("active_tab", "nilai")
                        text_size 20 
                        text_color ("#fff" if active_tab == "nilai" else "#7f8c8d")
                        background (Solid("#8e44ad") if active_tab == "nilai" else Solid("#2c3e50"))
                        hover_background Solid("#9b59b6")
                        padding (20, 10)

                # Content Area
                frame:
                    background Solid("#151f28")
                    xsize 820 ysize 220
                    align (0.5, 0.5)
                    padding (20, 20)
                    
                    $ tab_content = data.get(active_tab, ("", ""))
                    vbox:
                        spacing 10
                        text tab_content[0] bold True color ("#e74c3c" if active_tab=="arti" else "#3498db" if active_tab=="asal_usul" else "#9b59b6") size 22
                        text tab_content[1] size 18 color "#bdc3c7"

                null height 20
                textbutton "TUTUP":
                    action Hide("ensiklopedia_karakter")
                    xalign 0.5
                    text_size 24 text_bold True 
                    background Solid("#27ae60") hover_background Solid("#2ecc71")
                    text_color "#fff" padding (40, 10)
                    
                text "Opsional — menutup tidak mempengaruhi cerita." italic True size 14 color "#7f8c8d" xalign 0.5 yoffset 10

label scene_d03:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-05 / BG-06 (Kamp Hutan Tarik)

    if d01_choice == "A":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene10.mp3"
        narrator "[[CUTSCENE] Raden Wijaya memeluk Ken Kara. 'Kamu datang sendiri, tanpa diminta. Itulah keberanian yang Majapahit butuhkan.'"
    elif d01_choice == "B":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene11.mp3"
        narrator "[[CUTSCENE] Raden Wijaya meninjau 200 prajurit. 'Kamu tidak hanya membawa dirimu. Kamu membawa Madura.'"
    elif d01_choice == "C":
        # TODO: Tambahkan aset cutscene
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene12.mp3"
        narrator "[[CUTSCENE] Raden Wijaya berbisik. 'Wiraraja bilang kamu sudah tahu semuanya. Aku butuh orang seperti itu di dekatku.'"

    voice "audio/scene13.mp3"
    show raden_k berwibawa
    raden "Mulai hari ini, kamu kupanggil {a=call:show_ensik_ranggalawe}Ranggalawe{/a} — ia yang boleh memerintah anak buahku. Nama ini bukan hadiah. Ini tanggung jawab."

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
    voice "audio/scene14.mp3"
    narrator "Malam pertama di Hutan Tarik. Ada satu malam untuk berkenalan dengan orang-orang yang akan mewarnai perjalanannya."

    menu:
        "[[Duduk bersama {a=call:show_ensik_lembu_sora}Lembu Sora{/a} di api unggun] Paman punya cerita perang malam ini? (Mediasi)":
            $ mediasi += 1
            $ d04_choice = "A"
            $ kebijakan += 10
            $ loyalitas_sora += 15
            lembu "Kamu tahu kenapa aku masih hidup? Karena aku tahu kapan harus maju dan kapan harus diam."
            ranggalawe "Apakah ada saatnya diam adalah pengkhianatan, Paman?"
            lembu "Itu pertanyaan yang akan menjawab dirinya sendiri nanti."

        "[[Amati {a=call:show_ensik_nambi}Nambi{/a} dari kejauhan] Kenapa ia selalu di sisi {a=call:show_ensik_raden_wijaya}Raden Wijaya{/a}? (Siasat)":
            $ siasat += 1
            $ d04_choice = "B"
            $ kebijakan += 10
            $ kehormatan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            voice "audio/scene15.mp3"
            narrator "Kamu mengamati {a=call:show_ensik_nambi}Nambi{/a} lekat-lekat dari bayangan, mencari kelemahannya."

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
            voice "audio/scene16.mp3"

            narrator "Kamu memilih istirahat demi menyimpan tenaga."
            
    return

# ==========================================
# SCENE D05 - SIASAT MASUK KE KEDIRI
# ==========================================

init python:
    class D05InfiltrationPlanner:
        def __init__(self):
            # Properti yang bisa dipilih pemain
            self.route = None      # "hutan", "utama", "brantas"
            self.time = None       # "siang", "malam", "subuh"
            self.disguise = None   # "pedagang", "pengungsi", "prajurit_pembelot"
            self.score = 0
            self.feedback = ""

        def set_route(self, r):
            self.route = r

        def set_time(self, t):
            self.time = t

        def set_disguise(self, d):
            self.disguise = d

        def calculate_score(self):
            self.score = 0
            # ----- Logika Route -----
            if self.route == "hutan":
                self.score += 10
                if self.time == "malam":
                    self.score += 20 # Sinergi: Hutan + Malam sangat stealth
                else:
                    self.score -= 5  # Berbahaya di siang hari
            elif self.route == "utama":
                if self.disguise == "pedagang":
                    self.score += 25 
                elif self.disguise == "prajurit_pembelot":
                    self.score += 10
                else:
                    self.score -= 10
            elif self.route == "brantas":
                self.score += 15
                if self.time == "subuh":
                    self.score += 15 # Sinergi: Kabut sungai Brantas

            # Feedback Generator
            if self.score >= 35:
                self.feedback = "Rencana Sempurna. Kita akan masuk Kediri seperti bayangan."
            elif self.score >= 15:
                self.feedback = "Rencana yang cukup baik, meskipun ada sedikit risiko patroli Kediri."
            else:
                self.feedback = "Terlalu gegabah! Rencana ini berpotensi membahayakan seluruh operasi."
                
            return self.score

        def is_ready(self):
            return self.route is not None and self.time is not None and self.disguise is not None

    d05_drag_starts = {
        "hutan": (40, 270), "utama": (40, 360), "brantas": (40, 450),
        "siang": (360, 270), "malam": (360, 360), "subuh": (360, 450),
        "pedagang": (680, 270), "pengungsi": (680, 360), "prajurit_pembelot": (680, 450)
    }

    def d05_dragged(drags, drop):
        drag = drags[0]
        
        cat = None
        if drag.drag_name in ["hutan", "utama", "brantas"]: cat = "route"
        elif drag.drag_name in ["siang", "malam", "subuh"]: cat = "time"
        elif drag.drag_name in ["pedagang", "pengungsi", "prajurit_pembelot"]: cat = "disguise"

        if drop:
            # Match slot category
            if drop.drag_name == "drop_" + cat:
                if cat == "route": store.d05_planner.set_route(drag.drag_name)
                elif cat == "time": store.d05_planner.set_time(drag.drag_name)
                elif cat == "disguise": store.d05_planner.set_disguise(drag.drag_name)
                
                # Snap perfectly to the center of the slot wrapper
                drag.snap(drop.x + 5, drop.y + 5, 0.1)
                renpy.restart_interaction()
                return

        # Snap back if no valid drop
        if cat == "route" and store.d05_planner.route == drag.drag_name:
            store.d05_planner.set_route(None)
        elif cat == "time" and store.d05_planner.time == drag.drag_name:
            store.d05_planner.set_time(None)
        elif cat == "disguise" and store.d05_planner.disguise == drag.drag_name:
            store.d05_planner.set_disguise(None)
            
        x, y = d05_drag_starts[drag.drag_name]
        drag.snap(x, y, 0.2)
        renpy.restart_interaction()

default d05_planner = D05InfiltrationPlanner()

screen d05_minigame_peta():
    modal True
    add "#000000e6" # Muted very dark background

    on "show" action Function(d05_planner.__init__) # Reset state setiap minigame dimulai

    # Border frame luar
    frame:
        align (0.5, 0.5)
        xysize (1040, 760)
        background Solid("#f39c12") # Accent gold border
        
        # Frame dalam
        frame:
            align (0.5, 0.5)
            xysize (1036, 756)
            background Solid("#121a22") 
            
            vbox:
                spacing 10
                align (0.5, 0.0)
                yoffset 25
                
                text "🗺️ PETA STRATEGI INFILTRASI KEDIRI 🗺️" size 38 bold True xalign 0.5 color "#f1c40f" outlines [(2, "#000", 0, 0)]
                text "Susun taktik dengan memindahkan strategi dari panel bawah ke slot aktif di atas." size 18 xalign 0.5 color "#bdc3c7" italic True
                
                null height 5
                add Solid("#f39c12") xsize 950 ysize 2 xalign 0.5 alpha 0.5

            # Area Drag and Drop
            draggroup:

                # Titik Tempat Drop (Slot)
                drag:
                    drag_name "drop_route"
                    xpos 35 ypos 140
                    draggable False
                    droppable True
                    frame:
                        xysize (290, 80)
                        background Solid("#c0392b") # Accent route
                        frame:
                            align (0.5, 0.5)
                            xysize (286, 76)
                            background Solid("#1a252f")
                            text "{{alpha=0.4}} SLOT RUTE {{/alpha}}" align (0.5, 0.5) color "#e74c3c" size 18 bold True

                drag:
                    drag_name "drop_time"
                    xpos 355 ypos 140
                    draggable False
                    droppable True
                    frame:
                        xysize (290, 80)
                        background Solid("#2980b9") # Accent time
                        frame:
                            align (0.5, 0.5)
                            xysize (286, 76)
                            background Solid("#1a252f")
                            text "{{alpha=0.4}} SLOT WAKTU {{/alpha}}" align (0.5, 0.5) color "#3498db" size 18 bold True
                        
                drag:
                    drag_name "drop_disguise"
                    xpos 675 ypos 140
                    draggable False
                    droppable True
                    frame:
                        xysize (290, 80)
                        background Solid("#8e44ad") # Accent disguise
                        frame:
                            align (0.5, 0.5)
                            xysize (286, 76)
                            background Solid("#1a252f")
                            text "{{alpha=0.4}} SLOT SAMARAN {{/alpha}}" align (0.5, 0.5) color "#9b59b6" size 18 bold True


                # Pilihan yang bisa di Drag (Draggables)
                # ========================================

                # Rute
                drag:
                    drag_name "hutan"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["hutan"][0] ypos d05_drag_starts["hutan"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#801b12") hover_background Solid("#c0392b")
                        hbox:
                            align (0.5, 0.5)
                            spacing 15
                            add Transform("images/Icon/hutan_gelap.png", size=(45, 45)) align (0.5, 0.5)
                            text "Hutan Gelap" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "utama"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["utama"][0] ypos d05_drag_starts["utama"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#801b12") hover_background Solid("#c0392b")
                        hbox:
                            align (0.5, 0.5)
                            spacing 15
                            add Transform("images/Icon/gerbang_kerajaan.png", size=(45, 45)) align (0.5, 0.5)
                            text "Jalur Utama" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "brantas"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["brantas"][0] ypos d05_drag_starts["brantas"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#801b12") hover_background Solid("#c0392b")
                        hbox:
                            align (0.5, 0.5)
                            spacing 15
                            add Transform("images/Icon/sungai.png", size=(45, 45)) align (0.5, 0.5)
                            text "Lewat Sungai" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                # Waktu
                drag:
                    drag_name "siang"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["siang"][0] ypos d05_drag_starts["siang"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#1a5276") hover_background Solid("#2980b9")
                        text "☀️ Siang Hari" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "malam"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["malam"][0] ypos d05_drag_starts["malam"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#1a5276") hover_background Solid("#2980b9")
                        text "🌙 Malam Buta" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "subuh"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["subuh"][0] ypos d05_drag_starts["subuh"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#1a5276") hover_background Solid("#2980b9")
                        text "🌅 Subuh" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                # Penyamaran
                drag:
                    drag_name "pedagang"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["pedagang"][0] ypos d05_drag_starts["pedagang"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#5b2c6f") hover_background Solid("#8e44ad")
                        text "🌾 Pedagang Padi" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "pengungsi"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["pengungsi"][0] ypos d05_drag_starts["pengungsi"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#5b2c6f") hover_background Solid("#8e44ad")
                        text "⛺ Pengungsi" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]

                drag:
                    drag_name "prajurit_pembelot"
                    dragged d05_dragged
                    droppable False
                    xpos d05_drag_starts["prajurit_pembelot"][0] ypos d05_drag_starts["prajurit_pembelot"][1]
                    frame:
                        xysize (280, 70)
                        background Solid("#5b2c6f") hover_background Solid("#8e44ad")
                        text "💂 Prajurit Pembelot" align (0.5, 0.5) color "#fff" size 22 outlines [(1, "#000", 0, 0)]


            # --- Konfirmasi Action ---
            vbox:
                align (0.5, 1.0)
                yoffset -40
                spacing 15

                # --- Panel Rekap ---
                frame:
                    background Solid("#1c2833")
                    padding (20, 15)
                    xsize 950
                    vbox:
                        spacing 5
                        xalign 0.5
                        text "Ringkasan Rencana Operasi:" bold True color "#7f8c8d" size 16 xalign 0.5
                        text ("Jalur: " + (d05_planner.route.capitalize() if d05_planner.route else "___") + "  |  Waktu: " + (d05_planner.time.capitalize() if d05_planner.time else "___") + "  |  Samaran: " + (d05_planner.disguise.replace("_", " ").title() if d05_planner.disguise else "___")) size 24 xalign 0.5 color "#f39c12" bold True outlines [(1, "#000", 0, 0)]

                if d05_planner.is_ready():
                    textbutton "✓ JALANKAN OPERASI":
                        action [Function(d05_planner.calculate_score), Return(d05_planner)]
                        xalign 0.5
                        text_size 28
                        text_bold True
                        background Solid("#27ae60")
                        hover_background Solid("#2ecc71")
                        text_color "#ffffff"
                        padding (30, 15)

label scene_d05:
    scene bg 06 with fade
    # TODO: Gunakan aset BG asli: BG-06 (Kamp Hutan Tarik - Siang)
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene17.mp3"
    narrator "Rapat strategi. Wiraraja menguraikan rencana: berpura-pura tunduk kepada Jayakatwang dan masuk ke Kediri sebagai 'pengabdi'."
    narrator "Sebuah peta lusuh digelar di atas meja kayu. Ranggalawe harus menentukan langkah masuk paling aman."

    # Memanggil Minigame Peta Strategi Menggunakan Python Hook
    call screen d05_minigame_peta

    # Mengembalikan nilai objek 'planner' yang memuat skor dan logikanya
    $ d05_planner_result = _return
    
    # Memberi tanggapan naratif berdasarkan hasil kalkulasi sistem
    narrator "[d05_planner_result.feedback]"

    if d05_planner_result.score >= 35:
        $ siasat += 2
        narrator "Wiraraja mengangguk puas melihat pilihan strategimu."
    elif d05_planner_result.score >= 15:
        $ keberanian += 1
        narrator "Rencana disetujui, meskipun ada beberapa petinggi yang masih ragu."
    else:
        $ kebijakan -= 1
        narrator "Wiraraja memandangmu lama. Akhirnya ia menghela napas panjang dan mencoba memperbaiki beberapa celah rencanamu."

    # Interaksi Lanjutan setelah Map Puzzle diselesaikan
    narrator "Selain menyusupkan pasukan, siapa yang akan memimpin kelompok barisan terdepan masuk ke jantung istana?"
    
    menu:
        "Hamba siap. Hamba akan menjadi utusan pribadi Tuanku di Kediri. (Konfrontasi)":
            $ konfrontasi += 1
            $ kebijakan += 10
            $ keberanian += 5
            # TODO: Tambahkan Voice Over (VO) narrator
            voice "audio/scene18.mp3"
            narrator "Kamu mengajukan diri sebagai garda terdepan utusan pura-pura ini."

        "Hamba minta jaminan keamanan Hutan Tarik selama hamba pergi. (Mediasi)":
            $ mediasi += 1
            $ kehormatan += 10
            $ kebijakan += 15
            # TODO: Tambahkan Voice Over (VO) narrator
            voice "audio/scene19.mp3"
            narrator "Kamu menetapkan syarat rasional demi keselamatan pasukan."

        "Izinkan hamba ikut langsung ke Kediri mengantisipasi dari dalam. (Siasat)":
            $ siasat += 1
            $ loyalitas += 20
            $ keberanian += 10
            $ kebijakan -= 5
            # TODO: Tambahkan Voice Over (VO) narrator
            voice "audio/scene20.mp3"
            narrator "Kamu mencari posisi strategis di pusat intrik musuh."

    return

# ==========================================
# SCENE D06 - DI DALAM SARANG MUSUH
# ==========================================
label scene_d06:
    scene bg 08 with fade
    # TODO: Gunakan aset BG asli: BG-08 (Kediri - Alun-alun) / BG-09 (Kediri - Dalam Istana)
    # TODO: Tambahkan Voice Over (VO) narrator
    voice "audio/scene21.mp3"
    narrator "Berminggu-minggu bersandiwara di Kediri. Tunduk, menghormati, sambil menyiapkan kejatuhan musuh."
    
    if siasat > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene22.mp3"
        narrator "[[Batin] Aku mengamati mereka dengan kalkulasi... dan Nambi selalu dekat dengan kekuasaan tanpa harus berkeringat sepertiku."
    elif konfrontasi > 0:
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene23.mp3"
        narrator "[[Batin] Sandiwara ini membuatku muak. Aku tak sabar menarik pedang, apalagi saat melihat mereka percaya begitu saja pada Nambi yang tak teruji."
    else:
        # TODO: Tambahkan Voice Over (VO) narrator
        voice "audio/scene24.mp3"
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
