from ascii_encryption import encrypt_string
import io
from bit_encryption import encrypt
from bit_decryption import decrypt
import os

def is_binary_data(byte_data):
    binary_count = 0
    total_count = len(byte_data)

    for byte in byte_data:
        # 检查是否为控制字符或者空字节
        if byte == 0x00 or (0x00 < byte < 0x20) or (byte == 0x7F):
            binary_count += 1

    # 根据控制字符的比例判断是否为二进制数据
    if total_count > 0 and (binary_count / total_count) > 0.1:
        return True
    return False

def process_file_upload(file, key, save_path):
    try:
        # 读取文件内容（以二进制模式）
        file_content = file.read()
        print(file_content)

        # 检查文件内容是否仅包含 '0' 和 '1'
        if all(char in b'01' for char in file_content):
            print("文件内容仅包含 '0' 或 '1'，执行 encrypt 函数")
            encrypted_content = encrypt(file_content, key)
        else:
            if is_binary_data(file_content):
                print("true binary")
                encrypted_content = encrypt(file_content, key)
            else:
                print("false binary")
                try:
                    # 尝试将内容解码为ASCII
                    ascii_content = file_content.decode('ascii')
                    print(ascii_content)
                    encrypted_content = encrypt_string(ascii_content, key)
                except UnicodeDecodeError:
                    print(f"可能是二进制文件，解码为ASCII失败")

        # 确保加密后的内容是字节类型，以便可以写入文件
        if isinstance(encrypted_content, str):
            encrypted_content = encrypted_content.encode('utf-8')

        # 保存加密后的文件（以二进制模式写入）
        with open(save_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_content)

        return {'status': 'success', 'message': '文件加密保存成功'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}