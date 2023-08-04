# WordGen

O WordGen é um programa desenvolvido em Python que permite gerar sequências de caracteres personalizadas com base nas preferências do usuário. Com o WordGen, é possível criar wordlists para testes de segurança, quebras de senha, e outras análises em que a geração de combinações de caracteres é necessária.

## Uso ético e legalidade

O uso de ferramentas de geração de wordlists, como o WordGen, pode ser benéfico quando utilizado para fins legítimos, como testes de segurança em sistemas e redes de computadores de propriedade do usuário ou com autorização explícita. É importante respeitar as leis e regulamentações de cada país em relação ao uso de ferramentas de segurança e garantir que sejam usadas apenas para fins éticos e autorizados.

É essencial obter permissão por escrito dos proprietários dos sistemas ou redes antes de realizar qualquer teste de penetração ou análise de segurança. O uso não autorizado de ferramentas como o WordGen em sistemas ou redes pode ser ilegal e acarretar em sérias consequências legais.

## Instalação

Para utilizar o WordGen como um comando executável no terminal, siga as etapas abaixo:

1. Faça o download dos arquivos do WordGen em seu computador.

2. Certifique-se de ter o Python 3.x instalado em sua máquina.

3. Abra o terminal (ou prompt de comando no Windows) e navegue até o diretório onde os arquivos do WordGen estão localizados.

4. Execute o seguinte comando para tornar o arquivo `main.py` executável:

`$ chmod +x main.py`

5. Em seguida, adicione um link simbólico para o arquivo `main.py` com o nome `wgen` (ou qualquer outro nome de sua preferência) no diretório `/usr/local/bin/` (ou outro diretório no PATH do seu sistema):

`$ ln -s /caminho/para/o/arquivo/main.py /usr/local/bin/wgen`

6. Agora você pode usar o WordGen digitando `wgen` seguido dos parâmetros desejados no terminal:

`$ wgen (parametros)`

Certifique-se de que o diretório onde o arquivo `main.py` está localizado está presente no PATH do seu sistema para que o comando `wgen` funcione corretamente.

## Exemplos de uso

Aqui estão alguns exemplos de uso do WordGen:

1. Gerar sequências de 4 a 6 caracteres com alfabeto minúsculo:

`$ wgen 4 6 -a -w sequences.txt`

2. Gerar sequências de 6 a 8 caracteres com letras maiúsculas, números e caracteres especiais:

`$ wgen 6 8 -A -n -e \!\@\# -w passwords.txt`

3. Gerar sequências de 1 a 3 caracteres com letras maiúsculas, minúsculas, números e todos os caracteres especiais:

`$ wgen 1 3 -aAn -ae -w results.txt`

Lembre-se de utilizar o WordGen de forma ética e respeitar as leis e regulamentações aplicáveis ao uso de ferramentas de segurança.
