import os
import subprocess
import json

LINGUAGENS = {
    '1': {
        'nome': 'C',
        'comando': './',
        'extensao': ''
    },
    '2': {
        'nome': 'Python',
        'comando': 'python3',
        'extensao': '.py'
    },
    '3': {
        'nome': 'Haskell',
        'comando': 'runhaskell',
        'extensao': '.hs'
    }
}

CONFIG_FILE = 'test_config.json'
RESULTADO_FOLDER = "resultado"

def obter_configuracoes():
    if not os.path.isfile(CONFIG_FILE):
        print("Esta parece ser a primeira vez que você está rodando o script.")
        config = {}
        escolha_linguagem = input("Qual a linguagem que será utilizada nesse projeto?\n1- C\n2-Python\n3-Haskell\n")
        linguagem = LINGUAGENS[escolha_linguagem]
        config['linguagem'] = linguagem['nome']
        config['comando'] = linguagem['comando']
        config['extensao'] = linguagem['extensao']
        config['nome_arquivo'] = input("Qual o nome do arquivo (sem a extensão)?\n")
        config['caminho_testes'] = input("Qual o caminho da pasta que possui os testes (arquivos .in e .out)?\nSe ele estiver em uma pasta aqui dentro chamada 'casos' digite apenas casos\n")
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        print("As configurações foram salvas no arquivo 'test_config.json'.")

def carregar_configuracoes():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def executar_testes():
    config = carregar_configuracoes()
    main_file = config['nome_arquivo'] + config['extensao']
    command = config['comando']
    casos_folder = config['caminho_testes']
    
    aprovados = []
    reprovados = []
    
    for in_file in os.listdir(casos_folder):
        if in_file.endswith(".in"):
            num_caso = os.path.splitext(in_file)[0]
            out_file = os.path.join(casos_folder, f"{num_caso}.out")
    
            with open(os.path.join(casos_folder, in_file)) as input_file:
                input_data = input_file.read()
    
            process = subprocess.run([command, main_file], input=input_data, capture_output=True, text=True)
    
            if process.stdout.strip() == open(out_file).read().strip():
                aprovados.append(num_caso)
            else:
                reprovados.append(num_caso)
    
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
    
    aprovados.sort(key=int)
    
    print("Casos aprovados:", ", ".join(aprovados))
    print("Casos reprovados:", ", ".join(reprovados))
    
    total = len(aprovados) + len(reprovados)
    print(f"Total: {len(aprovados)}/{total}")

def main():
    obter_configuracoes()
    executar_testes()

if __name__ == "__main__":
    main()
