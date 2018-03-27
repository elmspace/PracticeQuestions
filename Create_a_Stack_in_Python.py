"""
Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.
"""

"""
	So this is what I am doing here:
	- I am extending the list object in Pyhton to used it as a stack object.
	- I know the question says not to use array or list, but wtf, Pyhton does not have builtin stack.
	- I am also writting a push method, to append data to the object, and also keep track of the minimum value of the value in the stack. 
"""

"""
	Import this so we can use obj.method().
"""
import __builtin__;

"""
	Stack class, extending list object.
"""
class Stack(list):

	"""
		The __MinStackVal is a private variable, which will store the min val in the stack.
	"""
	def __init__(self):
		self.__MinStackVal = [];

	"""
		The push will do a simple append, and also check the min value in the current stack.
		see below for details.
	"""
	def push(self,input_int):
		if(len(self.__MinStackVal) != 0):
			currentVal = self.__MinStackVal.pop();
			if(input_int <= currentVal):
				self.__MinStackVal.append(input_int);
			else:
				self.__MinStackVal.append(currentVal);
		else:
			self.__MinStackVal.append(input_int);
		self.append(input_int);

	"""
		The getMin method will return the minimum value in the stack.
	"""
	def getMin(self):
		if(len(self.__MinStackVal) != 0):
			return self.__MinStackVal[0];
		else:
			return None;

########################################
"""
	Testing the code:
"""
stack = Stack();
stack.push(2);
stack.push(4);
stack.push(1);
stack.push(5);
stack.push(0);

print stack;

print stack.getMin();
