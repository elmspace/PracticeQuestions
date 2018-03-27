"""
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
"""


def Print_K_Largest_Elements(input_List, input_K):
	"""
		This is a cheap way of doing this, but the sort function in
		Pyhton is O(nlog(n)), so from the big-O prespective it make sense. 
	"""
	input_List = sorted(input_List, reverse = True);
	return input_List[0:input_K];



# Example:
input_List = [1, 23, 12, 9, 30, 2, 50];
input_K = 3;
print Print_K_Largest_Elements(input_List, input_K);