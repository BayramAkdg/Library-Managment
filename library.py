import sqlite3

conn = sqlite3.connect("kutuphane.db", check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS kitaplar (id INTEGER PRIMARY KEY AUTOINCREMENT, kitapadi TEXT NOT NULL, yazar TEXT NOT NULL, tarih INTEGER, sayfasayisi INTEGER)''')

conn.commit()


def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    tarih = int(input("Yayın yılı: "))
    sayfa_sayisi = int(input("Sayfa sayısı: "))

    conn = sqlite3.connect("kutuphane.db") 
    c = conn.cursor()
    c.execute("INSERT INTO kitaplar (kitapadi, yazar, tarih, sayfasayisi) VALUES (?, ?, ?, ?)", (kitap_adi, yazar, tarih, sayfa_sayisi))
    conn.commit() 
    conn.close() 
    print("Kitap eklendi!")


def kitaplari_listele():
    conn = sqlite3.connect("kutuphane.db")
    c = conn.cursor()
    c.execute("SELECT * FROM kitaplar")
    kitaplar = c.fetchall()
    conn.close()

    if kitaplar:
        for kitap in kitaplar:
            print(kitap)
    else:
        print("Kütüphane boş.")


def kitap_guncelle():
    kitap_id = int(input("Güncellenecek kitap ID: "))
    kitap_adi = input("Yeni kitap adı: ")
    yazar = input("Yeni yazar: ")
    tarih = int(input("Yeni yayın yılı: "))
    sayfa_sayisi = int(input("Yeni sayfa sayısı: "))

    conn = sqlite3.connect("kutuphane.db")
    c = conn.cursor()
    c.execute("UPDATE kitaplar SET kitapadi = ?, yazar = ?, tarih = ?, sayfasayisi = ? WHERE id = ?",
              (kitap_adi, yazar, tarih, sayfa_sayisi, kitap_id))
    conn.commit()
    conn.close()
    print("Kitap güncellendi!")


def kitap_sil():
    kitap_id = int(input("Silinecek kitap ID: "))

    conn = sqlite3.connect("kutuphane.db")
    c = conn.cursor()
    c.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))
    conn.commit()  
    conn.close()
    print("Kitap silindi!")


def main():
    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Güncelle")
        print("4. Kitap Sil")
        print("5. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_guncelle()
        elif secim == "4":
            kitap_sil()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")


if __name__ == "__main__":
    main()

conn.close()
