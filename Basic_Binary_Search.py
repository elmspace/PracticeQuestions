"""
	In this code,
	we will implement a simple binary search to find the index of a number in an sorted list.
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

	# We start by setting the mid point index to be the same as the length of the list
	midPoint = len(input_List);
	# We also need a parameter to keep track of the first component of the lits (this is for cases where val > midPoint)
	midPointInd = 0;
	# We loop while the midPoint is not 0
	while (midPoint):
		# Divide the current list length by 2, and set it to mid point
		# Be careful if you are using Python 3.x
		midPoint = midPoint/2;
		# Add the adjustment, in case we need to. This is due to the fact that our list is
		# divided into two everytime
		lookInThisIndex = midPoint + midPointInd;
		# Look to see if we found the value, if yes, return the index.
		if(input_List[lookInThisIndex] == input_SearchVal):
			return lookInThisIndex;
		# If not, and if the value is in the right hand side of the list, we need to make an adjustment.
		elif(input_List[lookInThisIndex] < input_SearchVal):
			# So now the begining of the list is shifted up
			midPointInd += midPoint;
			midPoint += 1;
	# Return None, if it can not find the item
	return None;

"""
	Test the Binary Search Algo
"""
if __name__ == '__main__':
	myList = [i for i in range(0,30,1)];
	print myList;
	print "Lets do some examples:"
	print BinarySearch(myList, 12);
	print BinarySearch(myList, -1);
	print BinarySearch(myList, 2);
	print BinarySearch(myList, 6);
	print BinarySearch(myList, 8);