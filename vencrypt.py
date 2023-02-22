import sys

plaintext_file=sys.argv[1]
ciphertext_file=sys.argv[2]
key_file=sys.argv[3]

plain_text = ""
with open(plaintext_file,'r') as file:
    for i in file:
        plain_text += i

key = ""
with open(key_file,'r') as file:
    for i in file:
        key += i

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""

    split_message = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for element in split_message:
        i = 0
        for letter in element:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

output = encrypt(plain_text, key)

with open(ciphertext_file,'w') as file:
    file.write(output)