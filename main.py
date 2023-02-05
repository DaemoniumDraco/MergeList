#import random

list1 = [
 2, 5, 15, 36, 47, 56, 59, 78, 156, 244, 268, 350, 360, 375, 380, 600, 999
]
list2 = [18, 39, 42, 43, 66, 69, 100, 101, 107, 300, 400, 1000]


def mergeList1(list1, list2):
	list3 = []

	index1 = 0
	index2 = 0

	if len(list1) < len(list2):
		min = len(list1) - 1
		max = len(list2)
	else:
		max = len(list1)
		min = len(list2) - 1

	print(min, max)
	print()

	while (index1 < max and index2 < max):

		if list1[index1] < list2[index2]:
			list3.append(list1[index1])
			index1 += 1

		elif list1[index1] > list2[index2]:
			list3.append(list2[index2])
			index2 += 1

		else:
			list3.append(list1[index1])
			list3.append(list2[index2])
			index1, index2 = index1 + 1, index2 + 1

		print(list3)
		print(index1, index2)
		print()

	#ENDWHILE

	if index2 <= len(list2):
		for i in range(index2, len(list2)):
			list3.append(list2[i])

	elif index1 <= len(list1):
		for i in range(index1, len(list1)):
			list3.append(list1[i])

	print(list3)
	return (list3)


def mergeList2(list1, list2):

	list4 = list1 + list2
	list4 = sorted(list4)

	print(list4)
	return list4


mergeList1(list1, list2)
mergeList2(list1, list2)
