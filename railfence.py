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