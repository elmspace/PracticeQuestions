"""
	In this problem we have the following data structure:
	- Normal doubly linked list, with a reference to a head and tail.
	- We also in addition to the next and previous pointers, a third pointer which can point either to:
		- None
		- Another doubly linked list (which we dont have a specific head and tail references)
	- Lets also assume no circular properties.

	Problem: We want to flatten the list, so it looks like a basic doubly linked list.

	Approach: There maybe many different ways of flattening the list, here is how we will solve it:
	- Traverse through the list
	- If the node has a side child, add that child list to the end of the top level list
	- Modify the last node, and reassign the tail.
	- Continue traversing until you have gone through all elements. 
"""