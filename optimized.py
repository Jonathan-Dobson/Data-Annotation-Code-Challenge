def decode(message_file):
    OVERWRITE_DUPLICATE = True
    sentence = {}
    steps = []

    with open(message_file, "r") as file:
        for line in file:
            n, word = line.strip().split(" ")
            n = int(n)

            nKey = (n * (n + 1)) // 2
            maxKey = len(steps) * (len(steps) + 1) // 2

            # add more steps only when needed
            while nKey >= maxKey:
                steps.append(maxKey)
                sentence[maxKey] = None
                maxKey = len(steps) * (len(steps) + 1) // 2

            # add the word to the sentence dictionary
            if n in sentence and (OVERWRITE_DUPLICATE or sentence[n] is None):
                sentence[n] = word

    # compile the sentence dictionary into a decoded string
    decoded_string = " ".join(
        sentence[val] for val in steps if sentence[val] is not None
    )
    return decoded_string


decoded_message = decode("example.txt")
print(decoded_message)
