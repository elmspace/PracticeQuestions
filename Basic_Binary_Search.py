"""
	In this practice question will do the following:
	We will implement a simple binary search to find the index of a number in an sorted list.
"""

def BinarySearch(input_List, input_SearchVal):

	# In case the input list is None, just return.
	if input_List == None:
		return None;
	# Check if the value is outside of the bounds
	if input_SearchVal > input_List[-1]:
		return None;
	if input_SearchVal < input_List[0]:
		return None;

	# We start by setting the divided value to be the same as the length of the list
	divInd = len(input_List);
	# We also need a parameter to keep track of the first component of the lits (this is for cases where val > divInd)
	midPointInd = 0;
	# We loop while the divInd is not 0
	while (divInd):
		# Divide the current list length by 2
		divInd = divInd/2;
		# Add the adjustment, in case we need to
		lookInThisIndex = divInd + midPointInd;
		# Look to see if we found the value, if yes, return the index.
		if(input_List[lookInThisIndex] == input_SearchVal):
			return lookInThisIndex;
		# If not, and if the value is in the right hand side of the list, we need to make an adjustment.
		elif(input_List[lookInThisIndex] < input_SearchVal):
			midPointInd += divInd;


	# Return None, if it can not find the item
	return None;



"""
	Test the Binary Search Algo
"""
myList = [1,2,3,4,5,6,7,9];

print BinarySearch(myList, 12);
print BinarySearch(myList, -1);
print BinarySearch(myList, 2);
print BinarySearch(myList, 6);
print BinarySearch(myList, 8);