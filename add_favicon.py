import os
import re

FAVICON_TAG = """    <!-- Tarayıcı Sekme Logosu (Favicon) -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='25' fill='%23238636'/><text x='50' y='65' font-family='system-ui, sans-serif' font-size='50' font-weight='900' fill='%23ffffff' text-anchor='middle'>PF</text></svg>">"""

TARGET_DIR = "blog"  # Makalelerin bulunduğu klasör adı

def process_html_files():
    # Klasörün varlığını kontrol et
    if not os.path.exists(TARGET_DIR):
        print(f"Hata: '{TARGET_DIR}' klasörü bulunamadı. Lütfen betiği sitenizin ana dizininde çalıştırın.")
        return

    updated_count = 0
    skipped_count = 0

    # Klasördeki tüm dosyaları tara
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Eğer dosyada zaten bir favicon tanımlandıysa işlem yapma
                if "rel=\"icon\"" in content or "rel='icon'" in content:
                    print(f"Atlandı (Zaten logo var): {file_path}")
                    skipped_count += 1
                    continue

                # <head> etiketini bul ve hemen arkasına favicon satırını ekle
                if "<head>" in content:
                    new_content = content.replace("<head>", f"<head>\n{FAVICON_TAG}")
                    
                    # Değişiklikleri dosyaya geri yaz
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"Güncellendi: {file_path}")
                    updated_count += 1
                else:
                    print(f"Uyarı (<head> etiketi bulunamadı): {file_path}")

    print("\n--- İŞLEM TAMAMLANDI ---")
    print(f"Toplam Güncellenen Makale: {updated_count}")
    print(f"Zaten Logosu Olan/Atlanan: {skipped_count}")

if __name__ == "__main__":
    process_html_files()
```
eof

### Bu Python Aracını Nasıl Kullanırsın?
1. Bilgisayarında web sitenin dosyalarının bulunduğu klasörün ana dizininde (yani `blog/` klasörünün hemen dışındaki ana yerde) boş bir metin belgesi oluşturup adını `add_favicon.py` yap.
2. Yukarıdaki kod bloğunu bu dosyanın içine yapıştırıp kaydet.
3. Terminal/Komut Satırını açıp bu klasörün dizinine git ve `python add_favicon.py` yazıp çalıştır. 
4. Saniyeler içinde tüm eski makalelerine o yeşil **PF** logo kodunu hatasız bir şekilde yerleştirecektir!

Benim sana tavsiyem, gelecekte de rahat etmek adına **Yöntem 1**'i uygulayıp sitenin root dizinine bir `favicon.ico` yerleştirmendir Murat. Böylece yeni bir sayfa açtığında kod eklemeyi unutsan bile logon hep orada kalır!
