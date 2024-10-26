from data import *


# 二进制解密算法（由于逻辑与加密算法类似，故此处我们不再提供详细注释）
def decrypt(ciphertext, key):
    ciphertext = int(ciphertext, 2)
    if isinstance(key, str):
        key = int(key, 2)
    key0, key1, key2 = key_expansion(key)
    state = add_roundkey(key2, int_to_state(ciphertext))
    state = half_substitution(S1_BOX, line_shift(state))
    state = inverse_mix_columns(add_roundkey(key1, state))
    state = half_substitution(S1_BOX, line_shift(state))
    state = add_roundkey(key0, state)
    # 将最终的state转换为十进制数
    encrypted_int = state_to_int(state)
    # 将十进制数转换为16位二进制字符串，左侧补零
    encrypted_binary = bin(encrypted_int)[2:].zfill(16)
    return encrypted_binary
