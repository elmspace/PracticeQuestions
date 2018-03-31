"""
	In this problem, we want to write a function which will take a string and will pring all possible permutations of it.
	Example: String = abc
	Output: abc, bac, bca, cba, cab, acb.
	The number of permutation is N!, where N is the number of characters in the string.
"""

"""
	This class contains the method, which will print all possible permutations of a string.
"""
class CalculatePermutatoin:

	"""
		Initialize the object, by setting:
		- The input string.
		- The output string, this will be printed at every step.
		- The Used list, which keeps track of which letter was used. 
	"""
	def __init__(self, input_String):
		self.In = input_String;
		self.Out = [];
		# We set all the values to false at the begining, since none of the values have been used yet
		self.Used = [False for i in range(len(self.In))];

	"""
		This is a recursive function, which will pring all possible permutations of the input string.
	"""
	def permuteMyString(self):
		# If the length of the output list is the same as the input list, print the output
		if(len(self.Out) == len(self.In)):
			# Im doing a join, to print as string
			print "".join(self.Out);
			# After printing return.
			return;
		else:
			# If the length is not equal, then keep going
			for i in range(0,len(self.In)):
				# Check the letter we are on, is it already in the Out list
				if(self.Used[i]):
					# If yer, we cant use it again, so skip it
					pass;
				else:
					# If is is not, then add it to the out list
					self.Out.append(self.In[i]);
					# Set the used indicator to be true, so we dont use it again.
					self.Used[i] = True;
					# Call the function again, with this new information
					self.permuteMyString();
					# Once we are out, for what ever level we are on, remove the used indicator
					self.Used[i] = False;
					# And remove the letter from list
					del self.Out[-1];



"""
	Test the function here:
"""
Permu = CalculatePermutatoin("abc");
Permu.permuteMyString();