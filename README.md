# Forening-Portal

Selv‑hostet portal for båtforening:
- NocoDB som database‑frontend
- Enkel statisk frontend (HTML/CSS/JS) med hero‑bilde og nyheter
- Python‑skript (`invoicer/run.py`) for fakturagenerering mot NocoDB API
- Docker Compose + GitHub Actions CI/CD

## Kom i gang

1. Klon: `git clone git@github.com:techneguru/forening.git`
2. Juster miljø­variabler i `docker‑compose.yml` (DB‑passord, API‑keys)
3. Kjør `docker compose up -d`
4. Åpne `http://<VM_IP>:8080` for NocoDB, `http://<VM_IP>` for frontend
5. Push endringer til `main` for auto‑deploy
