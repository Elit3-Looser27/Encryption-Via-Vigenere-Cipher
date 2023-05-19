# Vigenere Cipher

import encrypt
import decrypt
from asyncore import write
import string
import random

# The function makes it that the key has the same length as the text
def generateKey(text, key):
    if len(text) <= len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]
    return key      


def main():
     

        while True:
            enc_or_dec = input("Do you want to encrypt or decrypt or exit? \n").lower().strip()
            if enc_or_dec == "encrypt":
                
                while True:
                
                    user_choice = input(
                        "Do you want to encrypt your own text type 'text' or encrypt from existing file type 'file' ? \n"
                    ).lower().strip()
                
                    if user_choice == "text":
                            text = input("Enter your text: \n")
                            text_file = input("Enter the name for the text file: \n").lower().strip()
                            file1 = open(text_file, "w")
                            file1.write(text)
                            file1.close()
                            break
                    elif user_choice == "file":
                            filename = input(
                                "Choose the name of the text file from the below : \n phrase1.txt\n phrase2.txt\n phrase3.txt\n or any other file that you created\n please make sure that you type it with respect of spelling and file type\n"
                            ).lower().strip()
                            file2 = open(filename, "r")
                            text = file2.read()
                            file2.close()
                            break
                    else:
                            print(
                                "False input please enter either choices 'text' ~ for inputting text yourself or \n 'file' ~ for encrypting text from existing file \n"
                            )
                    
                while True:
                    
                        mode = input(
                            "Choose from the following: ~ \n type (1) ~ To Generate a random key\n type (2) ~ To Type the key\n type (3) ~ To Import an existing key from given files \n if you choose  (3) please make sure that you type the name of teh file with respect of spelling and file type\n"
                        ).lower().strip()
                        if mode == "1":
                            key = "".join(
                                random.choice(string.printable) for i in range(random.randint(3, 9))
                            )
                            filename1 = input("Enter the name of the new key file:\n").lower()
                            file3 = open(filename1, "w")
                            file3.write(key)
                            file3.close()
                            new_key = generateKey(text, key)
                            ciphered = encrypt.encrypt(text, new_key)
                            enc_filename1 = input("Enter the name of the new encrypted file:\n").lower().strip()
                            file4 = open(enc_filename1, "w")
                            file4.write(ciphered)
                            file4.close()
                            break
                        elif mode == "2":
                            key = input("Enter your key: ")
                            filename2 = input("Enter the name of your key file: \n").lower()
                            file5 = open(filename2, "w")
                            file5.write(key)
                            file5.close()
                            new_key = generateKey(text, key)
                            ciphered = encrypt.encrypt(text, new_key)
                            enc_filename2 = input("Enter the name of the new encrypted file:\n").lower().strip()
                            file6 = open(enc_filename2, "w")
                            file6.write(ciphered)
                            file6.close()
                            break
                        elif mode == "3":
                            filename3 = input(
                                "Choose a key file name from the following :\n key1.txt\n key2.txt\n key3.txt\nor any other file that you created\n"
                            ).lower().strip()
                            file7 = open(filename3, "r")
                            key = file7.read()
                            file7.close()
                            new_key = generateKey(text, key)
                            ciphered = encrypt.encrypt(text, new_key)
                            enc_filename3 = input("Enter the name of the new encrypted file:\n").lower().strip()
                            file8 = open(enc_filename3, "w")
                            file8.write(ciphered)
                            file8.close()
                            break
                        
                        else:
                            print(
                                "false input please enter either choice '1'To Generate a random key\n or '2' To Type the key\n '3' To Import key from given files \n "
                            )
                new_key = generateKey(text, key)
                ciphered = encrypt.encrypt(text, new_key)
                og = decrypt.decrypt(ciphered, new_key)
                print("Your key is:\n", key)
                print("Your ciphered text is:\n", ciphered)
                print("Your deciphered tex is:\n", og)
            
            elif enc_or_dec == "decrypt":
                while True:
                    while True:
                        try:
                            c_dec_filename = input("Enter the name of the file you want to decrypt:\nplease make sure that you type it with respect of spelling and file type\n").lower().strip()
                            ciphered1 = open(c_dec_filename, "r")
                            break
                        except FileNotFoundError:
                            print("File does not exist please check for spelling mistakes and if you have written the file type\n ")
                    r_ciphered = ciphered1.read()
                    ciphered1.close()
                    while True:    
                        try:
                            inp_filename = input("input the file name of the key used to encrypt:\nplease make sure that you type it with respect of spelling and file type\n").lower().strip()
                            keyfile = open(inp_filename, "r")
                            break
                        except FileNotFoundError:
                            print("File does not exist please check for spelling mistakes and if you have written the file type\n ")

                    r_new_key = keyfile.read()
                    keyfile.close()
                    last_new_key = generateKey(r_ciphered, r_new_key)
                    all_decrypted = decrypt.decrypt(r_ciphered, last_new_key)
                    file9 = open("all_decrypted.txt", "w")
                    file9.write(all_decrypted)  
                    file9.close()
                    break

            elif enc_or_dec == "exit":
                break
            else:
                print("False input please enter your choice of either 'encrypt' to encrypt ---- 'decrypt' to decrypt ---- 'exit' to exit the program\n")

                
        
        

    
    
if __name__ == '__main__':
    main()
