from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import os
from werkzeug.utils import secure_filename
from ascii_encryption import encrypt_string
from ascii_decryption import decrypt_string
from double_method import *
from triple_method1 import triple_encrypt, triple_decrypt
from triple_method2 import triple_encrypt1, triple_encrypt2, triple_decrypt1, triple_decrypt2
from meetInTheMiddleAttack import meet_in_the_middle_attack
from cipherBlockChaining import cbc_encrypt,cbc_decrypt
from fileEncryption import process_file_upload

# 使用Flask框架
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 设置上传文件夹

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# flask框架中的默认初始页面（begin页）
@app.route('/')
def index():
    return render_template('begin.html')


# flask框架中的页面跳转（跳转至app页面）
@app.route('/app')
def app_page():
    return render_template('app.html')


# 通过Web API将JS文件中的请求发送到后端服务
# 16 bit加密
@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    # 验证长度
    if len(plaintext) != 16 or len(key) != 16:
        return jsonify({'error': '明文和密钥必须为16位！'}), 400

    # 假设你已经有一个处理16位数据的加密函数
    encrypted = encrypt(plaintext, key)  # 确保encrypt函数能处理16位数据

    return jsonify({'encrypted': encrypted})


# 16 bit解密
@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    # 验证长度
    if len(ciphertext) != 16 or len(key) != 16:
        return jsonify({'error': '明文和密钥必须为16位！'}), 400
    decrypted = decrypt(ciphertext, key)
    return jsonify({'decrypted': decrypted})


# ASCII加密
@app.route('/encrypt1', methods=['POST'])
def encrypt1_endpoint():
    data = request.json
    cleartext = data['cleartext']
    key = data['key']
    encrypted = encrypt_string(cleartext, key)
    return jsonify({'encrypted': encrypted})


# ASCII解密
@app.route('/decrypt1', methods=['POST'])
def decrypt1_endpoint():
    data = request.json
    encrypted_string = data['ciphertext']
    key = data['key']
    decrypted = decrypt_string(encrypted_string, key)
    return jsonify({'decrypted': decrypted})


# 二重加密1
@app.route('/double_encrypt', methods=['POST'])
def double_encrypt_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypted = double_encrypt(plaintext, key)
    return jsonify({'encrypted': encrypted})


# 二重解密1
@app.route('/double_decrypt', methods=['POST'])
def double_decrypt_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted = double_decrypt(ciphertext, key)
    return jsonify({'decrypted': decrypted})


# 二重加密2
@app.route('/double_encrypt1', methods=['POST'])
def double_encrypt1_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypted = double_encrypt1(plaintext, key)
    return jsonify({'encrypted': encrypted})


# 二重解密2
@app.route('/double_decrypt1', methods=['POST'])
def double_decrypt1_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted = double_decrypt1(ciphertext, key)
    return jsonify({'decrypted': decrypted})


# 三重加密：32 bit
@app.route('/triple_encrypt', methods=['POST'])
def triple_encrypt_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypted = triple_encrypt(plaintext, key)
    return jsonify({'encrypted': encrypted})


# 三重解密：32 bit
@app.route('/triple_decrypt', methods=['POST'])
def triple_decrypt_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted = triple_decrypt(ciphertext, key)
    return jsonify({'decrypted': decrypted})


# 三重加密：48 bit
# 方法一：
@app.route('/triple_encrypt1', methods=['POST'])
def triple_encrypt1_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypted = triple_encrypt1(plaintext, key)
    return jsonify({'encrypted': encrypted})


# 方法二：
@app.route('/triple_encrypt2', methods=['POST'])
def triple_encrypt2_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    encrypted = triple_encrypt2(plaintext, key)
    return jsonify({'encrypted': encrypted})


# 三重解密：48 bit
# 方法一：
@app.route('/triple_decrypt1', methods=['POST'])
def triple_decrypt1_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted = triple_decrypt1(ciphertext, key)
    return jsonify({'decrypted': decrypted})


# 方法二：
@app.route('/triple_decrypt2', methods=['POST'])
def triple_decrypt2_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted = triple_decrypt2(ciphertext, key)
    return jsonify({'decrypted': decrypted})

#中间相遇攻击
@app.route('/meet_in_the_middle_attack', methods=['POST'])
def meet_in_the_middle():
    data = request.json
    plaintext = data['plaintext']
    ciphertext = data['ciphertext']

    # 验证明文和密文的长度
    if len(plaintext) != 16 or len(ciphertext) != 16:
        return jsonify({'error': '明文和密文必须为16位！'}), 400

    found_key = meet_in_the_middle_attack(plaintext, ciphertext)
    if found_key:
        return jsonify({'found_key': found_key})
    else:
        return jsonify({'error': '未找到密钥组合'}), 404

# 文件加密
@app.route('/upload', methods=['POST'])
def upload_file():
    # 获取上传的文件、密钥和保存地址
    file = request.files['file']
    key = request.form['key']
    save_path = request.form['savePath']

    # 检查文件是否为空
    if file and allowed_file(file.filename):
        # 调用file_encrypt.py中的函数处理文件
        result = process_file_upload(file, key, save_path)
        return jsonify(result), 200 if result['status'] == 'success' else 400
    else:
        return jsonify({'status': 'error', 'message': '无效的文件或文件为空'}), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'txt'

@app.route('/cbc_encrypt', methods=['POST'])
def encrypt_route():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']
    iv = data['iv']
    ciphertext = cbc_encrypt(plaintext, key, iv)
    return jsonify({'ciphertext': ciphertext})

@app.route('/cbc_decrypt', methods=['POST'])
def decrypt_route():
    data = request.json
    ciphertext = data['ciphertext']
    key = data['key']
    iv = data['iv']
    plaintext = cbc_decrypt(ciphertext, key, iv)
    return jsonify({'plaintext': plaintext})

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'  # 设置上传文件夹
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(port=6606, debug=True)
