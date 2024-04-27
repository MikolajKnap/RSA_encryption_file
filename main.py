import random
import math
import sys

#Functions

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d

# Main

# Generating p, q large prime numbers
p = generate_prime(1000,5000)
q = generate_prime(1000,5000)

# In case we generate same numbers
while p == q:
    q = generate_prime(1000, 5000)

# Calculating n
n = p * q

# Calculating phi(n)
phi_n = (p-1) * (q-1)

# Calculating e
e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

# Calculating d
d = mod_inverse(e, phi_n)

# Encryption
print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)

message = "Hello"

encoded_message = [ord(ch) for ch in message] # ASCII conversion

# (m^e) mod n = c
# pow(ch, e, n) => ch^e mod n
cipher_text = [pow(ch, e, n) for ch in encoded_message]
print("Cipher: ", cipher_text)

# Decryption
decoded_message = [pow(ch, d, n) for ch in cipher_text] # ASCII conversion
message = "".join(chr(ch) for ch in decoded_message)
print("Decrypted: ", message)

## File encryption

# Read file
file_name = sys.argv[1]
with open(file_name, "rb") as file:
    content = file.read()

# Encrypt file
encoded_content = [ch for ch in content]
cipher_content = [pow(ch, e, n) for ch in encoded_content]

# Save encrypted file content
encrypted_file_name = "encrypted_file.txt"
with open(encrypted_file_name, "w") as encrypted_file:
    for item in cipher_content:
        encrypted_file.write("%s\n" % item)

print("File encrypted and saved as: ", encrypted_file_name)