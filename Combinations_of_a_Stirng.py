"""
	In this problem, we want to do the following:
	Given a string, we want to be able to print all possible unique combinations of characters from that string.
	For example:
	Input: abc
	Output would be:
	a, b, c, ab, ac, bc, abc
	We note that, abc is the same as bca and cba and so on.
"""

"""
	This class contains a recursive function which prints out all possible combinations of a string.
	As described above.
"""
class CombinationOfString:

	"""
		Initialize the object setting the input string.
		Also, the output list, which will hold different letters to be printed.
	"""
	def __init__(self, input_String):
		self.In = input_String;
		self.Out = [];

	"""
		This is the recursive function, which will start by default from the first character
		and advances character by character through the input string.
	"""
	def MakeCombinations(self, input_Start=0):
		# Start from the input starting point in the string.
		# Loop through to the end of the string.
		for i in range(input_Start,len(self.In)):
			# Append the current character to the output
			self.Out.append(self.In[i]);
			# print the output
			print "".join(self.Out);
			# Increment the index and call the this function again (recurive)
			self.MakeCombinations(i+1);
			# Remove the last character from the output and continue
			del self.Out[-1];



"""
	Test the code here:
"""
comboObj = CombinationOfString("abc");
comboObj.MakeCombinations();