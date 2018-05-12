"""
	This is a generic implementation of binary tree.
	There are two classes:
	1) Node class -> which will be used to build individual nodes of a tree
	2) BinaryTree class -> which is used to represent a tree object.
"""

# Here we import external modules to make things a little easier.
# We use it in some of the tree algorithm, where we would need to use queues.
from collections import deque;


"""
	This is the basic node class, which represents every node in the tree.
"""
class Node:
	def __init__(self, input_Data):
		# This contains the data object at each node
		self.Data = input_Data;
		# This is the reference to the left child (node)
		self.Left = None;
		# This is the reference to the right child (node)
		self.Right = None;


"""
	This is the binary tree representation.
	It has a method which will self-generate either a normal binary tree or a binary
	search tree. See each method for more detail.
"""
class BinaryTree:

	# Initialize the class with a root object set to None.
	# The root is how we represent a tree.
	def __init__(self): 
		self.Root = None;


	"""
		This method is going to setup a basic binary tree.
		As input it will take directions on what kind of tree you want.
		default = normal Binary Tree
		BST = Binary Search Tree
		This method is used for testing, so for specific use, you can write
		your own.
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
		This function will print the nodes of the tree in a Breath or Level-Order way.
		It uses a Queue to keep track of the nodes on the tree.
		To see how this algorithm works, draw a tree on a paper and follow this algorithm.
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
		This method will print the nodes of the tree in the X_Order format.
		Here X  can be pre, post or in.
		As default, the node we start at is the root node.
		This function uses recursion.
		Pre-order -> Root,Left,Right
		In-order -> Left, Root, Right.
		Post-order -> Left, Right, Root.
		Pay attention to where the print statement is with respect to the
		recursion calls.
	"""
	def print_X_Order(self, input_Format, input_Node="Root"):
		# If no input is given, take root to be the default
		if(input_Node=="Root"):
			input_Node = self.Root;
		# If we are at the leaf, return and go back.
		if(input_Node == None):
			return;
		# check the order and set format.
		if(input_Format == "pre"):
			# Print the node data.
			print input_Node.Data;
			# Pass in the left node, then the right node.
			self.print_X_Order(input_Format,input_Node.Left);
			self.print_X_Order(input_Format,input_Node.Right);
		elif(input_Format == "in"):
			# Pass in the left node, then print the root, then pass the right node.
			self.print_X_Order(input_Format,input_Node.Left);
			# Print the node data.
			print input_Node.Data;
			self.print_X_Order(input_Format,input_Node.Right);
		else:
			# Pass in the left node, then the right node.
			self.print_X_Order(input_Format,input_Node.Left);
			self.print_X_Order(input_Format,input_Node.Right);
			# then print the node data.
			print input_Node.Data;


	"""
		This function will do a Depth First search. The format it is using is a pre-order traversal.
		By default, the node is set to root.
	"""
	def depthFirstSearch(self, input_Data, input_Node="Root"):
		# If node is not given, set it to root.
		if(input_Node == "Root"):
			input_Node = self.Root;
		# If we are at the leaf, return Not found. This will keep the algorithm searching.
		if(input_Node == None):
			return "Not found.";
		# If we have found the data at current node, return we found it, to stop searching.
		if(input_Node.Data == input_Data):
			return "Found it.";
		# The status here holds the status of the search.
		status = self.depthFirstSearch(input_Data, input_Node.Left);
		# If the status is found, just return, else keep looking in the right branch.
		if(status == "Found it."):
			return status;
		else:
			status = self.depthFirstSearch(input_Data, input_Node.Right);
		return status;


	"""
		The Breath First search is very similar to the level-order print.
		well, it is basically the exact same, but the goal is not printing
		it is searching.
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
			if(node.Data == input_Data):
				# If the value is found, return. Remember this is not a recursion
				# return jumps out of the function.
				return "Found it."
			# If the node has a left/right element, add them to the queue.
			if(node.Left):
				q.append(node.Left);
			if(node.Right):
				q.append(node.Right);
		# If we are here, it means we could not find the element in the tree.
		return "Did not find it."


	"""
		In this function, we will calculate the height of the tree.
		We do this by using the fact that the height of a tree is:
		Max(height of left sub-tree, height of right sub-tree) + 1;
		This can be found recursively.
	"""
	def findHeightOfTree(self, input_Node = "Root"):
		# If the input is default, set it to root.
		if(input_Node == "Root"):
			input_Node = self.Root;
		# If we are at the leaf node, return -1, since the height at leaf is 0.
		# The -1 is the height of leaf's child, which is None object.
		if(input_Node == None):
			return -1;
		# Calculate the height of left and right sub-tree.
		leftHeight = self.findHeightOfTree(input_Node.Left);
		rightHeight = self.findHeightOfTree(input_Node.Right);
		# The height of the node, is the max of the left vs right, plus 1.
		return max([leftHeight,rightHeight]) + 1;







"""
	Try the above functions here:
"""
if __name__ == "__main__":
	# Create a tree object
	BT = BinaryTree();
	# Set up a random normal binary tree
	BT.testSetup();

	print BT.findHeightOfTree();

	####################################################################################
	# Print the elements in a level-order, pre, in and post order method
	# print "Print Level-Order:";
	# BT.printLevelOrder();
	# print "Print preOrder:";
	# BT.print_X_Order("pre");
	# print "Print inOrder:";
	# BT.print_X_Order("in");
	# print "Print postOrder:";
	# BT.print_X_Order("post");
	####################################################################################

	####################################################################################
	# Do a Breath First search
	#print BT.breathFirstSearch(50);
	# Do a Depth First search.
	#print BT.depthFirstSearch(-8);
	####################################################################################