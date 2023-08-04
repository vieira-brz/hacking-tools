# Informações de Rede e Teste de Portas com Telnet

Este script Python é usado para obter informações sobre a rede do computador, incluindo o endereço IP, o gateway, o nome da interface, o endereço MAC e o BSSID da rede Wi-Fi (se aplicável). Além disso, ele utiliza o Nmap para listar as portas abertas no gateway da rede e, em seguida, faz um teste de conexão Telnet para cada porta aberta encontrada.

## Requisitos

- Python 3.x
- Nmap (https://nmap.org)

## Como usar

1. Certifique-se de que o Python 3.x está instalado em seu computador.
2. Instale o Nmap a partir do site oficial (https://nmap.org) e certifique-se de que o executável "nmap" esteja no seu PATH do sistema.
3. Baixe o arquivo `main.py` deste repositório.
4. Abra o terminal ou prompt de comando e navegue até o diretório onde você baixou o arquivo `main.py`.
5. Execute o comando `python main.py`.

## Instruções para utilizar o netwinf

Para utilizar o script `main.py` como um comando executável no terminal, siga as etapas abaixo:

1. Faça o download dos arquivos do projeto em seu computador.

2. Certifique-se de ter o Python 3.x instalado em sua máquina.

3. Abra o terminal (ou prompt de comando no Windows) e navegue até o diretório onde os arquivos do projeto estão localizados.

4. Execute o seguinte comando para tornar o arquivo `main.py` executável:

`$ chmod +x main.py`

O script irá imprimir as informações do PC, as informações da rede e os resultados do Nmap no gateway. Em seguida, ele mostrará as portas abertas encontradas e fará um teste de conexão Telnet para cada uma delas.

Em seguida, crie um link simbólico para o arquivo main.py com o nome netwinf (ou qualquer outro nome de sua preferência) no diretório /usr/local/bin/ (ou outro diretório no PATH do seu sistema):

`$ ln -s /caminho/para/o/arquivo/main.py /usr/local/bin/netwinf`

Agora você pode usar o comando netwinf seguido dos parâmetros desejados no terminal:

`$ netwinf`

O script main.py será executado com os privilégios necessários e exibirá as informações sobre a rede, incluindo as portas abertas e os testes Telnet. Certifique-se de que confia completamente no que o script faz antes de executá-lo com privilégios de administrador usando sudo.

## Saída Exemplo

```
Informações do PC:
Endereço IP: 192.168.1.100
MAC do PC: 11:22:33:44:55:66

Informações da Rede:
Gateway da rede: 192.168.1.1
Nome da interface: eth0
Tipo de rede conectada: Cabeada

Resultado do Nmap no gateway: 192.168.1.1
PORT STATE SERVICE
22/tcp open ssh
53/tcp open domain
80/tcp open http
113/tcp closed ident
161/tcp closed snmp
541/tcp open uucp-rlogin

Portas abertas encontradas: 22, 53, 80, 541

Testando as portas abertas usando Telnet
A porta 22/tcp open ssh responde a conexões Telnet.
A porta 53/tcp open domain responde a conexões Telnet.
A porta 80/tcp open http responde a conexões Telnet.
A porta 541/tcp open uucp-rlogin não está aberta e/ou não responde a conexões Telnet.
```

## Notas

- O script foi projetado para sistemas Linux/Unix. Pode ser necessário fazer ajustes para funcionar em outros sistemas operacionais.
- Certifique-se de que você tem permissões suficientes para executar o Nmap e o script.
- O teste de conexão Telnet pode falhar se o serviço na porta estiver inacessível ou bloqueado por um firewall.

