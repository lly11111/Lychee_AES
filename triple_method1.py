from bit_encryption import encrypt
from bit_decryption import decrypt


# 三重加密方式1：使用32bit的密钥Key（K1+K2）
# 拆分输入的32 bit密钥，按高位和低位拆分位key1 key2
def create_two_key(key):
    key = int(key, 2)
    if key < 0 or key > 0xFFFFFFFF:
        raise ValueError("错误，密钥输入必须为32 bit")

    key1 = (key & 0xFFFF0000) >> 16  # 密钥的高16位
    key2 = key & 0x0000FFFF  # 密钥的低16位

    return key1, key2


# 加密过程:
def triple_encrypt(plaintext, key):
    key1, key2 = create_two_key(key)
    mid_text = encrypt(plaintext, key1)  # key1加密
    mid_text = decrypt(mid_text, key2)  # key2解密
    ciphertext = encrypt(mid_text, key1)  # key1加密
    return ciphertext


# 解密过程：
def triple_decrypt(ciphertext, key):
    key1, key2 = create_two_key(key)
    mid_text = decrypt(ciphertext, key1)  # key1解密
    mid_text = encrypt(mid_text, key2)  # key2加密
    plaintext = decrypt(mid_text, key1)  # key1解密
    return plaintext
