# TPC4 - Analisador Léxico

📅 **Data:** 2025-03-05  
👤 **Autor:** Rodrigo Mendes Lima, A104181  
![Foto](../Images/foto.jpg)  

## Resumo

Este trabalho consiste no desenvolvimento de um analisador léxico para uma linguagem de consulta, utilizando a biblioteca PLY (Python Lex-Yacc) em Python. O objetivo é processar consultas escritas em uma linguagem específica e identificar os tokens correspondentes, como comandos, identificadores, URIs, strings, números, entre outros.

## Funcionalidades

O analisador léxico suporta as seguintes funcionalidades:

- **Atributos**: Reconhece letras chave.
- **Comandos Reservados**: Reconhece palavras-chave como `SELECT`, `WHERE`, e `LIMIT`.
- **Identificadores**: Reconhece identificadores no formato `?nome`, `?desc`, etc., e os mapeia para tipos personalizados (ex: `VAR_NOME`, `VAR_DESC`).
- **URIs**: Reconhece URIs no formato `prefixo:valor` (ex: `dbo:MusicalArtist`).
- **Strings**: Reconhece strings no formato `"texto"` com suporte a idiomas (ex: `"Chuck Berry"@en`).
- **Números**: Reconhece números inteiros (ex: `1000`).
- **Símbolos Especiais**: Reconhece símbolos como `{`, `}`, `.`, e `#`.

## Testes

Para testar as funcionalidades no analisador léxico, foram utilizados os seguintes ficheiros:

- 📄 [input.txt](./results/input.txt): Arquivo de entrada com consultas para serem processadas.
- 📄 [output.txt](./results/output.txt): Arquivo de saída com os tokens gerados pelo analisador.


---

ℹ️ Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagens** da **Universidade do Minho**.