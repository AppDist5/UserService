import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("❌ DATABASE_URL no encontrada")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    print("🔍 Buscando transacciones colgadas...")

    # Ver transacciones activas
    result = conn.execute(text("""
        SELECT pid, state, query_start, query 
        FROM pg_stat_activity 
        WHERE state = 'idle in transaction'
        AND datname = current_database()
    """))

    transactions = result.fetchall()

    if not transactions:
        print("✅ No hay transacciones colgadas")
    else:
        print(f"⚠️ Encontradas {len(transactions)} transacciones colgadas:")
        for t in transactions:
            print(f"  - PID: {t[0]}, Estado: {t[1]}, Inicio: {t[2]}")
        
        print("\n🔨 Haciendo ROLLBACK de transacciones colgadas...")
        # Rollback de todas las transacciones inactivas de la sesión actual
        for t in transactions:
            try:
                conn.execute(text(f"ROLLBACK;"))
            except Exception as e:
                print(f"❌ Error haciendo rollback: {e}")

        print("✅ Rollback completado")

print("\n✅ Limpieza completada")
