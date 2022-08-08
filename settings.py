import os
from datetime import date

API_BASE_URL = str("https://api.splink.org.br/records/")
WORKING_DIR = os.getcwd()
DATA = date.today()

NIVEL = ["ScientificName", "family"]

ERRO_COLUNA_ARQUIVO = str(
    "Erro: Verificar se há coluna Especie no arquivo. Busca não iniciada.")
ERRO_NIVEL = str(
    f"Erro: nível taxonômico deve ser 'ScientificName' ou 'family'. Busca não iniciada.")
