# SMEHKING - Social Media Hacking

## Objetivo:
O SMEHKING (Social Media Hacking) tem como objetivo buscar e identificar informações relacionadas a redes sociais, registros e traços online de indivíduos, visando auxiliar na localização de pessoas desaparecidas ou no mapeamento de suspeitos criminais (golpe, fraude, etc.).

## Instalação:
1. Instalar o Firefox:
```
# Linux
sudo apt update
sudo apt install firefox

# CentOS/Fedora
sudo dnf install firefox
 
# Arch Linux
sudo pacman -S firefox
```
2. Instalar o ```requirements.txt```:
```
cd ~
git clone https://github.com/vieira-brz/hacking-tools.git
cd hacking-tools/
sudo mv smehking /opt/smehking
cd .. && sudo rm -fr hacking-tools/ && cd ~ && cd /opt/smehking
pip install -r requirements.txt
```

## Como usar:
1. Execute ```proxychains python3 smehking.py``` para manter-se anônimo ou somente ```python3 smehking.py```.
2. Insira: 

   ```Name: John Doe```

   ```Username: john.doe```
3. Ao teclar *Enter* o programa abrirá várias abas no *Firefox* utilizando técnicas de *Google Hacking* para encontrar dados sobre a pessoa referenciada.  

