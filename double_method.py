from bit_encryption import encrypt
from bit_decryption import decrypt


# 二重加密
# 拆分输入的32 bit密钥，按高位和低位拆分位key1 key2
def create_key(key):
    # print(key)
    key = int(key, 2)

    # if key < 0 or key > 0xFFFFFFFF:
    #     raise ValueError("错误，密钥输入必须为32 bit")

    key1 = (key & 0xFFFF0000) >> 16  # 密钥的高16位
    key2 = key & 0x0000FFFF  # 密钥的低16位

    return key1, key2


# 第一种二重加密方式
# 加密过程：key1 key2均执行加密过程
def double_encrypt(plaintext, key):
    key1, key2 = create_key(key)
    mid_text = encrypt(plaintext, key1)  # key1加密
    ciphertext = encrypt(mid_text, key2)  # key2加密
    return ciphertext


# 解密过程：key1 key2均执行解密过程
def double_decrypt(ciphertext, key):
    key1, key2 = create_key(key)
    mid_text = decrypt(ciphertext, key2)  # key2解密
    plaintext = decrypt(mid_text, key1)  # key1解密
    return plaintext


# 第二种二重加密方式
# 加密过程：key1执行加密过程，key2执行解密过程
def double_encrypt1(plaintext, key):
    key1, key2 = create_key(key)
    mid_text = encrypt(plaintext, key1)  # key1加密
    ciphertext = decrypt(mid_text, key2)  # key2解密
    return ciphertext


# 解密过程：key1执行解密过程，key2执行加密过程
def double_decrypt1(ciphertext, key):
    key1, key2 = create_key(key)
    mid_text = encrypt(ciphertext, key2)  # key2加密
    plaintext = decrypt(mid_text, key1)  # key1解密
    return plaintext
