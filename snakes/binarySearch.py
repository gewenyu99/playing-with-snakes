import math
someArbitrarySortedArray = [1,2,3,4,5,6,6,7,8,9,20,123,314,45736,12345667]
shortArray = [1,2]
def binarySearch(array, val):
	if len(array) < 2:
		if array[0] == val:
			return True
		else:
			return False
	midPoint = math.floor(len(array)/2)
	if array[midPoint] == val:
		return True
	elif array[midPoint] < val:
		return binarySearch(array[midPoint:], val)
	else :
		return binarySearch(array[:midPoint],val)

print(binarySearch(shortArray, 2))
print (binarySearch(shortArray, 1))
print(binarySearch(shortArray, -1))
print(binarySearch(someArbitrarySortedArray, 9))
