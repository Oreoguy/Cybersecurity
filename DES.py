def fillupbyte(ch, padn=8, padchar="0", mode="l"):
    n = len(ch)
    l = n
    while l % padn != 0:
        l += 1
    result = ""
    j = 0
    for i in range(l):
        if i < l - n:
            if mode == "l":
                result = padchar + result
            else:
                result = result + padchar
        else:
            if mode == "l":
                result = result + ch[j]
                j += 1
            else:
                result = ch[::-1][j] + result
                j += 1

    return result


def bytes2binary(input):
    """
    >>> bytes2binary(b'\\x01')
    '00000001'
    """
    return fillupbyte(bin(int.from_bytes(input, byteorder="big"))[2:])


def binary2bytes(input):
    """
    >>> binary2bytes('00000001')
    b'\\x01'
    """
    result = bytearray(b"")
    for item in range(0, len(input), 8):
        tmp = input[item : item + 8]
        result += int.to_bytes(int(tmp, 2), byteorder="big", length=1)
    return bytes(result)


def bin_xor(input, input2):
    """
    >>> bin_xor('1011','0000')
    '1011'
    """
    xor = ""
    if len(input) > len(input2):
        input2 = input2.rjust(len(input), "0")

    if len(input) < len(input2):
        input = input.rjust(len(input2), "0")

    for item in range(len(input)):
        if input[item] == input2[item]:
            tmp = "0"
        else:
            tmp = "1"
        xor += tmp

    if len(xor) < len(input):
        xor = xor.rjust(len(input), "0")
    return xor


left_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
PC1 = [
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    60,
    52,
    44,
    36,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    28,
    20,
    12,
    4,
]
PC2 = [14,17,11,24,1,5,
       3,28,15,6,21,10,
       23,19,12,4,26,8,
       16,7,27,20,13,
    2,
    41,
    52,
    31,
    37,
    47,
    55,
    30,
    40,
    51,
    45,
    33,
    48,
    44,
    49,
    39,
    56,
    34,
    53,
    46,
    42,
    50,
    36,
    29,
    32,
]


def create_DES_subkeys(input):
    tmp = ""
    if len(input) < len(PC1):
        input = input.zfill(len(PC1))
    for item in PC1:
        tmp += input[item - 1]

    key1 = tmp[:28]
    key2 = tmp[28:]
    result = []
    for num in range(16):
        curr1 = key1[left_shifts[num] :] + key1[: left_shifts[num]]
        curr2 = key2[left_shifts[num] :] + key2[: left_shifts[num]]
        key1 = curr1
        key2 = curr2

        c1c2 = curr1 + curr2
        tmp2 = ""
        if len(c1c2) < len(PC2):
            c1c2 = c1c2.zfill(len(PC2))
        for item in PC2:
            tmp2 += c1c2[item - 1]

        result.append(tmp2)
    return result


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())