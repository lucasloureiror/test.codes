# Run.Codes Test Helper

Este script foi desenvolvido para auxiliar os estudantes a executarem automaticamente seus casos de testes localmente antes de submetê-los ao Run.Codes, uma plataforma de correção automática de código frequentemente utilizada no Instituto de Ciências Matemáticas e de Computação (ICMC) da Universidade de São Paulo (USP).

O script é compatível com as linguagens de programação C, Python e Haskell.

# Como Utilizar

### Configurando o ambiente

1. Clone o repositório ou baixe o script `runner.py` para o seu computador.
2. Crie uma pasta chamada `casos` no mesmo diretório do script.
3. Coloque os seus arquivos de teste (com as extensões `.in` e `.out`) na pasta `casos`.
4. Na primeira vez que você executar o script, ele fará algumas perguntas para configurar o ambiente de testes:
    - "Qual a linguagem que será utilizada nesse projeto? 1- C, 2- Python, 3- Haskell"
    - "Qual o nome do arquivo (sem a extensão)?"
    - "Qual o caminho da pasta que possui os testes (arquivos .in e .out)? Se ele estiver em uma pasta aqui dentro chamada 'casos' digite apenas casos"

5. As respostas serão salvas em um arquivo chamado `test_config.json`. Caso queira alterar as configurações, você pode editar este arquivo diretamente ou excluí-lo e executar o script novamente para responder às perguntas.

### Executando os testes

1. Com o ambiente devidamente configurado, execute o script no terminal com o comando `python3 runner.py`.
2. O script executará cada caso de teste e comparará a saída do seu programa com a saída esperada. Ele exibirá quais casos foram aprovados e quais foram reprovados, e salvará as entradas, saídas esperadas e saídas do programa para cada caso de teste em um arquivo `.diff` na pasta "resultado".

# Observações

Por favor, observe que o script executa o seu programa usando os comandos de terminal padrão para cada linguagem (`./` para C, `python3` para Python e `runhaskell` para Haskell). Garanta que você tenha as devidas permissões para executar os comandos de terminal no seu ambiente.

Este script é um auxiliar para o teste de códigos a serem submetidos ao Run.Codes e não garante que a submissão será aprovada na plataforma. Ainda assim, ele pode ajudar a identificar erros no seu código antes da submissão, economizando tempo e reduzindo a quantidade de submissões necessárias.
