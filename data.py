# 用于半字节替换（S_BOX和S_BOX的逆）
S_BOX = [
    0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7
]
S1_BOX = [
    0xA, 0x5, 0x9, 0xB, 0x1, 0x7, 0x8, 0xF, 0x6, 0x0, 0x2, 0x3, 0xC, 0x4, 0xD, 0xE
]

# 密钥拓展中的轮常数
RCON1 = 0x80
RCON2 = 0x30


# 密钥扩展：交换N0，N1.将一个字节的半字节进行循环移位
def circular_shift(word):
    return ((word & 0x0F) << 4) + ((word & 0xF0) >> 4)


# 密钥扩展：用S-BOX替换N0、N1。使用S盒替换一个字节的高4位和低4位
def key_substitution(word, sbox):
    return (sbox[(word >> 4)] << 4) + sbox[word & 0x0F]


# 生成状态矩阵：将一个16位整数转换为4元素的状态矩阵。
def int_to_state(n):
    return [n >> 12 & 0xF, (n >> 4) & 0xF, (n >> 8) & 0xF, n & 0xF]


# 返回二进制：将4元素的状态矩阵转换为16位整数。
def state_to_int(state):
    return (state[0] << 12) + (state[2] << 8) + (state[1] << 4) + state[3]


# 密钥加：将状态矩阵与轮密钥进行逐字节异或操作。
# 逆函数与之相同
def add_roundkey(state, round_key):
    return [i ^ j for i, j in zip(state, round_key)]


# 半字节代替：使用S盒替换状态矩阵中的每个字节
# 逆函数调用只需将S_BOX换位逆S_BOX
def half_substitution(sbox, state):
    return [sbox[nibble] for nibble in state]


# 行移位：对状态矩阵进行简单的行移位操作。
# 逆函数与之相同
def line_shift(state):
    return [state[0], state[1], state[3], state[2]]


# 列混淆：定义伽罗瓦有限域乘法
def galois_field_multiply(a, b):
    product = 0
    a = a & 0x0F
    b = b & 0x0F

    while a and b:
        if b & 1:
            product ^= a
        a = a << 1
        if a & (1 << 4):
            a ^= 0b10011
        b = b >> 1

    return product


# 列混淆
def mix_columns(state):
    return [
        state[0] ^ galois_field_multiply(4, state[2]),
        state[1] ^ galois_field_multiply(4, state[3]),
        state[2] ^ galois_field_multiply(4, state[0]),
        state[3] ^ galois_field_multiply(4, state[1]),
    ]


# 列混淆的逆运算
def inverse_mix_columns(state):
    return [
        galois_field_multiply(9, state[0]) ^ galois_field_multiply(2, state[2]),
        galois_field_multiply(9, state[1]) ^ galois_field_multiply(2, state[3]),
        galois_field_multiply(9, state[2]) ^ galois_field_multiply(2, state[0]),
        galois_field_multiply(9, state[3]) ^ galois_field_multiply(2, state[1]),
    ]


# 密钥扩展
def key_expansion(key):
    w = [None] * 6
    w[0] = (key & 0xFF00) >> 8
    w[1] = key & 0x00FF
    w[2] = w[0] ^ (key_substitution(circular_shift(w[1]), S_BOX) ^ RCON1)
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ (key_substitution(circular_shift(w[3]), S_BOX) ^ RCON2)
    w[5] = w[4] ^ w[3]

    return (
        # 第一次轮密钥
        int_to_state((w[0] << 8) + w[1]),
        # 第二次轮密钥
        int_to_state((w[2] << 8) + w[3]),
        # 第三次轮密钥
        int_to_state((w[4] << 8) + w[5])
    )


