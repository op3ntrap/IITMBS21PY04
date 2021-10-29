# first method
def sort(array):
	length = len(array)
	temp = [0] * length
	merge_sort(array, temp, 0, length - 1)


def merge_sort(array, temp, left, right):
	if left < right:
		center = (left + right) // 2
		merge_sort(array, temp, left, center)  # Left merge sort
		merge_sort(array, temp, center + 1, right)  # Right merge sort
		merge(array, temp, left, center + 1, right)  # Merge two ordered arrays.


def merge(array, temp, left, right, right_end_index):
	left_end_index = right - 1  # / End subscript on the left
	temp_index = left  # Starting from the left count
	element_number = right_end_index - left + 1
	while left <= left_end_index and right <= right_end_index:
		if array[left] <= array[right]:
			temp[temp_index] = array[left]
			temp_index += 1
			left += 1
		else:
			temp[temp_index] = array[right]
			temp_index += 1
			right += 1
	while left <= left_end_index:  # If there is element on the left
		temp[temp_index] = array[left]
		temp_index += 1
		left += 1
	while right <= right_end_index:  # If there is element on the right
		temp[temp_index] = array[right]
		temp_index += 1
		right += 1
	for i in range(0, element_number):
		array[right_end_index] = temp[right_end_index]
		right_end_index -= 1
