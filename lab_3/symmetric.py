import os
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import TripleDES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from file import File


class Symmetric:
    @staticmethod
    def generate_symmetric_key(length: int) -> bytes:
        if length not in [64, 128, 192]:
            raise ValueError("Длина ключа должна быть 64, 128 или 192 бита:")
        key = os.urandom(length // 8)
        return key

    @staticmethod
    def encrypt_text(text_path: str, encrypted_text: str, symmetric_key_path: str):
        key = File.read_bytes(symmetric_key_path)
        text = File.read_bytes(text_path)
        iv = os.urandom(8)
        padder = padding.PKCS7(TripleDES.block_size).padder()
        padded_text = padder.update(text)+padder.finalize()
        cipher = Cipher(TripleDES(key), modes.CBC(iv),
                        backend=default_backend())
        encryptor = cipher.encryptor()
        encryptor_text = iv + \
            encryptor.update(padded_text) + encryptor.finalize()
        File.write_bytes(encrypted_text, encryptor_text)
        return encryptor_text

    @staticmethod
    def decrypt_text(encrypted_text_path: str, decrypted_text: str, symmetric_key_path: str):
        key = File.read_bytes(symmetric_key_path)
        encrypted_data = File.read_bytes(encrypted_text_path)
        iv = encrypted_data[:8]
        encrypted_text = encrypted_data[8:]
        cipher = Cipher(TripleDES(key), modes.CBC(iv),
                        backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded_text = decryptor.update(
            encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(TripleDES.block_size).unpadder()
        unpadded_text = unpadder.update(
            decrypted_padded_text) + unpadder.finalize()
        File.write_bytes(decrypted_text, unpadded_text)
        return unpadded_text
