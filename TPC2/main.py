import re

def listar_compositores(linhas):
    compositores = set()
    for linha in linhas[1:]: 
        tokens = re.split(r';', linha)
        if len(tokens) > 5:  
            compositores.add(tokens[5].strip())   
    return sorted(compositores)

def periodos(linhas):
    periodos = set()
    for linha in linhas[1:]: 
        tokens = re.split(r';', linha)
        if len(tokens) > 4:  
            periodos.add(tokens[4].strip()) 
    return periodos

def count_obras_periodos(linhas, periodos):
    obras_por_periodo = {periodo: 0 for periodo in periodos}
    for linha in linhas[1:]:  
        tokens = re.split(r';', linha)
        if len(tokens) > 4:  
            periodo = tokens[4].strip() 
            obras_por_periodo[periodo] += 1  
    return obras_por_periodo

def obras_periodos(linhas, periodos):
    obras_por_periodo = {periodo: [] for periodo in periodos}
    
    for linha in linhas[1:]:  
        tokens = re.split(r';', linha)
        if len(tokens) > 4:  
            periodo = tokens[4].strip()
            titulo_obra = tokens[1].strip()
            obras_por_periodo[periodo].append(titulo_obra) 
    
    for periodo in obras_por_periodo:
        obras_por_periodo[periodo].sort()
    
    return obras_por_periodo

def processar_arquivo(caminho, caminho_saida):    
    with open(caminho, "r", encoding="utf-8") as file:
        linhas = file.readlines()
        
        if caminho_saida.endswith("compositores.txt"):
            compositores = listar_compositores(linhas)
            with open(caminho_saida, "w", encoding="utf-8") as log_file:
                for compositor in compositores:
                    log_file.write(compositor + "\n")
        
        elif caminho_saida.endswith("periodos.txt"):
            periodos_set = periodos(linhas)  
            obras_por_periodo = count_obras_periodos(linhas, periodos_set) 
            with open(caminho_saida, "w", encoding="utf-8") as log_file:
                for periodo, count in obras_por_periodo.items():
                    log_file.write(f"{periodo}: {count} obras\n")

        elif caminho_saida.endswith("periodo.txt"):
            periodos_set = periodos(linhas)  
            obras_por_periodo = obras_periodos(linhas, periodos_set) 
            with open(caminho_saida, "w", encoding="utf-8") as log_file:
                for periodo, count in obras_por_periodo.items():
                    log_file.write(f"{periodo}: {count} obras\n") 

processar_arquivo("data/obras_new.csv", "results/compositores.txt") 
processar_arquivo("data/obras_new.csv", "results/periodos.txt")
processar_arquivo("data/obras_new.csv", "results/obras_periodo.txt") 