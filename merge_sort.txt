import math

sortThis = [2,3,2,1,0]
print('this is supposed to merge sort this: \n')
print(sortThis)

def mergeSort(array):
	if len(array) > 1:
		if len(array) > 1:
			mid = len(array)//2
			left = array[:mid]
			right = array[mid:]

			mergeSort(left)
			mergeSort(right)

			a = 0
			b = 0
			c = 0
			lenLeft = len(left)
			lenRight = len(right)

			while a < lenLeft and b < lenRight:
				if left[a] < right[b]:
					array[c] = left[a]
					a = a + 1
				else:
					array[c]=right[b]
					b = b + 1
				c = c + 1
			while a < lenLeft :
				array[c] = left[a]
				a = a + 1
				c = c + 1
			while b < lenRight:
				array[c] = right[b]
				b = b + 1
				c = c + 1

mergeSort(sortThis)
print("I sorted this: ", sortThis) 
