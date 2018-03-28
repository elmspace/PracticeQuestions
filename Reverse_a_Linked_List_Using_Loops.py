"""
Reverse a linked list using loops.
For example:
1 -> 2 -> 3 -> 4 -> None
4 -> 3 -> 2 -> 1 -> None
"""

"""
	We can think about a linked list as a collection of Nodes.
	This class has all we need for creating a linked list.
"""
class Node:
	"""
		The init function has a data component and a next component.
		Next will point to another Node object.
	"""
	def __init__(self,input_Data):
		self.data = input_Data;
		self.next = None;

	"""
		This a utility function to just print the link list.
		It will traverse through the elements and will print the values.
	"""
	def printLinkedList(self):
		head = self;
		while (head):
			print head.data;
			head = head.next;

	"""
		This method will do the following:
		- It reverses the links (pointers) from their original order to point backwards.
		hence reversing a link list.
		- It will return the pointer (reference) to the head of the reveresed list.
	"""
	def reverseLinkedList(self):
		reversedLinkedList = self;
		prevNode = None;
		nextNode = None;
		while(reversedLinkedList):
			nextNode = reversedLinkedList.next;
			reversedLinkedList.next = prevNode;
			prevNode = reversedLinkedList;
			reversedLinkedList = nextNode;
		return prevNode;




"""
	This is for testing:
"""
#############################################
Head = Node(1);
Head.next = Node(2);
Head.next.next = Node(3);
print "Normal list:";
Head.printLinkedList();
print "Revered list:";
RevList = Head.reverseLinkedList();
RevList.printLinkedList();




