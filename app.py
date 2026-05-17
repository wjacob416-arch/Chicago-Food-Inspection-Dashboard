from flask import Flask, render_template, request, abort
import database
import fetch_data

app = Flask(__name__)

database.create_database()
fetch_data.run()

# Home page - renders the search form
@app.route("/")
def index():
    return render_template("index.html")

# Search route - queries establishments by name and optional ZIP code
@app.route("/search")
def search():
    q = request.args.get("q","")
    zip_code = request.args.get("zip","")
    conn = database.get_connection()

    if zip_code:
        results = conn.execute(
            "SELECT * FROM establishment WHERE zip_code = ? AND name LIKE ? COLLATE NOCASE",
            (zip_code, f"%{q}%")
        ).fetchall()
    else:
        results = conn.execute(
            "SELECT * FROM establishment WHERE name LIKE ? COLLATE NOCASE",
            (f"%{q}%",)
        ).fetchall()

    conn.close()
    return render_template("results.html", results=results, q=q, zip=zip_code)

# Detail page - shows inspection history and violations for a single establishment
@app.route("/restaurant/<license_number>")
def details(license_number):
    conn = database.get_connection()

    establishment = conn.execute(
        "SELECT * FROM establishment WHERE license_number = ?",
        (license_number,)
    ).fetchone()

    # Single JOIN query to get inspections and their violations together
    inspections = conn.execute(
        """SELECT i.id, i.date, i.result, i.inspection_type,
                  v.code, v.description, v.severity
           FROM inspection i
           LEFT JOIN violation v ON v.inspection_id = i.id
           WHERE i.license_number = ?
           ORDER BY i.date DESC""",
        (license_number,)
    ).fetchall()

    conn.close()
    if establishment is None:
        abort(404)
    return render_template("detail.html", establishment=establishment, inspections=inspections)

if __name__ == "__main__":
    app.run(debug=True)
