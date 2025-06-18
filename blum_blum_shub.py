def blum_blum_shub_generator(p, q, s, num_bits):
    """
    Parâmetros da função:
        p (int): Um número primo grande congruente a 3 (mod 4).
        q (int): Outro número primo grande (diferente de p) congruente a 3 (mod 4).
        s (int): A semente, um inteiro coprimo a M.
        num_bits (int): O número de bits a serem gerados.

    Retorno:
        str: Uma string contendo a sequência de bits gerados.
    """
    # Validação das premissas para p e q
    if p % 4 != 3:
        raise ValueError("O primo p não é congruente a 3 (mod 4).")
    if q % 4 != 3:
        raise ValueError("O primo q não é congruente a 3 (mod 4).")

    # Cálculo de M
    M = p * q
    
    # Inicialização
    x = s
    bit_sequence = ""

    print(f"Iniciando a geração de {num_bits} bits...")
    print(f"p = {p}, q = {q}, s = {s}")
    print(f"M = {M}")

    for _ in range(num_bits):
        # A fórmula principal do BBS: x_i = (x_{i-1})^2 mod M
        # Usamos pow(x, 2, M) por ser mais eficiente para números grandes === SUGESTÃO DADA PELA IA GEMINI PRO
        x = pow(x, 2, M)
        
        # O bit de saída é o bit menos significativo de x (paridade)
        bit = x % 2
        
        # Adiciona o bit à sequência
        bit_sequence += str(bit)
        
    print("Geração concluída.")
    return bit_sequence

# Parâmetros Escolhidos (ESCOLHIDOS PELA IA GEMINI PRO)
p_val = 10007
q_val = 10019
s_val = 719283
bits_to_generate = 100000  


if __name__ == "__main__":
    random_bits = blum_blum_shub_generator(p_val, q_val, s_val, bits_to_generate)

    file_path = "bbs_bitstream.txt"
    with open(file_path, "w") as f:
        f.write(random_bits)
        
    print(f"\nSequência de {bits_to_generate} bits salva em '{file_path}'.")

    # Apresentou alguns erros, vamos utilizar outro s_val gerado pela mesma IA para ver se conseguimos melhorar 
    s_val = 98765
    random_bits = blum_blum_shub_generator(p_val, q_val, s_val, bits_to_generate)

    file_path = "bbs_bitstream_melhorado.txt"
    with open(file_path, "w") as f:
        f.write(random_bits)
        
    print(f"\nSequência de {bits_to_generate} bits salva em '{file_path}'.")


# Para realizar os testes, siga estes passos:

#     Execute o script Python acima. Ele criará um arquivo chamado bbs_bitstream.txt.
#     Abra o arquivo bbs_bitstream.txt e copie todo o seu conteúdo (a sequência de '0's e '1's).
#     Acesse a ferramenta de teste online: https://mzsoltmolnar.github.io/random-bitstream-tester/
#     Cole a sequência de bits na área de texto indicada na página.
#     Clique no botão "Run tests" e aguarde a conclusão da análise.
    
#     PASSO A PASSO GERADO POR IA
