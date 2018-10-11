def loadWords(txtfile):
    # This line fixes a decoding error by ignoring those characters.
    # This does mean that some information was lost
    with open(txtfile, 'r', encoding='utf-8', errors='ignore') as txt:
        # Read the file as a string, converts to lowercase, and then splits it by words
        x = txt.read().lower().split()
        return x


def radix(array):
    base = 27
    maxVal = max(map(len, array))
    for x in range(maxVal - 1, -1, -1):
#        breakpoint()
        buckets = [[] for x in range(base)]
        for word in array:
            if (len(word)  < x + 1):
                index = 0
            else:
                index = ((ord(word[x]) - ord('`')) % 27)
            buckets[index].append(word)
        array = []
        for bucket in buckets:
            for word in bucket:
                array.append(word)
    return array


if __name__ == '__main__':
    words = loadWords('BookText.txt.txt')
    print(radix(words))
