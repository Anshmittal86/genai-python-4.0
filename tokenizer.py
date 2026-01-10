import tiktoken

text = input("👨: ")

# Encoder
encoder = tiktoken.encoding_for_model("gpt-4o")
tokenIds = encoder.encode(text=text)

print(tokenIds)

# Decoder
text = encoder.decode(tokenIds)
print(text)