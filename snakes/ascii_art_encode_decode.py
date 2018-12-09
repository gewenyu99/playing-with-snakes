import array


def solution(art):
    # Type your solution here
    def Encode(art):
        # First we will get some meta data surrounding the image
        # The assumption is the image has constant width and finite charset
        charSet = {}
        for char in art:
            if char not in charSet:
                charSet[char] = 1
            else:
                charSet[char] += 1
        # We sort the chars found from most common to least common
        # This lets us know which character is most commonly found, so we can optimize for space
        charSet = {k: v for k, v in sorted(charSet.items(), key=lambda x: x[1], reverse=True)}
        # We now build a dictionary for the characters given based off of frequency of occurence
        hashLengthCount = 1
        hashDict = {}
        for char, occurence in charSet.items():
            # The most frequent characters will have the fewest bits to represent it
            # We store the key as an array of bits for now
            hashDict[char] = buildKey(hashLengthCount)
            hashLengthCount += 1
        # We will encode into a binary stream for optimal space efficiency
        # Each char is turned into a stream of 1's separated by 0
        hashedBinArr = array.array('B', []);
        for char in art:
            hashedBinArr.extend(hashDict[char])
            # Notice that we separate chars with a 0
            hashedBinArr.extend([0])
        # For our decoder to unpack, we need to know the bit length of 1s representing each character
        for char, key in hashDict.items():
            hashDict[char] = len(key)
        # the dict is inversed from key:val to val:key so it is able to be unpacked
        return {"dict": {v: k for k, v in hashDict.items()}, "encodedArt": hashedBinArr}

    def Decode(package):
        # We get out dict and encoded art
        dict = package['dict']
        encodedArt = package['encodedArt']
        # We declare the unencoded art
        unencodedArt = ''

        # we track the number of ones found in the stream with charKey
        charKey = 0
        for num in encodedArt:
            # wait for char termination character
            if num != 0:
                charKey += 1
            # found a character
            else:
                # Add character to unencoded art
                unencodedArt += dict[charKey]
                charKey = 0

        # Return art
        return unencodedArt

    # return for testcase sake
    return Decode(Encode(art))
    pass


# Helper to build a bit stream of n 1s
def buildKey(n):
    key = array.array('B', []);
    for i in range(0, n):
        key.append(1)
    return key