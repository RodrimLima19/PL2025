# TPC5 - Máquina de Vending

📅 **Data:** 2025-03-12 
👤 **Autor:** Rodrigo Mendes Lima, A104181  
![Foto](../Images/foto.jpg)  

## Resumo

Este trabalho consiste no desenvolvimento de um programa que simula o funcionamento de uma **máquina de vending**. O programa permite a interação com o utilizador, permitindo a compra de produtos, gestão de stock e cálculo de troco. O stock de produtos é armazenado num ficheiro JSON, que é carregado no início do programa e atualizado no final.

O objetivo é criar uma simulação realista de uma máquina de vending, com funcionalidades como listagem de produtos, inserção de moedas, seleção de produtos e devolução de troco.

## Funcionalidades

O programa suporta as seguintes funcionalidades:

- **Listagem de Produtos**: Comando `LISTAR` para exibir todos os produtos disponíveis, com código, nome, quantidade e preço.
- **Inserção de Moedas**: Comando `MOEDA` para adicionar moedas ao saldo (ex: `MOEDA 1e, 50c`).
- **Seleção de Produtos**: Comando `SELECIONAR` para escolher um produto pelo código (ex: `SELECIONAR A23`).
- **Devolução de Troco**: Comando `SAIR` para terminar a interação e devolver o troco, se houver saldo restante.
- **Gestão de Stock**: O stock é carregado de um ficheiro JSON (`stock.json`) e atualizado no final da execução.

## Estrutura do Projeto

- **stock.json**: Ficheiro JSON que contém o stock de produtos, com informações como código, nome, quantidade e preço.
- **main.py**: Programa principal que implementa a lógica da máquina de vending.

## Testes

Para testar as funcionalidades da máquina de vending, foram utilizados os seguintes cenários:

1. **Listagem de Produtos**:
   - Comando: `LISTAR`
   - Saída esperada: Lista de produtos com código, nome, quantidade e preço.

2. **Inserção de Moedas**:
   - Comando: `MOEDA 1e, 50c`
   - Saída esperada: Saldo atualizado (ex: `Saldo = 1e50c`).

3. **Seleção de Produtos**:
   - Comando: `SELECIONAR A23`
   - Saída esperada: Mensagem de sucesso (ex: `Pode retirar o produto dispensado "água 0.5L"`) ou erro, se o saldo for insuficiente ou o produto estiver fora de stock.

4. **Devolução de Troco**:
   - Comando: `SAIR`
   - Saída esperada: Troco devolvido (ex: `Pode retirar o troco: 1x 50c, 1x 20c, 1x 10c`) e término da interação.

---

ℹ️ Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagens** da **Universidade do Minho**.

