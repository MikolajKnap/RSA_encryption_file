import math
import sys

n = int(sys.argv[1])
d = int(sys.argv[2])
cipher_text = []
file_name = sys.argv[3]
with open(file_name, "r") as file:
    for line in file:
        cipher_text.append(int(line.strip()))  # Convert every line to int


decoded_message = [pow(ch, d, n) for ch in cipher_text]  # Decryption
plain_text = "".join(chr(ch) for ch in decoded_message)  # Conversion to string

# Save file
with open("decrypted_file.txt", "w") as file:
    file.write(plain_text)