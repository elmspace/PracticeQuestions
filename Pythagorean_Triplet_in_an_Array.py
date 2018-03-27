"""
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.
Example:
Input: arr[] = {3, 1, 4, 6, 5}
Output: list of value which satisfy the this condition.
There is a Pythagorean triplet (3, 4, 5).
"""



def Find_Triple_In_This_Array(input_List):
	# First we will sort the list; O(nlog(n));
	input_List = sorted(input_List, reverse=True);
	# Then we will square all the elements; O(n)
	input_List = [i**2 for i in input_List];


	# The following section has time complexity O(n^2)
	"""
	What we want to do is put an index at position i, on one edge of the list
	and make index j and k, on opposite end of window outside of i.
	This window closes while searching for a condition where j + k = i.  
	"""
	solutionList = [];
	# loop through all i value
	for i in range(0,len(input_List)):
		# Define the size of the window
		j = i+1;
		k = len(input_List) - 1;
		# Keep searching until you find a solution
		ContinueSearching = True;
		while(j<k and ContinueSearching):
			# If you find a solution, take a note and continue to next i
			if(input_List[j]+input_List[k]==input_List[i]):
				solutionList.append([input_List[i],input_List[j],input_List[k]]);
				ContinueSearching = False;
			# If the value is too large, index up the j, to smaller values, since our list is ordered
			elif(input_List[j]+input_List[k]>input_List[i]):
				j += 1;
			# If the value is too small, then index down the k, again since our list is sorted
			else:
				k -= 1;

	"""
		The overall time complexity of this solution is nlog(n) + n + n^2,
		which is a lot better thank the n^3.
	"""
	return solutionList;


# Test the above function
input_List = [3, 1, 4, 6, 5];
print Find_Triple_In_This_Array(input_List);