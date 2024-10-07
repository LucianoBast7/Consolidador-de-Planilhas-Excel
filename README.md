# 📊 Consolidador de Planilhas do Excel

## Descrição do Projeto

O projeto **Consolidador de Planilhas Excel com Pandas** tem como objetivo agrupar e consolidar dados de várias planilhas Excel em um único arquivo. Utilizando a biblioteca **Pandas** em Python, o script lê arquivos Excel de um diretório específico, extrai informações relevantes e gera um relatório consolidado, facilitando a análise e o gerenciamento dos dados.

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **OpenPyXL**: Biblioteca auxiliar para leitura/escrita de arquivos Excel.
- **Datetime**: Módulo para trabalhar com datas e horas.

## 🚀 Funcionalidades

- **Leitura de Arquivos Excel**: O script lê todos os arquivos com a extensão `.xlsx` de um diretório específico.
- **Extração de Dados**: Extrai informações como segmento, país e dados de vendas de cada planilha.
- **Tratamento de Erros**: Caso ocorra um erro ao ler um arquivo, uma mensagem de erro é registrada em um arquivo `log_erros.txt`.
- **Geração de Relatório**: Os dados consolidados são salvos em um novo arquivo Excel chamado `Report Consolidado - DD-MM-YYYY.xlsx`, onde a data é a data da execução do script.

## 📂 Estrutura de Diretórios

├── planilhas
│   ├── arquivo1-segmento1-pais1.xlsx
│   ├── arquivo2-segmento2-pais2.xlsx
│   └── ...
├── log_erros.txt
└── consolidar_planilhas.py

# 🛠️ Como Usar

## 1. Instale as Dependências
Certifique-se de que você tenha o Python e as bibliotecas necessárias instaladas. Você pode instalar o Pandas usando o seguinte comando:

```bash
pip install pandas openpyxl
```

## 2. Prepare seus Arquivos
Coloque suas planilhas Excel no diretório planilhas. Certifique-se de que cada arquivo siga o padrão segmento-pais.xlsx.

```bash
pip install pandas openpyxl
```

## 3. Execute o Script
Execute o script consolidar_planilhas.py:

```bash
python consolidar_planilhas.py
```

## 4. Verifique o Resultado
Um novo arquivo Excel chamado Report Consolidado - DD-MM-YYYY.xlsx será gerado na pasta do projeto. Além disso, verifique log_erros.txt para qualquer erro registrado.
