# TEKNOFEST 2026 Tarım Teknolojileri Yarışması
## Proje Ön Değerlendirme Raporu (Taslak)

**Proje Adı:** Smart Agriculture (Tarımsal İHA & IoT Destekli Akıllı Takip Sistemi)  
**Kategori:** Sosyoloji -> Tarım ve Hayvansal Üretim Veri Analitiği ve Bilgi Sistemleri  
**Takım ID:** [KYS Üzerinden Alınan ID]  
**Takım Adı:** [Takım Adınız]  

---

### 1. PROJE ÖZETİ (Project Summary)
Bu proje, geniş tarım arazilerinde bitki sağlığını otonom İHA'lar (Görüntü İşleme) ve yerel sensör ağları (IoT) aracılığıyla izleyen bütünleşik bir karar destek sistemidir. Sistem, LoRaWAN üzerinden gelen toprak verilerini (NPK, nem, sıcaklık) ve İHA'dan alınan görüntüleri derin öğrenme modelleriyle analiz ederek çiftçiye anlık hastalık teşhisi ve hassas sulama/gübreleme önerileri sunar.

### 2. PROJENİN AMACI (Aim of the Project)
Şartnamenin 2.2.2 maddesinde belirtilen "üretim verimliliğini, sürdürülebilirliği ve karar alma kalitesini artırmaya yönelik akıllı bilgi ve karar destek sistemleri" hedefine uygun olarak; geleneksel tarımdaki fiziksel iş yükünü azaltmak, kaynak israfını (su, gübre, ilaç) önlemek ve verim kaybına neden olan hastalıkları henüz başlangıç aşamasında tespit etmektir.

### 3. HEDEF KİTLE (Target Audience)
- Büyük ölçekli tarım işletmeleri.
- Hassas tarım uygulamalarına geçmek isteyen bireysel üreticiler.
- Zirai danışmanlık hizmeti veren kurumlar.

### 4. YENİLİKÇİ (İNOVATİF) YÖNÜ (Innovation)
Mevcut çözümler genellikle sadece sensör verisi veya sadece görüntü işleme sunarken, projemiz bu iki farklı veri kaynağını hibrit bir yapıda birleştirir. Özellikle LoRaWAN kullanımı sayesinde internet altyapısının olmadığı çok geniş arazilerde dahi düşük güç tüketimiyle kesintisiz veri akışı sağlaması projenin teknolojik farkıdır.

### 5. KULLANILACAK YÖNTEMLER (Methods to be Used)
- **Görüntü İşleme:** TensorFlow/PyTorch altyapılı CNN (Convolutional Neural Networks) modelleri ile yaprak analizleri.
- **IoT Katmanı:** LoRaWAN protokolü, NPK ve nem sensörleri, ESP32/Raspberry Pi tabanlı uç cihazlar.
- **Backend/Analiz:** FastAPI tabanlı mikroservis mimarisi, gerçek zamanlı veri analitiği ve tahmin modelleri.
- **Frontend:** Kullanıcı dostu web tabanlı dashboard ve verilerin görselleştirilmesi.

---
> [!IMPORTANT]
> Bu belge bir taslaktır. Yarışma başvurusu için şartname güncellemelerini ve KYS portalındaki güncel rapor şablonunu takip etmeniz önerilir.
