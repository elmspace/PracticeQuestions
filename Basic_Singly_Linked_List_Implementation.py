"""
	In this code, we will implement a basic singly linked list data model.
	It will have the following properties:
	- Data and Next property.
	- Print Link List method.
	- Delete element method.
	- Insert element method.
"""


"""
	Linked-List class.
"""
class SinglyLinkedList:

	def __init__(self, input_Data):
		self.Data = input_Data;
		self.Next = None;


	"""
		This function will print the elemtns of the linked list.
	"""
	def PrintLinkedList(self):
		LLObj = self;
		# Loop through the object and print its elements
		while(LLObj):
			# Print the data for the node.
			print LLObj.Data;
			# Set the node to be equal to the next node.
			LLObj = LLObj.Next;

	"""
		This function will delete any element from the list.
		It looks to see if the element to be deleted is the head or not.
		It returns the modified list.
	"""
	def DeleteThisElementFromLL(self, input_DataToDelete):
		LLObj = self;
		# Check to see if the element to be deleted is the head
		if(LLObj.Data == input_DataToDelete):
			LLObj = LLObj.Next;
		# If it is not, start looking for it.
		else:
			while(LLObj.Next):
				# Once you find it, link the current element to the next of the
				# element which is gonna be deleted.
				if(LLObj.Next.Data == input_DataToDelete):
					LLObj.Next = LLObj.Next.Next;
					break;
				# Else if we have not found the element, keep stepping down the link.
				else:
					LLObj = LLObj.Next;
		# Return the modified object.
		return self;


	"""
		This function will insert a new node in the middle of a link list.
		It takes the valye of a new node, and the value of the node the new
		node should be added to list after.
	"""
	def InsertThisElementAfterThisNode(self, input_Insert, input_AfterThis):
		LLObj = self;
		# Loop through the list to find the element we need to add a new node after
		while(LLObj):
			# If we found the element, create a new instance of Linked List object
			# And reorganize the links.
			if(LLObj.Data == input_AfterThis):
				NewObj = SinglyLinkedList(input_Insert);
				NewObj.Next = LLObj.Next;
				LLObj.Next = NewObj;
				break;
			# If we have not found the element yet, keep looking.
			else:
				LLObj = LLObj.Next;
		# Return the modified linked list.
		return self;
###########################################################33

"""
	Test code here:
"""
Head = SinglyLinkedList(1);
Node_1 = SinglyLinkedList(2);
Node_2 = SinglyLinkedList(5);
Node_3 = SinglyLinkedList(3);
Head.Next = Node_1;
Node_1.Next = Node_2;
Node_2.Next = Node_3;

print "Original List:"
Head.PrintLinkedList();
print "---"
print "Delete node with valye 2:"
NewList = Head.DeleteThisElementFromLL(2);
NewList.PrintLinkedList();
print "---";
print "Insert a node with value 4 after the node with value 5:"
NewList = Head.InsertThisElementAfterThisNode(4,1);
NewList.PrintLinkedList();





