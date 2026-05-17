CREATE TABLE IF NOT EXISTS establishment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_number TEXT NOT NULL UNIQUE CHECK(length(license_number) <= 20),
    name TEXT NOT NULL CHECK(length(name) <= 200),
    address TEXT CHECK(length(address) <= 200),
    zip_code TEXT CHECK(length(zip_code) <= 10),
    neighborhood TEXT CHECK(length(neighborhood) <= 100)
);

CREATE TABLE IF NOT EXISTS inspection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_number TEXT NOT NULL,
    date TEXT NOT NULL,
    result TEXT NOT NULL,
    inspection_type TEXT,
    FOREIGN KEY (license_number) REFERENCES establishment(license_number)
);

CREATE TABLE IF NOT EXISTS violation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inspection_id INTEGER NOT NULL,
    code TEXT,
    description TEXT NOT NULL CHECK(length(description) <= 500),
    severity TEXT CHECK(length(severity) <= 20),
    FOREIGN KEY (inspection_id) REFERENCES inspection(id)
);

CREATE INDEX IF NOT EXISTS idx_establishment_name ON establishment(name);
CREATE INDEX IF NOT EXISTS idx_establishment_zip ON establishment(zip_code);
CREATE INDEX IF NOT EXISTS idx_establishment_neighborhood ON establishment(neighborhood);
CREATE INDEX IF NOT EXISTS idx_inspection_license ON inspection(license_number);
CREATE INDEX IF NOT EXISTS idx_violation_inspection ON violation(inspection_id);