# 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
import base64
print(type(bytearray.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))
message_bytes = bytearray.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
print(message_bytes)
base64_bytes = base64.b64encode(message_bytes)
print(base64_bytes)



