**_GAWE RANGGALAWE_**

**DOKUMEN PRODUKSI VISUAL NOVEL**

**SISTEM PERCABANGAN DINAMIS D01-D40+**

Disusun untuk Pengembangan Ren'Py

Teknologi Rekayasa Multimedia - PENS 2025/2026

_"Bagi sebagian, ia pemberontak. Bagi Tuban... ia simbol keberanian melawan ketidakadilan."_

# **PANDUAN SISTEM PERCABANGAN DINAMIS**

**Prinsip Utama:** Semua pilihan pemain bersifat DINAMIS. Tidak ada jalur tetap. Player dapat memilih A, B, atau C secara acak di setiap scene - dan narasi harus tetap logis untuk semua kombinasi.

## **SISTEM TIGA KECENDERUNGAN KARAKTER**

**🗡️ KONFRONTASI (+1):** Ranggalawe menghadapi masalah secara langsung dan tegas. Jika dominan → karakter lebih keras, dialog lebih keras, NPC lebih waspada.

**🤝 MEDIASI (+1):** Ranggalawe berusaha mencari jalan tengah dan kompromi. Jika dominan → karakter lebih ragu dan penuh dilema, dialog lebih hati-hati.

**🔮 SIASAT (+1):** Ranggalawe bermain cerdas, mengumpulkan informasi, dan bergerak di balik layar. Jika dominan → karakter lebih dingin dan kalkulatif.

**CATATAN PENTING:** Player TIDAK selalu konsisten. Contoh pola nyata: D01→A, D02→B, D03→A, D04→C. Maka setiap scene HARUS masuk akal untuk SEMUA kombinasi sebelumnya.

## **CONTOH KONDISI ADAPTIF DIALOG**

_Jika akumulasi Konfrontasi dominan: tone keras, langsung, penuh keyakinan_

_Jika akumulasi Mediasi dominan: tone ragu, penuh pertimbangan, mencari kompromi_

_Jika akumulasi Siasat dominan: tone dingin, kalkulatif, tidak banyak bicara_

_Jika nilai hampir seimbang: tampilkan konflik batin (internal monologue)_

## **LEGENDA SIMBOL NODE**

**⑂ SPLIT-MERGE** → Pilihan membelah alur nyata (NPC, info, dialog berbeda)

**◆ BOTTLENECK** → Peristiwa sejarah wajib, semua jalur melewati ini

**⟺ PARALLEL** → Dua perspektif berjalan bersamaan, tanpa keputusan

**↪ DETOUR** → Konten opsional, bisa dilompati tanpa kehilangan plot

**♥ RELATIONSHIP** → Sistem emosi & loyalitas berubah tiap keputusan

**🔒 STAT GATE** → Node tersembunyi, hanya terbuka jika syarat stat terpenuhi

**★ EXCLUSIVE** → Konten eksklusif satu jalur, insentif replay

**W-SHAPE** → Split kedua setelah merge - konten eksklusif per jalur

## **FORMAT PENULISAN SCENE (Ren'Py Ready)**

_Setiap scene mencantumkan:_

_• Karakter bicara: nama karakter + kode sprite + ekspresi_

_• Aset yang digunakan: background, sprite, BGM, SFX_

_• Catatan adaptif: cara dialog berubah berdasarkan akumulasi pilihan_

## **STRUKTUR ENDING**

**ENDING TUNGGAL:** Ranggalawe gugur di Sungai Tambak Beras, 1295 M. Tidak bisa diubah.

**TONE BERBEDA per Akumulasi:**

_Dominan Konfrontasi → Kematian penuh keyakinan, berteriak nama Mahapati_

_Dominan Mediasi → Kematian penuh dilema, menatap Lembu Sora_

_Dominan Siasat → Kematian penuh ironi, menatap Ra Galatik di kejauhan_

# **BABAK I - EKSPOSISI: Lahirnya Seorang Ksatria (1292 M)**

_Sumenep, Madura & Hutan Tarik, Jawa Timur_

**SCENE D01 - KABAR DATANG KE SUMENEP** ◆ ⑂

**Tipe Node:** BOTTLENECK + SPLIT-MERGE + RELATIONSHIP

**Lokasi:** INT. Pendopo Adipati Sumenep, Madura - Malam

**📦 ASET: BG-02 (Pendopo Sumenep - Interior) | BGM-02 (Sumenep Damai) | FX-05 (Transisi Cutscene)**

**🎭 Arya Wiraraja** \[CH-02 | NPC Wajib | ekspresi: serius\]

**🎭 Ken Kara / Ranggalawe** \[CH-01 | Protagonist | ekspresi: netral → determinasi\]

### **Deskripsi**

Ruang dalam pendopo. Lampu minyak berkedip. Arya Wiraraja berdiri di meja kayu, surat di tangannya. Tangannya sedikit gemetar. Ken Kara masuk perlahan, membaca ekspresi ayahnya yang tidak biasa.

### **Narasi 01 (VO) - Narator**

_"Singhasari, 1292 M. Prabu Kertanegara gugur di tangan Jayakatwang dari Kediri. Raden Wijaya, menantu sekaligus penerus dinasti, berhasil melarikan diri. Di Sumenep, Madura - seorang ayah menunggu putranya untuk menyampaikan berita yang akan mengubah segala-galanya."_

### **Dialog Pembuka**

**ARYA WIRARAJA** _\[CH-02, ekspresi: serius, gestur meja\]:_

_"Anakku. Raden Wijaya dalam pelarian. Ia membutuhkan orang-orang yang ia percaya - sekarang, malam ini. Ini bukan waktunya menangis. Ini waktunya memilih."_

### **Narasi 02 (VO) - Ken Kara Batin**

_"Ayah tidak pernah berbicara seperti ini sebelumnya. Ada yang bergetar di dadaku - entah ketakutan, entah kegembiraan, entah keduanya sekaligus."_

### **Percabangan D01 - TITIK PERCABANGAN UTAMA**

**CATATAN NARATIF ADAPTIF:** _Ini pilihan PERTAMA. Belum ada akumulasi sebelumnya. Tampilkan Ken Kara sebagai sosok muda yang penuh gairah namun belum teruji._

**A \[Konfrontasi +1\].** "Katakan di mana Raden Wijaya. Aku akan pergi malam ini." - Ken Kara berdiri tegak, tidak ada keraguan.

_➤ Dampak: Berangkat sendiri. Modal: TIBA PERTAMA. Unlock NPC Nyai Sembada. Di D17-A raja lebih segan. Keberanian+15 Loyalitas+10_

**B \[Mediasi +1\].** "Satu hari, Ayah. Aku butuh mengumpulkan pria terbaik Madura. Kita tidak pergi dengan tangan kosong." - Logis dan terencana.

_➤ Dampak: Berangkat dengan 200 prajurit. Modal: PASUKAN MADURA. Leverage mediasi di D17-B lebih kuat. Kebijakan+15 Loyalitas+5_

**C \[Siasat +1\].** "Aku tahu ada lebih dari sekadar 'pergi membantu'. Apa yang sebenarnya Ayah rencanakan?" - Tatapan tajam ke Wiraraja.

_➤ Dampak: Wiraraja buka rencana dua wajah. Modal: INFO TERSEMBUNYI. Unlock Ra Galatik di D17-C. Kebijakan+10 Kehormatan+10_

### **Respons Wiraraja per Pilihan**

**Jika A:** _"Pergi. Tapi ingat, anakku - yang pertama datang adalah yang paling dikenang." \[ekspresi: bangga tersembunyi\]_

**Jika B:** _"Kamu bijak. Kumpulkan 200 prajurit terbaik. Pasukan Madura adalah kekuatan nyata yang tidak bisa diabaikan." \[ekspresi: bangga\]_

**Jika C:** _(Wiraraja tersenyum tipis) "Kamu lebih cerdas dari yang kukira. Duduk. Dengarkan rencanaku yang sebenarnya." - Membuka surat kedua: rencana infiltrasi dua wajah. \[ekspresi: ambigu\]_

### **Cutscene D01**

_\[JALUR A\] EXT. Jalan Sumenep - Malam. Ken Kara berangkat sendiri, hanya membawa pedang dan bekal seadanya. Silhuetnya hilang dalam kegelapan. FX: Debu Kaki (FX-06). SFX: Langkah Kaki Pasir (SFX-08)._

_\[JALUR B\] EXT. Halaman Pendopo - Pagi keesokan harinya. 200 prajurit berjejer. Ken Kara memimpin di depan. SFX: Genderang ringan._

_\[JALUR C\] INT. Ruang Dalam Pendopo - Lanjutan malam itu. Peta jaringan dan siasat ganda digelar di atas meja. Cahaya lampu minyak membuat bayangan bergerak dramatis._

**Transisi:** → Semua jalur lanjut ke D02

**SCENE D02 - DUA DUNIA BERGERAK BERSAMAAN** ⟺

**Tipe Node:** PARALLEL - Tidak ada pilihan

**Lokasi:** INT. Pendopo Sumenep (kiri) | EXT. Jalan menuju Hutan Tarik (kanan) - Malam hingga Fajar

**📦 ASET: BG-02 & BG-05 split screen | BGM-02 fade ke BGM-03 | FX-05 (wipe tengah layar)**

**🎭 Arya Wiraraja** \[CH-02 | ekspresi: ambigu, menulis\]

**🎭 Ken Kara** \[CH-01 | ekspresi: determinasi, berjalan\]

### **Narasi VO - Narator**

_"Dua dunia bergerak bersamaan. Satu di balik meja dengan surat dan siasat. Satu lagi di jalan panjang dengan pedang dan tekad. Keduanya menuju satu tujuan - dari arah yang tidak pernah persis sama."_

### **Cutscene Paralel - Tidak Ada Pilihan**

**LAYAR KIRI - WIRARAJA** _\[CH-02, menulis, ambang cahaya rendah\]:_

_Wiraraja menulis dua surat sekaligus. Satu untuk Raden Wijaya (dukungan penuh). Satu untuk Jayakatwang di Kediri (sanjungan palsu - agar tidak curiga)._

**ARYA WIRARAJA** _\[bergumam sendirian, ekspresi: ambigu-berat\]:_

_"Maafkan anakku, Jayakatwang. Ini bukan pengkhianatan. Ini... politik."_

**LAYAR KANAN - KEN KARA** _\[CH-01, berjalan/menunggu sesuai jalur\]:_

_Ken Kara berjalan atau menunggu, tergantung jalur. Tangannya menggenggam pedang. Wajahnya tidak menoleh._

**KEN KARA (V.O.)** _\[suara batin\]:_

_"Bermain dua wajah terasa merendahkan harga diri ksatria. Tapi tanpa siasat, perlawanan terbuka berarti kematian sia-sia. Aku percaya ayahku. Untuk sekarang."_

### **Catatan Naratif Adaptif**

_Tidak ada pilihan di scene ini. Namun jika player sebelumnya memilih C (Siasat), monolog batin Ken Kara sedikit berbeda - lebih sadar dan kalkulatif, bukan hanya mengikuti naluri. Engine Ren'Py dapat menampilkan variasi teks kecil berdasarkan flag siasat_aktif._

**Transisi:** → Semua jalur lanjut ke D03

**SCENE D03 - NAMA BARU, TANGGUNG JAWAB BARU** ♥ ⑂

**Tipe Node:** RELATIONSHIP + SPLIT-MERGE

**Lokasi:** EXT. Kamp Hutan Tarik, Jawa Timur - Siang

**📦 ASET: BG-05/BG-06 (Kamp Hutan Tarik) | BGM-03 (Tarik - Hutan dan Api) | SFX-01 (Pedang Terhunus, opsional)**

**🎭 Raden Wijaya** \[CH-03 kostum pelarian | NPC Wajib | ekspresi: tulus/berwibawa\]

**🎭 Lembu Sora** \[CH-04 | NPC Wajib | ekspresi: tegas/penuh kasih\]

**🎭 Ken Kara → Ranggalawe** \[CH-01 | Protagonist\]

### **Cutscene Pembuka - Berbeda per Jalur**

**\[JALUR A\]** _Raden Wijaya memeluk Ken Kara. "Kamu datang sendiri, tanpa diminta. Itulah keberanian yang Majapahit butuhkan." \[ekspresi Wijaya: tulus\]_

**\[JALUR B\]** _Raden Wijaya meninjau 200 prajurit yang berbaris. "Kamu tidak hanya membawa dirimu. Kamu membawa Madura." \[ekspresi Wijaya: berwibawa\]_

**\[JALUR C\]** _Raden Wijaya berbisik di telinga Ken Kara. "Wiraraja bilang kamu sudah tahu semuanya. Aku butuh orang seperti itu di dekatku." \[ekspresi Wijaya: ambigu\]_

### **Dialog Utama**

**RADEN WIJAYA** _\[CH-03, ekspresi: berwibawa\]:_

_"Mulai hari ini, kamu kupanggil Ranggalawe - ia yang boleh memerintah anak buahku. Nama ini bukan hadiah. Ini tanggung jawab."_

### **Percabangan D03**

**CATATAN NARATIF ADAPTIF:** _Jika pilihan D01 adalah C (Siasat), Ranggalawe lebih cepat menawarkan rencana. Jika D01 adalah A (Konfrontasi), respons lebih emosional dan bersumpah. Jika D01 adalah B (Mediasi), ada sedikit keraguan sebelum menjawab._

**A \[Konfrontasi +1\].** "Hamba berjanji akan mempertahankan nama ini dengan kehidupan hamba." - Suara tegas, tidak bergetar.

_➤ Dampak: Loyalitas kuat terbentuk. Dialog Lembu Sora di D25 terbuka. Loyalitas+20 Kehormatan+15_

**B \[Mediasi +1\].** "Hamba bersedia. Tapi apa artinya Ranggalawe dalam situasi yang belum pasti ini?" - Pertanyaan jujur.

_➤ Dampak: Info rencana lebih panjang terbuka. Raden Wijaya senyum ambigu. Kebijakan+10 Kehormatan+15_

**C \[Siasat +1\].** "Hamba bersedia. Dan izinkan hamba langsung menawarkan satu rencana, Tuanku." - Langsung ke substansi.

_➤ Dampak: Reputasi strategis sejak awal. Raden Wijaya terkesan. Keberanian+10 Kebijakan+15_

### **Reaksi Lembu Sora - Adaptif**

**\[Jika A dipilih\] LEMBU SORA** _\[CH-04, ekspresi: tegas-bangga, menepuk bahu\]: "Nama yang berat. Tapi kamu kuat untuk membawanya."_

**\[Jika B dipilih\] LEMBU SORA** _\[CH-04, ekspresi: tegas-diam\]: mengangguk pelan dari kejauhan, tidak berkata apa-apa._

**\[Jika C dipilih\] LEMBU SORA** _\[CH-04, ekspresi: konflik batin\]: "Hati-hati, keponakanku. Di sini orang dinilai dari cara ia diam, bukan berbicara."_

**Transisi:** → Semua jalur lanjut ke D04

**SCENE D04 - MALAM PERTAMA DI HUTAN TARIK** ↪ 🔒

**Tipe Node:** DETOUR OPSIONAL + SEED STAT GATE

**Lokasi:** EXT./INT. Kamp Hutan Tarik - Malam

**📦 ASET: BG-07 (Kamp Hutan Tarik - Malam) | FX-01 (Api Unggun) | FX-02 (Kabut Hutan) | SFX-07 (Ambient Hutan) | BGM-03**

**🎭 Lembu Sora** \[CH-04 | NPC Opsional pilihan A\]

**🎭 Nambi** \[CH-05 | NPC Opsional pilihan B\]

**🎭 Kebo Anabrang** \[CH-06 | NPC Opsional pilihan C\]

### **Deskripsi**

Api unggun menyala. Bintang di langit terlihat lewat celah pepohonan. Tiga tokoh kunci hadir di kamp. Pemain bisa skip ke D05 langsung.

### **Narasi VO**

_"Malam pertama di Hutan Tarik. Sebelum sandiwara besar dimulai, ada satu malam untuk berkenalan dengan orang-orang yang akan mewarnai hidupnya - dan satu di antara mereka akan jadi ujian terbesar yang pernah ia hadapi."_

### **Catatan Naratif Adaptif**

_Scene ini OPSIONAL. Namun pilihan C menanam SEED krusial untuk Stat Gate tersembunyi di D26. NPC lain tidak bisa diajak bicara setelah satu dipilih. Jika tidak ada pilihan yang diambil (skip), tidak ada stat yang berubah._

### **Percabangan D04**

**A \[Mediasi +1\].** \[Duduk bersama Lembu Sora di api unggun\] "Paman punya cerita perang yang bisa aku dengar malam ini?"

_➤ Dampak: Belajar strategi dari veteran. Dialog khusus Lembu Sora di D25 terbuka (opsi emosional tambahan). Kebijakan+10 Loyalitas(Sora)+15_

**B \[Siasat +1\].** \[Amati Nambi dari kejauhan\] "Kenapa ia selalu di sisi Raden Wijaya? Apa yang ia tahu yang aku tidak tahu?"

_➤ Dampak: Tahu kelemahan Nambi, berguna di D17-B. Kehormatan turun karena memata-matai. Kebijakan+10 Kehormatan-5_

**C \[Konfrontasi +1\].** \[Ajak Kebo Anabrang latihan fisik\] "Ayo, aku ingin tahu seberapa baik pendekar Majapahit bertarung."

_➤ Dampak: 🔒 SEED DITANAM: Jika Kehormatan≥7 saat D26, terbuka Node Tersembunyi "Perjanjian Diam Kebo Anabrang". Keberanian+15 Kehormatan+5_

### **Dialog Eksklusif per Pilihan**

**\[PILIHAN A\] LEMBU SORA** _\[CH-04, ekspresi: penuh kasih, api unggun\]:_

_"Kamu tahu kenapa aku masih hidup setelah belasan perang? Bukan karena aku paling kuat. Tapi karena aku tahu kapan harus maju dan kapan harus diam."_

**RANGGALAWE:** _"Apakah ada saatnya diam adalah pengkhianatan, Paman?"_

**LEMBU SORA** _\[diam panjang, ekspresi: konflik batin\]: "Itu pertanyaan yang akan menjawab dirinya sendiri nanti."_

**\[PILIHAN C\] KEBO ANABRANG** _\[CH-06, ekspresi: dingin-respek, stance tempur\]:_

_"Bagus. Di darat kamu tangguh. Tapi ingat - setiap orang punya tempat di mana ia paling lemah."_

**RANGGALAWE:** _"Termasuk kamu?"_

**KEBO ANABRANG** _\[tertawa singkat, pertama kali\]: "Tidak ada yang tidak bisa dipikirkan jawabannya. Termasuk pertanyaan itu."_

**Transisi:** → D05

**SCENE D05 - SIASAT MASUK KE KEDIRI** ⑂

**Tipe Node:** SPLIT-MERGE

**Lokasi:** INT. Pendopo Kamp Hutan Tarik - Pagi

**📦 ASET: BG-06 (Kamp Hutan Tarik - Siang) | BGM-03 | Item: Dokumen Prasasti (jika C)**

**🎭 Arya Wiraraja** \[CH-02 | NPC Wajib\]

**🎭 Raden Wijaya** \[CH-03 | NPC Wajib\]

### **Deskripsi**

Rapat strategi. Peta kasar terbentang di meja kayu. Wiraraja menguraikan rencana: berpura-pura tunduk kepada Jayakatwang, masuk ke Kediri sebagai "pengabdi yang kalah", siapkan kejatuhan dari dalam.

### **Narasi VO**

_"Untuk pertama kalinya, ia melihat betapa besar rencana yang sedang dimainkan. Bukan hanya soal perang - ini soal siapa yang bisa berpura-pura paling meyakinkan."_

### **Catatan Naratif Adaptif**

_Opsi yang tersedia bergantung pada modal D01. Modal TIBA PERTAMA membuka peran utusan langsung. Modal 200 PRAJURIT membuka leverage tawar. Modal INFO TERSEMBUNYI membuka akses infiltrasi lebih dalam. Namun semua pilihan di bawah tetap tersedia sebagai pilihan "karakter saat ini" - hanya teksnya yang sedikit berbeda berdasarkan konteks._

### **Percabangan D05**

**A \[Konfrontasi +1\].** "Hamba siap. Ini rencana yang brilian. Hamba akan menjadi utusan pribadi Tuanku di Kediri." - Penuh semangat.

_➤ Dampak: Akses informasi internal Kediri lebih cepat saat D06. Kebijakan+10 Keberanian+5_

**B \[Mediasi +1\].** "Hamba setuju. Tapi hamba minta jaminan keamanan Hutan Tarik selama hamba pergi." - Terencana dan bertanggung jawab.

_➤ Dampak: Posisi tawar lebih kuat karena 200 prajurit tetap siaga. Kehormatan+10 Kebijakan+15_

**C \[Siasat +1\].** "Izinkan hamba ikut langsung ke Kediri - hamba sudah tahu rencananya dan bisa mengantisipasi dari dalam." - Kalkulatif.

_➤ Dampak: Informasi lebih lengkap. Kehormatan sedikit turun karena siasat aktif. Loyalitas+20 Keberanian+10 Kebijakan-5_

**Transisi:** → D06 (Bottleneck)

**SCENE D06 - DI DALAM SARANG MUSUH** ◆

**Tipe Node:** BOTTLENECK - Peristiwa Sejarah Wajib

**Lokasi:** INT. Istana Kediri | EXT. Alun-alun Kediri - Berminggu-minggu

**📦 ASET: BG-08 (Kediri - Alun-alun) | BG-09 (Kediri - Dalam Istana) | BGM-04 (Kediri - Bayangan Musuh) | SFX-07**

**🎭 Raden Wijaya** \[CH-03 | ekspresi: waspada, berpura-pura tunduk\]

**🎭 Nambi** \[CH-05 | di latar, selalu dekat Wijaya\]

### **Narasi VO - Bottleneck**

_"Raden Wijaya diterima Jayakatwang dengan tangan terbuka. Berminggu-minggu mereka bersandiwara - tunduk, menghormati, menyiapkan kejatuhan dari dalam. Ranggalawe bolak-balik antara Madura, Tarik, dan Kediri."_

### **Monolog Batin - Adaptif**

_"Setiap kali aku masuk ke Kediri, aku melihat hal yang sama: Nambi. Selalu di sisi Raden Wijaya. Selalu diberi kepercayaan yang aku tidak tahu darimana asalnya. Sementara aku bekerja di balik layar - tanpa tepuk tangan, tanpa pengakuan."_

### **Catatan Naratif Adaptif**

_Tidak ada pilihan. Namun nada monolog batin berubah tipis: jika Siasat dominan, Ranggalawe mengamati dengan lebih kalkulatif. Jika Konfrontasi dominan, ada frustrasi yang mulai mengendap. Jika Mediasi dominan, ia mencoba memahami logika kepercayaan yang diberikan kepada Nambi._

**Transisi:** → D07

**SCENE D07 - SUB-ARC MADURA: MODAL D01 BERGEMA** ⑂ ★

**Tipe Node:** SPLIT EKSKLUSIF - NPC berbeda per jalur

**Lokasi:** Bervariasi per jalur - dalam perjalanan bolak-balik Madura-Tarik

**📦 ASET: BG-03 (Pelabuhan Sumenep, jalur A) | BG-06 (Kamp Tarik, jalur B) | BG-02 (Arsip Sumenep, jalur C) | BGM sesuai lokasi**

**🎭 \[JALUR A\] Nyai Sembada** \[CH-13 | NPC Opsional | ekspresi: ramah → serius\]

**🎭 \[JALUR B\] Komandan Garda Madura** \[CH-16 | NPC Wajib B | ekspresi: khawatir\]

**🎭 \[JALUR C\] Arsip Sumenep (NPC minor)** \[Tidak ada sprite - eksplorasi dokumen\]

### **Catatan Naratif Adaptif**

_Ini adalah scene EKSKLUSIF per jalur. Player di jalur A tidak bisa melihat konten jalur B atau C. Insentif replay. Semua scene memberi modal berbeda yang bergema di Babak III._

### **\[JALUR A\] Nyai Sembada - Pelabuhan Sumenep**

**NYAI SEMBADA** _\[CH-13, ekspresi: serius, tepi dermaga\]:_

_"Anak Wiraraja? Kamu tidak kenal aku, tapi aku kenal ayahmu sejak lama. Ada yang perlu kamu tahu tentang jaringan yang ia bangun - jaringan yang bahkan kamu tidak tahu ada."_

**RANGGALAWE:** _"Jaringan apa?"_

**NYAI SEMBADA:** _"Nelayan-nelayan ini... mereka bukan sekadar nelayan. Mereka telinga Wiraraja di seluruh pesisir Jawa."_

_\[Kebijakan+10\] Quest Q-02 selesai. Info jaringan rahasia berguna di Babak III jalur A._

### **\[JALUR B\] Komandan Garda Madura - Kamp Tarik**

**KOMANDAN GARDA** _\[CH-16, ekspresi: khawatir, armor penuh\]:_

_"Ranggalawe, ada masalah. Beberapa prajurit mulai ragu. Mereka tidak tahu apakah Raden Wijaya benar-benar akan menang - atau apakah kita hanya mengorbankan diri untuk yang tidak pasti."_

**RANGGALAWE:** _"Kumpulkan mereka. Malam ini aku bicara langsung."_

_\[Loyalitas Prajurit+15\] Quest Q-03 selesai. Bonus koordinasi di D10._

### **\[JALUR C\] Arsip Sumenep - Penelusuran Dokumen**

**NARASI (V.O.)** _\[sambil menampilkan sprite gulungan surat\]:_

_"Di antara gulungan-gulungan tua itu, ada satu surat yang tidak pernah disebutkan Wiraraja. Ditujukan kepada seseorang yang namanya tidak Ranggalawe kenal - tapi dengan isi yang mengubah cara ia melihat seluruh permainan ini."_

**RANGGALAWE (V.O.):** _"Ayahku memainkan lebih banyak papan catur dari yang aku kira."_

_\[Kebijakan+15\] Item: Surat Ketiga Wiraraja didapat. Modal krusial untuk hadapi Ra Galatik di D17-C._

**Transisi:** → D08 (Babak II)

# **BABAK II - RISING ACTION: Darah untuk Majapahit (1293 M)**

_Kamp Hutan Tarik, Medan Jongbiru, Kediri, Trowulan_

**SCENE D08 - KEPUTUSAN BESAR: MANFAATKAN TARTAR** ⑂

**Tipe Node:** SPLIT-MERGE

**Lokasi:** INT. Pendopo Kamp Hutan Tarik - Pagi

**📦 ASET: BG-06 (Kamp Hutan Tarik - Siang) | BGM-03 | Cutscene: pasukan Mongol di pesisir**

**🎭 Raden Wijaya** \[CH-03 | ekspresi: tegas, berdiri\]

**🎭 Lembu Sora** \[CH-04 | ekspresi: serius, duduk\]

**🎭 Kebo Anabrang** \[CH-06 | ekspresi: dingin, bersila\]

### **Narasi VO**

_"20.000 prajurit Mongol mendarat di pantai utara Jawa. Mereka datang menuntut balas atas penghinaan terhadap utusan mereka yang dibunuh Kertanegara. Semua orang di kamp ini tahu: ini adalah saat yang tidak akan datang dua kali."_

### **Dialog - Raden Wijaya**

**RADEN WIJAYA** _\[CH-03, ekspresi: tegas, berdiri di depan peta\]:_

_"Dua puluh ribu prajurit Mongol datang menuntut balas atas penghinaan terhadap utusan mereka. Ini bukan ancaman - ini kesempatan. Kita sekutui mereka, gunakan untuk menghancurkan Kediri, lalu usir setelah selesai."_

### **Catatan Naratif Adaptif**

_Jika akumulasi sebelumnya lebih ke Siasat: Ranggalawe sudah memikirkan langkah pengusiran bahkan sebelum dialog ini muncul. Jika lebih ke Konfrontasi: ia langsung setuju tanpa kalkulasi panjang. Jika lebih ke Mediasi: ia langsung bertanya soal rencana jangka panjang._

### **Percabangan D08**

**A \[Konfrontasi +1\].** "Tuanku, ini saat yang tidak akan datang dua kali. Kita harus bergerak sekarang, sebelum mereka mengubah pikiran." - Tidak ada keraguan.

_➤ Dampak: Reputasi keberanian tinggi. Kertarajasa nilai Ranggalawe sebagai figur tak terkontrol. Keberanian+15 Loyalitas+10_

**B \[Mediasi +1\].** "Hamba setuju, Tuanku. Tapi setelah Kediri jatuh, kita harus sudah punya rencana mengusir mereka. Kalau tidak, kita hanya mengganti satu penjajah dengan yang lain." - Berpikir jauh.

_➤ Dampak: UNLOCK: Rencana usir Tartar di D12 lebih matang. Kertarajasa catat Ranggalawe sebagai pemikir strategis. Kebijakan+20 Kehormatan+10_

**C \[Siasat +1\].** "Izinkan hamba yang memimpin garis depan bersama pasukan Tartar. Hamba akan membangun relasi dengan komandan mereka - berguna nanti." - Kalkulatif.

_➤ Dampak: UNLOCK: Relasi komandan Tartar. Leverage lebih besar di D12. Kertarajasa khawatir Ranggalawe terlalu dekat kekuatan asing. Keberanian+20 Loyalitas+15 Kebijakan-5_

**Transisi:** → D09

**SCENE D09 - PERSIAPAN PERANG: DUA PERSPEKTIF** ⟺

**Tipe Node:** PARALLEL - Tidak ada pilihan

**Lokasi:** EXT. Kamp Hutan Tarik (kiri) | INT. Pendopo Sumenep (kanan) - Beberapa hari

**📦 ASET: BG-06 & BG-02 split screen | BGM-03 & BGM-02 bergantian | SFX-07**

**🎭 Ranggalawe** \[CH-01 | ekspresi: determinasi, melatih pasukan\]

**🎭 Lembu Sora** \[CH-04 | ekspresi: tegas, mengawasi\]

**🎭 Arya Wiraraja** \[CH-02 | ekspresi: ambigu, menulis surat\]

### **Cutscene Paralel**

**LAYAR KIRI - RANGGALAWE DI KAMP:**

_Ranggalawe melatih prajurit setiap pagi. Memimpin dengan contoh, bukan perintah. Tidak tidur dua hari sebelum pertempuran._

**LEMBU SORA** _\[berbisik ke Ranggalawe, ekspresi: bijak\]:_

_"Kamu tahu cara perang yang baik bukan dari serangan pertama, tapi dari cara kamu pulang."_

**RANGGALAWE (V.O.):** _"Aku tidak pernah memikirkan pulang. Apakah itu kekuatan atau kebodohan, aku belum tahu."_

**LAYAR KANAN - WIRARAJA DI SUMENEP:**

_Arya Wiraraja duduk sendirian, menulis surat terakhir untuk Jayakatwang - sanjungan palsu terakhir._

**WIRARAJA** _\[bergumam, ekspresi: berat\]:_

_"Jayakatwang yang terhormat... semoga kamu tidak pernah tahu berapa banyak kebohongan yang aku tulis atas namamu."_

**Transisi:** → D10

**SCENE D10 - PERTEMPURAN DI JONGBIRU** ⑂ ◆

**Tipe Node:** SPLIT-MERGE + SEGMEN PERANG

**Lokasi:** EXT. Medan Jongbiru - Siang

**📦 ASET: BG-17 (Medan Perang Tuban, adaptasi Jongbiru) | BGM-07 (Tema Perang) | SFX-01 SFX-02 FX-04**

**🎭 Lembu Sora** \[CH-04 | ekspresi: combat stance\]

**🎭 Kebo Anabrang** \[CH-06 | ekspresi: combat heavy\]

### **Narasi VO**

_"Pertempuran besar. Pasukan Majapahit dan Tartar bergerak. Ini bukan latihan. Di atas tanah Jongbiru, sejarah Majapahit mulai ditulis dengan darah."_

### **Catatan Naratif Adaptif**

_Sebelum memilih taktik, Lembu Sora bertanya. Cara Ranggalawe menjawab mencerminkan akumulasi sebelumnya: jika dominan Konfrontasi, ia tidak perlu berpikir panjang. Jika dominan Mediasi, ada momen ragu sebelum menjawab. Jika dominan Siasat, ia sudah merencanakan sebelum Lembu Sora bertanya._

### **Percabangan D10**

**A \[Konfrontasi +1\].** \[kepada Lembu Sora\] "Jika aku menerobos langsung, seluruh barisan mereka akan runtuh. Serangan frontal. Ikut aku." - Berani.

_➤ Dampak: Reputasi keberanian tinggi. Kertarajasa nilai Ranggalawe sebagai figur sulit dikendalikan. Keberanian+20 Kehormatan+10 Kebijakan-5_

**B \[Mediasi +1\].** \[kepada Lembu Sora\] "Biarkan yang lain menyerang dari depan. Kita kepung sayap kanan - potong jalur mundur mereka." - Terencana.

_➤ Dampak: Reputasi strategis. Kertarajasa kagum tapi nilai Ranggalawe tidak ingin sorotan. Kebijakan+20 Keberanian+10_

**C \[Siasat +1\].** \[kepada Komandan Tartar melalui penerjemah\] "Serangan simultan dari dua arah. Kamu dari barat, aku dari timur. Pada hitungan genderang ketiga." - Presisi.

_➤ Dampak: Relasi Tartar kuat. Leverage besar di D12. Kertarajasa khawatir terlalu dekat kekuatan asing. Kebijakan+15 Loyalitas+10_

**Transisi:** → D11

**SCENE D11 - KEDIRI JATUH** ◆

**Tipe Node:** BOTTLENECK - Peristiwa Sejarah Wajib

**Lokasi:** EXT./INT. Kota Kediri - Siang hingga Sore

**📦 ASET: BG-08 BG-09 (Kediri) | BGM-07 | FX-03 FX-04 | SFX-01 SFX-02 SFX-03 | CG (opsional): Kediri Jatuh**

**🎭 Lembu Sora** \[CH-04 | ekspresi: combat stance → kemenangan\]

**🎭 Jayakatwang** \[Sprite minor | ekspresi: menyerah\]

### **Cutscene Wajib - Tidak Bisa Diubah**

_Lembu Sora mengalahkan Patih Mundharang dalam duel. Jayakatwang menyerah. Kerajaan Kediri runtuh dalam satu hari. Majapahit lahir dari abu kemenangan ini._

### **Narasi VO**

_"Hari itu Majapahit lahir. Tapi Ranggalawe berdiri di pinggir kemenangan yang bukan miliknya - orang yang melakukan paling banyak, diingat paling sedikit."_

### **Dialog Emosional**

**LEMBU SORA** _\[kepada Ranggalawe, ekspresi: kemenangan-lelah\]: "Kita menang, keponakanku."_

**RANGGALAWE** _\[(menatap punggung Raden Wijaya yang sudah dikelilingi orang banyak), ekspresi: ambigu\]: "Ya. Kita menang."_

### **Catatan Naratif Adaptif**

_Kata "Ya. Kita menang." diucapkan dengan nada berbeda berdasarkan akumulasi: jika Konfrontasi dominan - bangga tapi ada duri kecil frustrasi. Jika Mediasi dominan - ada pertanyaan yang belum terjawab. Jika Siasat dominan - sudah mengantisipasi momen ini dan mulai memikirkan langkah berikutnya._

**Transisi:** → D12

**SCENE D12 - SIASAT MENGUSIR TARTAR** ⑂

**Tipe Node:** SPLIT-MERGE

**Lokasi:** INT. Kamp Trowulan - Malam

**📦 ASET: BG-15 (Trowulan - Balai Sidang) | BGM-06 | SFX-04**

**🎭 Lembu Sora** \[CH-04 | ekspresi: serius\]

**🎭 Komandan Tartar** \[Sprite minor | ekspresi: dingin\]

### **Narasi VO**

_"Pasukan Tartar masih ada. Kertarajasa tidak bisa mengusir mereka dengan kekuatan langsung - terlalu berbahaya. Rapat kecil antara Ranggalawe, Lembu Sora, dan beberapa komandan. Cara mengusir Tartar ini akan membentuk reputasi Ranggalawe di mata raja."_

### **Catatan Naratif Adaptif**

_Jika D08-B aktif: Ranggalawe sudah memiliki rencana usir yang lebih matang. Jika D10-C aktif: ada leverage relasi dengan komandan Tartar. Pilihan yang tersedia sama, tapi dialog pembuka Ranggalawe sedikit berbeda mencerminkan persiapan sebelumnya._

### **Percabangan D12**

**A \[Siasat +1\].** "Kita adakan pesta besar. Arak, gamelan, hidangan - biarkan mereka lengah. Saat pesta paling meriah, kita sergap dari semua sisi." - Licik tapi efektif.

_➤ Dampak: Sangat efektif. Kertarajasa: "Ranggalawe terlalu licik untuk jabatan tertinggi." Kehormatan-10 Kebijakan+20_

**B \[Mediasi +1\].** "Lembu Sora yang paling bisa mereka percaya - ia tidak terlihat mengancam. Paman yang pimpin tipu daya. Aku siaga di luar." - Delegasi dengan kepercayaan.

_➤ Dampak: Lembu Sora dapat pengakuan. Loyalitas Sora naik. Kertarajasa: "Tidak cukup tegas untuk Patih." Kehormatan+10 Loyalitas(Sora)+15_

**C \[Konfrontasi +1\].** "Aku tantang komandan Tartar dalam duel terbuka. Jika aku menang, mereka pergi sebagai penghormatan atas kekalahan pemimpin mereka." - Berani habis.

_➤ Dampak: Jika menang: nama melegenda. Kertarajasa TAKUT - Ranggalawe terlalu populer. Keberanian+25 Kehormatan+20 Kebijakan-15_

**Transisi:** → D13

**SCENE D13 - TARTAR TERUSIR - MAJAPAHIT MERDEKA** ◆

**Tipe Node:** BOTTLENECK - Peristiwa Sejarah Wajib

**Lokasi:** EXT. Pesisir Jawa Utara | INT. Balai Trowulan - Hari Penobatan

**📦 ASET: BG-14 (Trowulan - Istana) | BGM-06 | FX-05 | CG: Upacara Penobatan (opsional)**

**🎭 Kertarajasa** \[CH-03 kostum mahkota | ekspresi: berwibawa\]

**🎭 Lembu Sora** \[CH-04 | ekspresi: tegas-bangga\]

**🎭 Nambi** \[CH-05 | ekspresi: dingin-ambigu, dekat raja\]

### **Narasi VO - Bottleneck**

_"Pasukan Tartar mundur dari pesisir Jawa. Majapahit benar-benar merdeka. Kertarajasa dinobatkan sebagai raja pertama Majapahit. Upacara besar di Trowulan. Dan Ranggalawe hadir - tapi posisinya mulai ambigu. Nambi lebih dekat dari sebelumnya ke raja."_

### **Detail Emosional**

_Ranggalawe menyaksikan dari barisan belakang upacara. Di sisinya Lembu Sora. Di sisi raja: Nambi. Detail kecil yang tidak bisa ia abaikan._

**RANGGALAWE (V.O.):** _"Aku membantu mendirikan ini. Tapi ada yang mengisi ruang di sisi raja yang aku pikir akan ada namaku."_

**Transisi:** → D14

**SCENE D14 - KONSEKUENSI CARA MENGUSIR TARTAR** ◆ ★

**Tipe Node:** INFORMATIF - Reputasi Terbentuk

**Lokasi:** INT. Balai Audiensi Trowulan - Sehari setelah penobatan

**📦 ASET: BG-15 (Trowulan - Balai Sidang) | BGM-06 | SFX-04**

**🎭 Pejabat Istana** \[Sprite minor\]

### **Deskripsi**

Ranggalawe dipanggil untuk audiensi singkat. Bukan oleh raja langsung - tapi oleh pejabat yang menyampaikan pesan raja. Cara pesan itu disampaikan sudah cukup mengatakan segalanya.

### **Pesan Per Akumulasi D12**

**\[Jalur A - "Terlalu licik"\]:** _Pejabat menyampaikan dengan nada datar bahwa raja menghargai "kreativitas strategi" Ranggalawe, namun mengingatkan bahwa "cara yang terlalu tidak terduga bisa menciptakan ketidakpastian di antara sekutu."_

**\[Jalur B - "Tidak cukup tegas"\]:** _Pejabat menyampaikan bahwa raja menghargai "kerendahan hati" Ranggalawe. Tapi keputusan besar membutuhkan sosok yang "bisa berdiri di garis depan tanpa mendelegasikan."_

**\[Jalur C - "Terlalu populer"\]:** _Pejabat tidak menyampaikan apapun yang negatif secara langsung. Tapi Ranggalawe melihat: Nambi berdiri jauh di belakang raja, menatap dengan ekspresi yang tidak bisa ia baca._

### **Catatan Naratif Adaptif**

_Tidak ada pilihan di scene ini. Ini adalah informasi kontekstual yang membantu player memahami "mengapa" Nambi dipilih - bukan karena ia lebih baik, tapi karena ia lebih aman bagi raja._

**Transisi:** → D15 (Babak III)

# **BABAK III - KLIMAKS: Duri di Mahkota Majapahit (W-SHAPE)**

_Tuban, Trowulan - W-Shape Branching dimulai dari D16_

**SCENE D15 - KEHIDUPAN SEBAGAI ADIPATI TUBAN** ↪ ⑂

**Tipe Node:** DETOUR OPSIONAL - Sumber Daya Epilog

**Lokasi:** EXT./INT. Kadipaten Tuban - Beberapa Tahun Kemudian

**📦 ASET: BG-11 (Kadipaten Tuban - Pendopo) | BG-12 (Pasar Tuban) | BGM-05 (Tuban - Kota Ksatria) | SFX-06 (Ambient Laut)**

**🎭 Ra Jaran Waha** \[CH-10 | NPC Opsional | ekspresi: setia\]

**🎭 Pedagang Garam Tuban** \[CH-15 | NPC Opsional\]

### **Narasi VO**

_"Beberapa tahun berlalu. Ranggalawe mendapat Tuban sebagai hadiah atas jasanya. Ia adalah Adipati Tuban sekarang. Tapi hadiah bisa terasa seperti pengasingan, tergantung cara kamu melihatnya."_

### **Catatan Naratif Adaptif**

_Jika dominan Konfrontasi sebelumnya: Ranggalawe melihat Tuban sebagai benteng, bukan hadiah. Jika dominan Mediasi: ia membangun Tuban dengan musyawarah, mencari harmoni. Jika dominan Siasat: ia melihat Tuban sebagai basis kekuatan yang perlu dioptimalkan._

### **Percabangan D15 - Opsional, bisa skip ke D16**

**A \[Siasat +1\].** "Bayar upeti sambil siapkan argumen hukum tertulis berdasarkan Prasasti Sima. Jika nanti ada konflik, aku punya dasar hukum." - Berjaga-jaga.

_➤ Dampak: UNLOCK: Dokumen Hukum aktif di D19. Ditemukan setelah kematian Ranggalawe di D29. Kebijakan+15 Kehormatan+10_

**B \[Konfrontasi +1\].** "Tolak pembayaran - tunggu respons resmi Trowulan dulu. Aku ingin tahu seberapa serius mereka soal hak adipati." - Berani.

_➤ Dampak: Posisi hukum kuat tapi memancing eskalasi lebih cepat. Kehormatan+15 Keberanian+10 Kebijakan-5_

**C \[Mediasi +1\].** "Kumpulkan kepala desa - musyawarah rakyat Tuban. Keputusan besar harus diputuskan bersama." - Demokratis.

_➤ Dampak: UNLOCK: Loyalitas Rakyat Tuban sangat tinggi. Bonus pertahanan D21. Aktifkan D39 setelah kematian. Kehormatan+20 Loyalitas Rakyat+20_

**Transisi:** → D16 (W-Shape Merge Pertama)

**SCENE D16 - NAMBI DIANGKAT SEBAGAI PATIH AMANGKUBUMI** ◆ W-MERGE

**Tipe Node:** BOTTLENECK + W-SHAPE MERGE PERTAMA

**Lokasi:** EXT. Pelabuhan Tuban - Sore (semua jalur bertemu di sini)

**📦 ASET: BG-10 (Pelabuhan Tuban) | BGM-05 → fade | SFX-06 | CG: Ranggalawe di Dermaga (VN-CG-03)**

**🎭 Kurir Istana** \[Sprite minor | NPC Wajib\]

**🎭 Ranggalawe** \[CH-01 | ekspresi: terkejut → sedih → marah\]

### **Cutscene Wajib - W-MERGE PERTAMA**

_Semua jalur A/B/C bertemu di scene ini. Ranggalawe di pelabuhan Tuban menerima surat dari Trowulan. Nambi diangkat Patih Amangkubumi._

### **Narasi VO**

_"Surat itu tidak panjang. Tapi beratnya terasa seperti seluruh Majapahit ditaruh di atas telapak tangannya."_

**KURIR ISTANA:** _"Dari Yang Mulia Kertarajasa. Beliau mengumumkan pengangkatan Nambi sebagai Patih Amangkubumi Kerajaan Majapahit."_

**RANGGALAWE** _\[(duduk di tepi dermaga, menatap laut), ekspresi: sedih-marah\]: "Namanya tidak ada. Bukan Ranggalawe. Bukan Lembu Sora. Nambi."_

### **Catatan Naratif Adaptif**

_Ekspresi Ranggalawe di scene ini berbeda berdasarkan akumulasi. Jika Konfrontasi dominan: langsung marah, ingin bergerak. Jika Mediasi dominan: ada diam yang panjang, mencoba memahami. Jika Siasat dominan: dingin, mulai menghitung langkah. Jika nilai seimbang: konflik batin yang paling jelas - ia tidak tahu harus merasakan apa._

**Transisi:** → D17 (W-SHAPE SPLIT KEDUA - Tiga Jalur Eksklusif)

**SCENE D17 - API DALAM DADA: RESPONS PERTAMA** ⑂ W-SHAPE ★

**Tipe Node:** W-SHAPE SPLIT KEDUA - Konten Eksklusif per Jalur

**⚠️ W-SHAPE SPLIT KEDUA:** Tiga jalur membawa Exclusive Content yang TIDAK BISA diakses dari jalur lain. Ini adalah insentif utama untuk replay.

### **═══ JALUR A: KONFRONTASI LANGSUNG ═══**

**Lokasi:** INT. Istana Trowulan - Balai Sidang

**📦 ASET: BG-15 (Trowulan - Balai Sidang) | BGM-06 | SFX-04**

**🎭 Kertarajasa** \[CH-03 kostum mahkota | ekspresi: ragu → tegas\]

**🎭 Mahapati** \[CH-07 | ekspresi: tersenyum licik (di latar)\]

**RANGGALAWE** _\[CH-01, datang sendiri, ekspresi: marah\]: "Mengapa Nambi? Ia tidak pernah menumpahkan darah untuk kerajaan ini."_

**KERTARAJASA** _\[CH-03, ekspresi: ragu-tegas\]: "Keputusan ini bukan untuk diperdebatkan."_

**RANGGALAWE:** _"Hamba tidak bermaksud memperdebatkan. Hamba bermaksud memahami - apakah ada yang hamba lewatkan selama ini?"_

_\[INFO EKSKLUSIF A\]: Ranggalawe melihat ekspresi Mahapati - tipis, hampir tidak terlihat - tapi ia tahu. Mahapati adalah dalang di balik ini. Mahapati bergerak hari itu. Ultimatum 3 hari._

**Kemarahan+20 Kehormatan+10 → D17-A★ EKSKLUSIF terbuka.**

### **★ D17-A★ EKSKLUSIF - Surat Gelap Mahapati**

_Seorang pelayan istana diam-diam mendekati Ranggalawe sebelum ia pergi. Dengan ekspresi ketakutan, pelayan itu menyelipkan satu gulungan kecil._

**PELAYAN ISTANA** _\[berbisik\]: "Tuan... hati-hati. Ini dari dalam. Isinya... berbahaya."_

_\[Item diterima: Surat Gelap Mahapati - amplop hitam, segel merah. Isi: fitnah bahwa Ranggalawe sudah menyiapkan kudeta.\]_

_EFEK: Di D27, terbuka Opsi D eksklusif - serahkan surat ke Lembu Sora sebelum mati._

**📦 ASET: Item: Surat Gelap Mahapati (32x24px, amplop hitam segel merah)**

### **═══ JALUR B: MEDIASI LEMBU SORA ═══**

**Lokasi:** INT. Pendopo Tuban - Malam (mengirim Lembu Sora, menunggu di Tuban)

**📦 ASET: BG-11 (Kadipaten Tuban - Pendopo) | BGM-05 sendu | SFX-04**

**🎭 Nambi** \[CH-05 | kunjungan rahasia malam | ekspresi: ragu → tulus (tersembunyi)\]

**🎭 Lembu Sora** \[CH-04 | pergi sebagai utusan\]

**★ D17-B★ EKSKLUSIF - Lobi Rahasia Nambi:**

_Malam hari, Nambi datang sendiri ke Tuban - tanpa pengawal, tanpa pakaian resmi._

**NAMBI** _\[ekspresi: ragu-tulus\]: "Aku tidak datang sebagai Patih. Aku terjebak juga. Mahapati yang mengusulkan namaku - aku tidak meminta ini."_

**\[B1 - Percaya Nambi\] \[Mediasi +1\]:** _"Jika kamu serius, aku percaya. Tapi buktikan nanti, bukan sekarang." → Kesepakatan rahasia. Di D25: Nambi tunda pasukan 2 jam. Kebijakan+15 Kehormatan+5_

**\[B2 - Netral\] \[Siasat +1\]:** _"Jika kamu serius, buktikan dengan tindakan, bukan kata-kata." → Tidak membantu tapi tidak mengkhianati. Kehormatan+10 Kebijakan-5_

**\[B3 - Gunakan Nambi\] \[Siasat +1\]:** _"Baik, aku percaya. (beri info posisi pasukan yang salah)" → Mahapati dapat info palsu - strategi musuh kacau di D23/D24. Kehormatan-15 Kebijakan+20_

### **═══ JALUR C: MOBILISASI DIAM-DIAM ═══**

**Lokasi:** EXT. Pegunungan Utara Tuban - Malam

**📦 ASET: BG-13 (Pegunungan Utara Tuban) | BGM-05 gelap | FX-02 (Kabut Hutan)**

**🎭 Ra Galatik** \[CH-08 | NPC Wajib C | ekspresi: gugup → pengkhianat\]

**🎭 Ra Lintang** \[CH-09 | ekspresi: battle ready\]

**★ D17-C★ EKSKLUSIF - Pengkhianat Ra Galatik:**

_Ranggalawe diam, tidak bersuara ke luar. Konsolidasi pasukan pegunungan. Tapi Ra Jaran Waha melapor: ada kebocoran informasi. Ra Galatik - orang kepercayaan - adalah mata-mata Mahapati._

**\[C1 - Tangkap\] \[Konfrontasi +1\]:** _"Tangkap Ra Galatik - hukum sebagai pengkhianat." → Rantai mata-mata Mahapati terputus. Di D23: pasukan musuh lebih kecil dari perkiraan. Kehormatan+10 Kebijakan+5_

**\[C2 - Gunakan\] \[Siasat +1\]:** _"Biarkan bebas tapi beri dia info palsu melalui Ra Galatik." → Mahapati salah baca strategi. Efek kacau di D24. Kebijakan+20 Kehormatan-10_

**\[C3 - Ampuni\] \[Mediasi +1\]:** _"Kamu tidak harus memilih sisi itu. Aku tawarkan pengampunan." → Ra Galatik berbalik. Info intelijen rencana Mahapati terbuka. Kehormatan+15 Kebijakan+15_

**Transisi:** → D18 (semua jalur D17 konvergen)

**SCENE D18 - MALAM YANG MEMBELAH** ⟺

**Tipe Node:** PARALLEL - Refleksi Sebelum Eskalasi

**Lokasi:** INT. Pendopo Tuban (kiri) | INT. Istana Trowulan (kanan) - Malam

**📦 ASET: BG-11 & BG-15 split screen | BGM-05 fade ke BGM-06 | SFX-04**

**🎭 Lembu Sora** \[CH-04 | ekspresi: konflik batin\]

**🎭 Mahapati** \[CH-07 | ekspresi: puas, di latar Trowulan\]

### **Cutscene Paralel**

**LAYAR KIRI - RANGGALAWE & LEMBU SORA di Tuban:**

_Dua orang berdiri di teras pendopo. Angin malam. Masing-masing menatap ke arah berbeda._

**LEMBU SORA** _\[ekspresi: konflik batin\]: "Masih ada jalan damai, keponakanku. Aku bisa pergi ke Trowulan sekali lagi."_

**RANGGALAWE** _\[tanpa menoleh\]: "Kita sudah melewati batas itu, Paman. Yang tersisa hanya cara kita berdiri di hadapannya."_

**LAYAR KANAN - MAHAPATI di Trowulan:**

_Mahapati menyerahkan laporan kepada Kertarajasa. Tangannya tidak gemetar. Wajahnya tenang._

**MAHAPATI** _\[bergumam, ekspresi: puas\]: "Yang penting: Ranggalawe harus dikategorikan sebagai ancaman. Sisanya... raja yang memutuskan."_

### **Catatan Naratif Adaptif**

_Ekspresi Ranggalawe dalam dialog Lembu Sora berubah berdasarkan akumulasi. Jika Mediasi dominan: ada keraguan nyata sebelum menjawab. Jika Siasat dominan: sudah mengantisipasi percakapan ini. Jika Konfrontasi dominan: nada lebih keras, sudah bertekad._

**Transisi:** → D19

**SCENE D19 - ULTIMATUM DARI TROWULAN** ⑂

**Tipe Node:** SPLIT-MERGE

**Lokasi:** INT. Pendopo Kadipaten Tuban - Pagi

**📦 ASET: BG-11 (Kadipaten Tuban) | BGM-05 | SFX-02 (Surat kertas) | Item: Ultimatum Resmi**

**🎭 Kurir Trowulan** \[Sprite minor | NPC Wajib\]

**🎭 Lembu Sora** \[CH-04 | ekspresi: serius\]

### **Narasi VO**

_"Ultimatum resmi tiba. Ranggalawe diminta mengakui Nambi sebagai Patih dan menyerahkan beberapa wilayah Tuban sebagai tanda tunduk. Ini bukan permintaan. Ini penghinaan yang dibalut kata-kata resmi."_

### **Catatan Naratif Adaptif**

_Jika D15-A aktif (dokumen hukum disiapkan): ada pilihan proklamasi hukum yang terbuka. Jika D17-B1 (percaya Nambi): ada harapan bahwa Nambi mungkin bisa membantu dari dalam. Jika dominan Siasat: Ranggalawe sudah tahu isi ultimatum sebelum dibuka._

### **Percabangan D19**

**A \[Konfrontasi +1\].** \[Jika D15-A aktif\] "Proklamasi otonomi Tuban - lampirkan dokumen Prasasti Sima. Ini jalur hukum, bukan perlawanan bersenjata." - Cerdas.

_➤ Dampak: Jalur hukum resmi terbuka. Kertarajasa harus respons formal - beri sedikit waktu lebih. Kebijakan+15 Kehormatan+10_

**B \[Mediasi +1\].** "Kirim mediator terakhir - satu upaya diplomatik lagi. Lembu Sora atau tokoh netral." - Masih ada harapan.

_➤ Dampak: Lembu Sora atau tokoh netral dikirim. Waktu lebih panjang tapi Mahapati sabotase lagi. Kehormatan+10 Kebijakan+5_

**C \[Konfrontasi +1\].** "Mobilisasi penuh - tidak ada lagi negosiasi. Kita siapkan pertahanan Tuban." - Tegas dan final.

_➤ Dampak: Langsung ke persiapan perang. Kondisi pertahanan lebih matang jika D15-C sudah dilakukan. Keberanian+15 Kehormatan+10_

**Transisi:** → D20

**SCENE D20 - PERANG TIDAK BISA DIHINDARI** ◆

**Tipe Node:** BOTTLENECK

**Lokasi:** EXT./INT. Tuban - Beberapa hari kemudian

**📦 ASET: BG-11 BG-10 (Tuban) | BGM-05 menuju BGM-07 | SFX-03 (tanda bahaya) | Item: Keris Leluhur (Quest Q-10)**

**🎭 Lembu Sora** \[CH-04 | ekspresi: berat, mungkin terakhir kali | NPC Wajib interaksi\]

**🎭 Ra Jaran Waha** \[CH-10 | ekspresi: siap tempur\]

### **Narasi VO**

_"Rekonsiliasi tidak mungkin. Mahapati berhasil menutup semua ruang damai. Kertarajasa kerahkan pasukan. Lembu Sora datang ke Tuban - mungkin untuk terakhir kali sebelum perang pecah."_

### **Dialog Wajib - Lembu Sora**

**LEMBU SORA** _\[CH-04, ekspresi: konflik batin-lelah\]: "Keponakanku... aku sudah coba semua jalan yang aku tahu."_

**RANGGALAWE** _\[adaptif per akumulasi\]:_

_\[Dominan Konfrontasi\] "Aku tahu, Paman. Dan aku tidak menyalahkanmu. Ini pilihan Mahapati - bukan pilihanmu."_

_\[Dominan Mediasi\] "Masih ada satu jalan yang belum kita coba, Paman. Atau sudah tidak ada?"_

_\[Dominan Siasat\] "Aku sudah memperkirakan ini, Paman. Terima kasih sudah berusaha."_

_\[Nilai Seimbang\] (diam panjang) "...Ya. Aku tahu."_

### **Quest Q-10 - Keris Leluhur (Opsional)**

_Ra Jaran Waha menawarkan keris pusaka dari gudang Tuban. Bisa disimpan / diberikan ke Lembu Sora / dibawa ke pertempuran. Jika diberikan ke Lembu Sora: dialog tambahan terbuka di D25._

**📦 ASET: Item: Keris Ranggalawe (16x32px, blade emas-hitam)**

**Transisi:** → D21

**SCENE D21 - STRATEGI PERTAHANAN TUBAN** ⑂

**Tipe Node:** SPLIT-MERGE

**Lokasi:** INT. Pendopo Kadipaten Tuban - Malam (peta pertahanan)

**📦 ASET: BG-11 | BGM-07 mulai pelan | SFX-04**

**🎭 Ra Lintang** \[CH-09 | ekspresi: battle ready | NPC Wajib\]

**🎭 Komandan Pasukan** \[Sprite minor\]

### **Catatan Naratif Adaptif**

_Kondisi pertahanan berbeda berdasarkan pilihan sebelumnya. Jika D15-C (loyalitas rakyat tinggi): rakyat sipil sukarela ikut. Jika D21-C dipilih dan D15-C aktif: momen paling mengharukan - rakyat Tuban berperang untuk adipati mereka._

### **Percabangan D21**

**A \[Siasat +1\].** "Pertahanan di garis pantai. Di pasir, kuda mereka lambat. Di sana, kita sejajar." - Memanfaatkan medan.

_➤ Dampak: Menguntungkan jika pasukan sedikit. Rakyat tidak terekspos langsung. Kebijakan+15 Keberanian+10_

**B \[Siasat +1\].** "Gerilya - serang cepat, mundur ke pegunungan. Biarkan mereka kelelahan." - Efektif dan efisien.

_➤ Dampak: Efektif karena pasukan lebih kecil. Ra Lintang unggul medan. Kehormatan sedikit turun. Kebijakan+20 Kehormatan-5_

**C \[Konfrontasi +1\].** "Hadapi langsung di depan gerbang Tuban. Ksatria tidak bersembunyi." - Kehormatan tertinggi.

_➤ Dampak: Kehormatan tertinggi. Jika D15-C: rakyat sipil sukarela ikut bertempur. Keberanian+25 Kehormatan+20 Kebijakan-15_

**Transisi:** → D22

**SCENE D22 - WAJAH-WAJAH YANG DIKENAL DI GARIS MUSUH** ♥

**Tipe Node:** RELATIONSHIP - Emosional

**Lokasi:** EXT. Medan Sebelum Gerbang Tuban - Fajar

**📦 ASET: BG-17 (Medan Perang) | BGM-07 pelan, mendekat | FX-04 | CG: Pertemuan Terakhir Lembu Sora (VN-CG-04, opsional)**

**🎭 Kebo Anabrang** \[CH-06 | garis depan musuh | ekspresi: dingin\]

**🎭 Lembu Sora** \[CH-04 | latar jauh, sisi berlawanan | ekspresi: konflik batin\]

### **Cutscene Emosional - Tidak Ada Pilihan**

_Pasukan Majapahit tiba. Di garis depan: Kebo Anabrang. Di belakang, jauh: Lembu Sora - pamannya - di sisi berlawanan._

**\[Jika akumulasi A - Konfrontasi dominan\]:** _Ranggalawe menatap Kebo Anabrang. Tahu Mahapati yang mengirimnya. Matanya menyala._

**\[Jika akumulasi B - Mediasi dominan\]:** _Menatap Lembu Sora. Ada sesuatu yang ingin ia katakan dari jarak ini. Ia hanya mengangguk. "Paman sudah berusaha. Aku tahu itu."_

**\[Jika akumulasi C - Siasat dominan\]:** _Waspada. Informasi Ra Galatik memberi gambaran pasukan lebih akurat. Ia menghitung, bukan merasakan._

**\[Jika nilai seimbang\]:** _Ranggalawe menatap dua orang sekaligus. Dua arah yang tidak bisa ia pilih._

**Transisi:** → D23 (Babak IV)

# **BABAK IV - FALLING ACTION: Sungai Tambak Beras (1295 M)**

_Medan Pertempuran Tuban & Sungai Tambak Beras_

**SCENE D23 - PERTEMPURAN PECAH: GELOMBANG PERTAMA** ⑂ ◆

**Tipe Node:** SPLIT-MERGE + SEGMEN PERANG

**Lokasi:** EXT. Medan Pertempuran Tuban - Pagi

**📦 ASET: BG-17 BG-18 (Pantai Tuban - Pertahanan) | BGM-07 penuh | SFX-01 SFX-02 FX-03 FX-04 | FX-03 (percikan air)**

**🎭 Ra Jaran Waha** \[CH-10 | ekspresi: siap tempur | NPC Wajib\]

**🎭 Ra Lintang** \[CH-09 | ekspresi: battle ready\]

### **Narasi VO**

_"Genderang perang. Dua pasukan berhadapan. Ini bukan pertempuran yang bisa dimenangkan - tapi harus dijalani. Karena bagi Ranggalawe, ini bukan soal menang. Ini soal berdiri."_

### **Catatan Naratif Adaptif - Efek Otomatis**

_Sebelum pilihan taktis, efek jalur sebelumnya aktif otomatis:_

_\[Jika D17-B1\] Nambi tunda satu kompi 2 jam - celah terbuka di sisi timur._

_\[Jika D17-B3/C2\] Mahapati panik karena info dimanipulasi - koordinasi musuh kacau._

_\[Jika D17-C1\] Pasukan musuh lebih kecil dari perkiraan - Ra Galatik berhasil dinetralkan._

### **Percabangan D23**

**A \[Konfrontasi +1\].** "Kejutkan mereka sebelum mereka mengejutkan kita. Serangan balik langsung - jangan beri mereka waktu mengatur barisan."

_➤ Dampak: Momentum awal untuk pasukan Tuban. Berisiko jika kekuatan tidak seimbang. Keberanian+20 Kebijakan+10_

**B \[Mediasi +1\].** "Tunggu di ketinggian - biarkan mereka masuk, semakin sulit mundur. Kita pilih medan, bukan mereka."

_➤ Dampak: Efektif maksimalkan medan. Jika D17-B1: Nambi tunda satu kompi 2 jam menjadi keuntungan nyata. Kebijakan+20 Keberanian+5_

**C \[Mediasi +1\].** "Kirim utusan negosiasi terakhir. Ini tidak harus terjadi." - Tahu ini sia-sia, tapi mencoba tetap.

_➤ Dampak: Jika D04-C (latihan Kebo Anabrang): Kebo memberi jeda 1 jam sebagai penghormatan sesama pendekar. Kehormatan+15 Kebijakan+5 Keberanian-5_

**Transisi:** → D24

**SCENE D24 - DI DUA FRONT SEKALIGUS** ⟺

**Tipe Node:** PARALLEL - Medan Perang & Intrik Trowulan

**Lokasi:** EXT. Medan Pertempuran (kiri) | INT. Trowulan (kanan) - Sepanjang hari

**📦 ASET: BG-17 & BG-16 split screen | BGM-07 & BGM-06 bergantian | FX-04 kiri | SFX-04 kanan**

**🎭 Ra Jaran Waha** \[CH-10 | pertempuran\]

**🎭 Mahapati** \[CH-07 | Trowulan, menunggu laporan | ekspresi: puas tersembunyi\]

### **Cutscene Paralel**

**LAYAR KIRI - PERTEMPURAN:**

_Sepanjang hari. Ranggalawe di garis depan. Pasukan Majapahit terdesak di beberapa titik tapi terus datang. Tanpa henti. Seperti laut yang tidak bisa dihentikan._

**LAYAR KANAN - MAHAPATI di TROWULAN:**

**MAHAPATI** _\[menerima laporan, ekspresi: puas\]: "Yang penting: Ranggalawe harus tidak ada lagi setelah ini."_

_Ia tidak berperang. Ia menunggu. Di ruang yang nyaman, dengan secangkir teh yang tidak ia sentuh._

### **Catatan Naratif Adaptif**

_Efek eksklusif jalur muncul di layar kiri. Jika B1 aktif: ada celah pasukan yang terlihat jelas. Jika C1 aktif: pasukan musuh memang lebih sedikit dari yang dilaporkan Mahapati kepada raja._

**Transisi:** → D25

**SCENE D25 - BERTEMU LEMBU SORA DI TENGAH PERTEMPURAN** ♥ ⑂

**Tipe Node:** RELATIONSHIP + SPLIT-MERGE

**Lokasi:** EXT. Sela Pertempuran - Sore

**📦 ASET: BG-17 | BGM-07 fade pelan | CG: Pertemuan Lembu Sora di Perang (VN-CG-04)**

**🎭 Lembu Sora** \[CH-04 | di antara dua garis | NPC Wajib | ekspresi: konflik batin\]

### **Cutscene Emosional**

_Di sela pertempuran, dua orang yang saling mencintai - di sisi berlawanan. Sejenak, pertempuran seolah berhenti di sekitar mereka berdua._

**LEMBU SORA** _\[ekspresi: konflik batin-lelah pasrah\]: "Keponakanku. Masih belum terlambat."_

### **Catatan Naratif Adaptif**

_Jika Quest Q-10 (Keris) diberikan ke Lembu Sora di D20: dialog tambahan terbuka. Lembu Sora mengeluarkan keris itu. "Kamu mau aku kembalikan ini?" Ranggalawe: "Simpan. Sebagai pengingat." Kehormatan+5 tambahan._

### **Percabangan D25 - Menentukan Tindakan Lembu Sora di D30**

**A \[Konfrontasi +1\].** "Paman tahu saya benar. Tapi Paman tetap berdiri di sana." - Jujur, tidak menyerang, tidak membela.

_➤ Dampak: Konfrontasi jujur. Lembu Sora bawa rasa bersalah sangat besar. Di D30: ia akhirnya memberontak juga - korban sistem yang sama. Kehormatan+15 Loyalitas(Sora)-10_

**B \[Mediasi +1\].** "Jika Paman bisa pastikan ini berakhir tanpa lebih banyak darah... aku dengarkan." - Masih memberi celah.

_➤ Dampak: Lembu Sora janjikan pengampunan resmi (tidak bisa ditepati). Di D30: hidup dengan beban tak terampuni. Kebijakan+10 Kehormatan+5 Loyalitas+5_

**C \[Siasat +1\].** "Pergilah, Paman. Jangan paksa aku berhadapan denganmu." - Melindungi, bukan memutus.

_➤ Dampak: Lembu Sora pergi, hati utuh tapi retak. Di D30: jadi penjaga makam Ranggalawe - diam, sendirian. Kehormatan+20 Keberanian+10_

**Transisi:** → D26

**SCENE D26 - DI TEPI SUNGAI TAMBAK BERAS** ◆ 🔒

**Tipe Node:** BOTTLENECK + STAT GATE

**Lokasi:** EXT. Sungai Tambak Beras - Senja

**📦 ASET: BG-19 (Sungai Tambak Beras) | BGM-08 (Tambak Beras - Requiem) | SFX-03 (Percikan Air) | FX-03 | VN-SFX-01 (Gemericik Air Loop)**

**🎭 Kebo Anabrang** \[CH-06 | ekspresi: dingin-respek | NPC Wajib\]

### **Cutscene Dramatis**

_Pasukan Ranggalawe terdesak ke Sungai Tambak Beras. Air sungai mengalir tenang - kontras dengan kekacauan di sekitarnya._

**KEBO ANABRANG** _\[berdiri di tepi, ekspresi: dingin-respek\]: "Ranggalawe! Masuk ke air. Selesaikan ini seperti ksatria."_

### **🔒 STAT GATE - Perjanjian Diam Kebo Anabrang**

_SYARAT: D04-C (latihan bersama Kebo Anabrang DI D04) DAN Kehormatan ≥ 7 saat ini._

_Jika syarat terpenuhi → Node Tersembunyi D26★ terbuka SEBELUM D27._

### **★ D26★ PERJANJIAN DIAM - Konten Tersembunyi**

_Kebo Anabrang tiba-tiba berhenti. Tatapan sesama pendekar - sesuatu yang hanya dipahami dua orang yang sudah berlatih bersama._

**KEBO ANABRANG** _\[berbisik, ekspresi: respek diam\]: "Aku tidak bisa membiarkanmu menang. Tapi aku bisa memberimu satu hal - bertempur dengan martabat, tanpa penonton."_

_Ia mengusir semua prajurit dari tepi sungai._

**\[TERSEMBUNYI - Terima Perjanjian\]:** _"Terima Perjanjian Diam. Masuk ke air berdua. Tidak ada yang menonton." → EFEK ENDING: Kebo Anabrang tidak mati dalam duel ini - meninggal kemudian dari luka berbeda. Ia memberitahu Kertarajasa tentang martabat Ranggalawe. UNLOCK: Variasi Ending B. Kehormatan+25_

**Transisi:** → D27 (Keputusan Terakhir)

**SCENE D27 - KEPUTUSAN TERAKHIR SEORANG KSATRIA** ⑂ ◆

**Tipe Node:** SPLIT-MERGE - Kata-Kata Terakhir

**Lokasi:** EXT. Sungai Tambak Beras - Senja Merah

**📦 ASET: BG-19 | BGM-08 crescendo | SFX-03 FX-03 | VN-VO-02 (Kata-kata Terakhir Ranggalawe) | CG: Gugurnya Ranggalawe (VN-CG-05)**

**🎭 Kebo Anabrang** \[CH-06 | ekspresi: tegas | NPC Wajib\]

**🎭 Lembu Sora** \[CH-04 | jauh di kejauhan | ekspresi: patah\]

### **Catatan Naratif Adaptif - Kata Terakhir per Akumulasi**

_Kata-kata terakhir otomatis per akumulasi dominan, SEBELUM pilihan:_

_\[Dominan Konfrontasi\] "MAHAPATI! Sejarah akan mengingatmu!" - berteriak ke arah Trowulan._

_\[Dominan Mediasi\] Menatap Lembu Sora dari kejauhan. Mengangguk. Tidak ada kata._

_\[Dominan Siasat\] Menatap Ra Galatik di kejauhan - jika C3 aktif, Ra Galatik berdiri di sana. Senyum ironis tipis._

_\[Nilai Seimbang\] Menatap langit. Satu tarikan napas panjang. Tidak ada kata yang cukup._

### **Percabangan D27 - Cara Menghadapi Akhir**

**A \[Konfrontasi +1\].** "Seorang ksatria tidak memilih medan demi keselamatannya sendiri. Masuk ke air." - Tanpa ragu.

_➤ Dampak: Gugur sebagai ksatria sejati. Paling sesuai kode kehormatan Madura. Keberanian+25 Kehormatan+25_

**B \[Mediasi +1\].** "Mundur strategis - cari medan menguntungkan." - Tapi pasukan Majapahit sudah mengepung. Tidak ada jalan.

_➤ Dampak: Tetap gugur, tapi lebih tragis karena sempat mencoba. Tone ending lebih melankolik. Kebijakan+5 Kehormatan+5_

**C \[Konfrontasi +1\].** "Berdiri, berteriak ke langit: Aku tidak melawan Majapahit - aku tidak bisa tinggal diam di depan ketidakadilan! Lalu melompat."

_➤ Dampak: Kematian paling bermakna secara moral. Kata-kata ini diingat rakyat Tuban berabad-abad. Kehormatan+30 Keberanian+20_

**D ★ \[EKSKLUSIF JALUR A - hanya jika D17-A★ aktif\].** "Sebelum masuk air, serahkan surat gelap Mahapati ke Lembu Sora. Paman - ini buktinya. Jangan biarkan Mahapati menang sepenuhnya."

_➤ Dampak: WARISAN KEBENARAN: Beberapa tahun kemudian surat itu menjatuhkan Mahapati. HANYA TERSEDIA jika D17-A★ aktif. Kehormatan+30 Keberanian+20_

**Transisi:** → D28 (Gugur)

**SCENE D28 - RANGGALAWE GUGUR DI TAMBAK BERAS - 1295 M** ◆

**Tipe Node:** BOTTLENECK FINAL - Tidak Bisa Diubah

**Lokasi:** EXT. Sungai Tambak Beras - Senja Merah

**📦 ASET: BG-19 | BGM-08 puncak | SFX-03 FX-03 | FX-05 (transisi gelap perlahan) | CG-05 (full screen)**

**🎭 Kebo Anabrang** \[CH-06 | duel | ekspresi: gugur juga\]

**🎭 Lembu Sora** \[CH-04 | tepi sungai | ekspresi: patah - membeku\]

### **Cutscene Final Wajib - Peristiwa Sejarah**

_Ranggalawe gugur di tangan Kebo Anabrang di Sungai Tambak Beras. Kebo Anabrang sendiri tewas terkena kerisnya sendiri._

_"Dua ksatria. Satu sungai. Satu nasib."_

_Lembu Sora menyaksikan dari tepi, berdiri membeku. Tangannya mengepal. Tidak ada kata._

### **Reaksi NPC per Jalur**

**\[Jalur A\]:** _Kata "Mahapati" mulai menyebar dari mulut ke mulut prajurit Tuban yang masih hidup._

**\[Jalur A★ + D27-D\]:** _Lembu Sora mengepal surat gelap Mahapati di tangannya. Matanya tidak bergerak dari sungai._

**\[Jalur B1\]:** _Nambi menerima kabar sendirian di Trowulan. Ada sesuatu yang berubah dalam matanya - untuk selamanya._

**\[Jalur B★ Perjanjian Diam\]:** _Kebo Anabrang, sebelum pergi, sempat melapor ke raja: "Ranggalawe adalah ksatria terbesar yang pernah kuhadapi."_

**\[Jalur C1\]:** _Ra Galatik berdiri di kejauhan medan. Tidak pernah kembali ke Majapahit setelah hari ini._

### **Narasi Penutup Babak IV**

_"Ada yang pergi dengan kalimat. Ada yang pergi dalam diam. Tapi keduanya tetap pergi - ke tempat yang tidak bisa diikuti oleh siapapun yang masih hidup dan menyesal."_

**Transisi:** → Babak V (Resolusi & Epilog)

# **BABAK V - RESOLUSI: Warisan yang Tidak Bisa Dihapus (Epilog, setelah 1295 M)**

**SCENE D29 - DOKUMEN SIMA: KEMENANGAN SETELAH KEMATIAN** ↪

**Tipe Node:** DETOUR OPSIONAL - Aktif hanya jika D15-A

**Lokasi:** INT. Kadipaten Tuban - Beberapa hari setelah D28 (sudut pandang penerus)

**📦 ASET: BG-11 | BGM-09 (Epilog - Warisan) | Item: Dokumen Prasasti Sima**

**🎭 Ra Jaran Waha** \[CH-10 | NPC Opsional\]

**🎭 Kuda Anjampiani** \[CH-11 | 12 tahun, wajah berduka\]

### **Catatan Naratif**

_HANYA AKTIF jika D15-A (dokumen hukum disiapkan di Babak III). Beberapa hari setelah kematian Ranggalawe._

**A \[Mengirim Dokumen\].** "Kirim dokumen Sima ke Kertarajasa." - Ra Jaran Waha membawanya ke Trowulan.

_➤ Dampak: Kertarajasa membaca lama. 3 bulan kemudian Tuban diakui sebagai Sima. Ranggalawe menang hukum - setelah mati. UNLOCK Epilog D34-A. Kehormatan Warisan+20_

**B \[Simpan untuk Putra\].** "Simpan - berikan ke Kuda Anjampiani." - Warisan untuk putranya.

_➤ Dampak: Putra Ranggalawe tumbuh berbeda - lebih sabar, tidak kalah gigih. UNLOCK Epilog D34-B. Warisan Tuban hidup._

**Transisi:** → D30

**SCENE D30 - LEMBU SORA MENGHADAPI DIRI SENDIRI** ⑂ ♥

**Tipe Node:** RELATIONSHIP - Perspektif Lembu Sora

**Lokasi:** EXT. Makam Ranggalawe, Tuban - Malam

**📦 ASET: BG-20 (Makam Ranggalawe) | BGM-09 | SFX-07 (Ambient Hutan)**

**🎭 Lembu Sora** \[CH-04 | ekspresi: lelah pasrah | perspektif utama scene ini\]

### **Catatan Naratif Adaptif - per Pilihan D25**

**\[D25-A\]:** _Lembu Sora terjebak di antara dua loyalitas. Beberapa tahun kemudian, ia juga memberontak - dan gugur. Korban sistem yang sama. Ia mengulang apa yang dilakukan keponakannya._

**\[D25-B\]:** _Lembu Sora membawa beban tak terampuni sampai akhir. Ia tidak pernah memaafkan dirinya sendiri. Helai kain Ranggalawe ia bawa ke Wiraraja yang sudah tua - Wiraraja menerimanya dengan tangan gemetar, tidak berkata apa-apa._

**\[D25-C\]:** _Lembu Sora menjaga makam Ranggalawe - tinggal di Tuban, diam, sendirian, sampai akhir hayat. Tidak pergi ke mana-mana. Tidak melakukan apa-apa. Hanya ada._

**Transisi:** → D31

**SCENE D31 - MAHAPATI DAN WARISAN INTRIK** ↪

**Tipe Node:** DETOUR OPSIONAL

**Lokasi:** INT. Trowulan - Beberapa bulan kemudian

**📦 ASET: BG-16 (Kediaman Mahapati) | BGM-06 sendu**

**🎭 Mahapati** \[CH-07 | ekspresi: puas → terkejut (jika A★ aktif)\]

### **Narasi Opsional**

_Mahapati tidak menikmati kemenangan lama. Ia disingkirkan dengan cara yang sama: fitnah dan intrik. Karma yang tidak ia antisipasi._

**\[Jika D17-A★ + D27-D - Surat Gelap\]:** _Lembu Sora akhirnya menggunakan surat gelap Mahapati. Raja membacanya. Tidak berkata apa-apa. Tapi minggu berikutnya Mahapati tidak lagi terlihat di istana. "Ranggalawe menang - dengan cara yang tidak pernah ia bayangkan."_

**Transisi:** → D32

**SCENE D32 - SESUDAH RANGGALAWE: DUA VERSI SEJARAH** ⟺

**Tipe Node:** PARALLEL - Naratif

**📦 ASET: BG-14 (Trowulan) & BG-20 (Makam) split screen | BGM-09 | FX-05**

### **Cutscene Paralel Naratif**

**VERSI KERAJAAN:**

_"Ranggalawe dicatat sebagai pemberontak pertama Majapahit. Namanya jadi peringatan. Tapi tanpa Ranggalawe, tidak ada Majapahit untuk memberontak."_

**VERSI TUBAN:**

_"Tidak ada yang menyebutnya pemberontak. Makamnya dijaga. Diucapkan dengan hormat berabad-abad. Ia berperang bukan untuk menjatuhkan mahkota - tapi karena mahkota melupakan janjinya."_

_Pemain tidak memilih. Keduanya benar sekaligus._

**Transisi:** → D33

**SCENE D33 - STATUS HUBUNGAN AKHIR: WARISAN EMOSIONAL** ♥

**Tipe Node:** RELATIONSHIP - Rangkuman

**📦 ASET: VN-UI-06 (Relationship Meter) | BGM-09 | UI-10 (Relationship Status Screen)**

### **Layar Statistik Emosional**

_Rangkuman hubungan yang dibangun sepanjang permainan. Setiap angka mencerminkan pilihan yang dibuat._

**Ranggalawe ↔ Raden Wijaya/Kertarajasa** _- Dari sahabat pelarian ke raja yang takut pada bayangannya sendiri_

**Ranggalawe ↔ Lembu Sora** _- Bervariasi per D25: penyesalan mendalam / beban tak terampuni / penjaga setia_

**Ranggalawe ↔ Arya Wiraraja** _- Ayah yang mencintai dengan cara yang paling rumit_

**Ranggalawe ↔ Rakyat Tuban** _- Tertinggi jika D15-C; warisan tulus yang tidak bisa diperintahkan_

**Ranggalawe ↔ Mahapati** _- Musuh selamanya; tapi siapa yang benar-benar menang?_

**Ranggalawe ↔ Sejarah Majapahit** _- Ambigu - tergantung dari sisi mana kita berdiri_

**Transisi:** → D34

**SCENE D34 - KUDA ANJAMPIANI: SANG PUTRA** ⑂

**Tipe Node:** SPLIT-MERGE - Penutup Narasi

**Lokasi:** EXT. Tepi Laut Tuban - Pagi

**📦 ASET: BG-10 (Pelabuhan Tuban) | BGM-09 | CG-06 (Kuda Anjampiani di Tepi Laut)**

**🎭 Kuda Anjampiani** \[CH-11 | 12 tahun | NPC Wajib | ekspresi: kesedihan → bertekad\]

### **Narasi VO**

_"Kuda Anjampiani berdiri di tepi laut Tuban. Angin sepoi. Ia berusia 12 tahun ketika ayahnya gugur. Ia tidak ingat banyak - tapi ia ingat cara ayahnya berdiri. Selalu menghadap ke depan."_

### **Percabangan D34 - Sudut Pandang Putra**

**A \[Siasat +1\].** "Pergi ke Trowulan, pelajari hukum kerajaan, ajukan klaim warisan ayah." - Meneruskan perjuangan melalui hukum.

_➤ Dampak: Ranggalawe menang secara hukum melalui putranya. Epilog D34-A terbuka. Kehormatan+15 Kebijakan+20_

**B \[Mediasi +1\].** "Ayahku mati karena mencintai tempat ini. Aku akan membuatnya pantas dicintai." - Membangun, bukan berperang.

_➤ Dampak: Warisan Ranggalawe hidup dalam kota yang tumbuh. Rakyat mengenang lewat pembangunan. Kehormatan+10 Loyalitas Rakyat+25_

**C \[Konfrontasi +1\].** "Nama Ranggalawe lebih besar dari Tuban. Aku akan membawanya ke mana aku pergi." - Warisan menyebar.

_➤ Dampak: Kisah Ranggalawe menjadi cerita lintas daerah. Keberanian+15 Kehormatan+10_

**Transisi:** → D35 → D36/D37/D38 (Ending per Jalur)

**SCENE D35 - DUA TAFSIR YANG ABADI** ⟺

**Tipe Node:** PARALLEL - Naratif Terakhir

**📦 ASET: BG-14 & BG-20 split terakhir | BGM-09 fade | FX-05**

### **Cutscene Paralel Naratif Terakhir**

**IA ADALAH PEMBERONTAK:**

_"Ia melawan raja yang sah. Mengangkat senjata kepada Majapahit yang ia ikut mendirikan. Dan karena itu ia mati - sebagai catatan kaki dalam sejarah."_

**IA ADALAH PAHLAWAN:**

_"Ia berdiri untuk rakyat Tuban ketika tidak ada yang berani. Dan karena itu ia dikenang - sebagai manusia paling manusiawi dalam kisah Majapahit."_

_"Di antara kedua tafsir itu, kisah Ranggalawe hidup - tidak dalam hitam atau putih, tapi dalam warna abu-abu yang paling jujur dari kondisi manusia."_

**Transisi:** → D36 (Jalur A) / D37 (Jalur B) / D38 (Jalur C)

# **BABAK V - DIVERGENT ENDING: Tiga Tone Epilog**

**SCENE D36 - ENDING A - JALUR KONFRONTASI** ◆ ★

**Tipe Node:** TONE: PAHIT

**📦 ASET: BG-20 (Makam Ranggalawe) fade to black | BGM-09 | VN-VO-01 (Narasi Penutup)**

### **Tone: PAHIT - Ranggalawe pergi sebagai orang yang tahu ia benar**

_Kata-kata terakhir menyebut Mahapati. Rakyat Tuban berbisik nama itu bertahun-tahun. Mahapati tahu ia menang - tapi tidak pernah tidur nyenyak._

**\[Jika D17-A★ + D27-D aktif\]:** _Bertahun-tahun kemudian, Lembu Sora keluarkan surat gelap. Raja membacanya diam. Minggu berikutnya Mahapati tidak lagi terlihat di istana._

_"Ranggalawe menang - dengan cara tidak pernah ia bayangkan."_

### **Narasi Penutup (VO)**

_"Bagi sebagian, ia pemberontak. Bagi Tuban... ia simbol keberanian melawan ketidakadilan."_

_"Ada orang yang meninggalkan nama. Ada yang meninggalkan kebenaran. Yang terbaik meninggalkan keduanya - dan Ranggalawe tidak punya pilihan selain menjadi yang terbaik."_

**SCENE D37 - ENDING B - JALUR MEDIASI** ◆ ★

**Tipe Node:** TONE: MELANKOLIK

**📦 ASET: BG-20 | BGM-09 melankolik | CG-04 (Lembu Sora membawa kain)**

### **Tone: MELANKOLIK - Ranggalawe pergi dengan damai yang pahit**

_Ranggalawe pergi sebagai orang yang sempat melihat musuhnya tidak sepenuhnya jahat. Nambi mendengar kabar kematiannya sendirian - ada sesuatu yang berubah dalam matanya untuk selamanya._

_Lembu Sora membawa satu helai kain Ranggalawe ke Wiraraja yang sudah tua. Wiraraja menerimanya dengan tangan gemetar, tidak berkata apa-apa._

**\[Jika Stat Gate D26★ - Perjanjian Diam aktif\]:** _Kebo Anabrang, sebelum meninggal dari luka berbeda, memberitahu Kertarajasa: "Ranggalawe adalah ksatria terbesar yang pernah kuhadapi." Raja duduk lama tanpa bergerak._

### **Narasi Penutup (VO)**

_"Ia tidak membenci siapa pun di akhirnya. Dan itu yang membuatnya sulit dilupakan."_

_"Ada keindahan yang menyakitkan dalam memaafkan orang yang tidak meminta maaf. Ranggalawe melakukan itu - tanpa menyadarinya."_

**SCENE D38 - ENDING C - JALUR SIASAT/MOBILISASI** ◆ ★

**Tipe Node:** TONE: ENIGMATIK

**📦 ASET: BG-20 | BGM-09 enigmatik | SFX-02 (kertas) jika keris Ra Galatik disebutkan**

### **Tone: ENIGMATIK - Ranggalawe pergi dalam diam yang penuh makna**

_Ranggalawe pergi sebagai orang yang tahu ada pengkhianat di barisannya - dan memilih tetap bertempur. Ra Galatik tidak pernah kembali ke Majapahit. Hidup sebagai pedagang di pantai utara._

_Tidak ada yang tahu namanya sebenarnya. Tidak ada yang tahu apakah ia menyesal. Tapi setiap kali ada yang menyebut nama Ranggalawe, tangannya berhenti bergerak._

**\[Jika D17-C★ aktif\]:** _Di suatu pasar Tuban bertahun-tahun kemudian, pedagang tua membeli keris. Pedagang itu Ra Galatik. Keris itu milik Ranggalawe. Ia tidak pernah menggunakannya. Ia hanya membawanya._

### **Narasi Penutup (VO)**

_"Ada yang pergi dengan kalimat. Ada yang pergi dalam diam. Keduanya tetap pergi."_

_"Dan diam, kadang, adalah cara paling lantang untuk berkata bahwa kamu pernah ada."_

**SCENE D39 - RAKYAT TUBAN BERGERAK** ↪ ♥

**Tipe Node:** DETOUR OPSIONAL - Aktif jika D15-C

**Lokasi:** EXT. Tuban - Beberapa tahun setelah 1295 M

**📦 ASET: BG-10 BG-12 (Tuban) | BGM-09**

**🎭 Warga Tuban (kolektif)** \[Sprite minor rakyat | NPC Opsional kolektif\]

### **Catatan Naratif**

_HANYA AKTIF jika D15-C (Loyalitas Rakyat Tuban sangat tinggi). Perspektif rakyat yang ditinggalkan._

**A \[Izinkan monumen\].** "Izinkan rakyat bangun monumen Ranggalawe." - Tuban jadi pusat ziarah.

_➤ Dampak: Kisah hidup dalam tradisi lisan dan fisik. Warisan tercatat._

**B \[Larang\].** "Larang - terlalu berbahaya secara politik." - Rakyat simpan kenangan dalam lagu.

_➤ Dampak: Memori tersembunyi tapi tidak bisa dipadamkan. Justru lebih abadi._

**C \[Biarkan rakyat memutuskan\].** "Biarkan rakyat memutuskan sendiri." - Tanpa instruksi dari atas.

_➤ Dampak: Selalu ada yang bawa bunga ke tepi Tambak Beras. Warisan organik paling tulus._

**Transisi:** → D40 (Epilog Akhir Bersama)

**SCENE D40 - EPILOG AKHIR: NILAI YANG TIDAK BISA DIUSIR** ◆

**Tipe Node:** BOTTLENECK FINAL - Semua Jalur Bermuara di Sini

**📦 ASET: BG-20 → fade black | BGM-09 fade out | FX-05 (transisi akhir) | VN-VO-01 (Narasi Pembuka & Penutup)**

### **Cutscene Penutup Wajib - Sama untuk SEMUA Jalur**

_Tiga nilai Ranggalawe yang ia bawa ke sungai Tambak Beras - dan yang tidak ikut tenggelam:_

**_Seca Wecana - Setia pada janji_**

**_Sura ing Pati - Berani demi kebenaran_**

**_Lila ing Donya - Ikhlas berkorban_**

### **Narasi Penutup Final (VO) - Narator**

_"Di antara kedua tafsir itu, kisah Ranggalawe hidup - tidak dalam hitam atau putih, tapi dalam warna abu-abu yang paling jujur dari kondisi manusia."_

_"Bahwa seseorang bisa sekaligus benar dan salah, setia dan memberontak - tergantung dari sisi mana kita berdiri dan apa yang kita anggap lebih penting: aturan atau keadilan, kesetiaan pada raja atau kesetiaan pada hati nurani."_

_"Dan mungkin - justru mungkin - itulah mengapa kisah ini masih diceritakan."_

**_"Bagi sebagian, ia pemberontak. Bagi Tuban... ia simbol keberanian melawan ketidakadilan."_**

_- Narator, Scene Terakhir_

**- GAME OVER -**

**RANGGALAWE: GAWE RANGGALAWE**

_Total: 40 Decision Points · W-Shape Branching · Stat Gate · Divergent Ending (3 Tone Epilog)_

# **APPENDIX - REFERENSI CEPAT PRODUKSI**

## **A. Daftar Karakter & Aset Sprite**

**CH-01 Ranggalawe (Ken Kara):** 64x128px, 4 arah, idle/walk/run/attack/hurt/death, 8 frame. Armor Madura, keris di pinggang. 7 ekspresi VN.

**CH-02 Arya Wiraraja:** 64x128px, idle+talk, 4 frame. Adipati Madura, gestur tangan serius. 5 ekspresi VN.

**CH-03 Raden Wijaya/Kertarajasa:** 64x128px, 2 kostum (pelarian + mahkota). 4 ekspresi per kostum VN.

**CH-04 Lembu Sora:** 64x128px, idle/walk/combat. Armor tua, rambut abu. 6 ekspresi VN.

**CH-05 Nambi:** 64x128px, idle+talk. Patih resmi, ekspresi ambigu. 5 ekspresi VN.

**CH-06 Kebo Anabrang:** 64x128px, combat heavy. Bertubuh besar, spear stance. 4 ekspresi VN.

**CH-07 Mahapati:** 64x128px, idle+gesture. Penasihat mewah, selalu di bayangan. 5 ekspresi VN.

**CH-08 Ra Galatik:** 64x128px, idle+suspicious. Ekspresi dua wajah. Jalur C. 4 ekspresi VN.

**CH-09 Ra Lintang:** 64x128px, idle+battle ready. Busur di punggung.

**CH-10 Ra Jaran Waha:** 64x128px, idle+talk. Perwira loyal Tuban.

**CH-11 Kuda Anjampiani:** 48x96px, anak, idle+sad. 12 tahun. Wajah mirip Ranggalawe.

**CH-12 Ki Wira:** 48x96px, idle+crafting. Pandai besi, opsional.

**CH-13 Nyai Sembada:** 48x96px, nelayan tua, Jalur A opsional.

**CH-14 Buyut Macan Kuping:** 48x96px, tetua desa, opsional.

**CH-15 Pedagang Garam Tuban:** 48x96px, opsional.

**CH-16 Komandan Garda Madura:** 64x128px, armor penuh. Jalur B opsional.

## **B. Daftar Background & Scene**

**BG-01 Pendopo Sumenep Eksterior:** 320x180px, 3-layer parallax. D01 pembuka.

**BG-02 Pendopo Sumenep Interior:** 320x180px. D01, D07-C. Lampu minyak dramatis.

**BG-03 Pelabuhan Sumenep:** 320x180px, 2-layer, siang/senja. D07-A.

**BG-04 Pasar Sumenep:** 320x180px. Ki Wira, opsional.

**BG-05 Hutan Tarik Jalan:** 320x180px, 4-layer parallax. D02-kanan, D03 awal.

**BG-06 Kamp Hutan Tarik Siang:** 320x180px. D05, D08, D09-kiri.

**BG-07 Kamp Hutan Tarik Malam:** 320x180px, api unggun. D04, D03.

**BG-08 Kediri Alun-alun:** 320x180px. D06, D11.

**BG-09 Kediri Dalam Istana:** 320x180px. D06, D11.

**BG-10 Pelabuhan Tuban:** 320x180px, sunset. D16, D34, D39.

**BG-11 Kadipaten Tuban Pendopo:** 320x180px. D15, D17-B, D18, D19, D20, D21.

**BG-12 Pasar Tuban:** 320x180px. D15 opsional, D39.

**BG-13 Pegunungan Utara Tuban:** 320x180px, 5-layer. D17-C.

**BG-14 Trowulan Istana Majapahit:** 320x180px. D13, D32, D35.

**BG-15 Trowulan Balai Sidang:** 320x180px. D14, D17-A.

**BG-16 Trowulan Kediaman Mahapati:** 320x180px. D24-kanan, D31.

**BG-17 Medan Perang Tuban:** 320x180px, battlefield fx. D22, D23, D24.

**BG-18 Pantai Tuban Pertahanan:** 320x180px. D23 jalur A.

**BG-19 Sungai Tambak Beras:** 320x180px, 3-layer, senja merah. D26, D27, D28. KEY SCENE.

**BG-20 Makam Ranggalawe:** 320x180px. D30, D36, D37, D38, D39.

## **C. Daftar BGM & Penggunaan**

**BGM-01 Tema Utama:** Loop ~2 menit, orkestral gamelan. Menu, cutscene key.

**BGM-02 Sumenep Damai:** Loop ~90 detik, gamelan lembut. D01, D02.

**BGM-03 Tarik - Hutan dan Api:** Loop, perkusi + seruling. D03, D04, D05, D07-B, D08, D09.

**BGM-04 Kediri - Bayangan Musuh:** Loop, ambius misterius. D06, D07-C, D12.

**BGM-05 Tuban - Kota Ksatria:** Loop, pentatonik teguh. D15-D22, D29-D30.

**BGM-06 Trowulan - Mahkota Emas:** Loop, mewah ambigu. D13, D14, D17-A, D18-kanan, D24-kanan.

**BGM-07 Tema Perang:** Loop, perkusi intens. D10, D22-D24. Segmen combat aktif.

**BGM-08 Sungai Tambak Beras:** TIDAK loop, ~3-4 menit. D26-D28. KLIMAKS. Violin + gamelan.

**BGM-09 Epilog - Warisan:** Loop lembut, fade. D29-D40.

## **D. Item & Props**

**Item: Keris Ranggalawe** - 16x32px, blade emas-hitam. Quest Q-10. D20.

**Item: Dokumen Prasasti Sima** - 32x24px, gulungan kulit. D15-A, D29.

**Item: Surat Gelap Mahapati** - 32x24px, amplop hitam segel merah. D17-A★. EKSKLUSIF.

**Item: Surat Ketiga Wiraraja** - 32x24px, gulungan biasa. D07-C. EKSKLUSIF.

**Item: Senjata Kustom Ki Wira** - 16x32px, bervariasi. Q-01, combat.

## **E. CG Illustrations (VN Platform)**

**VN-CG-01 Ranggalawe Terima Nama:** Full 1920x1080px. D03.

**VN-CG-02 Kediri Jatuh - Jayakatwang Menyerah:** Full 1920x1080px. D11.

**VN-CG-03 Nambi Diangkat - Ranggalawe di Dermaga:** Full 1920x1080px. D16. KEY.

**VN-CG-04 Pertemuan Terakhir Ranggalawe & Lembu Sora:** Full 1920x1080px. D25.

**VN-CG-05 Gugurnya Ranggalawe di Tambak Beras:** Full 1920x1080px. D28. KEY.

**VN-CG-06 Kuda Anjampiani di Tepi Laut:** Full 1920x1080px. D34.

**VN-CG-07 Surat Gelap Mahapati Ditemukan:** Half 1280x720px. D17-A★. EKSKLUSIF A.

**VN-CG-08 Lobi Malam Nambi di Tuban:** Half 1280x720px. D17-B★. EKSKLUSIF B.

**VN-CG-09 Perjanjian Diam Kebo Anabrang:** Full 1920x1080px. D26★. STAT GATE.

## **F. Flags & Variables Ren'Py**

_Variabel yang perlu dilacak engine:_

**stat_konfrontasi, stat_mediasi, stat_siasat:** Integer, akumulasi sepanjang game.

**modal_d01:** "tiba_pertama" | "pasukan" | "info_tersembunyi"

**flag_nyai_sembada:** Boolean - aktif jika D01-A

**flag_ra_galatik:** Boolean - aktif jika D01-C

**seed_d04c:** Boolean - aktif jika D04-C dipilih

**flag_dokumen_sima:** Boolean - aktif jika D15-A

**flag_loyalitas_rakyat:** Boolean - aktif jika D15-C

**flag_surat_gelap:** Boolean - aktif jika D17-A★

**flag_perjanjian_nambi:** "percaya" | "netral" | "jebakan" | None

**flag_ra_galatik_jalur:** "tangkap" | "gunakan" | "ampuni" | None

**kehormatan_total:** Integer, diakumulasi. Gate di D26: ≥7.

**flag_perjanjian_diam:** Boolean - aktif jika D04-C AND kehormatan_total ≥ 7

**pilihan_d25:** "A" | "B" | "C" - menentukan nasib Lembu Sora

**ending_tone:** Auto-calculated: "pahit" | "melankolik" | "enigmatik" berdasarkan jalur dominan D17

## **G. Panduan Implementasi Teknis Ren'Py (Dialog, VO, & Cutscene)**

**1\. Sistem Percabangan (Invisible Choices):**

_Gunakan conditional statement (if/elif) berdasarkan histori stat untuk mengubah dialog otomatis tanpa memicu menu pilihan._

**2\. Dialog & Dynamic Tags:**

_Manfaatkan fitur Image Tag di Ren'Py. Deklarasikan \`image ranggalawe marah = "ch01_marah.png"\`. Bedakan warna teks atau gunakan format khusus untuk memisahkan Monolog Batin (Internal Monologue) dengan Dialog Diucapkan._

**3\. Pengaturan Voice Over (VO):**

_Pakai Partial VO (Barks) berupa suara pendek untuk mayoritas dialog agar file game tidak membengkak. Cadangkan Full VO khusus untuk cutscene puncak (seperti D26 dan D27). Pastikan fitur Voice Auto Mute aktif agar BGM otomatis meredup ketika VO diputar._

**4\. Animasi Cutscene Split-Screen:**

_Untuk scene paralel seperti D02 dan D09, aplikasikan fungsi \`crop\` dan position \`xalign\` dalam blok \`transform\`. Berikan efek partikel (jatuhnya debu, gemericik air berulang) untuk menghidupkan CG statis menjadi sinematik._

**- DOKUMEN SELESAI -**

_Gawe Ranggalawe: Dokumen Produksi Visual Novel_

_40 Decision Points · W-Shape · Stat Gate · Divergent Ending_

_Teknologi Rekayasa Multimedia - PENS 2025/2026_