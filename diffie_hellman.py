def diffie_hellman_simulation():
    # Acordo sobre os parâmetros públicos (p e g)
    # (Foi pedido à IA Gemini PRO para gerar estes parâmetros)
    p = 3571  # Um número primo grande 
    g = 2     # Uma raiz primitiva módulo p
    
    print("--- 1. Parâmetros Públicos Acordados ---")
    print(f"Primo (p): {p}")
    print(f"Raiz Primitiva (g): {g}\n")
    
    # Geração das chaves privadas (secretas)
    # (Foi pedido à IA Gemini PRO para gerar estes parâmetros)
    a = 987   # Chave privada secreta de Alice
    b = 1234  # Chave privada secreta de Bob
    
    print("--- 2. Chaves Privadas (Secretas) ---")
    print(f"Segredo de Alice (a): {a}")
    print(f"Segredo de Bob (b): {b}\n")
    
    
    # Cálculo das chaves públicas

    A = pow(g, a, p)  # Chave pública de Alice
    B = pow(g, b, p)  # Chave pública de Bob
    
    print("--- 3. Troca de Chaves Públicas (Valores que podem ser interceptados) ---")
    print(f"Alice calcula A = g^a mod p => {g}^{a} mod {p} = {A}")
    print(f"Bob calcula B = g^b mod p   => {g}^{b} mod {p} = {B}")
    print("Alice envia 'A' para Bob. Bob envia 'B' para Alice.\n")
    
    # Cálculo do segredo compartilhado (s)
    print("--- 4. Cálculo do Segredo Compartilhado ---")
    
    # Alice calcula o segredo: s_alice = B^a mod p
    secret_alice = pow(B, a, p)
    print(f"Alice calcula: s = B^a mod p => {B}^{a} mod {p} = {secret_alice}")
    
    # Bob calcula o segredo: s_bob = A^b mod p
    secret_bob = pow(A, b, p)
    print(f"Bob calcula:   s = A^b mod p => {A}^{b} mod {p} = {secret_bob}\n")

    # Verificação (O objetivo é chegar no mesmo valor para ambos)
    print("--- 5. Verificação ---")
    if secret_alice == secret_bob:
        print(f"✅ Sucesso! O segredo compartilhado é: s = {secret_alice}")
        return {
            "p": p, "g": g, "a": a, "b": b,
            "A": A, "B": B, "s": secret_alice
        }
    else:
        print("❌ Falha! Os segredos calculados não são iguais.")
        return None

if __name__ == "__main__":
    valores = diffie_hellman_simulation()