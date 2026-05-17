import requests
import json
import database

api_url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json?$limit=1000"


def fetch_url():
    response = requests.get(api_url)
    data = response.json()
    return data

def load_data():
    conn = database.get_connection()
    records = fetch_url()
    
    for record in records:
        license_number = record.get("license_","")
        name = record.get("dba_name","")
        address = record.get("address","")
        zip_code = record.get("zip","")
        conn.execute("""
            INSERT OR IGNORE INTO establishment (license_number, name, address, zip_code)
            VALUES (?, ?, ?, ?)
        """, (license_number, name, address, zip_code))
        cursor = conn.execute("""
            INSERT INTO inspection (license_number, date, result, inspection_type)
            VALUES (?, ?, ?, ?)
        """, (
            license_number,
            record.get("inspection_date", ""),
            record.get("results", ""),
            record.get("inspection_type", "")
        ))

        inspection_id = cursor.lastrowid

        violations_text = record.get("violations", "")
        if violations_text:
            for violation in violations_text.split("|"):
                violation = violation.strip()
                if violation:
                    conn.execute("""
                        INSERT INTO violation (inspection_id, description)
                        VALUES (?, ?)
                    """, (inspection_id, violation[:500]))

    conn.commit()
    conn.close()
    print("Data loaded successfully.")
    
if __name__ == "__main__":
    load_data()