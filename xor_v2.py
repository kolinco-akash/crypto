encoded_data_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

encoded_data = bytes.fromhex(encoded_data_hex)

for key in range(256):
    decoded_message = bytes(c ^ key for c in encoded_data)
    if all(32 <= char <= 126 for char in decoded_message):
        print(f"Key: {key}, Decoded message: {decoded_message.decode()}")

