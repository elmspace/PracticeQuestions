



def counts(nums, maxes):

	nums_rorted = sorted(nums);
	print nums_rorted;
	print maxes;
	print "----"
	answer = [];
	for i in range(len(maxes)):

		if(maxes[i] < nums_rorted[0]):
			answer.append(0);
		else:

			keepLooking = True;
			j = len(nums_rorted)-1;
			while (keepLooking):

				if(nums_rorted[j] <= maxes[i]):
					answer.append(j+1);
					keepLooking = False;
				elif(j==0):
					answer.append(0);
					keepLooking = False;
				else:
					j -= 1;



	print answer;






nums = [1,4,2,4]
maxes = [3,5]


counts(nums, maxes);