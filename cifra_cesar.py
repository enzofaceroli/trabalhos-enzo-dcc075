from collections import Counter # Será utilizado para a 2a parte do exercício

def cifra_cesar(texto, chave_k):
    """
    Parâmetros da função:
        texto (str): O texto a ser encriptado.
        chave_k (int): O número de posições para deslocar (a chave).

    Retornos:
        str: O texto encriptado.
    """
    
    texto_cifrado = ""
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letra in texto:
        if letra in alfabeto_minusculo:
            # Encontra a posição da letra no alfabeto
            posicao_original = alfabeto_minusculo.find(letra)
            # Calcula a nova posição com deslocamento e faz o "wrap-around" (módulo 26)
            nova_posicao = (posicao_original + chave_k) % 26
            # Adiciona a nova letra ao resultado
            texto_cifrado += alfabeto_minusculo[nova_posicao]
        elif letra in alfabeto_maiusculo:
            # Repete o processo para letras maiúsculas
            posicao_original = alfabeto_maiusculo.find(letra)
            nova_posicao = (posicao_original + chave_k) % 26
            texto_cifrado += alfabeto_maiusculo[nova_posicao]
        else:
            # Se o caractere não for uma letra, mantém ele como está
            texto_cifrado += letra
            
    return texto_cifrado

# Demonstração: 
print("Demonstração da Cifra de César")
texto_original_simples = "Ataque ao amanhecer!"
chave_simples = 5

texto_cifrado_simples = cifra_cesar(texto_original_simples, chave_simples)

print(f"Texto Original: '{texto_original_simples}'")
print(f"Chave (k): {chave_simples}")
print(f"Texto Cifrado: '{texto_cifrado_simples}'")

# Abaixo, a continuação do código conforme solicitado no exercício 2: 

def criptoanalise_frequencia(texto_cifrado):
    """
    Tenta quebrar a Cifra de César usando análise de frequência de letras.

    Args:
        texto_cifrado (str): O texto encriptado para ser analisado.

    Returns:
        dict: Um dicionário contendo a chave provável e o texto decifrado.
    """
    # Letra mais frequente na língua portuguesa é 'A' (seguida de perto por 'E') === INFORMAÇÃO DA IA GEMINI PRO
    letra_mais_frequente_pt = 'a'
    
    # Contagem de ocorrência de letras
    letras_do_cifrado = [letra for letra in texto_cifrado.lower() if 'a' <= letra <= 'z']
    if not letras_do_cifrado:
        return {"chave_provavel": 0, "texto_decifrado": "Texto sem letras para analisar."}
        
    frequencia = Counter(letras_do_cifrado)
    
    # Encontrar a letra mais comum no texto cifrado
    letra_mais_frequente_cifrado = frequencia.most_common(1)[0][0]
    
    # Cálculo da chave provável
    deslocamento = ord(letra_mais_frequente_cifrado) - ord(letra_mais_frequente_pt)
    chave_provavel = deslocamento % 26
    
    # Decifrando o texto usando a chave encontrada (Cifra c/ chave negativa)
    texto_decifrado = cifra_cesar(texto_cifrado, -chave_provavel)
    
    return {
        "chave_provavel": chave_provavel,
        "texto_decifrado": texto_decifrado,
        "letra_cifrada_comum": letra_mais_frequente_cifrado
    }


# Demonstração da Criptoanálise 
print("\nExercício 2: Demonstração da Criptoanálise")

# P/ garantir que analise de frequência vai ser boa, o texto usado é maior (TEXTO GERADO PELA IA GEMINI PRO).
texto_longo_original = """
A criptografia ou criptologia é a prática de princípios e técnicas para comunicação 
segura na presença de terceiros, chamados adversários. Mais geralmente, a criptografia 
é sobre a construção e análise de protocolos que impedem terceiros ou o público de 
ler mensagens privadas.
"""

chave_secreta = 12

print("Encriptando um texto longo com uma chave secreta...")
print(f"Chave Secreta Real: {chave_secreta}\n")
texto_longo_cifrado = cifra_cesar(texto_longo_original, chave_secreta)

print("--- Texto Cifrado ---")
print(texto_longo_cifrado)
print("---------------------\n")

# Tentativa de quebrar a cifra sem saber a chave_secreta
print("Iniciando a criptoanálise por frequência de letras...")
resultado_analise = criptoanalise_frequencia(texto_longo_cifrado)

print(f"A letra mais comum no texto cifrado foi: '{resultado_analise['letra_cifrada_comum']}'")
print(f"Assumindo que esta letra corresponde a 'A', a chave provável é: {resultado_analise['chave_provavel']}")
print("\n--- Texto Decifrado pela Criptoanálise ---")
print(resultado_analise['texto_decifrado'])
print("------------------------------------------\n")

# Verificação final
if chave_secreta == resultado_analise['chave_provavel']:
    print("✅ SUCESSO: A chave foi descoberta corretamente!")
else:
    print("❌ FALHA: A chave não foi descoberta. Tente um texto maior ou assuma 'E' como a letra mais comum.")
