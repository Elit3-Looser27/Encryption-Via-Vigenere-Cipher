def encrypt(text, key):
    ciphered = ""
    for i in range (len(text)):
        ascii_no = ord(text[i])
        if 127 > ascii_no > 31:
            ascii_no = ((ascii_no + ord(key[i]) - 32 ) % 95 ) + 32
        ciphered += chr(ascii_no)
    return ciphered
    