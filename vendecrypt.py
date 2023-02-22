import sys

plaintext_file=sys.argv[2]
ciphertext_file=sys.argv[1]
key_file=sys.argv[3]

cipher = ""
with open(ciphertext_file,'r') as file:
    for i in file:
        cipher += i

key = ""
with open(key_file,'r') as file:
    for i in file:
        key += i

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def decrypt(cipher_text, key):
    decrypted = ""

    split_message = [
        cipher_text[i : i + len(key)] for i in range(0, len(cipher_text), len(key))
    ]

    for element in split_message:
        i = 0
        for letter in element:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

output = decrypt(cipher_text, key)

with open(plaintext_file, "w") as file:
    file.write(output)
