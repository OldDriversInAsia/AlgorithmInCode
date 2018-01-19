def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[int(len(arr) / 2)]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	print (pivot)
	return quicksort(left) + middle + quicksort(right)
  
#print (quicksort([3,6,8,10,1,2,5]))
#print (quicksort([3,1,8,10,6,2,5]))
print (quicksort([3,10,8,6,1,2,5]))




'''
10
3 6 8 1 2 5:10:
3 6 8 1 2 5 10

1
:1:3 6 8 2 5
1 3 6 8 2 5 10

8
3 6 2 5:8: 
1 3 6 2 5 8 10

2
:2:3 6 5
1 2 3 6 5 8 10

6
3 5:6:
1 2 3 5 6 8 10

5
3:5:
1 2 3 5 6 8 10




10
3 1 8 6 2 5:10:
3 1 8 6 2 5 10

6
3 1 2 5:6:8
3 1 2 5 6 8 10

2
1:2:3 5
1 2 3 5 6 8 10

5
3:5:
1 2 3 5 6 8 10





6
3 1 2 5:6:10 8
3 1 2 5 6 10 8

2|8
1:2:3 5|:8:10
1 2 3 5 6 8 10

5
3:5:
1 2 3 5 6 8 10

'''
