# TPC2 - Análise de um Dataset de Obras Musicais

📅 **Data:** 2025-02-19  
👤 **Autor:** Rodrigo Mendes Lima, A104181  
![Foto](../Images/foto.jpg)  

## Resumo

Este trabalho consiste na análise de um dataset de obras musicais, onde o objetivo é processar e extrair informações relevantes sem utilizar o módulo CSV do Python. O trabalho envolveu:

- Leitura e processamento de um ficheiro CSV contendo informações sobre obras musicais, incluindo compositores, títulos e períodos históricos.
- Implementação de um **parser** para normalizar o dataset, garantindo que os dados estejam consistentes e prontos para análise. O parser foi responsável por:
  - Remover inconsistências nos dados.
  - Garantir que os campos estivessem corretamente formatados (por exemplo, normalizando nomes de compositores por ordem de nome, sobrenome ...).
  - Gerar o ficheiro `obras_new.csv`, que foi utilizado como base para a análise.
  - O código do parser pode ser encontrado aqui: [parser.py](data/parser.py).
- Criação de três resultados principais:
  1. Uma lista ordenada alfabeticamente dos compositores musicais.
  2. A distribuição das obras por período histórico, contabilizando quantas obras estão catalogadas em cada período.
  3. Um dicionário que associa cada período histórico a uma lista alfabética dos títulos das obras desse período.

## Testes

Os testes realizados basearam-se num conjunto de dados de entrada e nos respetivos resultados processados. Para este efeito, foram utilizados os seguintes ficheiros:

- 📄 [obras.csv](data/obras.csv) - Dataset original, utilizado como entrada para o parser.
- 📄 [obras_new.csv](data/obras_new.csv) - Dataset normalizado, gerado pelo parser e utilizado como base para a análise.
- 📄 [compositores.txt](results/compositores.txt) - Contém a lista ordenada alfabeticamente dos compositores.
- 📄 [periodos.txt](results/periodos.txt) - Contém a distribuição das obras por período histórico.
- 📄 [obras_periodo.txt](results/obras_periodo.txt) - Contém o dicionário com os títulos das obras organizados por período histórico.

---

ℹ️ Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagens** da **Universidade do Minho**.