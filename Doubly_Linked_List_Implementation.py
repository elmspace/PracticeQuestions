"""
	In this code, we will be implementing a doubly link list.
	It will going to have a head and tail pointer.
	This problem is meant to simply play around with doubly linked-lists.
"""


class DNode:

	def __init__(self, input_Data):
		self.Data = input_Data;
		self.Next = None;
		self.Prev = None;

class DLinkedList:

	def __init__(self):
		self.Head = None;
		self.Tail = None;

	def InsertAtHead(self, input_Data):
		if(self.Head == None):
			newNode = DNode(input_Data);
			self.Head = newNode;
			self.Tail = newNode;
		else:
			newNode = DNode(input_Data);
			newNode.Next = self.Head;
			self.Head.Prev = newNode;
			self.Head = newNode;


	def InsertAtTail(self, input_Data):
		if(self.Head == None):
			newNode = DNode(input_Data);
			self.Head = newNode;
			self.Tail = newNode;
		else:
			newNode = DNode(input_Data);
			self.Tail.Next = newNode;
			newNode.Prev = self.Tail;
			self.Tail = newNode;


	def printListForward(self):
		nodeObj = self.Head;
		while(nodeObj):
			print nodeObj.Data;
			nodeObj = nodeObj.Next;

	def printListBackward(self):
		nodeObj = self.Tail;
		while(nodeObj):
			print nodeObj.Data;
			nodeObj = nodeObj.Prev;


##################################################################################
##################################################################################

DList = DLinkedList();
DList.InsertAtHead(1);
DList.InsertAtHead(4);
DList.InsertAtHead(2);
DList.InsertAtHead(7);
print "From head to tail: ";
DList.printListForward();

print "Adding from Tail: ";
DList.InsertAtTail(3);
DList.printListForward();

