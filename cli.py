#!/usr/bin/env python3
import typer
from typing import List

import core

main = typer.Typer(
    help="Busca e salva informações de coletas de espécies disponíveis no SPLink (https://specieslink.net/) através de API e salva em arquivo '.csv'."
)


@main.command("buscaSp")
def buscaSp(
    especies: List[str],
    nivel: str = typer.Option(None, "-t", "--nivel"),
    caminho_tabela: str = typer.Option(None, "-s", "--nome"),
):
    """Funcao que busca informacoes de espécies disponíveis no SPLink (https://specieslink.net/) através de API e salva em arquivo '.csv.'

    Argumentos:\n
    especies: OBRIGATÓRIO. A ou as espécies a serem procuradas (pode ser gênero). Pode ser o caminho para um arquivos ".csv" ou ".txt" e nesse caso, as espécies devem estar listadas em uma coluna com nome "Especies".\n
    nivel: OPCIONAL. Por padrão busca por espécie ou gênero. Se "family", busca por espécies da família.\n
    caminho_tabela: OPCIONAL. Localizacao em que a tabela com as informações das espécies serão salvas.
    Se deixado em branco, a tabela será salva no diretório corrente, com o nome 'busca_SPLink_data.csv',
    com a data no formato ano_mes_dia. Fornecer caminho completo + nome do arquivo (e.g. "home/usuario/tabela.csv")
    """

    core.buscaAPI(especies, nivel, caminho_tabela)


@main.command("teste")
def teste():
    """Funcao testando como chamar a funcao caso o "programa" tenha mais de uma. Sem utilidade"""
    print("teste")
