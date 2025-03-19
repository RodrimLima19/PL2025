from exp_anasin_ri import rec_Parser

filename = "./results/input.txt"
output_filename = "./results/output.txt"

if __name__ == "__main__":
    with open(filename, "r", encoding='utf-8') as file:
        with open(output_filename, "w", encoding='utf-8') as output_file:
            for line in file:
                exp = rec_Parser(line)
                resultado = exp.calc()
                resultado_formatado = round(float(resultado), 1)
                output_file.write(f"Valor da Expressão: {resultado_formatado:.1f}!\n")
                    
                


