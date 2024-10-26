// 下拉框实现效果
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    dropdown.style.display = dropdown.style.display === 'none' || dropdown.style.display === '' ? 'block' : 'none';
}
//页面切换函数：根据传入参数选择显示特定的页面
function showContent(page) {
    var contentItems = Array.from(document.querySelectorAll('.content-item'));
    contentItems.forEach(function (item) {
        item.style.display = 'none';
    });
    document.getElementById(page).style.display = 'block';
}

//16 bit加密算法（获取明文和密钥文本框）
document.querySelector('#eightBit #encrypt').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#eightBit #cleartext').value;
    var key = document.querySelector('#eightBit #key').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#eightBit #result').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});

//16 bit解密算法（获取密文和密钥文本框）
document.querySelector('#eightBit #decrypt').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#eightBit #ciphertext').value;
    var key = document.querySelector('#eightBit #key').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#eightBit #result').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});


//ASCII码加密算法（获取明文和密钥文本框）
document.querySelector('#string #encrypt').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#string #cleartext').value;
    var key = document.querySelector('#string #key').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/encrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            cleartext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 转换二进制到ASCII
            var encryptedText =data.encrypted;
            var asciiText = binaryToASCII(data.encrypted);
            // 设置显示内容
            document.querySelector('#string #result').value =
                '二进制：' + encryptedText + '\n' +
                'ASCII码：' + asciiText;
        })
        .catch(error => console.error('Error:', error));
});

//二进制转换ASCII码函数：ASCII码加解密算法调用该函数
function binaryToASCII(binaryString) {
    let ascii = '';
    // 每8个字符作为一组
    for (let i = 0; i < binaryString.length; i += 8) {
        // 获取当前8位的二进制子串
        const byte = binaryString.substr(i, 8);
        // 将二进制转为十进制并转换为对应的ASCII字符
        ascii += String.fromCharCode(parseInt(byte, 2));
    }
    return ascii;
}

//ASCII码解密算法（获取密文和密钥文本框）
document.querySelector('#string #decrypt').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#string #ciphertext').value;
    var key = document.querySelector('#string #key').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到解密服务器
    fetch('/decrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            var decryptedText = data.decrypted;
            // 转换二进制到ASCII
            var asciiText = binaryToASCII(data.decrypted);
            // 设置显示内容
            document.querySelector('#string #result').value =
                '二进制：' + decryptedText + '\n' +
                'ASCII码：' + asciiText;
        })
        .catch(error => console.error('Error:', error));
});

//二重加密算法1（获取明文和密钥文本框）
document.querySelector('#double #encrypt1').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#double #cleartext1').value;
    var key = document.querySelector('#double #key1').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }
    // 发送POST请求到服务器
    fetch('/double_encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#double #result1').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});
//二重解密算法1（获取密文和密钥文本框）
document.querySelector('#double #decrypt1').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#double #ciphertext1').value;
    var key = document.querySelector('#double #key1').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/double_decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#double #result1').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});
//二重加密算法2（获取明文和密钥文本框）
document.querySelector('#double #encrypt2').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#double #cleartext2').value;
    var key = document.querySelector('#double #key2').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }
    // 发送POST请求到服务器
    fetch('/double_encrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#double #result2').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});

//二重解密算法2（获取密文和密钥文本框）
document.querySelector('#double #decrypt2').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#double #ciphertext2').value;
    var key = document.querySelector('#double #key2').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/double_decrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#double #result2').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});

//三重加密算法：密钥为32 bit（获取明文和密钥文本框）
document.querySelector('#triple1 #encrypt').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#triple1 #cleartext').value;
    var key = document.querySelector('#triple1 #key').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/triple_encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#triple1 #result').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});

//三重解密算法：密钥为32 bit（获取密文和密钥文本框）
document.querySelector('#triple1 #decrypt').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#triple1 #ciphertext').value;
    var key = document.querySelector('#triple1 #key').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/triple_decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#triple1 #result').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});

//三重加密算法1：密钥为48 bit（获取明文和密钥文本框）
document.querySelector('#triple2 #encrypt1').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#triple2 #cleartext1').value;
    var key = document.querySelector('#triple2 #key1').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }
    // 发送POST请求到服务器
    fetch('/triple_encrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#triple2 #result1').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});
//三重解密算法1：密钥为48 bit（获取密文和密钥文本框）
document.querySelector('#triple2 #decrypt1').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#triple2 #ciphertext1').value;
    var key = document.querySelector('#triple2 #key1').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/triple_decrypt1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#triple2 #result1').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});
//三重加密算法2：密钥为48 bit（获取明文和密钥文本框）
document.querySelector('#triple2 #encrypt2').addEventListener('click', function () {
    // 获取输入框的值
    var cleartext = document.querySelector('#triple2 #cleartext2').value;
    var key = document.querySelector('#triple2 #key2').value;

    if (cleartext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }
    // 发送POST请求到服务器
    fetch('/triple_encrypt2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: cleartext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            document.querySelector('#triple2 #result2').value = data.encrypted;
        })
        .catch(error => console.error('Error:', error));
});

//三重解密算法2：密钥为48 bit（获取密文和密钥文本框）
document.querySelector('#triple2 #decrypt2').addEventListener('click', function () {
    // 获取输入框的值
    var ciphertext = document.querySelector('#triple2 #ciphertext2').value;
    var key = document.querySelector('#triple2 #key2').value;

    if (ciphertext.trim() === '' || key.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/triple_decrypt2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ciphertext: ciphertext,
            key: key
        })
    })
        .then(response => response.json())
        .then(data => {
            // 显示16位二进制结果
            document.querySelector('#triple2 #result2').value = data.decrypted;
        })
        .catch(error => console.error('Error:', error));
});
//中间相遇攻击算法
document.querySelector('#meetInTheMiddleAttack #performMeetInTheMiddleAttack').addEventListener('click', function () {
    // 获取输入框的值
    var plaintext = document.querySelector('#meetInTheMiddleAttack #cleartext').value;
    var ciphertext = document.querySelector('#meetInTheMiddleAttack #ciphertext').value;

    if (plaintext.trim() === '' || ciphertext.trim() === '') {
        // 如果任何一个输入框为空，弹出alert并退出函数
        alert('输入框不能为空！');
        return;
    }

    // 发送POST请求到服务器
    fetch('/meet_in_the_middle_attack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            plaintext: plaintext,
            ciphertext: ciphertext
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.found_key) {
            document.querySelector('#meetInTheMiddleAttack #result').value = '找到的密钥组合为: ' + data.found_key;
        } else {
            document.querySelector('#meetInTheMiddleAttack #result').value = data.error;
        }
    })
    .catch(error => console.error('Error:', error));
});

// 文件加密
// document.getElementById('selectFolder').addEventListener('click', function() {
//     if (window.showDirectoryPicker) {
//         window.showDirectoryPicker().then(directoryHandle => {
//             document.getElementById('savePath').value = directoryHandle.name;
//         }).catch(err => {
//             console.error('Error:', err);
//         });
//     } else {
//         alert('您的浏览器不支持文件夹选择功能。');
//     }
// });
document.getElementById('fileInput').addEventListener('change', function() {
    var file = this.files[0];
    if (file) {
        var fileName = file.name;
        document.getElementById('fileName').value = fileName;
    }
});

document.getElementById('encryptFile').addEventListener('click', function() {
    var formData = new FormData();
    formData.append('file', document.getElementById('fileInput').files[0]);
    formData.append('key', document.getElementById('fileKey').value);
    formData.append('savePath', document.getElementById('savePath').value);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('FileResult').value = data.status === 'success' ? '文件加密成功已保存' : '发生错误: ' + data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('FileResult').value = '发生错误: ' + error.message;
    });
});

//CBC模式加密
document.addEventListener('DOMContentLoaded', () => {
    const encryptButton = document.getElementById('cbcEncrypt');
    const decryptButton = document.getElementById('cbcDecrypt');
    const cleartextInput = document.getElementById('cbcCleartext');
    const keyInput = document.getElementById('cbcKey');
    const ivInput = document.getElementById('iv');
    const ciphertextOutput = document.getElementById('cbcCiphertext');
    const resultOutput = document.getElementById('cbcResult');

    encryptButton.addEventListener('click', () => {
        const plaintext = cleartextInput.value;
        const key = keyInput.value;
        const iv = ivInput.value;
        fetch('/cbc_encrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ plaintext, key, iv })
        })
        .then(response => response.json())
        .then(data => {
            resultOutput.value = '加密结果：' + data.ciphertext;
        })
        .catch(error => console.error('加密错误:', error));
    });

    decryptButton.addEventListener('click', () => {
        const ciphertext = ciphertextOutput.value;
        const key = keyInput.value;
        const iv = ivInput.value;
        fetch('/cbc_decrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ciphertext, key, iv })
        })
        .then(response => response.json())
        .then(data => {
            resultOutput.value = '解密结果：' + data.plaintext;
        })
        .catch(error => console.error('解密错误:', error));
    });
});

//清屏算法
document.addEventListener('DOMContentLoaded', (event) => {
    var clears = document.getElementsByClassName("clearButton");
    Array.prototype.forEach.call(clears, function (e) {
        e.addEventListener('click', function () {
            // 获取所有input和textarea元素
            var inputs = document.querySelectorAll('input, textarea');
            // 遍历所有input和textarea元素并清除它们的内容
            inputs.forEach(function (element) {
                element.value = ''; // 将每个元素的值设置为空字符串
            });
        });
    });
});
