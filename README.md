# PythonAPISPlink

Busca informações de coletas (ou observação) de espécies, gêneros ou famílias no SPLink (https://specieslink.net/) através da API deles.
As informações são salvas em um arquivo .csv.

Projeto feito para treinar o que foi apresentado pelo Bruno Rocha na #PythonWeek 2022 na LinuxTips (https://www.youtube.com/watch?v=NqUC-G_Pu-o&list=PLf-O3X2-mxDlfAv8IOfic1sHArdwrrkgh).

######Argumentos:
   - **especies:** OBRIGATÓRIO. A ou as espécies a serem procuradas (pode ser gênero). Pode ser o caminho para um arquivos ".csv" ou ".txt" e nesse caso, 
    as espécies devem estar listadas em uma coluna com nome "Especies".
   - **nivel:** OPCIONAL. Por padrão busca por espécie ou gênero. Se "family", busca por espécies da família.
   - **caminho_tabela:** OPCIONAL. Localizacao em que a tabela com as informações das espécies serão salvas.
    Se deixado em branco, a tabela será salva no diretório corrente, com o nome 'busca_SPLink_data.csv',
    com a data no formato ano_mes_dia. Fornecer caminho completo + nome do arquivo (e.g. "home/usuario/tabela.csv")
