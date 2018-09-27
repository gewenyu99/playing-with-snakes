class Node():
	def __init__(self, data, next):
		self.data = data
		self.next = next
class twoEndNode(Node):
	def __init__(self, prev, data, next):
		super().__init__(data, next)
		self.prev = prev

class singlyLinkedList():
	def __init__(self):
		self.head = none
		self.tail = none
	def append(data):
		newNode = Node(data, None)
		if self.head is not None:
			self.head = node
			self.tail = node
		else:	
			self.tail.next = node
			self.tail = node
	def remove(data):
		retNode = None
		prevNode = None
		node = self.head
		while node.next is not None:
			if node.data == data:
				retNode = node
				if prevNode != None:
					prevNode.next = node.next
				else:
					self.head = node.next
			prevNode = node
			node = node.next
					
		return retNode
		
	def insert(data, position):
		newNode = Node(data, Node)
		prevNode = None
		node = self.head
		for i in position:
			if i == position:
				prevNode.next = newNode
				newNode.next = node
				return true
			prevNode = node
			node = node.next
		return false


				
