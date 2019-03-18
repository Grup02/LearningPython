from film import *

print("""***********************************

Film Ar�iv Program�na Ho�geldiniz.

��lemler;

1. Filmleri G�ster

2. Film Sorgulama

3. Film Ekle

4. Film Sil 

5. Filmin t�r�n� de�i�tir

��kmak i�in 'q' ya bas�n.
***********************************""")

film = Arsiv()

while True:
    islem = input("Yap�lacak i�lemi se�iniz:")
    if islem == "q":
        print("Programdan ��k�l�yor...")
        break

    if islem == "1":
        film.filmleri_goster()

    if islem == "2":
        islem2 = input("Arad���n�z filmin ad�n� yaz�n�z: ")

        print("Film sorgulan�yor.....")
        time.sleep(1)
        film.film_sorgula(islem2)


    if islem == "3":
        film_ismi = input("Film Ismi: ")
        yonetmen = input("Y�netmen: ")
        tur = input("Film T�r�: ")
        sure = input("Filmin S�resi: ")
        yapimci = input("Yap�mc�: ")

        yeni_film = Film(film_ismi,yonetmen,tur,sure,yapimci)
        print("Film ekleniyor....")
        time.sleep(1)
        film.film_ekle(yeni_film)
        print("Film eklendi....")


    if islem == "4":
        silinecek_film = input("Silinecek filmin ad�n� giriniz: ")

        film.film_sil(silinecek_film)


    if islem == "5":
        eski_film = input("T�r�n� g�ncellemek istedi�iniz filmi giriniz: ")
        yeni_tur = input("Filmin yeni t�r�n� giriniz: ")

        print("Film g�ncelleniyor....")
        time.sleep(1)
        film.tur_guncelle(eski_film,yeni_tur)
        print("Film guncellendi........")


