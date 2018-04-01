"""
	In this function, we will implement the factorial function using loops.
"""

"""
	This function will calculate the factorial of a int.
"""
def calculateFactorial(input_data):
	# If the input is 0 or 1, the factorial is 1. 
	if(input_data == 0 or input_data == 1):
		return 1;
	# Otherwise, use loop to calculate factorial.
	else:
		result = 1;
		for i in range(input_data,1,-1):
			result = result * i;
		return result;

"""
	Test the functino here
"""
print calculateFactorial(12);