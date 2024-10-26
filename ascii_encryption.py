from bit_encryption import encrypt


# 扩展功能：字符串加密算法
def encrypt_string(ascii_string, key):
    # 将ASCII字符串转换为二进制数据
    binary_string = ASCII_to_Binary(ascii_string)

    # 初始化加密结果的二进制形式
    encrypted_binary = ""

    # 16位一组进行加密
    for i in range(0, len(binary_string), 16):
        plaintext = binary_string[i:i + 16]
        # 执行加密算法（假设encrypt函数能够处理16位的输入）
        ciphertext_binary = encrypt(plaintext, key)
        # 将加密后的二进制数据拼接起来
        encrypted_binary += str(ciphertext_binary)

    # 将最终的二进制结果转换为整数
    #encrypted_int = int(encrypted_binary, 2)

    return encrypted_binary


def ASCII_to_Binary(ASCII_string):
    binary = ""
    for character in ASCII_string:
        # 使用zfill填充0，确保每个字符都转换为16位二进制数
        binary += bin(ord(character))[2:].zfill(8)
    return binary