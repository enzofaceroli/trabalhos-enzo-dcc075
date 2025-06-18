# S-BOX 1 do DES (Data Encryption Standard) para introduzir não-linearidade.
# Mapeia uma entrada de 6 bits (linha + coluna) para uma saída de 4 bits.
S_BOX_1 = [
    [14,   4,  13,   1,   2,  15,  11,   8,   3,  10,   6,  12,   5,   9,   0,   7],
    [ 0,  15,   7,   4,  14,   2,  13,   1,  10,   6,  12,  11,   9,   5,   3,   8],
    [ 4,   1,  14,   8,  13,   6,   2,  11,  15,  12,   9,   7,   3,  10,   5,   0],
    [15,  12,   8,   2,   4,   9,   1,   7,   5,  11,   3,  14,  10,   0,   6,  13]
]

def generate_round_keys(main_key, num_rounds=16):
    """Gera 16 sub-chaves de 32 bits a partir de uma chave mestra de 64 bits."""
    round_keys = []
    key_mask_64 = (1 << 64) - 1
    key_mask_32 = (1 << 32) - 1

    for _ in range(num_rounds):
        # Gera uma nova chave por deslocamento circular (rotate) da chave mestra.
        main_key = ((main_key << 1) | (main_key >> 63)) & key_mask_64
        round_keys.append(main_key & key_mask_32)
        
    return round_keys

def s_box_substitution(input_32bit):
    """Aplica a substituição da S-BOX em um bloco de 32 bits."""
    output_32bit = 0
    for i in range(8):
        # Processa o input em 8 pedaços de 4 bits.
        four_bit_chunk = (input_32bit >> (i * 4)) & 0xF
        
        # Simplificação para uso da S-Box do DES: 2 bits para linha, 4 para coluna.
        row = (four_bit_chunk >> 2) & 0b01
        col = four_bit_chunk & 0b1111
        
        s_box_output = S_BOX_1[row][col]
        output_32bit |= (s_box_output << (i * 4))
        
    return output_32bit

def round_function(right_half, round_key):
    """A função 'f' da Cifra de Feistel: f(R, K) = S(R XOR K)."""
    xored = right_half ^ round_key
    substituted = s_box_substitution(xored)
    return substituted

def feistel_process(block, round_keys, is_decrypt=False):
    """Executa a rede de Feistel para encriptação ou decriptação."""
    mask_32 = (1 << 32) - 1
    left_half = block >> 32
    right_half = block & mask_32
    
    # Para decriptar, as sub-chaves são usadas na ordem inversa.
    keys_iterator = reversed(round_keys) if is_decrypt else round_keys

    # Executa as 16 rodadas da cifra.
    for round_key in keys_iterator:
        temp_left = left_half
        left_half = right_half
        # A lógica central da Cifra de Feistel.
        right_half = temp_left ^ round_function(right_half, round_key)

    # Recombina as metades com a troca final (Right | Left).
    combined_block = (right_half << 32) | left_half
    
    return combined_block

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Dados de entrada para a demonstração
    main_key = 0x133457799BBCDFF1 
    plaintext_block = 0x0123456789ABCDEF

    print("--- Cifra de Feistel com 16 Rodadas ---")
    print(f"Bloco Original..: {plaintext_block:016X}")
    print(f"Chave Mestra....: {main_key:016X}\n")

    # Geração das sub-chaves
    round_keys = generate_round_keys(main_key)

    # Processo de Encriptação
    ciphertext_block = feistel_process(plaintext_block, round_keys, is_decrypt=False)
    print(f"Bloco Cifrado...: {ciphertext_block:016X}")

    # Processo de Decriptação
    decrypted_block = feistel_process(ciphertext_block, round_keys, is_decrypt=True)
    print(f"Bloco Decifrado.: {decrypted_block:016X}\n")

    # Verificação Final
    if plaintext_block == decrypted_block:
        print("✅ SUCESSO: O bloco decifrado é idêntico ao original.")
    else:
        print("❌ FALHA: O bloco decifrado é diferente do original.")