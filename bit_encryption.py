from data import *


# 二进制加密算法
def encrypt(plaintext, key):
    plaintext = int(plaintext, 2)
    if isinstance(key, str):
        key = int(key, 2)
    key0, key1, key2 = key_expansion(key)
    # 轮密钥加（key0）
    state = add_roundkey(int_to_state(plaintext), key0)
    # 第一轮半字节代替
    state = half_substitution(S_BOX, state)
    # 第一轮行位移
    state = line_shift(state)
    # 第一轮列混淆
    state = mix_columns(state)
    # 第一轮轮密钥加（key1）
    state = add_roundkey(state, key1)
    # 第二轮半字节代替
    state = half_substitution(S_BOX, state)
    # 第二轮行位移
    state = line_shift(state)
    # 第二轮轮密钥加（key2）
    state = add_roundkey(key2, state)
    # 将最终的state转换为十进制数
    encrypted_int = state_to_int(state)
    # 将十进制数转换为16位二进制字符串，左侧补零
    encrypted_binary = bin(encrypted_int)[2:].zfill(16)

    return encrypted_binary
