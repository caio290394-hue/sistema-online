from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI()

# =========================
# CORS (obrigatório p/ frontend)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Banco de dados
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "banco.db")

def conectar():
    return sqlite3.connect(DB)

# =========================
# Rotas
# =========================
@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/estatisticas")
def estatisticas():
    conn = conectar()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM inquerito")
    inq = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM boletim")
    bol = c.fetchone()[0]

    conn.close()

    return {
        "inqueritos": inq,
        "boletins": bol
    }

@app.get("/inqueritos")
def listar_inqueritos():
    conn = conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM inquerito")
    colunas = [d[0] for d in c.description]
    dados = [dict(zip(colunas, row)) for row in c.fetchall()]

    conn.close()
    return dados


@app.get("/boletins")
def listar_boletins():
    conn = conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM boletim")
    colunas = [d[0] for d in c.description]
    dados = [dict(zip(colunas, row)) for row in c.fetchall()]

    conn.close()
    return dados
