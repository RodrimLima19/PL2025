def somador_on_off(texto, soma_acumulada, ligado, log_file):
    soma = soma_acumulada
    numero_atual = ""
    sinal_negativo = False  
    
    i = 0
    while i < len(texto):
        char = texto[i]

        if texto[i:i+3] == "off":
            ligado = False
            i += 2 

        elif texto[i:i+2] == "on":
            ligado = True
            i += 1  

        elif char == "=":
            log_file.write(f"Soma atual: {soma}\n")
            print(f"Soma atual: {soma}")

        elif char.isdigit():
            if ligado:
                numero_atual += char

        elif char == "-":
            if numero_atual:
                if ligado:
                    soma += int(numero_atual) if not sinal_negativo else -int(numero_atual)
                numero_atual = ""
            sinal_negativo = True
        else:
            if numero_atual:
                if ligado:
                    soma += int(numero_atual) if not sinal_negativo else -int(numero_atual)
                numero_atual = ""
            sinal_negativo = False  
        
        i += 1
    
    if numero_atual:
        if ligado:
            soma += int(numero_atual) if not sinal_negativo else -int(numero_atual)
    
    return soma, ligado


def processar_arquivo(caminho, caminho_saida):
    soma_total = 0
    ligado = True
    
    with open(caminho_saida, "w", encoding="utf-8") as log_file:
        with open(caminho, "r", encoding="utf-8") as file:
            for linha in file:
                linha = linha.strip().lower()  
                soma_total, ligado = somador_on_off(linha, soma_total, ligado, log_file)
        
        log_file.write(f"Resultado final do arquivo: {soma_total}\n")
    
    print(f"Resultado final do arquivo: {soma_total}")
    

resultado_final = processar_arquivo("data.txt", "results.txt")

