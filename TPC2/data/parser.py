import re

def corrigir_nome_compositor(nome):
    if ',' in nome:
        sobrenome, nome = nome.split(',')
        return f"{nome.strip()} {sobrenome.strip()}"
    return nome

def corrigir_descricao(descricao):
    descricao = descricao.replace(';', ',').replace('\n', ' ')
    descricao = re.sub(r'\s{2,}', ' ', descricao).strip()
    return descricao

def processar_csv(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, mode='r', encoding='utf-8') as infile, \
         open(arquivo_saida, mode='w', encoding='utf-8') as outfile:
        
        conteudo = infile.read()
        
        linhas = []
        dentro_de_campo = False
        buffer = ""
        for char in conteudo:
            if char == '"':
                dentro_de_campo = not dentro_de_campo 
                buffer += char
            elif char == '\n' and not dentro_de_campo:
                linhas.append(buffer)
                buffer = ""
            else:
                buffer += char
        
        if buffer:
            linhas.append(buffer)
        
        cabecalho = linhas[0].strip().split(';')
        novo_cabecalho = ['_id'] + [col for col in cabecalho if col != '_id']
        outfile.write(';'.join(novo_cabecalho) + '\n')
        
        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha:
                continue
            
            colunas = []
            buffer = ""
            dentro_de_campo = False
            for char in linha:
                if char == '"':
                    dentro_de_campo = not dentro_de_campo
                    buffer += char
                elif char == ';' and not dentro_de_campo:
                    colunas.append(buffer)
                    buffer = ""
                else:
                    buffer += char
            colunas.append(buffer) 
            dados = dict(zip(cabecalho, colunas))
            dados['compositor'] = corrigir_nome_compositor(dados['compositor'])
            dados['desc'] = corrigir_descricao(dados['desc'])
            nova_linha = [dados['_id']] + [dados[col] for col in novo_cabecalho[1:]]
            outfile.write(';'.join(nova_linha) + '\n')

processar_csv('data/obras.csv', 'data/obras_new.csv')
