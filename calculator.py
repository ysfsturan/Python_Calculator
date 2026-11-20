"""Basit ve anlaşılır konsol hesap makinesi (ek kütüphane gerektirmez)."""

import math


def topla(a: float, b: float) -> float:
    """İki sayıyı toplar."""
    return a + b


def cikar(a: float, b: float) -> float:
    """Birinci sayıdan ikinci sayıyı çıkarır."""
    return a - b


def carp(a: float, b: float) -> float:
    """İki sayıyı çarpar."""
    return a * b


def bol(a: float, b: float) -> float:
    """Birinci sayıyı ikinci sayıya böler (sıfıra bölünemez)."""
    if b == 0:
        raise ValueError("Bir sayı sıfıra bölünemez!")
    return a / b


def us_al(a: float, b: float) -> float:
    """Birinci sayının ikinci sayı kuvvetini hesaplar."""
    return a**b


def mod_al(a: float, b: float) -> float:
    """Bölümden kalanı (mod) verir."""
    if b == 0:
        raise ValueError("Sıfıra göre mod alınamaz!")
    return a % b


def karekok(a: float) -> float:
    """Sıfır veya pozitif bir sayının karekökünü alır."""
    if a < 0:
        raise ValueError("Negatif sayının karekökü alınamaz!")
    return math.sqrt(a)


def bicimli_sayi(sayi: float) -> str:
    """Tam sayıları '.0' olmadan gösterir (ör. 8.0 -> '8')."""
    if float(sayi).is_integer():
        return str(int(sayi))
    return f"{sayi:.6g}"


def sayi_oku(mesaj: str) -> float:
    """Kullanıcı geçerli bir sayı girene kadar ister (virgül de kabul edilir)."""
    while True:
        ham = input(mesaj).strip().replace(",", ".")
        try:
            return float(ham)
        except ValueError:
            print("Lütfen geçerli bir sayı girin (örnek: 12 veya 4.5).")


def menu_yazdir() -> None:
    print("\n=== Python Hesap Makinesi ===")
    print("1) Toplama (+)")
    print("2) Çıkarma (-)")
    print("3) Çarpma (*)")
    print("4) Bölme (/)")
    print("5) Üs Alma (**)")
    print("6) Mod / Kalan (%)")
    print("7) Karekök (√)")
    print("0) Çıkış")


def main() -> None:
    while True:
        menu_yazdir()
        secim = input("İşlem seçiniz (0-7): ").strip()

        if secim == "0":
            print("Görüşürüz!")
            break

        if secim in {"1", "2", "3", "4", "5", "6"}:
            a = sayi_oku("1. sayı: ")
            b = sayi_oku("2. sayı: ")
            try:
                if secim == "1":
                    sonuc, simge = topla(a, b), "+"
                elif secim == "2":
                    sonuc, simge = cikar(a, b), "-"
                elif secim == "3":
                    sonuc, simge = carp(a, b), "*"
                elif secim == "4":
                    sonuc, simge = bol(a, b), "/"
                elif secim == "5":
                    sonuc, simge = us_al(a, b), "**"
                else:
                    sonuc, simge = mod_al(a, b), "%"
                print(f"Sonuç: {bicimli_sayi(a)} {simge} {bicimli_sayi(b)} = {bicimli_sayi(sonuc)}")
            except ValueError as hata:
                print(f"Hata: {hata}")
        elif secim == "7":
            a = sayi_oku("Sayı: ")
            try:
                sonuc = karekok(a)
                print(f"Sonuç: √{bicimli_sayi(a)} = {bicimli_sayi(sonuc)}")
            except ValueError as hata:
                print(f"Hata: {hata}")
        else:
            print("Geçersiz seçim! Lütfen 0 ile 7 arasında bir değer girin.")


if __name__ == "__main__":
    main()
