def  getMinimumDifference(a, b):

	if(len(a) != len(b)):
		return None;
	else:
		# Lets create a answer list
		answer = [];
		# Since the len of the a and b are the same, we can do this:
		for i in range(len(a)):
			# Lets get the elements in each position:
			A = a[i];
			B = b[i];
			if(len(A) != len(B)):
				answer.append(-1);
			else:
				counter = 0;
				for i in A:
					indexOfThisElement = B.find(i);
					if(indexOfThisElement < 0):
						counter +=1;
					else:
						B = list(B);
						del B[indexOfThisElement];
						B = "".join(B);
				answer.append(counter);
						
	return answer;






a = ["hhpddlnnsjfoyxpci","xulkowreuowzxgnhmiqekxhz","dnqaurlp","aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqra","lbafwuoawkxydlfcbjjtxpzpchzrvbtiev","drngbjuuhmwqwxrinxccsqxkp","ubu","vxxzsqjqsnibgydzlyynqcrayvw","xtnipeqhxvafqaggqoanvwk","gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvz"]

b = [
"ioigvjqzfbpllssuj","istdocbnyozmnqthhpievvlj","lofnrtmh","sqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb","qbpedlqbktorypcjkzzkodrpvosqzxmpad","wygwcdbtriwaesjsobrntzaqbe","lzt","jurfsqfrivayopgrxewwruvemzy","mthtfirwhmjrbphlmeluvoa","nspiwquxxsiwuldizqkkaawpyyisnftdzklwagv"]
print getMinimumDifference(a,b)

