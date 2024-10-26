from bit_encryption import encrypt
from bit_decryption import decrypt

# 中间相遇攻击
def meet_in_the_middle_attack(plaintext, ciphertext):
    # 定义可能的密钥数量，这里我们只考虑16位密钥
    num_keys = 1 << 16

    # 创建前向表，枚举所有可能的前半部分密钥
    forward_table = {}
    for key1 in range(num_keys):
        key1_binary = format(key1, '016b')
        intermediate = encrypt(plaintext, key1_binary)
        forward_table[intermediate] = key1_binary

    # 创建后向表，枚举所有可能的后半部分密钥
    backward_table = {}
    for key2 in range(num_keys):
        key2_binary = format(key2, '016b')
        intermediate = decrypt(ciphertext, key2_binary)
        backward_table[intermediate] = key2_binary

    # 查找匹配项，尝试找到正确的密钥组合
    for intermediate, key1_binary in forward_table.items():
        if intermediate in backward_table:
            key2_binary = backward_table[intermediate]
            return key1_binary + key2_binary  # 返回找到的密钥组合

    return None  # 如果没有找到正确的密钥组合，则返回None