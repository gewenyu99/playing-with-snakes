# The number of 2s that appear between [0, n]
# 1,*2,3,4,5,6,7,8,9,10,11,*12

def bruteForce(n):
    twoCount = 0
    for i in range(0, n + 1):
        numStr = str(i)
        for char in numStr:
            if char == '2':
                twoCount += 1

    return twoCount


# Base number is (num 0's) * 10^(num 0's)-1
# Base number * base digit +    if(base digit > 2) -> 1*10^(num 0's)    <- two's tax
#                               elif(base digit == 2) -> + 1
#                               else + 0
# We can do the above recursively on each digit of the number


# Linear time on number of digits
def linearTime(n):
    digits = getDigits(n)
    twosCount = 0
    for i in range(0, len(digits)):
        digitsPlace = len(digits) - i - 1;
        if digitsPlace - 1 >= 0:
            twosCount += (digitsPlace * (10 ** (digitsPlace - 1)))*digits[i]

        if (digits[i]) > 2:
            twosCount += 10 ** (digitsPlace)
        elif (digits[i] == 2):
            twosCount += digitsToNum(digits[i + 1:]) + 1

    return twosCount


def getDigits(n):
    numStr = str(n)
    digits = []
    for digit in numStr:
        digits.append(int(digit))
    return digits


def digitsToNum(n):
    num = 0
    for i in range(0, len(n)):
        num += (n[i]) * 10 ** (len(n) - i - 1)
    return num

print(bruteForce(50046))

print(linearTime(50046))
