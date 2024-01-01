from Crypto.Util.number import long_to_bytes

given_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

message_bytes = long_to_bytes(given_integer)
message = message_bytes.decode('utf-8')  # Assuming it's a UTF-8 encoded string

print("Converted message:", message)
