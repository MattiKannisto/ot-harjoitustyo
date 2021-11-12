import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_rahan_ottaminen_vahentaa_saldoa_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_rahan_ottaminen_ei_vaikuta_saldoon_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_metodi_palauttaa_rahan_riittaessa_true(self):
        metodin_palautusarvo = self.maksukortti.ota_rahaa(10)
        self.assertEqual(metodin_palautusarvo, True)

    def test_ota_rahaa_metodi_palauttaa_rahan_ollessa_riittamatonta_false(self):
        metodin_palautusarvo = self.maksukortti.ota_rahaa(11)
        self.assertEqual(metodin_palautusarvo, False)