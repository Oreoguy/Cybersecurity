import argparse

def railfence_encrypt(word, n):
    if n <= 1:
        return word

    ascending = False
    encrypted = n * ['']
    counter = 0

    for letter in word:
        encrypted[counter] += letter
        if ascending:
            counter -= 1
            if counter == 0:
                ascending = False
        else:
            counter += 1
            if counter == n-1:
                ascending = True
    
    return ''.join(encrypted)


def railfence_decrypt(word, n):
    length = len(word)
    counter = 0
    offset = 0
    ascending = False
    decrypted = ''
    matrix = [['']*length for i in range(n)]

    while(offset != length):
        matrix[counter][offset] = '*'
        offset += 1
        if ascending:
            counter -= 1
            if counter == 0:
                ascending = False
        else:
            counter += 1
            if counter == n-1:
                ascending = True

    offset = 0

    for i in range(n):
        for j in range(length):
            if matrix[i][j] == '*':
                matrix[i][j] = word[offset]
                offset += 1
                
    for i in range(length):
        for j in range(n):
            if matrix[j][i] != '':
                decrypted += matrix[j][i]
    
    return decrypted

parser = argparse.ArgumentParser(description='Railfence cipher program')
parser.add_argument('string', help='string to process, between \'\' for multiple words')
parser.add_argument('-d', '--decrypt', action='storetrue', help='sets decryption flag to true')
parser.add_argument('key', type=int, help='number of rails')
args = parser.parse_args()
if args.decrypt:
    print(railfence_decrypt(args.string, args.key))
else:
    print(railfence_encrypt(args.string, args.key))




######### New code for Railfence ########
# this function is to get the desired sequence
def sequence(n):
    arr=[]
    i=0
    # creating the sequence required for
    # implementing railfence cipher
    # the sequence is stored in array
    while(i<n-1):
        arr.append(i)
        i+=1
    while(i>0):
        arr.append(i)
        i-=1
    return(arr)

# this is to implement the logic
def railfence(cipher_text,n):
    # converting into lower cases
    cipher_text=cipher_text.lower()

    # If you want to remove spaces,
    # you can uncomment this
    # s=s.replace(" ","")

    # returning the sequence here
    L=sequence(n)
    print("The raw sequence of indices: ",L)

    # storing L in temp for reducing additions in further steps
    # if not stored and used as below, the while loop
    # will create L of excess length
    temp=L
    
    # adjustments
    while(len(cipher_text)>len(L)):
        L=L+temp

    # removing the extra last indices
    for i in range(len(L)-len(cipher_text)):
        L.pop()
        
    # storing L.sort() in temp1
    temp1=sorted(L)
    
    print("The row indices of the characters in the cipher string: ",L)

    print("The row indices of the characters in the plain string: ",temp1)
    
    print("Transformed message for decryption: ",cipher_text)

    # converting into plain text
    plain_text=""
    for i in L:
        # k is index of particular character in the cipher text
        # k's value changes in such a way that the order of change
        # in k's value is same as plaintext order
        k=temp1.index(i)
        temp1[k]=n
        plain_text+=cipher_text[k]
        
    print("The cipher text is: ",plain_text)


cipher_text=input("Enter the string to be decrypted: ")
n=int(input("Enter the number of rails: "))
railfence(cipher_text,n)