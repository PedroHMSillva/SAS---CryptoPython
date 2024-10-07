def cifra_de_cesar(texto, desloc):
    resultado = ""

    # Loop através de cada caractere no texto
    for char in texto:
        # Verifica se o caractere é uma letra
        if char.isalpha():
            # Determina o ponto de origem Maiúscula e Minúscula (A, a)
            ponto_origem = ord('A') if char.isupper() else ord('a')
            # Aplica o deslocamento com aritmética modular
            novo_char = chr((ord(char) + desloc - ponto_origem) % 26 + ponto_origem)
            resultado += novo_char
        else:
            # Se não for letra, apenas adiciona o caractere original
            resultado += char

    return resultado

# Função para encriptar
def encriptar(texto, desloc):
    return cifra_de_cesar(texto, desloc)

# Função para decriptar
def decriptar(texto, desloc):
    return cifra_de_cesar(texto, -desloc)

# Exemplo de uso
texto_original = "helloworld"
desloc = 3

# Encripta o texto
texto_encriptado = encriptar(texto_original, desloc)
print(f"Texto Encriptado: {texto_encriptado}")

# Decripta o texto
texto_decriptado = decriptar(texto_encriptado, desloc)
print(f"Texto Decriptado: {texto_decriptado}")
