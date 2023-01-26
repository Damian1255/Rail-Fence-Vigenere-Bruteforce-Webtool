# Brute-force decryption of Rail-fence & Vigenere Product Cipher.
from pycipher import Railfence, Vigenere

glossaries = open('glossaries.txt', 'r').read().split("\n")
words = open('keywords.txt', 'r').read().split("\n")
rf_key_length = 8
results = []

print('Rail-Fence + Vigenere Cipher | Brute-Force Decryption by Damian')
ciphertext = input('Input Ciphertext: ')

for rf_key in range(2, rf_key_length + 1):
    rf_ciphertext = Railfence(rf_key).decipher(ciphertext, True)
    if "  " not in rf_ciphertext:
        for v_key in glossaries:
            v_ciphertext = Vigenere(v_key).decipher(rf_ciphertext)
            score = 0
            for word in words:
                score += v_ciphertext.count(word.upper())
            results.append([score, rf_key, v_key, v_ciphertext])

print('\n-- Top 3 Results --')
for result in sorted(results, reverse=True)[:3]:
    print(f'Score = {result[0]} | Rail-Fence Key = {result[1]} | Vigenere Key = {result[2]} | Plain Text = {result[3]}')

dummy = input("\nPress any key to exit.")
