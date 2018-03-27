"""
Convert a given Binary Tree to Doubly Linked List | Set 2
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
"""


"""
	This is the idea:
	- We create a binary tree, where nodes have left and right arm pointing to left and right nodes (or None for leaf nodes).
	- First we use a Inorder style or recursion, to re-assign the left arms to nodes as they would apear in a Inorder tree traversal.
	- The we will find the right most node, which would be last in a Inorder tree traversal, and propegate backwards, reassigning the right arms.
	- The re-assignment of the left and right arms will convert the binary tree into a doubly linked list.
"""


"""
	This is the node class.
	Basically, the tree, is jusr a collection of nodes.
"""
class Node:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None
###################################################

"""
	The ReAssignLeftArm class will do the following:
	- It will use the algorthm for traversing a tree in a InOrder way, and re-assigns the left arm of the nodes, to nodes
	in the order that they would be printed as if they were being traversed inorder.
	- At the end of this method, the root will be pointing to a modified tree, where the left arms have be reassigned.
"""
def ReAssignLeftArm(rootObj):
	if rootObj is not None:
		ReAssignLeftArm(rootObj.left);
		rootObj.left = ReAssignLeftArm.PreviousLeftObj;
		ReAssignLeftArm.PreviousLeftObj = rootObj;
		ReAssignLeftArm(rootObj.right);
	else:
		return;
###################################################

"""
	At this point, our tree has its left arms reassigned. The right arms are as they were before.
	What we want to do is traverse through the tree, and reassign the right arms, so our tree turn into a doubly
	linked list.
	At the end of this method, we have a doubly linked list, with the root pointing to the first element of the linked list.
"""
def ReAssignRightArm(rootObj):
	while ((rootObj is not None) and (rootObj.right is not None)):
		rootObj = rootObj.right;
	rootObj.right = None;
	while ((rootObj is not None) and (rootObj.left is not None)):
 		tempRootObj = rootObj;
 		rootObj = rootObj.left;
 		rootObj.right = tempRootObj;
###################################################

 
# Driver program to test above function
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
 

# This will be the object the most left node will be pointing to.
ReAssignLeftArm.PreviousLeftObj = None;
# Call this method to re-assign all the left arms of the tree.
ReAssignLeftArm(root);
# At this point, the left arms of the tree are re-assigned.
# The right arms are still pointing to the previous objects.
ReAssignRightArm(root);

# At this point, the root is a doubly linked list, with node ordered in the same order as they would apear in
#  an Inorder tree traversal.
 
	 
