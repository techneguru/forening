# Nordeidevågen Båtforening – Enkel hjemmeside + en database på baksiden

## Oversikt
Prosjektet setter opp:
- En offentlig nettside
- Medlemsområde for dokumenter, medlemslister og utlegg
- Automatisk fakturering (Python)
- Alt kjører i Docker-containere for enkel drift

---

## Forutsetninger
- Ubuntu 20.04 eller nyere
- Docker og Docker Compose installert
- (Valgfritt) Python 3.11 hvis du vil kjøre backend-script lokalt

---

## Oppsett – steg for steg

### 1. Oppdater og installer nødvendige pakker
```bash
sudo apt update
sudo apt install -y docker.io docker-compose python3-pip
```

### 2. Klon prosjektet
```bash
git clone https://github.com/techneguru/forening.git
cd forening
```

### 3. Sett opp miljøvariabler
Kopier eksempel-filen og rediger med dine egne passord:
```bash
cp .env.example .env
nano .env
```
**NB:** Bruk sterke passord for `MYSQL_ROOT_PASSWORD` og `NC_AUTH_JWT_SECRET` i produksjon.

---

### 4. Bygg og start alle tjenester
```bash
docker-compose up --build -d
```

---

### 5. Tilgang til tjenestene
- **Offentlig nettside:** http://<din-server-ip>
- **Medlemsområde:** http://<din-server-ip>/andelseier.html
- **NocoDB admin:** http://<din-server-ip>:8080

---

### 6. Stopp alle tjenester
```bash
docker-compose down
```

---

### 7. (Valgfritt) Kjør backend-script lokalt
Hvis du ønsker å kjøre backend-script (f.eks. proxy eller fakturering) utenfor Docker:
```bash
cd backend
pip install -r requirements.txt
python proxy.py
```
eller for fakturering:
```bash
cd invoicer
pip install -r requirements.txt
python run.py
```

---

### 8. Konfigurer NocoDB og brukertilgang
1. Gå til NocoDB admin: http://<din-server-ip>:8080
2. Logg inn som admin eller opprett ny admin-bruker.
3. Opprett roller (f.eks. "Admin", "Medlem") og sett riktige rettigheter på tabeller og visninger.
4. Legg til brukere og tildel roller.

---

## Slik setter du opp NocoDB

1. **Logg inn som admin**
   - Åpne `http://<din-server-ip>:8080` i nettleseren og logg inn med admin-bruker.

2. **Koble til databasen**
   - Velg "Add Database" og koble til MariaDB (bruk info fra `.env`).

3. **Opprett nødvendige tabeller**
   - Opprett tabeller for `news`, `documents`, `members` og `expenses` med relevante kolonner (se eksempel under).

   **Eksempel på kolonner:**
   - `news`: id, title, content, date
   - `documents`: id, title, file_url, date
   - `members`: id, name, boat_type, boat_length, outstanding_payments
   - `expenses`: id, member_name, description, amount, receipt_url, date

4. **Lag views og skjema**
   - Lag egne "Views" for dokumentarkiv (filtrer på siste 5 år), medlemsliste og utlegg (aktiver "Form View" for innsending).

5. **Sett opp roller og tilgang**
   - Gå til "Settings" → "Users & Roles".
   - Opprett roller som "Admin" og "Medlem".
   - Sett rettigheter slik at medlemmer kun kan se og sende inn det de skal.

6. **Legg til brukere**
   - Legg til brukere og tildel riktig rolle.

7. **Test fra nettsiden**
   - Sjekk at iframe-lenker i `andelseier.html` viser riktig view/skjema.
   - Sjekk at `/api/news` henter fra riktig tabell.

---

**Nå er NocoDB satt opp og klar til bruk med nettsiden og medlemsområdet!**

---

### 9. Backup og gjenoppretting av database

**Backup:**
```bash
docker exec -t <db_container_navn> mysqldump -u<MYSQL_USER> -p<MYSQL_PASSWORD> <MYSQL_DATABASE> > backup.sql
```

**Gjenopprett:**
```bash
docker exec -i <db_container_navn> mysql -u<MYSQL_USER> -p<MYSQL_PASSWORD> <MYSQL_DATABASE> < backup.sql
```

---

## Notater og tips

- `.env`-filen skal aldri deles offentlig.
- Husk å ta jevnlig backup av `db_data` og `noco_data` volumene.
- For å sjekke status og logger:
  ```bash
  docker-compose logs
  docker ps
  ```
- For å oppdatere til nyeste versjon:
  ```bash
  git pull
  docker-compose up --build -d
  ```

---

## Feilsøking

- **Tjeneste starter ikke:** Sjekk logger med `docker-compose logs <tjenestenavn>`
- **Endringer vises ikke:** Prøv å bygge på nytt med `docker-compose up --build -d`
- **NocoDB-tilgang:** Sjekk at port 8080 er åpen i brannmuren

---
