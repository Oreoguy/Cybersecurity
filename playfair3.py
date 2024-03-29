# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:29:12 2023

@author: Vansh
"""

import string

def key_generation(key):
    main=string.ascii_lowercase.replace('j','.')
    # convert all alphabets to upper
    key=key.upper()
    
    key_matrix=['' for i in range(5)]
    # if we have spaces in key, those are ignored automatically
    i=0;j=0
    for c in key:
        if c in main:
            # putting into matrix
            key_matrix[i]+=c
            main=main.replace(c,'.')
            # counting column change
            j+=1
            # if column count exceeds 5
            if(j>4):
                # row count is increased
                i+=1
                # column count is set again to zero
                j=0

    # to place other alphabets in the key_matrix
    # the i and j values returned from the previous loop
    # are again used in this loop, continuing the values in them
    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)
    

# Now plaintext is to be converted into cipher text

def encryption(plain_text):
    # seggrigating the message into pairs
    plain_text_pairs=[]
    # replacing repeated characters in pair with other letter, x
    cipher_text_pairs=[]

    # remove spaces
    plain_text=plain_text.replace(" ","")
    # convert to lower case
    plain_text=plain_text.lower()

    # if both letters in the pair are same or one letter is left at last,
    # replace second letter with x or add x, else continue with normal pairing

    i=0
    # let plain_text be abhi
    while i<len(plain_text):
        # i=0,1,2,3
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            # if the chosen letter is last and doesnt have pair
            # then the pai will be x
            b='x'
        else:
            # else the next letter will be pair with the previous letter
            b=plain_text[i+1]

        if(a!=b):
            plain_text_pairs.append(a+b)
            # if not equal then leave the next letter,
            # as it became pair with previous alphabet
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            # else dont leave the next letter and put x
            # in place of repeated letter and continue with the next letter
            # which is repeated (according to algo)
            i+=1
            
    print("plain text pairs: ",plain_text_pairs)
    for pair in plain_text_pairs:
        flag=False
        for row in key_matrix:
            if(pair[0] in row and pair[1] in row):
                # find will return index of a letter in string
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        # RULE3: if the letters are in the same column, replace them with
        # letters to their immediate below respectively
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0] in col and pair[1] in col):
                # find will return index of a letter in string
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue
        # if letters are not on the same row or column,
        # replace with the letters on the same row respectively but
        # at the other pair of corners of rectangle,
        # which is defined by the original pair

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]
        cipher_text_pairs.append(cipher_text_pair)
        
    print("cipher text pairs: ",cipher_text_pairs)
    print('plain text: ',plain_text)
    print('cipher text: ',"".join(cipher_text_pairs))
 
key=input("Enter the key: ")
key_matrix=key_generation(key)
print("Key Matrix for encryption:")
print(key_matrix)
plain_text=input("Enter the message: ")
encryption(plain_text)
