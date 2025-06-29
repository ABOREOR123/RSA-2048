from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# ==== Alice (envía datos seguros a Bob) ====
# 1. Generar clave AES aleatoria
clave_aes = get_random_bytes(16)

# 2. Cifrar datos con AES
datos = b"Informacion ultra secreta!"
cipher_aes = AES.new(clave_aes, AES.MODE_EAX)
nonce = cipher_aes.nonce
datos_cifrados, tag = cipher_aes.encrypt_and_digest(datos)

# 3. Cifrar la clave AES con RSA (clave pública de Bob)
clave_publica_bob = RSA.import_key(open("bob_public.pem").read())
cipher_rsa = PKCS1_OAEP.new(clave_publica_bob)
clave_aes_cifrada = cipher_rsa.encrypt(clave_aes)

# ==== Bob (descifra los datos) ====
# 1. Descifrar la clave AES con su clave privada
clave_privada_bob = RSA.import_key(open("bob_private.pem").read())
decipher_rsa = PKCS1_OAEP.new(clave_privada_bob)
clave_aes_recuperada = decipher_rsa.decrypt(clave_aes_cifrada)

# 2. Descifrar los datos con AES
cipher_aes = AES.new(clave_aes_recuperada, AES.MODE_EAX, nonce=nonce)
datos_recuperados = cipher_aes.decrypt_and_verify(datos_cifrados, tag)

print(f"Datos originales: {datos.decode()}")
print(f"Datos descifrados: {datos_recuperados.decode()}")
