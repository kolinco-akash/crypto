import base64
hexst = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
a = bytearray.fromhex(hexst)
b=base64.b64encode(a)
print(b)
