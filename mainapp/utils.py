from cryptography.fernet import Fernet
key = 'P-MAVmXuVvv4IMLfwI-OKPIi9DOSIK3rq5Tlhw-cfWw='
def encrypt(message):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print(encrypted_message)
    return encrypted_message.decode()


def decrypt(message):
    f = Fernet(key)
    decrypted_message = f.decrypt(message.encode())
    print(decrypted_message)
    return decrypted_message.decode()