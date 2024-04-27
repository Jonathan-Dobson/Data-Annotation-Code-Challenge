def decode(message_file):
    OVERWRITE_DUPLICATE = True
    sentence = {}
    steps = []

    with open(message_file, "r") as file:
        message = file.read().split("\n")

    for line in message:
        n, word = line.split(" ")
        n = int(n)

        nKey = (n * (n + 1)) // 2
        length = len(steps)
        maxKey = (length * (length + 1)) // 2

        # add more steps only when needed
        if nKey > maxKey:
            while nKey >= maxKey:
                steps.append(maxKey)
                sentence[maxKey] = None
                length += 1
                maxKey = (length * (length + 1)) // 2

        # add the word to the sentence dictionary
        if n in sentence:
            if OVERWRITE_DUPLICATE:
                sentence[n] = word
            elif sentence.get(n - 1) is None:
                sentence[n] = word

    # compile the sentence dictionary into a decoded string
    decoded_string = ""
    for val in steps:
        if sentence[val] is not None:
            decoded_string += sentence[val] + " "
    return decoded_string[:-1]


# Example usage:
decoded_message = decode("example.txt")
print(decoded_message)
