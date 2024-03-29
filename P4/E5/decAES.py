#DECRYPTION (decAES.py)
from Crypto.Cipher import AES
# Nombre del fichero de salida
out_filename = input("Enter the output file name: ")

i = input("Enter the key: ")

key= bytes.fromhex(i)

file_in = open("encrypted.bin", "rb")

nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

# Mostramos el texto desencriptado
with open(out_filename, "wb") as out_file:
    out_file.write(data)

print(data.decode())