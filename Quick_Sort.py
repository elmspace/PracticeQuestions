"""
	This problem covers the implementation of quick sort.
	It uses recursion to perform the sorting.
"""

"""
	This method performs the quick sort in-place using recursion.
	The start and end point in the list are by default set to 0 and len(list).
"""
def QuickSort(input_List, input_Start=None, input_End=None):
	# Set the default values.
	if(input_Start==None or input_End==None):
		input_Start = 0;
		input_End = len(input_List);
	# If the input list is None, just return.
	if(input_List == None):
		return;
	# If the start and end position are the same, return, this corresponds to
	# a list of size 1.
	if(input_Start == input_End):
		return;

	# Pivot around the start position to the end, pushing all smaller values
	# To the left of start.
	i = PivotThisList(input_List, input_Start, input_End);

	# Repeat this process for the left and right portion of the list.
	LeftList = QuickSort(input_List,input_Start,i);
	RigthList = QuickSort(input_List, i+1, input_End);


"""
	This function performs the pivot, and acts on the list itself, so it is in-place.
"""
def PivotThisList(input_List, input_Start, input_End):
	# Set the pivot value to the value at the start of the list
	pivotVal = input_List[input_Start];
	# Set the pivot index to be the index of the start, this will be shifted as we pivot
	pivotIndex = input_Start;
	# Loop through all elements
	for i in range(input_Start+1,input_End):
		# If the element is less than or equal to the current element, shift it to the left
		# Of the start position.
		if(input_List[i] <= pivotVal):
			tempVal = input_List[i];
			del input_List[i];
			input_List.insert(input_Start,tempVal);
			# Increment the index by 1, to keep track of our pivot point.
			pivotIndex +=1;
	# Return the pivot final index.
	return pivotIndex;



"""
	Test your function here:
"""
myList = [1,3,5,1,2,5,7,8,2,1,4,12];
QuickSort(myList);
print myList;