import argparse
import string
import itertools
import os
import shutil

def generate_sequence(include_lower, include_upper, include_numbers, include_special_chars):
    characters = ""

    if include_lower:
        characters += string.ascii_lowercase

    if include_upper:
        characters += string.ascii_uppercase

    if include_numbers:
        characters += string.digits

    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return "Você deve selecionar pelo menos uma opção para gerar a sequência."

    return characters


def generate_strings(min_length, max_length, include_lower, include_upper, include_numbers, include_special_chars, default_pattern):
    character_set = generate_sequence(include_lower, include_upper, include_numbers, include_special_chars)

    if not character_set:
        print("Erro: Nenhum conjunto de caracteres selecionado.")
        return [], 0

    strings = []
    estimated_size = 0
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(character_set, repeat=length):
            string = ''.join(combination)
            if default_pattern:
                string = default_pattern[:length]
            strings.append(string)
            estimated_size += len(string) + 1  # Add 1 for the newline character

    return strings, estimated_size


def format_size(size_in_bytes):
    # Function to format the size of the file in various units
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0


def main():
    examples = [
        "python main.py 2 -a -w sequencias.txt  # Gerar sequências de 2 caracteres com alfabeto minúsculo",
        "python main.py 3 5 -a -n -e !@# -w output.txt  # Gerar sequências de 3 a 5 caracteres com letras minúsculas, números e caracteres especiais !@#",
        "python main.py 1 3 -aA -n -ae -w resultados.txt  # Gerar sequências de 1 a 3 caracteres com letras maiúsculas, minúsculas, números e todos os caracteres especiais",
        "python main.py 6 5 -aAn -w teste.txt  # Tentativa inválida de gerar sequências de 6 a 5 caracteres com alfabeto maiúsculo, minúsculo e números",
        "python main.py 2 5 -w output.txt  # Gerar sequências de 2 a 5 caracteres com alfabeto minúsculo, sem números ou caracteres especiais",
        "python main.py 5 9 -aAn -w teste.txt --default 19_______49  # Gerar sequências iniciando com 19 e terminando com 49"
    ]

    parser = argparse.ArgumentParser(description='Gerar sequência de caracteres',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='\n'.join(examples))
    parser.add_argument('min_length', type=int, help='Tamanho mínimo da string')
    parser.add_argument('max_length', type=int, nargs='?', default=None, help='Tamanho máximo da string')
    parser.add_argument('-a', '--lowercase', action='store_true', help='Incluir alfabeto minúsculo')
    parser.add_argument('-A', '--uppercase', action='store_true', help='Incluir alfabeto maiúsculo')
    parser.add_argument('-n', '--numbers', action='store_true', help='Incluir números')
    parser.add_argument('-e', '--special_chars', nargs='?', const=True, help='Incluir caracteres especiais')
    parser.add_argument('-ae', '--all_special_chars', action='store_true',
                        help='Incluir alfabeto e todos os caracteres especiais')
    parser.add_argument('-w', '--write_file', help='Salvar os dados obtidos em um arquivo')
    parser.add_argument('--default', help='Definir um padrão para as sequências')

    args = parser.parse_args()

    if args.min_length < 1 or (args.max_length and args.max_length < 1) or (
            args.max_length and args.max_length < args.min_length):
        print("Erro: Tamanho mínimo e máximo da sequência devem ser valores inteiros positivos, com min_length <= max_length.")
        return

    if args.max_length is None:
        args.max_length = float('inf')  # Set max_length to infinity if not provided by the user

    estimated_size_warning = "\nAVISO: A geração do arquivo pode quebrar se o tamanho exceder 50% do armazenamento disponível no computador."
    print(estimated_size_warning)

    proceed = input("Deseja prosseguir com a geração das sequências? (y/n): ")
    if proceed.lower() != 'y':
        print("\nOperação cancelada.")
        return

    if args.all_special_chars:
        args.special_chars = True

    strings, estimated_size = generate_strings(args.min_length, args.max_length, args.lowercase, args.uppercase, args.numbers,
                                  args.special_chars, args.default)

    if not strings:
        return

    # Save the generated strings to a file if specified
    if args.write_file:
        with open(args.write_file, 'w') as file:
            for string in strings:
                file.write(f"{string}\n")

        # Print information about the generated file
        print("\nArquivo gerado!")
        print(f"Nome do arquivo: {os.path.abspath(args.write_file)}")
        print(f"Tamanho estimado do arquivo: {format_size(estimated_size)}")

if __name__ == '__main__':
    main()
