import time

def cifra_de_cesar_modular(texto, desloc):
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

def cifra_de_cesar_sem_modular(texto, desloc):
    resultado = ""
    
    # Loop através de cada caractere no texto
    for char in texto:
        if char.isalpha():
            ponto_origem = ord('A') if char.isupper() else ord('a')
            novo_char = chr(ord(char) + desloc)
            # Ajusta para manter dentro do alfabeto sem usar aritmética modular
            if char.isupper() and novo_char > 'Z':
                novo_char = chr(ord(novo_char) - 26)
            elif char.islower() and novo_char > 'z':
                novo_char = chr(ord(novo_char) - 26)
            resultado += novo_char
        else:
            resultado += char

    return resultado

# Função para encriptar
def encriptar(texto, desloc):
    return cifra_de_cesar_modular(texto, desloc)

# Função para decriptar
def decriptar(texto, desloc):
    return cifra_de_cesar_modular(texto, -desloc)

# Exemplo de uso
texto_original = "helloworld"
desloc = 3

# Encripta e mede o tempo com aritmética modular
start_modular = time.time()
texto_encriptado_modular = encriptar(texto_original, desloc)
end_modular = time.time()
tempo_modular = end_modular - start_modular

print(f"Texto Encriptado (Modular): {texto_encriptado_modular}")
print(f"Tempo de Execucao (Modular): {tempo_modular:.6f} segundos")

# Decripta e mede o tempo com aritmética modular
start_modular_decrypt = time.time()
texto_decriptado_modular = decriptar(texto_encriptado_modular, desloc)
end_modular_decrypt = time.time()
tempo_modular_decrypt = end_modular_decrypt - start_modular_decrypt

print(f"Texto Decriptado (Modular): {texto_decriptado_modular}")
print(f"Tempo de Execucao (Decriptar Modular): {tempo_modular_decrypt:.6f} segundos")

# Encripta e mede o tempo sem aritmética modular
start_sem_modular = time.time()
texto_encriptado_sem_modular = cifra_de_cesar_sem_modular(texto_original, desloc)
end_sem_modular = time.time()
tempo_sem_modular = end_sem_modular - start_sem_modular

print(f"Texto Encriptado (Sem Modular): {texto_encriptado_sem_modular}")
print(f"Tempo de Execucao (Sem Modular): {tempo_sem_modular:.6f} segundos")

# Decripta e mede o tempo sem aritmética modular
start_sem_modular_decrypt = time.time()
texto_decriptado_sem_modular = cifra_de_cesar_sem_modular(texto_encriptado_sem_modular, -desloc)
end_sem_modular_decrypt = time.time()
tempo_sem_modular_decrypt = end_sem_modular_decrypt - start_sem_modular_decrypt

print(f"Texto Decriptado (Sem Modular): {texto_decriptado_sem_modular}")
print(f"Tempo de Execucao (Decriptar Sem Modular): {tempo_sem_modular_decrypt:.6f} segundos")
