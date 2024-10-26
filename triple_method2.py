from bit_encryption import encrypt
from bit_decryption import decrypt


# 三重加密方式2：使用48bit的密钥Key（K1+K2+k3）
# 拆分输入的48 bit密钥，按高位和低位拆分位key1 key2 key3
def create_three_key(key):
    key = int(key, 2)
    # if key < 0 or key > 0xFFFFFFFFFFFF:
    #     raise ValueError("错误，密钥输入必须为48 bit")

    key1 = (key & 0xFFFF00000000) >> 32  # 密钥的高16位
    key2 = (key & 0x0000FFFF0000) >> 16  # 中间16位
    key3 = key & 0x00000000FFFF  # 密钥的低16位

    return key1, key2, key3


# 第一种加密方式
# 加密过程:key1 key2 key3均执行加密过程
def triple_encrypt1(plaintext, key):
    key1, key2, key3 = create_three_key(key)
    mid_text = encrypt(plaintext, key1)  # key1加密
    mid_text = encrypt(mid_text, key2)  # key2加密
    ciphertext = encrypt(mid_text, key3)  # key3加密
    return ciphertext


# 解密过程：key1 key2 key3均执行解密过程
def triple_decrypt1(ciphertext, key):
    key1, key2, key3 = create_three_key(key)
    mid_text = decrypt(ciphertext, key3)  # key3解密
    mid_text = decrypt(mid_text, key2)  # key2解密
    plaintext = decrypt(mid_text, key1)  # key1解密
    return plaintext


# 第二种加密方式
# 加密过程:key1 key3执行加密过程，key2执行解密过程
def triple_encrypt2(plaintext, key):
    key1, key2, key3 = create_three_key(key)
    mid_text = encrypt(plaintext, key1)  # key1加密
    mid_text = decrypt(mid_text, key2)  # key2解密
    ciphertext = encrypt(mid_text, key3)  # key3加密
    return ciphertext


# 解密过程：key1 key3执行解密过程，key2执行加密过程
def triple_decrypt2(ciphertext, key):
    key1, key2, key3 = create_three_key(key)
    mid_text = decrypt(ciphertext, key3)  # key3解密
    mid_text = encrypt(mid_text, key2)  # key2加密
    plaintext = decrypt(mid_text, key1)  # key1解密
    return plaintext
