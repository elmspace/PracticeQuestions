"""
	This problem implements a binary search using recursion.
"""


"""
	This is the recursive implementation of the binary search.
"""
def BinarySearch_recursion(input_List, input_LookForThis):
	# Check the corner cases, if the len of the list is 1, and the value in the list is what we are looking for.
	if(len(input_List) == 1 and input_LookForThis == input_List[0]):
		return "Found it.";
	# Else if the list is of size 1 and the value is not what we are looking for.
	elif(len(input_List) == 1 and input_LookForThis != input_List[0]):
		return "Value is not in the list";
	# In other case, break the list in half.
	else:
		# Find the mid point.
		midPoint = len(input_List)/2;
		# If the mid point, contains the value we are looking for.
		if(input_List[midPoint] == input_LookForThis):
			return "Found it.";
		# If the value is greater than the mid point value, send the upper half of the list to the same function again.
		elif(input_List[midPoint] < input_LookForThis):
			return BinarySearch_recursion(input_List[midPoint:len(input_List)],input_LookForThis);
		# Else do the exact opposite.
		else:
			return BinarySearch_recursion(input_List[0:midPoint],input_LookForThis);




"""
	Test the function here:
"""

myList = [1,2,3,4,5,6,7,9];

print BinarySearch_recursion(myList, 12);
print BinarySearch_recursion(myList, -1);
print BinarySearch_recursion(myList, 2);
print BinarySearch_recursion(myList, 6);
print BinarySearch_recursion(myList, 8);