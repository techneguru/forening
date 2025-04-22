import os
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import logging

API_BASE = os.getenv("API_BASE", "http://noco:8080/api/v1/db/data/v1/breforening")
HEADERS = {"xc-auth": os.getenv("API_KEY", "default_api_key")}

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_members():
    r = requests.get(f"{API_BASE}/members", headers=HEADERS,
                     params={"filter": "amount>0 AND invoice_status='ikke_generert'"})
    r.raise_for_status()
    return pd.DataFrame(r.json()['list'])

def generate_invoice(member):
    # Ensure the output directory exists
    os.makedirs("generated", exist_ok=True)
    # Load Jinja template
    env = Environment(loader=FileSystemLoader('.'))
    tmpl = env.get_template('invoice_template.html')
    html = tmpl.render(**member.to_dict())
    pdf_path = f"generated/{member.id}_{member.last_name}.pdf"
    HTML(string=html).write_pdf(pdf_path)
    return pdf_path

def main():
    logging.info("Fetching members with pending invoices...")
    df = fetch_members()
    for _, m in df.iterrows():
        logging.info(f"Generating invoice for member ID: {m.id}")
        generate_invoice(m)
        logging.info(f"Updating invoice status for member ID: {m.id}")
        requests.patch(f"{API_BASE}/members/{m.id}",
                       json={"invoice_status": "generert"},
                       headers=HEADERS)
    logging.info("All invoices processed successfully.")

if __name__ == "__main__":
    logging.info("Invoicer service started.")
    main()
