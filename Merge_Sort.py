"""
	In this problem we will be looking at the Merge Sort.
	Input to the merge sort is an un-ordered list.
	Output is a ordered list.
	The time complexity of merge sort is Nlog(N)
"""

"""
	This method will take in as input two ordered lists and will merge them into 
	1 list, such that the merged list is also sorted.
"""
def MergeLists(input_LeftList, input_RightList):
	# Set a new list, which will conatin the merged lists
	MergedList = [];
	# Initialize the indecies to 0
	i = 0;
	j = 0;
	# While we have ietms in either sets, traverse over them and append them to the merge set from smallest to largest.
	while(i<len(input_LeftList) and j<len(input_RightList)):
		if(input_LeftList[i] <= input_RightList[j]):
			MergedList.append(input_LeftList[i]);
			i+=1;
		else:
			MergedList.append(input_RightList[j]);
			j+=1;
	# Once we are done with one of the lists, empty the other one and append it to the end of the merged list.
	# Since the smaller lists are already ordered, it will be ok.
	while(i<len(input_LeftList)):
		MergedList.append(input_LeftList[i]);
		i+=1;
	while(j<len(input_RightList)):
		MergedList.append(input_RightList[j]);
		j+=1;
	# Return the merge list.
	return MergedList;

"""
	This is the method which will split the list recursively, until it is broken down to its
	elements, it will then use the MergeLists algorithm above to build back the list in order from
	ground up.
"""
def MergeSort(input_List):
	# If the length of list is less than 2, meaning it is a single element, return the list.
	if(len(input_List) < 2):
		return input_List;
	# Else, break up the list into two lists, left and right.
	# The left and right contains two un-ordered sets
	LeftList = [input_List[i] for i in range(0,len(input_List)/2)];
	RightList = [input_List[i] for i in range((len(input_List)/2),len(input_List))];
	# Send back in the left and right elements, recursivly, and they will be broken up again.
	LeftList = MergeSort(LeftList);
	RightList = MergeSort(RightList);
	# Once we are on our way back up the recursio stack, we merge the sets, according to the above algo.
	input_List = MergeLists(LeftList,RightList);
	# Return the merged set, which at this point should be sorted.
	return input_List;


"""
	This is for testing:
"""
input_List = [1,2,4,6,23,1,4,8,90,3,4];
print "original";
print input_List;
print "-----"
print MergeSort(input_List);
