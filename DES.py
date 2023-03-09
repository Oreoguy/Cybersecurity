def des(inputText, key, decrypt=False):
	plain = toStr([binary(ord(letter)) for letter in list(inputText)])
	output = ""
	while len(plain)>64:
		tmp = plain[:64]
		plain = plain[64:]
		output = output + binToText(toStr(desBlock(tmp, key, decrypt)))
	if len(plain)==0: return output
	while len(plain)!=64:
		plain = plain + "00000000"
	return output + binToText(desBlock(plain, key, decrypt))

def desBlock(block, key, decrypt=False):
	'''
		receives a 64-bit block and applies the DES algorithm to encrypt (or decrypt) it with the given key
	'''
	assert len(block)==64
	assert len(key)==64
	keys = genSubKeys(key)
	if decrypt: keys.reverse()
	inp = initialPerm(block)
	# Fiestel cipher:
	for subKey in keys:
		L, R = split(inp)
		Ln = xor(L, f(R, subKey))
		inp = toStr(R)+Ln
	output = finalPerm(Ln, R)
	return toStr(output)

def f(half, subKey):
	'''
		specific F function used in each round of the Fiestel stucture, for DES
	'''
	assert len(half)==32
	assert len(subKey)==48
	left = expansion(half)
	keyMix = xor(left, subKey)
	tmp = substit(keyMix)
	return permut(tmp)
    
##### SECONDARY FUNCTIONS #####

def initialPerm(block):
	return [block[initialPermData[i]-1] for i in range(1,len(initialPermData))]
	
def finalPerm(Ln, R):
	block = Ln+R
	return [block[finalPermData[i]-1] for i in range(1,len(finalPermData))]
	
def expansion(a):
	a = toStr(a)
	tmp=[]
	for i in range(8):
		inter=""
		if i==0:
			inter = a[-1] + a[:5]
		elif i==7:
			inter = a[-5:] + a[0]
		else:
			inter = a[i*6-(2*i+1): (i+1)*6-(2*i+2)+1]
		tmp.append(inter)
	output=""
	for j in tmp:
		output = output+j
	return output
	
def substit(inp):
	assert len(inp)==48
	pieces = []
	for i in range(8):
		pieces.append(inp[:6])
		inp = inp[6:]
	output = ""
	for i, piece in enumerate(pieces):
		output = output + binary(S[i][int(piece[1:-1], 2)][int(piece[0]+piece[-1], 2)])
	return output
	
def permut(inp):
	return [inp[permutation[i]-1] for i in range(1,len(permutation))]

def genSubKeys(key):
	key = pc1(key) # now of length 56
	keys = [] # subkeys of length 48
	L, R = split(key)
	for i in range(1, 17):
		L = rot(L, i)
		R = rot(R, i)
		keys.append(pc2(L, R))
	return keys

def pc1(key):
	left=""; right=""
	for i in range(1, len(pc1Left)):
		left=left+key[pc1Left[i]-1]
		right=right+key[pc1Right[i]-1]
	return left+right
	
def pc2(L, R):
	inp = L+R
	tmp = [inp[pc2Data[i]-1] for i in range(1, len(pc2Data))]
	output=""
	for elem in tmp:
		output = output + elem
	return output


def keyGen(length, nbrKeys):
    output=[]
    for i in range(nbrKeys):
        k=""
        for i in range(length):
            k = k + str(rd.randint(0, 1))
        output.append(k)
    return output

def binToHex(binar):
	res="0x"
	hexList = [hex(int(binar[i:i+8], 2))[2:] for i in range(0, len(binar),8)]
	for hexa in hexList:
		if len(hexa)==1: hexa ="0"+hexa
		res = res + hexa
	return res
    
def toStr(charList):
	'''
	charList should be a list of characters
	concatenates all the characters from the list and returns the final string
	'''
	res = ""
	for letter in charList:
		res = res+letter
	return res
   
def binToText(inp):
	# inp is a string of binary digits corresponding to several bytes. e.g. '1001010011101011'
	assert len(inp)%8==0
	output = ""
	while len(inp)!=0:
		output = output + chr(int(inp[:8], 2))
		inp = inp[8:]
	return output

def binary(a):
	'''
	a should be a positive integer smaller than 256
	returns the 8-bit binary writing of a
	'''
	assert a<256
	res = bin(a)[2:]
	while len(res)!=8:
		res = "0"+res
	return res


def xor(a,b):
	ans =""
