#1 defining a function to take the basic input for the plaintext and key
def main():
    plaintext = input("Enter your message to be encrypted :")
    key = input("Enter a key of length 8 or 64 bits : ")

    print()


    if len(key)!= 8 :
        print ("Invalid key length!!")
        return
    
    padding_req = (len(plaintext)% 8 != 0)
#2 Defining the encryption fucntion
    ciphertext = DES_encrypt(key,plaintext,padding_req)

    print("Encrypted text is :" % ciphertext)

#3 Function for initial permutation for DES 
def DES_encrypt(key,plaintext,padding_req):

#4 function for converting plaintext in a 64 bit block cipher
def bin2hex(text):
    