import psutil
import netifaces as ni
import subprocess
import re
import socket

def get_network_info():
    # Obter informações sobre a interface de rede padrão
    default_interface = ni.gateways()['default'][ni.AF_INET][1]

    # Obter o endereço IP do seu PC
    ip_address = ni.ifaddresses(default_interface)[ni.AF_INET][0]['addr']

    # Obter o gateway da rede
    gateway = ni.gateways()['default'][ni.AF_INET][0]

    # Obter o nome da interface de rede padrão
    interface_name = default_interface

    # Verificar se a interface tem suporte a Wi-Fi
    supports_wifi = "Access Point:" in subprocess.getoutput(["iwconfig", interface_name])

    # Obter o modo em que a interface está rodando usando iwconfig
    if supports_wifi:
        try:
            iwconfig_output = subprocess.check_output(["iwconfig", interface_name]).decode("utf-8")
        except subprocess.CalledProcessError:
            iwconfig_output = ""
    else:
        iwconfig_output = ""

    # Obter o MAC do seu PC
    mac_address = ni.ifaddresses(default_interface)[ni.AF_LINK][0]['addr']

    # Obter o BSSID da rede Wi-Fi conectada (se for uma rede Wi-Fi)
    connected_bssid = format_red("Não conectado ao Wi-Fi")
    if supports_wifi and "Access Point:" in iwconfig_output:
        connected_bssid = iwconfig_output.split("Access Point:", 1)[-1].split()[0]

    return ip_address, gateway, interface_name, mac_address, connected_bssid

def format_blue(text):
    return "\033[34m" + text + "\033[0m"

def format_yellow(text):
    return "\033[93m" + text + "\033[0m"

def format_red(text):
    return "\033[91m" + text + "\033[0m"

def format_green(text):
    return "\033[92m" + text + "\033[0m"

def parse_nmap_ports(nmap_output):
    open_ports = []
    lines = nmap_output.strip().splitlines()
    for line in lines:
        if re.match(r"\d+\/tcp\s+open\s+\S+", line):
            open_ports.append(line)
    return open_ports

def test_telnet_connection(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, int(port)))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def main():
    # Chama a função para obter as informações
    ip_address, gateway, interface_name, mac_address, connected_bssid = get_network_info()

    # Imprime as informações obtidas
    print("\n" + format_blue("Informações do PC"))
    print(format_yellow("Endereço IP:") + " " + ip_address)
    print(format_yellow("MAC do PC:") + " " + mac_address)

    print("\n" + format_blue("Informações da Rede"))
    print(format_yellow("Gateway da rede:") + " " + gateway)
    print(format_yellow("Nome da interface:") + " " + interface_name)

    # Exibe BSSID apenas se for uma rede Wi-Fi
    if "N/A" not in connected_bssid:
        print(format_yellow("BSSID da rede conectada:") + " " + connected_bssid)
    else:
        print(format_yellow("Tipo de rede conectada:") + " Cabeada")

    # Executa o nmap no gateway da rede
    try:
        nmap_output = subprocess.check_output(["nmap", gateway]).decode("utf-8")
        print("\n" + format_blue("Resultado do nmap no gateway:") + " " + gateway)

        # Extrai as portas abertas retornadas pelo nmap
        open_ports = parse_nmap_ports(nmap_output)

        # Exibe somente as linhas com informações sobre portas abertas
        for line in open_ports:
            print(line)

        # Testa as portas abertas usando Telnet
        print("\n" + format_blue("Testando as portas abertas usando Telnet"))
        for port_line in open_ports:
            parts = port_line.split()
            port = parts[0].split('/')[0]
            if test_telnet_connection(gateway, port):
                print(f"A porta {format_green(port)} responde a conexões Telnet.")
            else:
                print(f"A porta {format_red(port)} não está aberta e/ou não responde a conexões Telnet.")

    except FileNotFoundError:
        print("\n" + format_blue("O nmap não está instalado. Por favor, instale-o para executar o comando."))
    except subprocess.CalledProcessError:
        print("\n" + format_blue("Não foi possível executar o nmap no gateway da rede."))

if __name__ == "__main__":
    main()
