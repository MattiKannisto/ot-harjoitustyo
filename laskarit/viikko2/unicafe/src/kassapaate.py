EDULLISEN_HINTA = 240
MAUKKAAN_HINTA = 400

class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= EDULLISEN_HINTA:
            self.kassassa_rahaa = self.kassassa_rahaa + EDULLISEN_HINTA
            self.edulliset += 1
            maksu -= EDULLISEN_HINTA
        return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= MAUKKAAN_HINTA:
            self.kassassa_rahaa = self.kassassa_rahaa + MAUKKAAN_HINTA
            self.maukkaat += 1
            maksu -= MAUKKAAN_HINTA
        return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= EDULLISEN_HINTA:
            kortti.ota_rahaa(EDULLISEN_HINTA)
            self.edulliset += 1
        return kortti.saldo >= EDULLISEN_HINTA

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= MAUKKAAN_HINTA:
            kortti.ota_rahaa(MAUKKAAN_HINTA)
            self.maukkaat += 1
        return kortti.saldo >= MAUKKAAN_HINTA

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa