import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_sisaltaa_oikean_maaran_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luotu_kassapaate_ei_sisalla_myytyja_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luotu_kassapaate_ei_sisalla_myytyja_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kasvattaa_kassan_saldoa_oikein_jos_maksu_on_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, (100000 + 240))

    def test_syo_edullisesti_kateisella_palauttaa_oikean_maaran_vaihtorahaa_jos_maksu_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240+100)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_edullisesti_kateisella_kasvattaa_kassan_myytyjen_edullisten_maaraa_onnistuessaan(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_kasvata_kassan_saldoa_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, (100000))

    def test_syo_edullisesti_kateisella_palauttaa_kaikki_rahat_jos_maksu_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(vaihtoraha, 239)

    def test_syo_edullisesti_kateisella_ei_kasvata_kassan_myytyjen_edullisten_maaraa_epaonnistuessaan(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassan_saldoa_oikein_jos_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, (100000 + 400))

    def test_syo_maukkaasti_kateisella_palauttaa_oikean_maaran_vaihtorahaa_jos_maksu_onnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400+100)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassan_myytyjen_edullisten_maaraa_onnistuessaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_ei_kasvata_kassan_saldoa_jos_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, (100000))

    def test_syo_maukkaasti_kateisella_palauttaa_kaikki_rahat_jos_maksu_epaonnistuu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(vaihtoraha, 399)

    def test_syo_maukkaasti_kateisella_ei_kasvata_kassan_myytyjen_edullisten_maaraa_epaonnistuessaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_vahentaa_kortin_saldoa_oikein_jos_kortilla_on_riittavasti_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)

    def test_syo_edullisesti_kortilla_palauttaa_true_jos_kortilla_on_riittavasti_rahaa(self):
        paluuarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(paluuarvo, True)

    def test_syo_edullisesti_kortilla_kasvattaa_kassan_myytyjen_edullisten_maaraa_onnistuessaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_muuta_kortin_saldoa_jos_silla_ei_ole_riittavasti_rahaa(self):
        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 40)

    def test_syo_edullisesti_kortilla_ei_muuta_myytyjen_edullisten_maaraa_jos_kortilla_ei_ole_riittavasti_rahaa(self):
        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 4)

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_kortilla_ei_ole_riittavasti_rahaa(self):
        for i in range(4):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        paluuarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(paluuarvo, False)

    def test_syo_edullisesti_kortilla_ei_onnistuessaan_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_vahentaa_kortin_saldoa_oikein_jos_kortilla_on_riittavasti_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)

    def test_syo_maukkaasti_kortilla_palauttaa_true_jos_kortilla_on_riittavasti_rahaa(self):
        paluuarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(paluuarvo, True)

    def test_syo_maukkaasti_kortilla_kasvattaa_kassan_myytyjen_edullisten_maaraa_onnistuessaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_muuta_kortin_saldoa_jos_silla_ei_ole_riittavasti_rahaa(self):
        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_syo_maukkaasti_kortilla_ei_muuta_myytyjen_edullisten_maaraa_jos_kortilla_ei_ole_riittavasti_rahaa(self):
        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_kortilla_ei_ole_riittavasti_rahaa(self):
        for i in range(2):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        paluuarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(paluuarvo, False)

    def test_syo_edullisesti_kortilla_ei_onnistuessaan_muuta_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kasvattaa_onnistuessaan_rahan_maaraa_kortilla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_lataa_rahaa_kortille_ei_kasvata_rahan_maaraa_kortilla_jos_ladattava_summa_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_kortille_kasvattaa_onnistuessaan_rahan_maaraa_kassassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_rahaa_kortille_ei_kasvata_rahan_maaraa_kassassa_jos_ladattava_summa_on_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)