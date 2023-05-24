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

# Pasta onde estão os arquivos de entrada (.in) e saída (.out)
CASOS_FOLDER = config["pasta_dos_casos_de_teste"]

# Criar a pasta "resultado" se não existir
RESULTADO_FOLDER = "resultado"
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

        # RODAR_ARQUIVO constant is moved inside the loop
        RODAR_ARQUIVO = f"{linguagens[linguagem_prog]['comando']}{config['nome_do_arquivo']} < {os.path.join(CASOS_FOLDER, in_file)}"

        # Executar o comando para rodar o arquivo e capturar a saída
        process = subprocess.run(RODAR_ARQUIVO, capture_output=True, text=True, shell=True)

        # Comparar a saída gerada com a arquivo .out correspondente
        if process.stdout.strip() == open(out_file).read().strip():
            # Caso aprovado
            aprovados.append(num_caso)
        else:
            # Caso reprovado
            reprovados.append(num_caso)

            # Criar o arquivo .diff com a entrada, saída gerada e saída esperada
                    # Ler o conteúdo do arquivo de entrada para escrever no .diff
        with open(os.path.join(CASOS_FOLDER, in_file)) as input_file:
            input_data = input_file.read()

        # Criar o arquivo .diff com a entrada, saída gerada e saída esperada
        diff_file = os.path.join(RESULTADO_FOLDER, f"{num_caso}.diff")
        with open(diff_file, "w") as file:
            file.write(f"Entrada:\n{input_data}\n\n")
            file.write(f"Saída gerada:\n{process.stdout}\n\n")
            file.write(f"Saída esperada:\n{open(out_file).read()}\n")


# Ordenar a lista de casos aprovados
aprovados.sort(key=int)

# Imprimir casos aprovados
print("Casos aprovados:", ", ".join(aprovados))

# Imprimir casos reprovados
print("Casos reprovados:", ", ".join(reprovados))

# Imprimir total de casos
total = len(aprovados) + len(reprovados)
print(f"Total: {len(aprovados)}/{total}")
