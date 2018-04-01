"""
	This is a generic implementation of binary tree.
"""

# Here we import external modules to make things a little easier.
from collections import deque;


"""
	This is the basic node class, which represents every node in the tree.
"""
class Node:
	def __init__(self, input_Data):
		self.Data = input_Data;
		self.Left = None;
		self.Right = None;


"""
	This is out binary tree representation.
"""
class BinaryTree:

	def __init__(self): 
		self.Root = None;


	"""
		This function will print the nodes of the tree in a Breath or Level-Order way.
		It uses a Queue to keep track of the nodes on the tree.
	"""
	def printLevelOrder(self):
		# Create a Queue
		q = deque();
		# Append the root as the first element in the queue.
		q.append(self.Root);
		# Loop while there are elements in the queue.
		while(len(q)):
			# Pop in a FIFO mode
			node = q.popleft();
			# Print the data
			# If the node has a left/right element, add them to the queue.
			print node.Data;
			if(node.Left):
				q.append(node.Left);
			if(node.Right):
				q.append(node.Right);



	"""
		The Breath First search is very similary to the level-order print.
		It is basically the exact same.
	"""
	def breathFirstSearch(self, input_Data):
		# Create a Queue
		q = deque();
		# Append the root as the first element in the queue.
		q.append(self.Root);
		# Loop while there are elements in the queue.
		while(len(q)):
			# Pop in a FIFO mode
			node = q.popleft();
			# Compare the value of the current node to the input data.
			# If the node has a left/right element, add them to the queue.
			if(node.Data == input_Data):
				return "Found it."
			
			if(node.Left):
				q.append(node.Left);
			if(node.Right):
				q.append(node.Right);

		return "Did not find it."


	"""
		This method is going to setup a basic bianry tree.
		As input it will take directions on what kind of tree you want.
		default = normal Binary Tree
		BST = Binary Search Tree
	"""
	def testSetup(self, input_Type = None):
		if(input_Type == None):
			self.Root = Node(1);
			self.Root.Left = Node(2);
			self.Root.Right = Node(5);
			self.Root.Left.Left = Node(12);
			self.Root.Left.Right = Node(0);
			self.Root.Right.Left = Node(3);
			self.Root.Right.Right = Node(8);
		elif(input_Type == "BST"):
			self.Root = Node(10);
			self.Root.Left = Node(5);
			self.Root.Right = Node(15);
			self.Root.Left.Left = Node(2);
			self.Root.Left.Right = Node(7);
			self.Root.Right.Left = Node(12);
			self.Root.Right.Right = Node(17);



"""
	Test function here:
"""
# Create a tree object
BT = BinaryTree();
# Set up a random normal binary tree
BT.testSetup();

# Print the elements in a level-order method
#BT.printLevelOrder();

# Do a Breath First search
print BT.breathFirstSearch(50);