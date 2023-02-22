from math import log
from english_words import english_words_set
import sys

cipher_text = sys.argv[1]
crib = sys.argv[2]

alphabet = "abcdefghijklmnopqrstuvwxyz "

cipher = ""
with open(cipher_text,"r") as file:
    for i in file:
        cipher += i

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

for i in range(len(cipher)-len(crib)):
    part = cipher[i:i+len(crib)]
    decryptedpart = decrypt(part,crib)
    if decryptedpart in english_words_set:
        print(decryptedpart)
