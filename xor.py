
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1_xor_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3_xor_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2_xor_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY1 = bytes.fromhex(KEY1_hex)
KEY2_KEY1_xor = bytes.fromhex(KEY2_KEY1_xor_hex)
KEY2_KEY3_xor = bytes.fromhex(KEY2_KEY3_xor_hex)
FLAG_KEY1_KEY3_KEY2_xor = bytes.fromhex(FLAG_KEY1_KEY3_KEY2_xor_hex)

KEY2 = bytes(a ^ b for a, b in zip(KEY2_KEY1_xor, KEY1))
KEY3 = bytes(a ^ b for a, b in zip(KEY2, KEY2_KEY3_xor))

flag = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(FLAG_KEY1_KEY3_KEY2_xor, KEY1, KEY3, KEY2))

print("The flag is:", flag.decode())
