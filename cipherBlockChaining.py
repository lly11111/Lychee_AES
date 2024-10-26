from bit_encryption import encrypt
from bit_decryption import decrypt

def cbc_encrypt(plaintext, key, iv):
    binary_plaintext = ''.join([bin(ord(char)).replace("0b", "").zfill(8) for char in plaintext])
    encrypted_blocks = []
    previous_cipherblock = iv

    for i in range(0, len(binary_plaintext), 16):
        block = binary_plaintext[i:i + 16]
        xor_block = ''.join([str(int(a) ^ int(b)) for a, b in zip(block.zfill(16), previous_cipherblock.zfill(16))])
        cipherblock = encrypt(xor_block, key)
        encrypted_blocks.append(cipherblock)
        previous_cipherblock = cipherblock

    return ''.join(encrypted_blocks)

def cbc_decrypt(ciphertext, key, iv):
    decrypted_blocks = []
    previous_cipherblock = iv

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = decrypt(block, key)
        xor_block = ''.join([str(int(a) ^ int(b)) for a, b in zip(decrypted_block.zfill(16), previous_cipherblock.zfill(16))])
        decrypted_blocks.append(xor_block)
        previous_cipherblock = block

    binary_plain_text = ''.join(decrypted_blocks)
    ascii_plain_text = ''.join([chr(int(binary_plain_text[i:i + 8], 2)) for i in range(0, len(binary_plain_text), 8)])
    return ascii_plain_text