# Chicago Food Inspection Dashboard

A web app that lets Chicago residents search food establishments and view their inspection history and violations.

## Stack
- Python, Flask, SQLite, Chart.js, Render

## Features
- Search establishments by name or ZIP code
- View full inspection history per restaurant
- Pass/Fail bar chart for each establishment
- Violation details for every inspection

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Create the database:
```
python database.py
```

3. Load inspection data (10,000 records):
```
python fetch_data.py
```

4. Run the app:
```
python app.py
```

5. Open your browser at `http://127.0.0.1:5000`

## Data Source
[City of Chicago Food Inspections](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5)

## Author
Jacob Williams — UIC Computer Science
