# def is_binary_data(byte_data):
#     binary_count = 0
#     total_count = len(byte_data)
#
#     for byte in byte_data:
#         # 检查是否为控制字符或者空字节
#         if byte == 0x00 or (0x00 < byte < 0x20) or (byte == 0x7F):
#             binary_count += 1
#
#     # 根据控制字符的比例判断是否为二进制数据
#     if total_count > 0 and (binary_count / total_count) > 0.1:
#         return True
#     return False

def is_binary_data(byte_data):
    # 检查是否包含非ASCII可打印字符（常见文本编码中不太可能出现的字符）
    # 通常，二进制数据包含较多的空字节、控制字符或超出正常文本范围的字符
    binary_count = 0
    total_count = 0

    for byte in byte_data:
        total_count += 1
        if byte == 0x00:  # 空字节通常是二进制数据的标志
            binary_count += 1
        elif 0x00 < byte < 0x08:  # 控制字符
            binary_count += 1
        elif byte == 0x0B:  # 控制字符
            binary_count += 1
        elif 0x0E < byte < 0x1F:  # 控制字符
            binary_count += 1
        elif byte == 0x7F:  # 删除控制字符
            binary_count += 1

    # 简单地设定一个阈值，如果一定比例的字节是二进制字符，就认为是二进制数据
    if total_count > 0 and (binary_count / total_count) > 0.1:
        return True
    return False

# 测试文本数据
text_data = b"Hello, this is a test string!"
print(is_binary_data(text_data))  # 输出: False

# 测试二进制数据
binary_data = b"\x00"
print(is_binary_data(binary_data))  # 输出: True

def binary_string_to_bytes(binary_string):
    """将二进制字符串（如 '11001100'）转换为实际的字节数据（如 b'\xcc'）"""
    # 确保输入是 8 的倍数
    if len(binary_string) % 8 != 0:
        raise ValueError("二进制字符串的长度必须是8的倍数")

    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        # 每8位转换为一个字节
        byte_value = int(binary_string[i:i+8], 2)
        byte_array.append(byte_value)
    return bytes(byte_array)


# 示例：使用 ASCII 解释的真实二进制值
binary_data_string = "11001100"  # 应该被视为二进制字符串

# 预处理步骤：如果输入是二进制字符串（仅包含 '0' 和 '1'），则进行转换
if all(char in '01' for char in binary_data_string):
    # 转换二进制字符串为实际的字节数据
    binary_data = binary_string_to_bytes(binary_data_string)
    print(f"转换后的二进制数据: {binary_data}")  # 调试输出转换结果
else:
    binary_data = binary_data_string.encode()

# 测试
print(is_binary_data(binary_data))  # 预期输出: True

# 测试文本数据
text_data = b"Hello, this is a test string!"
print(is_binary_data(text_data))  # 预期输出: False