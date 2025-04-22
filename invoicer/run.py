import requests, pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

API_BASE = "https://DIN_SERVER:8080/api/v1/db/data/v1/breforening"
HEADERS = {"xc-auth": "DIN_API_KEY"}

def fetch_members():
    r = requests.get(f"{API_BASE}/members", headers=HEADERS,
                     params={"filter":"amount>0 AND invoice_status='ikke_generert'"})
    return pd.DataFrame(r.json()['list'])

def generate_invoice(member):
    # last inn Jinja‑mal
    env = Environment(loader=FileSystemLoader('.'))
    tmpl = env.get_template('invoice_template.html')
    html = tmpl.render(**member.to_dict())
    pdf_path = f"generated/{member.id}_{member.last_name}.pdf"
    HTML(string=html).write_pdf(pdf_path)
    return pdf_path

def main():
    df = fetch_members()
    for _, m in df.iterrows():
        generate_invoice(m)
        # oppdater invoice_status via PATCH …
        requests.patch(f"{API_BASE}/members/{m.id}",
                       json={"invoice_status":"generert"},
                       headers=HEADERS)

if __name__ == "__main__":
    main()
