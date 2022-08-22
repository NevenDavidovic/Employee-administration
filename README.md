# Matična evidencija i administracija zaposlenika- projektni zadatak

**Opis projekta:**

Projektni zadatak je napravljen na način da aplikacija simulira evidenciju i administraciju zaposlenika unutar bolnice koja unutar svog sastava ima tri specijalnosti: **KIRURGIJA**, **TRAUMATOLOGIJA** i **ORTOPEDIJA**.
Aplikacija će osim simulacije unosa zaposlenika u bazu podataka, njihovog brisanja, izmjene i prikaza omogućavati pretraživanje zaposlenika  te prikaz statistike zaposlenih.

**CRUD funkcionalnosti** simuliraju funkcionalnosti unošenja, čitanja, izmjene i brisanja zaposlenika iz evidencije.


---

**DODATNE funkcionalnosti**:

***1. Funkcija pretraživanja:***
* obuhvaća pretraživanje po imenu,prezimenu i odjelu
* pronađenim zaposlenicima može se promijeniti odjel i ostale informacije koje su dostupne unutar baze podataka te ih se može izbrisati iz evidencije

***2. Statistika unešenih zaposlenika:***
* ukupan broj unešenih zaposlenika
* broj muških i ženskih zaposlenika te njihov postotak
* broj zaposlenika po odjelima



---
**Kako pokrenuti aplikaciju lokalno:**
 
1. preuzeti git repozitorij zajedno sa Dockerfileom i requirments.txt
2. napraviti docker sliku unutar terminala naredbom 
   ```bash 
   docker image build -t app-pis .
3. pokrenuti docker image unutar kontejnera i odabrati port 
    ```bash
    docker run -p 5000:5000 -d app-pis

4. zasutavljanje kontejnera se vrši sa naredbama 
    ```bash 
    docker stop

