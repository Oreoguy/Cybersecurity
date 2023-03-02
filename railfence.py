def rail_fence_encrypt(plain_text, num_rails):
    fence = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1

    # Build the fence by iterating through the plaintext
    for char in plain_text:
        fence[rail].append(char)
        rail += direction

        # Change direction if we reach the top or bottom rail
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Flatten the fence into a single list to get the ciphertext
    cipher_text = []
    for rail in fence:
        cipher_text.extend(rail)

    return ''.join(cipher_text)


def rail_fence_decrypt(cipher_text, num_rails):
    fence = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1

    # Build the fence by iterating through the ciphertext
    for char in cipher_text:
        fence[rail].append(None)
        rail += direction

        # Change direction if we reach the top or bottom rail
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    # Fill the fence with the ciphertext characters
    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = cipher_text[index]
            index += 1

    # Read off the plaintext from the fence
    plain_text = []
    rail = 0
    direction = 1
    for _ in range(len(cipher_text)):
        plain_text.append(fence[rail][0])
        fence[rail] = fence[rail][1:]
        rail += direction

        # Change direction if we reach the top or bottom rail
        if rail == num_rails - 1 or rail == 0:
            direction = -direction

    return ''.join(plain_text)
