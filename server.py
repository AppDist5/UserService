import os
from dotenv import load_dotenv
from src.app import create_app
from src.config.database import init_db, SessionLocal
from src.models.specialty import Specialty

load_dotenv()

PORT = int(os.getenv("PORT", 3001))

def initialize_specialties():
    db = SessionLocal()
    try:
        count = db.query(Specialty).count()
        if count == 0:
            specialties = [
                {"nombre": "Cardiología", "descripcion": "Especialidad del corazón"},
                {"nombre": "Pediatría", "descripcion": "Atención a niños"},
                {"nombre": "Dermatología", "descripcion": "Enfermedades de la piel"},
            ]
            for spec_data in specialties:
                db.add(Specialty(**spec_data))
            db.commit()
            print("✅ Initial specialties created")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    initialize_specialties()
    app = create_app()
    print(f"🚀 User Service running on port {PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=True)
