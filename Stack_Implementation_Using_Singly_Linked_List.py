"""
	In this practice problem, we will be implementing a Stack model, using singly linked list.
	The Stack is a Firts-In-Last_Out model, so we want to write a class which will have the following properties:
	- Push method
	- Pop method
	- Create Stack method
	- Delete Stack method 
"""

class Stack:
	"""
		The init has a data and a next, as do linked lists.
	"""
	def __init__(self):
		self.Data = None;
		self.Next = None;

	"""
		The push element will add a new node at the head of the list.
		If the list is empty, it will simply set the data of the head.
		If the list if not empty, it will vreate a new node, and change the reference
		to the head node.
	"""
	def Push(self, input_data):
		if(self.Data):
			# Move the head down, and add to head.
			NewNode = Stack();
			NewNode.Data = input_data;
			NewNode.Next = self;
			self = NewNode;
		else:
			self.Data = input_data;
		# Return the modified object
		return self;


	"""
		The pop will remove the first element (head) and will return its value
		in addition to the reference to new head.
	"""
	def Pop(self):
		if(self.Next == None):
			return Stack(), self.Data;
		else:
			Data = self.Data;
			self = self.Next;
			return self, Data;	


	"""
		Print stack will simply print the value sof the stack (linked-list)
	"""
	def PrintStack(self):
		while(self):
			print self.Data;
			self = self.Next;

	"""
		This method will simply pop all the elements in a list.
	"""
	def DeleteStack(self):
		while(self.Data):
			self, Data = self.Pop();	
		return self;

"""
	Test code here:
"""
stack = Stack();
stack = stack.Push(2);
stack = stack.Push(3);
stack = stack.Push(4);
stack = stack.Push(5);
stack = stack.Push(6);
print "The stack is now:"
stack.PrintStack();

print "Lets pop the first element:"
stack, Data = stack.Pop();
print "Data:", Data;
print "Remaining stack: "
stack.PrintStack();

print "Lets delete the whole stack:";
stack = stack.DeleteStack();
stack.PrintStack();






