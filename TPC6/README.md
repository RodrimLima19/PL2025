# TPC6 - Gramática Independente de Contexto

📅 **Data:** 2025-03-19  
👤 **Autor:** Rodrigo Mendes Lima, A104181  
![Foto](../Images/foto.jpg)  

## Resumo

Este trabalho consiste no desenvolvimento de um programa que implementa um **analisador léxico e sintático** para expressões aritméticas simples. O programa é capaz de reconhecer expressões como `5 - 4 * 3` ou `3 + 2`, calcular o resultado e escrever o valor formatado num arquivo de saída. 

O objetivo é criar um sistema que processe expressões aritméticas, respeitando a precedência de operadores (multiplicação e divisão têm prioridade sobre adição e subtração) e gere resultados formatados com uma casa decimal.

## Funcionalidades

O programa suporta as seguintes funcionalidades:

- **Análise Léxica**: Reconhece tokens como números (`NUM`), operadores de adição (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`).
- **Análise Sintática**: Implementa uma gramática independente de contexto para validar e processar expressões aritméticas.
- **Cálculo de Expressões**: Calcula o valor das expressões, respeitando a precedência dos operadores.
- **Formatação de Saída**: Escreve o resultado das expressões num arquivo de saída, com valores arredondados para uma casa decimal.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **exp_analex.py**: Implementa o analisador léxico, que reconhece os tokens das expressões.
- **exp_anasin_ri.py**: Implementa o analisador sintático recursivo, que processa as expressões e constrói a árvore sintática.
- **exp_ast.py**: Define a estrutura da árvore sintática abstrata (AST) com as classes `Exp` e `Num`.
- **exp_program_ri.py**: Programa principal que lê expressões de um arquivo de entrada, processa-as e escreve os resultados em um arquivo de saída.
- **input.txt**: Arquivo de entrada contendo as expressões a serem processadas.
- **output.txt**: Arquivo de saída onde os resultados das expressões são escritos.

## Gramática

A gramática independente de contexto é definida da seguinte forma:

```bash
P = {
    Expr -> Expr OP1 Termo
         | Termo

    Termo -> Termo OP2 Fator
           | Fator
    
    OP1 -> '+' | '-'
    OP2 -> '*' | '/'

    Fator -> Num
}

## Testes

Para testar as funcionalidades no interpretador de expressões, foram utilizados os seguintes ficheiros:

- 📄 [input.txt](./results/input.txt): Arquivo de entrada com expressões aritméticas para serem processadas.
- 📄 [output.txt](./results/output.txt): Arquivo de saída com os valores calculados pelo programa.


---

ℹ️ Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagens** da **Universidade do Minho**.