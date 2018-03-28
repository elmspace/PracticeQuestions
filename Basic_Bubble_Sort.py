"""
	In this problem, we are going to do the following:
	- Given an un-sorted array, and the direction of sort
	- Sort the array using bubble sort
	- Return a new sorted array

	Notes:
	The time complexity of the Bubble sort is O(N^2)
"""


"""
	Input: Un-Ordered list, A for ascending and D for descending.
	Output: Ordered List;
"""
def BubbleSortThisBaby(input_List, input_Direction):

	# Check if List is None, or the length is 0, or 1;
	if(input_List == None or len(input_List)==0):
		return None;
	if(len(input_List)==1):
		return input_List;

	# At this point, we know that the list is not None, and the length is > 1.
	# This parameter will let us know if we still flipping elements or are we done.
	KeepGoing = True;
	while(KeepGoing):
		# Set it to False, it will be set to True in one of the conditions below is met
		KeepGoing = False;
		# Loop through every element of the list
		for i in range(0,len(input_List)-1):
			# Check to see if we are sorting in ascending or descending order.
			if(input_Direction == "A"):
				# If ascending order, if the element at current position is greater than i+1 switch them
				if(input_List[i]>input_List[i+1]):
					temp = input_List[i];
					input_List[i] = input_List[i+1];
					input_List[i+1] = temp;
					# If we did a switch, re-set the KeepGoing parameter to True, to indicate the loop to continue.
					KeepGoing = True;
			else:
				# This is the same as above, but for the descending.
				if(input_List[i]<input_List[i+1]):
					temp = input_List[i];
					input_List[i] = input_List[i+1];
					input_List[i+1] = temp;
					KeepGoing = True;

	# Return the sorted list.
	return input_List;



"""
	Test the function here:
"""
input_List = [1,3,5,2,3,1,5,6,12,2,0];
input_List = None;
print BubbleSortThisBaby(input_List, "D");
