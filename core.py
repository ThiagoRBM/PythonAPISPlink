import typer
from typing import List

import requests
import pandas as pd
import re
import time

import settings


def buscaAPI(especies: List[str],
             nivel: str = typer.Option(None, "-t", "--nivel"),
             caminhoTabela: str = typer.Option(None, "-s", "--nome")
             ):

    if bool(re.search("\\.txt$|\\.csv$", especies[0])):
        sp = pd.read_csv(especies[0])
        try:
            sp["Especies"]
        except KeyError:
            print(f"\n\n{settings.ERRO_COLUNA_ARQUIVO}\n\n")
            return
        print(f"{sp}\n\n")
        especies = [especie.strip() for especie in sp["Especies"]]

    if caminhoTabela is None:
        caminhoTabela = f"{settings.WORKING_DIR}/busca_{settings.DATA.strftime('%Y_%m_%d')}.csv"
    if nivel is None:
        nivel = "ScientificName"
    elif str(nivel) not in settings.NIVEL:
        print(
            f"\n\n{settings.ERRO_NIVEL}\nNível taxônomico buscado: '{nivel}'\n\n")
        return

    urlBase = f"{settings.API_BASE_URL}{nivel}/"
    urlReq = [str(urlBase) + str(especie.replace(' ', '%20')).lower()
              for especie in especies]

    response = []
    for i, url in enumerate(urlReq):
        print(f"buscando informações para: {''.join(especies[i])}")
        rs = requests.get(url)
        if rs.status_code != 200:
            # print(rs.status_code)
            rs = str("STATUS CODE: ") + rs.status_code
        response.append(rs.text)
        if i % 3 == 0:  # caso o numero da iteracao seja multiplo de 3, esperar 4 segundos para o proximo request
            time.sleep(4)

    buscaTotal = []
    for i, x in enumerate(response):
        lista = []
        for line in x.splitlines():
            line = re.split("\t", line)
            lista.append(line)
            df = pd.DataFrame(lista[1:], columns=lista[0])
        if len(df) == 0:
            print(
                f"\nINFORMAÇÃO PARA {especies[i]} NÃO ENCONTRADA.")
        buscaTotal.append(df)
    buscaTotal = pd.concat(buscaTotal)
    buscaTotal.to_csv(caminhoTabela,
                      index=False, encoding='utf-8')

    print(f"\n\narquivo {caminhoTabela} salvo\n\n")
