import os
import subprocess
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

linguagens = {
    "c": {"comando": "./", "extensao": ""},
    "haskell": {"comando": "runhaskell ", "extensao": ".hs"},
    "python": {"comando": "python3 ", "extensao": ".py"},
}

# Converter a linguagem de programação para letras minúsculas
linguagem_prog = config["linguagem_de_prog"].lower()

# Verificar se a linguagem de programação está no dicionário
if linguagem_prog not in linguagens:
    print("Linguagem de programação inválida.")
    exit(1)

# Constante para rodar o arquivo
RODAR_ARQUIVO = linguagens[linguagem_prog]["comando"] + config["nome_do_arquivo"]

# Caminho para o arquivo main.hs
MAIN_FILE = config["nome_do_arquivo"]

# Pasta onde estão os arquivos de entrada (.in) e saída (.out)
CASOS_FOLDER = config["pasta_dos_casos_de_teste"]

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

        # Executar o comando para rodar o arquivo e capturar a saída
        process = subprocess.run(RODAR_ARQUIVO, input=input_data, capture_output=True, text=True, shell=True)

        # Comparar a saída gerada com o arquivo .out correspondente
        if process.stdout.strip() == open(out_file).read().strip():
            # Caso aprovado
            aprovados.append(num_caso)
        else:
            # Caso reprovado
            reprovados.append(num_caso)

# Ordenar a lista de casos aprovados
aprovados.sort(key=int)

# Imprimir casos aprovados
print("Casos aprovados:", ", ".join(aprovados))

# Imprimir casos reprovados
print("Casos reprovados:", ", ".join(reprovados))

# Imprimir total de casos
total = len(aprovados) + len(reprovados)
print(f"Total: {len(aprovados)}/{total}")
