from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generar par de claves RSA (2048 bits)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Cifrar un mensaje con la clave pública
mensaje = b"Clave secreta para AES-128!"
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
mensaje_cifrado = cipher_rsa.encrypt(mensaje)

# Descifrar con la clave privada
decipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
mensaje_descifrado = decipher_rsa.decrypt(mensaje_cifrado)

print(f"Mensaje original: {mensaje.decode()}")
print(f"Mensaje descifrado: {mensaje_descifrado.decode()}")
