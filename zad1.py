import base64

def code():
    yourtext = input("Your text: ")
    entxt = base64.b64encode(yourtext.encode()).decode()
    return entxt

result = code()
print(" Encrypted text:", result)
