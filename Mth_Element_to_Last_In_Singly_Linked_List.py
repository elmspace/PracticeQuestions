"""
	Given a singly linked list, devise a time- and space-efficient algorithm to find the mth-to-last element of the list.
	Implement your algorithm, taking care to handle relevant error conditions.
	Define mth to last such that when m = 0 the last element of the list is returned.
	Note here that we are measuring the distance to the last element. In a singly link list, we can only traverse in 1 direction. 

	Notes:
	Here are few ways we can look at this problem, remembering we need to save time and space.
	1) We can a double loop to check every element and count its position from the last element by traversing through the list.
	this is a simple yet dumb way of solving this problem, since its is a O(N^2) at worst case.

	2) Another way we can solve this problem is to find the size of the list, by traversing through it once, and then we know that,
	the length of the list is L = m + n, where n is the number of elements from the beginning, and since we can count from the
	beginning, we can find the element. This is a O(2n) or O(n) problem.

	3) The best way is to use a fuzzy queue, with depth of size m. Meaning as we traverse through the list, we keep track of the
	last mth element, once we get to the end, the element in the mth position of the queue is the mth element from the end. The only
	thing is that we dont want to keep all m elements in the queue, since that could take too much space.
	We can achieve this by using two pointers m nodes apart.
"""

