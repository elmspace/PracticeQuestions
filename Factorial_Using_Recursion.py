"""
	In this problem, we want to calculate the factorial of a number using recursion.
	The factorial of a number is N! = N(N-1)(N-2)...1
"""

"""
	This is a recursive function which will calculate the factorial of a number.
"""
def CalculateFactorial(input_Number):
	# If the input is None, return None
	if(input_Number == None):
		return None;
	# If the number is 0, return 1, since mathematically factorial of 0! = 1
	elif(input_Number == 0):
		return 1;
	# Under any other condition, call the function again, sending in the input number minus 1.
	# The return is multiplied by the input number.
	else:
		input_Number *= CalculateFactorial(input_Number - 1);
		return input_Number;


"""
	Test the function here:
"""
print CalculateFactorial(3);

