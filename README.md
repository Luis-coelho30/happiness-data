# happiness-data

Análise da relação entre idade e felicidade em escala global, usando dados do World Happiness Report 2024 e indicadores do Banco Mundial.

## Integrantes do projeto

Luís Augusto Coelho de Souza
Guilherme Schnekenberg Teixeira

## Estrutura do projeto
```
happiness-data/
├── README.md
├── requirements.txt
├── lab_helpers.py
├── .gitignore
└── happiness_data.ipynb
```

## Dados

- **Our World in Data** - escores da escada de Cantril por faixa etária e país (WHR 2024)
- **World Bank API** - PIB per capita PPP (NY.GDP.PCAP.PP.KD), população (SP.POP.TOTL) e área terrestre (AG.LND.TOTL.K2)
- **IMF World Economic Outlook** - complemento de GDP para Venezuela, Yemen e Taiwan
- Dados de área e população de Taiwan e Kosovo obtidos de fontes abertas e inseridos manualmente

## Metodologia

O notebook segue quatro partes:

1. **Coleta e limpeza** - download dos dados por faixa etária, integração com indicadores do Banco Mundial via ISO3, tratamento de dados faltantes (Kosovo, Taiwan, Venezuela, Yemen)
2. **Regressão linear** - três modelos aninhados (M1: idade, M2: idade + idade², M3: M2 + controles econômicos) com validação cruzada por país via GroupKFold
3. **Regressão logística** - classificação binária (feliz/não feliz) com limiar na mediana, avaliada com GroupShuffleSplit; comparação entre divisão por país e aleatória para Logistic Regression e Random Forest
4. **Função de predição** - `check_happiness(country, age)` retorna a probabilidade de felicidade para qualquer país e idade

## Principais achados

- Idade sozinha explica menos de 2% da variação da felicidade entre países (R² < 0.02)
- Adicionando controles econômicos, o R² sobe para 0.62 - riqueza domina
- Dentro dos países (controlando pela média nacional), idade explica até 38% da variação
- O mínimo da curva estimado foi de 62.8 anos, acima dos 40-50 anos reportados na literatura - possivelmente reflexo das mudanças geracionais identificadas no WHR 2024
- O modelo logístico atinge AUC-ROC de 0.925 em países não vistos

## Helpers

`lab_helpers.py` expõe `read_zip_wbd(indicator)`, que baixa e lê CSVs da API do Banco Mundial a partir do código do indicador.
