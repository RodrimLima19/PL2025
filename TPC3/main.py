import re
import sys
import re
import re

def main(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print("Ficheiro Inválido ou erro ao ler o arquivo:", e)
        return 0

    # Cabeçalhos: 
    for i in range(1, 4):
        pattern = rf'(?m)^{"#" * i} (.+)$'
        replacement = rf'<h{i}>\1</h{i}>\n'
        content = re.sub(pattern, replacement, content)

    # Bold: 
    content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)

    # Itálico: 
    content = re.sub(r'\*(.*?)\*', r'<i>\1</i>', content)

    # Lista:
    res = ""
    ol_open = False 
    for line in content.split("\n"):
        if re.match(r"^[ ]*[\d]+. (.*)$", line):
            if not ol_open: 
                res += "<ol>\n"
                ol_open = True
            item = re.sub(r"^[ ]*[\d]+. (.*)$", "\t<li>\\1</li>", line)
            res += item + "\n"
        else:
            if ol_open: 
                res += "</ol>\n"
                ol_open = False
            res += line + "\n" 

    content = res

    # Link: 
    content = re.sub(r'(.*?)\[(.*?)\]\((.*?)\)', r'\1 <a href="\3">\2</a>', content)

    # Imagem: 
    content = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1">', content)

    output_filename = 'output.html'
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(content)
    except Exception as e:
        print("Erro ao escrever no arquivo de saída:", e)


main('input.md')