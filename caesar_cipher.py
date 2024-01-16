def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            if encrypt:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char

    return result

print("Enter choice")
print("1.Encryption")
print("2.Decryption")
c=int(input())
if c==1:
    plain_text = input("Enter the plain text: ")
    shift = int(input("Enter the shift amount: "))
    cipher_text = caesar_cipher(plain_text, shift,encrypt=True)
    print(f"Ciphertext: {cipher_text}")
elif c==2:
    chipher_text = input("Enter the chipher text: ")
    shift = int(input("Enter the shift amount: "))
    decrypted_text = caesar_cipher(chipher_text, shift, encrypt=False)
    print(f"Decrypted text: {decrypted_text}")
else:
    print("wrong input")
