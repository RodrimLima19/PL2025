# TPC3 - Conversor de Markdown para HTML

📅 **Data:** 2025-02-21  
👤 **Autor:** Rodrigo Mendes Lima, A104181  
![Foto](../Images/foto.jpg)  

## Resumo

Este trabalho consiste num conversor de Markdown para HTML, desenvolvido em Python. O objetivo é transformar ficheiros Markdown em HTML, suportando as seguintes funcionalidades:

- **Cabeçalhos** (`#`, `##`, `###`).
- **Negrito** (`**texto**`).
- **Itálico** (`*texto*`).
- **Listas numeradas** (`1.`, `2.`, `3.`).
- **Links** (`[texto](URL)`).
- **Imagens** (`![texto alternativo](URL)`).

## Testes

Para testar as funcionalidades, foram utilizados os seguintes ficheiros:

- 📄 [input.md](input.md): Arquivo Markdown de entrada.
- 📄 [output.html](output.html): Arquivo HTML gerado após a conversão.

### Exemplos de Conversão

#### 1. Cabeçalhos  
**Entrada (`input.md`):** `# Título Principal`  
**Saída (`output.html`):** `<h1>Título Principal</h1>`

#### 2. Negrito  
**Entrada (`input.md`):** `Este é um **exemplo** de texto em negrito.`  
**Saída (`output.html`):** `Este é um <b>exemplo</b> de texto em negrito.`

#### 3. Itálico  
**Entrada (`input.md`):** `Este é um *exemplo* de texto em itálico.`  
**Saída (`output.html`):** `Este é um <i>exemplo</i> de texto em itálico.`

#### 4. Listas Numeradas  
**Entrada (`input.md`):** `1. Primeiro item`  
**Saída (`output.html`):** `<ol><li>Primeiro item</li></ol>`

#### 5. Links  
**Entrada (`input.md`):** `Como pode ser consultado em [página da UC](http://www.uc.pt).`  
**Saída (`output.html`):** `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>.`

#### 6. Imagens  
**Entrada (`input.md`):** `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coelho.com).`  
**Saída (`output.html`):** `Como se vê na imagem seguinte: <img src="http://www.coelho.com" alt="imagem dum coelho">.`

---

ℹ️ Este projeto foi desenvolvido no âmbito da disciplina de **Processamento de Linguagens** da **Universidade do Minho**.