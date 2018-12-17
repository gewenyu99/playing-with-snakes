# Find the majority element! More than half the items
# if none return -1

# brute force
def brute(arr):
    count = {}
    for item in arr:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    for key, talley in count.items():
        if talley > len(arr) / 2:
            return key
    return -1


print(brute([1, 2, 4, 3, 3, 3, 3, 3, 1]))


# We're guaranteed to see 2 of an element in a row if it is to hold majority, or it is the last element in the array.
# Think if these numbers sat around a round table. ^ must be true

def split(arr):
    if not arr:
        return -1
    curCandidate = arr[0]
    curCandidateCount = 1
    notCandidateCount = 0
    for num in arr[1:]:
        if num != curCandidate:
            notCandidateCount += 1
            if notCandidateCount >= curCandidateCount:
                curCandidate = num
                curCandidateCount = 1
                notCandidateCount = 0
        else:
            curCandidateCount += 1

    def check(candidate):
        count = 0
        for num in arr:
            if num == candidate:
                count += 1
        if count > len(arr)/2:
            return candidate
        return -1
    return check(curCandidate)
print(split([1]))
