import os
from datetime import date
import logging

API_BASE_URL = str("https://api.splink.org.br/records/")
WORKING_DIR = os.getcwd()

DATA = date.today()

NIVEL = ["ScientificName", "family"]

# BOILERPLATE (aula de logs)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("thiago", log_level)
ch = logging.StreamHandler()  # Console/terminal/stderr. Pode ser formatado
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

ERRO_COLUNA_ARQUIVO = str(
    "Erro: Verificar se há coluna Especie no arquivo. Busca não iniciada."
)
ERRO_NIVEL = str(
    f"Erro: nível taxonômico deve ser 'ScientificName' ou 'family'. Busca não iniciada."
)
