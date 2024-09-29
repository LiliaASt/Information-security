from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from file import File


class Asymmetric:
    @staticmethod
    def generate_asymmetric_keys() -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt_symmetric_key(encrypted_path: str, symmetric_key_path: str, public_key_path: str) -> bytes:
        public_key = File.deserialize_public_keys(public_key_path)
        symmetric_key = File.read_bytes(symmetric_key_path)

        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None))
        File.write_bytes(encrypted_path, encrypted_key)
        return encrypted_key

    @staticmethod
    def decrypt_symmetric_key(decrypted_path: str, encrypted_symmetric_key_path: str, private_key_path: str) -> bytes:
        private_key = File.deserialize_private_keys(private_key_path)
        encrypted_key = File.read_bytes(encrypted_symmetric_key_path)

        decrypted_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None))
        File.write_bytes(decrypted_path, decrypted_key)
        return decrypted_key
