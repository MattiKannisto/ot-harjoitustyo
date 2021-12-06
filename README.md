# DnaSequencingToolPython
DnaSequencingToolPython-sovellus mahdollistaa automatisoidun sekvensointialukkeiden suunnittelun käyttäjän antamille DNA-sekvensseille. Sovellus tarkistaa, että käyttäjän antama DNA-sekvenssi sisältää ainoastaan kirjaimia 'A', 'T', 'G' ja 'C'. Validi DNA-sekvenssi on myös mahdollista kääntää proteiinisekvenssiksi, jos siinä on aloituskodoni 'ATG' oikeassa lukukehyksessä.

## Dokumentaatio
[Tuntikirjanpito](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot
Sovelluksen käyttämistä ja testaamista varten tarvitaan vähintään [Pythonin versio 3.8](https://www.python.org/downloads/release/python-380/) ja [poetry](https://python-poetry.org/) tulee olla asennettuna. Ennen sovelluksen käyttämistä, **asenna riippuvuudet komennolla**: poetry install

**Ohjelman käynnistäminen:** poetry run invoke start

**Testien suorittaminen:** poetry run invoke test

**Testikattavuusraportin generoiminen:** poetry run invoke coverage-report

**Koodin tyylin tarkistaminen** poetry run invoke lint