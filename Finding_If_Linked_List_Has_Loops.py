"""
	In this problem, we wanna write an algorithm to check if a linked list has a loop.
	We are going to implement a simple linked list, then write a function to check if it does loop back on itself.
"""

"""
	This is a basic node class, the linked list will be built from linked lists.
"""
class Node:
	def __init__(self, input_Data):
		self.Data = input_Data;
		self.Next = None;


"""
	This is a basic linked list class. It uses the above node class to build the linked list.
	It has two new functions:
	1- addLoop, which will take the last node in the list and add its Next property to point another node in the list
	2- amILoopy, which will go through the list and if the list has loop it will retun True, else it will return False.
"""
class LinkedList:
	"""
		Initialize the class.
	"""
	def __init__(self):
		self.Head = None;

	"""
		This method will take data and it will add it to the head of the list.
	"""
	def addToHead(self, input_Data):
		if(self.Head):
			newNode = Node(input_Data);
			newNode.Next = self.Head;
			self.Head = newNode;
		else:
			newNode = Node(input_Data);
			self.Head = newNode;

	"""
		This function will take the end node and will assign the next component to
		the the node with the data = input_LoopToHere.
	"""
	def addLoop(self, input_LoopToHere):
		# Firts we are going to find the node we want to loop back to.
		nodeObj = self.Head;
		loopBackToHere = None;
		while(nodeObj):
			if(nodeObj.Data == input_LoopToHere):
				loopBackToHere = nodeObj;
				break;
			else:
				nodeObj = nodeObj.Next;
		if(loopBackToHere):
			nodeObj = self.Head;
			while(nodeObj.Next):
				nodeObj = nodeObj.Next;
			nodeObj.Next = loopBackToHere;
	

	"""
		This method will use a fats and a slow moving nodes to find if the linked list has a loop.
	"""
	def amILoopy(self):
		slowNode = self.Head;
		fastNode = self.Head.Next;
		keepLooking = True;
		while(keepLooking):
			if((slowNode == fastNode) or (fastNode.Next == slowNode)):
				keepLooking = False;
				return True;
			elif(fastNode.Next == None):
				keepLooking = False;
				return False;
			else:
				fastNode = fastNode.Next.Next;
				slowNode = slowNode.Next;


	"""
		This is a utility function used to print the linked list.
	"""
	def printList(self):
		nodeObj = self.Head;
		while(nodeObj):
			print nodeObj.Data;
			nodeObj = nodeObj.Next;


"""
	Here we test our function:
"""

ll = LinkedList();
ll.addToHead(6);
ll.addToHead(5);
ll.addToHead(4);
ll.addToHead(3);
ll.addToHead(2);
ll.addToHead(1);

print "This is basic liner linked-list:";
ll.printList();

print "Do I have a loop:";
print ll.amILoopy();

print "Now we add a loop:";
print "Am I loopy?"
ll.addLoop(2);
print ll.amILoopy();



