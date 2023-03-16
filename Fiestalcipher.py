import logging
from copy import copy
from typing import List, Tuple

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Define byte-wise XOR function
def byte_xor(ba1: List, ba2: List) -> List:
    return [a ^ b for a, b in zip(ba1, ba2)]

# Define a function to print arrays
def pp(arr) -> str:
    if type(arr) is int:
        return str(arr)
    return ' '.join(map(str, arr))

# Define the engine class
class Engine:
    def __init__(self, s, p, keys):
        # Store substitution and permutation blocks, keys, and register length
        self._n = len(s)
        self._s = s  # Substitution block
        self._p = p  # Permutation block
        self._keys = keys
        self._iter = 0
        self._register = [0] * self._n

    # Substitution function
    def __substitute(self, val: List) -> List:
        # Convert binary list to integer
        bin = int(''.join(map(str, val)), 2)
        logger.debug('Substitution')
        # Perform substitution
        res_bin = self._s[bin]
        # Convert substitution result back to binary list
        res = list(map(int, f'{res_bin:b}'))
        # Pad with zeros to the left if necessary
        res = [0] * (len(val) - len(res)) + res
        logger.debug(f'{pp(val)} ({bin}) -> {pp(res)} ({res_bin})')
        return res

    # Permutation function
    def __permutate(self, val: List) -> List:
        logger.debug('Permutation')
        # Copy input list
        res = copy(val)
        # Permute the elements of the copy according to the permutation block
        for dest, src in enumerate(self._p):
            res[dest] = val[src]
        logger.debug(f'{pp(val)} -> {pp(res)}')
        return res

    # Run the engine on a given input
    def run(self, input):
        self._register = list(input)
        print('REG: ', pp(self._register))
        for _ in range(len(self._keys)):
            print('REG: ', pp(self._step()))
        return self._register

    # Run one step of the engine
    def _step(self):
        # Split the register into left and right halves
        half = len(self._register) // 2
        left, right = self._register[:half], self._register[half:]
        # Get the key for this iteration
        key = self._keys[self._iter]
        # Print some debugging info
        print(
            f'ITERATION {self._iter}:',
            f'{pp(left)} | {pp(right)}',
            f'ROUND KEY: {pp(key)}',
            sep='\n'
        )

        # F function
        logger.debug('XOR')
        # XOR the right half of the register with the key
        block = byte_xor(right, key)
        logger.debug(f'{pp(right)} ^ {pp(key)} -> {pp(block)}')
        # Split the XOR result into left and right halves
        half_block = len(block) // 2
        l_block, r_block = block[:half_block], block[half_block:]
        logger.debug(f'{pp(l_block)} | {pp(r_block)}')
        l_s = self.__substitute(l_block)
        r_s = self.__substitute(r_block)
        s = l_s + r_s
        p = self.__permutate(s)

        logger.debug('XOR')
        new_p = byte_xor(left, p)
        logger.debug(f'{pp(left)} ^ {pp(p)} -> {pp(new_p)}')
        self._register = right + new_p
        self._iter += 1
        return self._register


def main(s: Tuple, p: Tuple, keys: Tuple, data: Tuple):
    e = Engine(s, p, keys)
    result = e.run(data)
    print(
        f'MSG:\t{pp(data)}',
        f'RES:\t{pp(result)}',
        sep='\n'
    )


if __name__ == '__main__':
    main(  # Example:
        s=(10, 14, 3, 12, 2, 5, 11, 8, 3, 10, 7, 12, 6, 9, 0, 8),
        p=(0, 4, 1, 6, 2, 6, 3, 7),
        keys=(
            (1,) * 8,
            (1, 0, 1, 0, 1, 0, 1, 0),
            (0, 1, 0, 1, 0, 1, 0, 1),
            (1,) * 8,
        ),
        data=(0,) * 16
    )