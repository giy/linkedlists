#!/usr/bin/python

class Node:
    def __init__(self, data):
	self.data = data
	self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
	self.tail = None

    def addNode(self, data):
	new_node = Node(data)
	if self.head == None:
	    self.head = new_node
	
	if self.tail is not None:
	    self.tail.next = new_node
	self.tail = new_node

    def removeNode(self, pos):
	node = self.head
	prev = None
        count = 0

	while count < pos and node is not None:
	    prev = node
	    node = node.next
	    count += 1

	if prev is not None:
	    prev.next = node.next
	else:
            self.head = node.next

    def printLinkedList(self):
	node = self.head    
	while node is not None:
	    print node.data
	    node = node.next

l = LinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.addNode(5)
print "First Print"
l.printLinkedList()
l.removeNode(1)
l.addNode(6)
print "Second Print"
l.printLinkedList()
l.removeNode(0)
l.removeNode(0)
print "Third Print"
l.printLinkedList()
