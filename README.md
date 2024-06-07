# Takipçi Analizi Dashboard

Bu uygulama, kullanıcıların takipçi verilerini analiz etmelerini sağlayan bir Streamlit tabanlı bir web uygulamasıdır.

## Nasıl Kullanılır

1. Ana başlık altında "Veri setini yükleyin" butonuna tıklayın ve bir Excel dosyası seçin.
2. Dosya yüklendikten sonra, dosyanın sütunları ve başlıkları listelenecektir.
3. "Lütfen bir grafik türü seçin" dropdown menüsünden bir grafik türü seçin: Pasta Grafik, Çizgi Grafik veya Bar Grafik.
4. Grafik türünü seçtikten sonra, "Lütfen bir kategori seçin" ve "Lütfen bir değer seçin" dropdown menülerinden birer sütun seçin.
5. Seçimlerinizi yaptıktan sonra, seçilen kategori ve değer üzerinde bir grafik görüntülenir.

## Kullanılan Kütüphaneler

- Pandas: Veri işleme ve manipülasyonu için kullanılmıştır.
- Matplotlib: Grafik çizimi için kullanılmıştır.
- Streamlit: Web uygulaması arayüzü oluşturmak için kullanılmıştır.

## Gereksinimler ve Kurulum

- Python 3.x
- Pandas
- Matplotlib
- Streamlit

Gereksinimleri yüklemek için terminalde aşağıdaki komutu çalıştırın:

pip install pandas matplotlib streamlit
streamlit run app.py


Uygulama bir tarayıcı penceresinde açılacak ve kullanıma hazır olacaktır.

