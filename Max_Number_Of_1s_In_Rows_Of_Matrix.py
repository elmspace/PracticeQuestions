"""
	In this problem, we are given a 2D Matrix, where in each row we have 0s and we have 1s.
	The 0s and 1s are sorted, so all zeros are at the left and 1s at the right. For example:
	[[0,0,1,1],[0,1,1,1],[0,0,0,1]].
	Question: Find the row with maximum number of 1s in the row.
"""

"""
	This function will do the following:
	- It will take in a 2D matrix.
	- It will loop through its rows and each element for that row,
	- If it comes across a 1, it knows the rest of that row is 1s, since the row is sorted,
	- The total number of 1s in that row is then length of that row minus the current spot of 1.
"""
def FindRowWithMaxOnes(input_Matrix):
	# If matrix is not defined return None.
	if(input_Matrix == None):
		return None;

	# Get the size of the matrix.
	numbRows = len(input_Matrix);
	numbCols = len(input_Matrix);

	# At the begining, the max numb of 1s is 0.
	MaxNumbOfOnes = 0;
	# Loop through the rows and columns.
	for rows in range(numbRows):
		# Set the number of 1s for a given row to 0, incase that row has no 1s.
		numbOfOnesInThisRow = 0;
		for cols in range(numbCols):
			# If we come across a 1, we know the rest of the row is also 1s
			if(input_Matrix[rows][cols] == 1):
				# Get the number of 1s, using the length of the row, and break.
				numbOfOnesInThisRow = numbCols - cols;
				break;
		# If the current number of 1s is bigger that previous, replace the max flag
		if(numbOfOnesInThisRow >= MaxNumbOfOnes):
			MaxNumbOfOnes = numbOfOnesInThisRow;
	# Return the max number of 1.
	return MaxNumbOfOnes;




"""
	Test your code here:
"""
Matrix = [];
Matrix.append([0,0,0,1,1]);
Matrix.append([0,0,1,1,1]);
Matrix.append([0,0,0,0,0]);
Matrix.append([0,0,1,1,1]);
Matrix.append([0,1,1,1,1]);

print FindRowWithMaxOnes(Matrix);
