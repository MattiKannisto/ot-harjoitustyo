# DnaSequencingToolPython
DnaSequencingToolPython-sovellus mahdollistaa automatisoidun sekvensointialukkeiden suunnittelun käyttäjän antamille DNA-sekvensseille. Sovellus tarkistaa, että käyttäjän antama DNA-sekvenssi sisältää ainoastaan kirjaimia 'A', 'T', 'G' ja 'C'. Validi DNA-sekvenssi on myös mahdollista kääntää proteiinisekvenssiksi, jos siinä on aloituskodoni 'ATG' oikeassa lukukehyksessä.

## Releaset
[Viikon 5 release](https://github.com/MattiKannisto/ot-harjoitustyo/releases/tag/viikko5)

[Viikon 6 release](https://github.com/MattiKannisto/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio
[Tuntikirjanpito](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Käyttöohje](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Komentorivitoiminnot
Sovelluksen käyttämistä ja testaamista varten tarvitaan vähintään [Pythonin versio 3.8](https://www.python.org/downloads/release/python-380/) ja [poetry](https://python-poetry.org/) tulee olla asennettuna. Ennen sovelluksen käyttämistä, **asenna riippuvuudet komennolla**: poetry install ja **alusta tietokanta komennolla**: poetry run invoke initialize

**Ohjelman käynnistäminen:** poetry run invoke start

Jos sovellusta käytetään virtuaalityöasemalla ja saadaan virheilmoitus 'database is locked', tulee toimia [kurssin ohjeiden mukaisesti](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla)

**Testien suorittaminen:** poetry run invoke test

**Testikattavuusraportin generoiminen:** poetry run invoke coverage-report

**Koodin tyylin tarkistaminen** poetry run invoke lint
