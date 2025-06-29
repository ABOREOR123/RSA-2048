from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generar clave AES (128 bits = 16 bytes)
clave_aes = get_random_bytes(16)

# Datos a cifrar (deben ser múltiplo de 16 bytes)
mensaje = b"Este es un mensaje secreto para AES-128!"

# Cifrado
cipher = AES.new(clave_aes, AES.MODE_CBC)  # Modo CBC (requiere IV)
iv = cipher.iv  # Vector de inicialización
mensaje_cifrado = cipher.encrypt(pad(mensaje, AES.block_size))

# Descifrado
decipher = AES.new(clave_aes, AES.MODE_CBC, iv)
mensaje_descifrado = unpad(decipher.decrypt(mensaje_cifrado), AES.block_size)

print(f"Mensaje original: {mensaje.decode()}")
print(f"Mensaje descifrado: {mensaje_descifrado.decode()}")
