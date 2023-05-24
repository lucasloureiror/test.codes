import os
import subprocess

# Caminho para o arquivo main.py
MAIN_FILE = "main.py"

# Pasta onde estão os arquivos de entrada (.in) e saída (.out)
CASOS_FOLDER = "casos"

# Pasta onde serão salvos os resultados
RESULTADO_FOLDER = "resultado"

# Criar a pasta "resultado" se não existir
if not os.path.exists(RESULTADO_FOLDER):
    os.makedirs(RESULTADO_FOLDER)

# Listas para casos aprovados e reprovados
aprovados = []
reprovados = []

# Loop para percorrer os arquivos de entrada
for in_file in os.listdir(CASOS_FOLDER):
    if in_file.endswith(".in"):
        # Extrair o número do caso a partir do nome do arquivo
        num_caso = os.path.splitext(in_file)[0]
        out_file = os.path.join(CASOS_FOLDER, f"{num_caso}.out")

        # Ler o conteúdo do arquivo de entrada
        with open(os.path.join(CASOS_FOLDER, in_file)) as input_file:
            input_data = input_file.read()

        # Executar o comando python3 e capturar a saída
        process = subprocess.run(["python3", MAIN_FILE], input=input_data, capture_output=True, text=True)

        # Comparar a saída gerada com o arquivo .out correspondente
        if process.stdout.strip() == open(out_file).read().strip():
            # Caso aprovado
            aprovados.append(num_caso)
        else:
            # Caso reprovado
            reprovados.append(num_caso)

        # Criar o arquivo de resultado para o caso de teste
        resultado_file = os.path.join(RESULTADO_FOLDER, f"{num_caso}.diff")
        with open(resultado_file, "w") as file:
            file.write(f"Arquivo origem da entrada: {in_file}\n")
            file.write("Entrada:\n")
            file.write(f"{input_data}\n\n")
            file.write(f"Arquivo origem da saída esperada: {out_file}\n")
            file.write("Saída esperada:\n")
            file.write(f"{open(out_file).read()}\n\n")
            file.write("Saída do programa:\n")
            file.write(f"{process.stdout}\n")

# Ordenar a lista de casos aprovados
aprovados.sort(key=int)

# Imprimir casos aprovados
print("Casos aprovados:", ", ".join(aprovados))

# Imprimir casos reprovados
print("Casos reprovados:", ", ".join(reprovados))

# Imprimir total de casos
total = len(aprovados) + len(reprovados)
print(f"Total: {len(aprovados)}/{total}")
