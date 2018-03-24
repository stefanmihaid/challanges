class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head is None:
			self.head = newNode
		else:
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode

	def printList(self):
		currentNode = self.head
		while True:
			if currentNode is None:
				print ("List is empty")
			print(currentNode.data)
			currentNode = currentNode.next
			

firstNode=Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode= Node("Ben")
linkedList.insert(secondNode)
thirdnode = Node("Mathew")
linkedList.insert(thirdnode)
linkedList.printList()