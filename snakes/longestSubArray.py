## The problem calls to find the largest sub array of equal number of letters and numbers

#Bruteforce

def bruteforce(s):
    largestSubarray = 0
    for i in range(1, len(s) + 1): # i is the size of subarray
        for j in range(0, len(s) + 1 - i): # j is the position of the left bound of sub array
            if isValidSubarray(s[j:j+i]) and i > largestSubarray:
                largestSubarray = i

    return largestSubarray


def isValidSubarray(subarray):
    letters = 0
    numbers = 0
    for char in subarray:
        if ord('0') <= ord(char) <= ord('9'):
            numbers += 1
        elif ord('a') <= ord(char) <= ord('z'):
            letters += 1
        else: return False
    if letters == numbers:
        return True
    return False

print(bruteforce('12a3333bbb12f24f'))

# Notice that we're checking for the same substrings of substrings again and again
# We really just want to know how we can get letterCount - numCount == 0
# We know that we can only have strings of even composition(so 0, 2, 4, 6)
# We can find serial sums, and then find partial sums differences
def linear(s):
    numbers = 0
    letters = 0
    test = []
    for char in s:
        if ord('0') <= ord(char) <= ord('9'):
            numbers += 1
        elif ord('a') <= ord(char) <= ord('z'):
            letters += 1
        test.append(letters - numbers)

    distHash = {}
    for i in range(0, len(test)):
        if test[i] in distHash:
            distHash[test[i]]['dist'] = i - distHash[test[i]]['beginPos']
        else:
            distHash[test[i]] = {}
            distHash[test[i]]['beginPos'] = i
    longest = -10000
    for _, dist in distHash.items():
        if dist['dist'] > longest:
            longest = dist['dist']
    return longest

print(linear('12a3333bbb12f24f'))


