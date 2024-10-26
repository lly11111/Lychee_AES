from bit_decryption import decrypt


# 扩展功能：字符串解密算法
def decrypt_string(encrypted_string, key):
    # 初始化解密结果
    decrypted_string = ""
    # 16位一组进行解密
    for i in range(0, len(encrypted_string), 16):
        ciphertext = encrypted_string[i:i + 16]
        # 执行解密算法
        plaintext = decrypt(ciphertext, key)
        decrypted_string += str(plaintext)
    return decrypted_string


def Binary_to_ASCII(binary):
    ASCII = ""
    # 每次处理16位二进制数据
    for i in range(0, len(binary), 16):
        # 将16位二进制数转换为整数
        ASCII += chr(int(binary[i:i + 16], 2))
    return ASCII
