import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# 👇 ESTA LÍNEA ES LA QUE FALTABA
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("❌ DATABASE_URL no encontrada")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("⚠️ Borrando TODA la base de datos de Render...")
    conn.execute(text("DROP SCHEMA public CASCADE;"))
    conn.execute(text("CREATE SCHEMA public;"))
    conn.execute(text("GRANT ALL ON SCHEMA public TO postgres;"))
    conn.execute(text("GRANT ALL ON SCHEMA public TO public;"))
    conn.commit()

print("✅ Base de datos de Render reseteada correctamente")
