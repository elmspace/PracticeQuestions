"""
	In this problem, we will implement the Selection Sort algorithm.
	- Using loops
	- Useing recursion
"""


"""
	In this function, we will be implementing the selection sort using loops.
"""
def SelectionSort_loops(input_List):
	# Lets check the corner cases.
	if(input_List == None):
		return None;
	# If the list has 0 or 1 element, return the list.
	if(len(input_List) < 2):
		return input_List;
	# If we are, we are ready to sort.
	# Lets loop through all the elements of the list.
	for i in range(0,len(input_List)-1):
		# Find the min value and its index.
		minIndex, minVal = findMinInThisList(input_List[i+1:len(input_List)]);
		# If the min value is less than out current value, swap them.
		if(minVal < input_List[i]):
			# Note that the index here for the sub-list, so we have to modify it.
			input_List = swapTheseTwoIndices(input_List, i, (minIndex+i+1));
	# Return the sorted list.
	return input_List;


"""
	In this method, we will do the selection sort using recursion.
"""
def SelectionSort_recursion(input_List):
	# The same checks apply here too.
	# Lets check the corner cases.
	if(input_List == None):
		return None;
	# If the list has 0 or 1 element, return the list.
	if(len(input_List) < 2):
		return input_List;

	# This is the sub-function which is recursive and does the sorting
	SelectionSort_recursion_func(0, input_List, len(input_List));
	return input_List;


"""
	This is the recursive function which does the sorting.
"""
def SelectionSort_recursion_func(input_Start, input_List, input_ListLen):
	# If the input index, is less than the length of the original list
	if(input_Start < input_ListLen -1):
		# Find the min value and its index in the list
		minIndex, minVal = findMinInThisList(input_List[input_Start+1:len(input_List)]);
		# If the current value we are on is greater than the min, swap them.
		if(minVal < input_List[input_Start]):
			input_List = swapTheseTwoIndices(input_List, input_Start, (input_Start+minIndex+1));
		# Call the recursive function again, and advance the index by 1.
		SelectionSort_recursion_func(input_Start+1, input_List, input_ListLen);

"""
	This function will swap the values at the two indices given.
	It will return a new list, with its values swaped.
"""
def swapTheseTwoIndices(input_List, input_index1, input_index2):
	tempVal = input_List[input_index1];
	input_List[input_index1] = input_List[input_index2];
	input_List[input_index2] = tempVal;
	return input_List;


"""
	This function will find the minimum value in a list and will return the index and value itself.
"""
def findMinInThisList(input_List):
	# Lets consider the corner cases.
	if(input_List == None or len(input_List) == 0):
		return None;
	# If the list has only 1 element, that is the min.
	if(len(input_List) == 1):
		return 0, input_List[0];

	# If we are here, we are ready to find the min.
	# Set the min value and idnex to be the first element of the list
	minVal = input_List[0];
	minIndex = 0;
	# Loop though all the values in the list
	for i in range(1,len(input_List)):
		# If the current value is amller than the min val, reset the min val and its index.
		if(input_List[i] <= minVal):
			minVal = input_List[i];
			minIndex = i;

	# Return the min index and min value
	return minIndex, minVal;







"""
	Test the functions here:
"""

input_List = [1,4,3,6,2,4,7,2,1,5,7];
print "Before sort:";
print input_List;
print "After sort:"
#print SelectionSort_loops(input_List);
print SelectionSort_recursion(input_List);