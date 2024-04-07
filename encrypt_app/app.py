from flask import Flask, render_template, request
from encrypt_app.elgamal import generate_keys, encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    message = request.form['message']
    public_key, private_key = generate_keys()
    encrypted_message = encrypt(message, public_key)
    return render_template('result.html', encrypted_message=encrypted_message)

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    encrypted_message = request.form['encrypted_message']
    private_key = request.form['private_key']
    decrypted_message = decrypt(encrypted_message, private_key)
    return render_template('result.html', decrypted_message=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
