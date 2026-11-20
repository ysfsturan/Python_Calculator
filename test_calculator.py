"""calculator.py için basit birim testleri."""

import unittest

from calculator import bicimli_sayi, bol, cikar, carp, karekok, mod_al, topla, us_al


class TestCalculator(unittest.TestCase):
    def test_temel_islemler(self) -> None:
        self.assertEqual(topla(10, 5), 15)
        self.assertEqual(cikar(10, 4), 6)
        self.assertEqual(carp(3, 7), 21)
        self.assertEqual(bol(20, 4), 5)
        self.assertEqual(us_al(2, 5), 32)
        self.assertEqual(mod_al(17, 5), 2)
        self.assertEqual(karekok(81), 9)

    def test_hata_durumlari(self) -> None:
        with self.assertRaises(ValueError):
            bol(10, 0)
        with self.assertRaises(ValueError):
            mod_al(10, 0)
        with self.assertRaises(ValueError):
            karekok(-4)

    def test_sayi_bicimleme(self) -> None:
        self.assertEqual(bicimli_sayi(12.0), "12")
        self.assertEqual(bicimli_sayi(3.5), "3.5")


if __name__ == "__main__":
    unittest.main()
