"""
Lowest Common Ancestor in a Binary Tree
Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
Look at wiki for full definition of Common Ancestor.
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
	The following method works in the following way:
	- Each node has a left arm and a right arm.
	- For each arm of the node, we consider the value of the child node.
		- If the value of the child node is None (leaf condition), the value of the arm is set to None.
		- If the value of the child node is equal to one of the nodes we are looking for, then the value of the arm is equal to the value of the child node.
		- Else, look at the left and right arms of the child node. The value going back up will depend on the values of the left and right arm of the child node.
"""
def FindCommonAncestor(NodeObj, val_1, val_2):

	# If Node Object is node, either:
	# We have a empty tree, or we are the leaf node.
	if NodeObj is None:
		return None;
 

	# If the Node we are looking at matches one of the values we are looking for, return.
	# In this case, we have two possibility:
	# We are at the root, and return will exit the function
	# We are at the sub-node, in which case the recursive function move down the stack, setting one of LeftArm or RightArm equaling the current Node.
	if (NodeObj.data == val_1 or NodeObj.data == val_2):
		return NodeObj 
 
	# If we are here, it means that the current Node Object is not one of the values we are looking for, so look into the left and right arm of the current node.
	# When the recursion comes back up to this point, the left arm will hold either None, meaning the value we are looking for does not exists in the left sub tree 
	# of the current node, or the value of the node, which matches one of the values we are looking for.
	LeftArm = FindCommonAncestor(NodeObj.left, val_1, val_2);
	
	# Same as above, but for the right arm.
	RightArm = FindCommonAncestor(NodeObj.right, val_1, val_2)
 	

	# At this point, for the current node, we have three options.
	if LeftArm and RightArm:
		return NodeObj 
 
	# Otherwise check if left subtree or right subtree is LCA
	return LeftArm if LeftArm is not None else RightArm
 
 
 
root = Node(1)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)
FindCommonAncestor(root, 5, 8)
 
