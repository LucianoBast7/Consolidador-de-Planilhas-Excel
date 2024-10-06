import pandas as pd
import os
import datetime as dt


def consolidar_arquivo():
    data = dt.datetime.now()

    colunas = [
        'Segmento',
        'País',
        'Produto',
	    'Qtde de Unidades Vendidas',
	    'Preço Unitário',
        'Valor Total',
        'Desconto',
        'Valor Total c/ Desconto',	
        'Custo Total',
        'Lucro',
	    'Data',
	    'Mês',
	    'Ano'

    ]
    consolidado = pd.DataFrame(columns=colunas)

    arquivos = os.listdir(r"C:\Users\lbbas\Desktop\Cursos\Python Avançado\Analise de Dados\Projetos\Consolidando Planilhas Excel com Pandas\Projeto - Luciano\planilhas")

    for excel in arquivos:

        if excel.endswith('.xlsx'):
            dados_arquivo = excel.split('-')
            segmento = dados_arquivo[0]
            pais = dados_arquivo[1].replace('.xlsx', '')

            try:
                df = pd.read_excel(f'planilhas\\{excel}')
                df.insert(0, 'Segmento', segmento)
                df.insert(1, 'País', pais)
                consolidado = pd.concat([consolidado, df])
            except:
                with open('log_erros.txt', 'a') as arquivo:
                    arquivo.write(f'Erro ao tentar consolidar arquivo {excel}')

        else:
            with open('log_erros.txt', 'a') as arquivo:
                arquivo.write(f'O arquivo {excel} não é um arquivo válido!')

            
    consolidado.to_excel(f"Report Consolidado - {data.strftime('%d-%m-%Y')}.xlsx", index=False, sheet_name='Relatório Consolidado')


consolidar_arquivo()